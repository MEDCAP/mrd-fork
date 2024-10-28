import sys
sys.path.append('..')
from python.mrd import (
    BinaryMrdReader,
    BinaryMrdWriter,
    StreamItem,
    Acquisition,
    AcquisitionFlags,
    Waveform,
    Image,
    Header)
from typing import (
    Iterable, 
    Generator,
    cast)
import numpy as np

read_filename = 'siemens_mrd.bin'
write_filename = 'test_file.bin'

'''
- yardl requires you to read and write every field in the order as defined in
  mrd_protocol.yml filr
- To add a custom field, the existing data is first read and wrote back
'''

def acquisition_reader(input: Iterable[StreamItem]) -> Iterable[Acquisition]:
    for item in input:
        if not isinstance(item, StreamItem.Acquisition):
            # Skip non-acquisition items
            continue
        if item.value.flags & AcquisitionFlags.IS_NOISE_MEASUREMENT:
            continue
        yield item.value

def generate_data() -> Generator[StreamItem, None, None]:
    # We'll reuse this Acquisition object
    acq = Acquisition()
    yield StreamItem.Acquisition(acq)

def generate_image() -> Generator[StreamItem, None, None]:
    image = Image()
    yield StreamItem.ImageUint(image)

def generate_waveform() -> Generator[StreamItem, None, None]:
    for i in range(10):
        waveform_data = np.array([[1, 2, 3],[4, 5, 6]], dtype=np.uint32)
        waveform_time_stamp = i
        waveform = Waveform[np.uint32](data=waveform_data, time_stamp=waveform_time_stamp)
        yield StreamItem.WaveformUint32(waveform)

# with BinaryMrdReader(read_filename) as r:
#     existing_header = r.read_header()
#     existing_data = r.read_data()
with BinaryMrdWriter(write_filename) as w:
    empty_header = Header()
    w.write_header(empty_header)
    # w.write_data(generate_image())
    w.write_data(generate_waveform())