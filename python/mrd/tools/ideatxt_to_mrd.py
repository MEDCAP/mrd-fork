import numpy as np
import re
import sys
import argparse
from typing import TextIO, Optional, Iterable, Tuple, List, Union
from dataclasses import dataclass

import mrd


@dataclass
class FieldTracker:
    """
    Compress a 
    Stores value changes and repetition counts.
    pulseq compresses by storing derivative values and repeated values with 
    """
    current_value: float = 0.0
    repetition_count: int = 0
    changes: List[Tuple[int, float, int]] = None  # (line_number, value, count)
    
    def __post_init__(self):
        if self.changes is None:
            self.changes = []
    
    def update(self, line_number: int, new_value: float):
        """Update the field with a new value. If different, record the change."""
        if self.repetition_count == 0:
            # First value
            self.current_value = new_value
            self.repetition_count = 1
        elif new_value == self.current_value:
            # Value repeats
            self.repetition_count += 1
        else:
            # Value changed - store the previous run
            self.changes.append((line_number - self.repetition_count, self.current_value, self.repetition_count))
            self.current_value = new_value
            self.repetition_count = 1
    
    def finalize(self, line_number: int):
        """Finalize tracking and store the last run."""
        if self.repetition_count > 0:
            self.changes.append((line_number - self.repetition_count + 1, self.current_value, self.repetition_count))

class _LinesIterator:
    """
    Internal implementation of a peekable line iterator for IDEA text files.

    Behavior:
      - Strips whitespace.
      - Skips comment lines beginning with ';'.
      - Skips empty lines.
      - Provides lookahead via peek().
      - Line numbers correspond to the original file (1-based).
    """

    def __init__(self, file: TextIO):
        self._file = file
        self._buffer: Union[Tuple[int, str], None] = None
        self._current_line = None
        self._line_number = 0

    def __iter__(self) -> "_LinesIterator":
        return self

    def __next__(self) -> Tuple[int, str]:
        if self._buffer is not None:
            item = self._buffer
            self._buffer = None
            return item

        while True:
            raw = self._file.readline()
            if raw == "":  # EOF
                raise StopIteration
            self._line_number += 1
            line = raw.strip()
            # Skip comment lines and empty lines
            if line.startswith(";") or line == "":
                continue
            return self._line_number, line

    def peek(self) -> Optional[Tuple[int, str]]:
        if self._buffer is not None:
            return self._buffer
        try:
            self._buffer = self.__next__()
        except StopIteration:
            return None
        return self._buffer
    # skip empty lines but keep track of the line number


class IdeaTextReader:
    """
    Reader for Siemens IDEA simulator text files.
    
    Efficiently tracks 7 fields (ADC, RF Ch0, Z Gradient, RF Ch1, X Gradient, Y Gradient, Phase)
    using run-length encoding - tracking repetitions and storing differences.
    """
    
    def __init__(self, file: TextIO):
        self._file = file
        self._lines = _LinesIterator(file)
        
        # Metadata
        self.start_time_ns: Optional[int] = None
        self.end_time_ns: Optional[int] = None
        self.time_step_ns: Optional[int] = None
        self.headers: List[str] = []
        
        # Field trackers for the 7 columns
        self.trackers: List[FieldTracker] = [FieldTracker() for _ in range(7)]
        
        self._parse_header()
    
    def _parse_header(self):
        """Parse the header section to extract metadata and column headers."""
        for line_number, line in self._lines:
            # Parse metadata from comment lines
            if line.startswith(";"):
                if "Start Time" in line:
                    match = re.search(r'Start Time\s*=\s*(\d+)', line)
                    if match:
                        self.start_time_ns = int(match.group(1))
                elif "End Time" in line:
                    match = re.search(r'End Time\s*=\s*(\d+)', line)
                    if match:
                        self.end_time_ns = int(match.group(1))
                elif "Time Step" in line:
                    match = re.search(r'Time Step\s*=\s*(\d+)', line)
                    if match:
                        self.time_step_ns = int(match.group(1))
                continue
            
            # Check if this is the header line (has tab-separated column names)
            if '\t' in line:
                self.headers = [h.strip() for h in line.split('\t') if h.strip()]
                # After headers, we should be ready to read data
                break
    
    def read_and_track_fields(self):
        """
        Read all data lines and track the 7 fields with run-length encoding.
        Returns the trackers with all changes recorded.
        """
        data_line_count = 0
        
        for line_number, line in self._lines:
            # Parse the 7 tab-separated float values
            try:
                values = [float(v.strip()) for v in line.split('\t') if v.strip()]
                if len(values) != 7:
                    continue  # Skip malformed lines
                
                # Update each field tracker
                for i, value in enumerate(values):
                    self.trackers[i].update(data_line_count, value)
                
                data_line_count += 1
                
            except ValueError:
                # Skip lines that can't be parsed as floats
                continue
        
        # Finalize all trackers
        for tracker in self.trackers:
            tracker.finalize(data_line_count)
        
        return self.trackers
    
    def get_field_summary(self, field_index: int) -> dict:
        """Get a summary of a specific field's tracking data."""
        if field_index < 0 or field_index >= 7:
            raise ValueError(f"Field index must be between 0 and 6, got {field_index}")
        
        tracker = self.trackers[field_index]
        return {
            'field_name': self.headers[field_index] if field_index < len(self.headers) else f"Field {field_index}",
            'num_changes': len(tracker.changes),
            'changes': tracker.changes,
        }
    
    def print_summary(self):
        """Print a summary of all tracked fields."""
        print(f"Start Time: {self.start_time_ns} ns")
        print(f"End Time: {self.end_time_ns} ns")
        print(f"Time Step: {self.time_step_ns} ns")
        print(f"\nHeaders: {self.headers}\n")
        
        for i in range(7):
            summary = self.get_field_summary(i)
            print(f"{summary['field_name']}:")
            print(f"  Number of value changes: {summary['num_changes']}")
            if summary['num_changes'] > 0:
                print(f"  First change: line {summary['changes'][0][0]}, value={summary['changes'][0][1]}, count={summary['changes'][0][2]}")
                if summary['num_changes'] > 1:
                    print(f"  Last change: line {summary['changes'][-1][0]}, value={summary['changes'][-1][1]}, count={summary['changes'][-1][2]}")
            print()


def test_reader(file: TextIO):
    """Test the IdeaTextReader with a given file."""
    reader = IdeaTextReader(file)
    reader.read_and_track_fields()
    reader.print_summary()
    
    # Example: Print detailed changes for the ADC field (field 0)
    print("\n" + "="*60)
    print("Detailed changes for ADC Signal Data (Field 0):")
    print("="*60)
    adc_summary = reader.get_field_summary(0)
    for line_num, value, count in adc_summary['changes'][:10]:  # Show first 10 changes
        print(f"  Line {line_num}: value={value}, repeated {count} times")
    if len(adc_summary['changes']) > 10:
        print(f"  ... and {len(adc_summary['changes']) - 10} more changes")


def idea_text_to_stream_items(file: TextIO) -> Iterable[mrd.StreamItem]:
    """
    Convert IDEA text file to MRD stream items.
    
    This function reads a Siemens IDEA simulator text file and converts it
    to MRD stream items for further processing.
    """
    reader = IdeaTextReader(file)
    reader.read_and_track_fields()
    
    # TODO: Implement conversion to MRD stream items based on tracked field data
    # For now, this is a placeholder
    
    # Example structure of what could be generated:
    definitions = mrd.PulseqDefinitions()
    if reader.start_time_ns is not None and reader.end_time_ns is not None and reader.time_step_ns is not None:
        definitions.block_duration_raster_ns = np.uint64(reader.time_step_ns)
        definitions.total_duration_ns = float(reader.end_time_ns - reader.start_time_ns)
    
    yield mrd.StreamItem.PulseqDefinitions(definitions)
    
    # Additional conversion logic would go here
    # - Process ADC events from field 0
    # - Process RF events from fields 1 and 3
    # - Process gradients from fields 2, 4, 5
    # - Process phase from field 6


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Read Siemens IDEA text file and track field changes efficiently.'
    )
    parser.add_argument(
        '-i', '--input', 
        type=str, 
        required=False, 
        help='Path to the Siemens IDEA text file. Defaults to stdin.'
    )
    parser.add_argument(
        '-o', '--output', 
        type=str, 
        required=False, 
        help='Path to the output MRD file (not yet implemented).'
    )

    args = parser.parse_args()
    # headers, seq_arr, sampletime = idea_text_to_stream_items(args.input)
    with (open(args.input, 'r') if args.input is not None else sys.stdin) as input:
        # headers, seq_arr, sampletime = idea_text_to_stream_items(input)
        test_reader(input) 

    # keep this for later edit to implement mrd encoding
    # write to mrd file pulseq fields
    #     with (open(args.output), 'wb') if args.output is not None else sys.stdout.buffer as output:
    #         with mrd.BinaryMrdWriter(output) as writer:
    #             writer.write_header(None)
    #             writer.write_data(idea_text_to_stream_items(input))
