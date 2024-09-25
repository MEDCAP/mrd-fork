import sys
sys.path.append('..')
from mrd import (
    BinaryMrdReader,
    BinaryMrdWriter,
    StreamItem,
    Acquisition,
    AcquisitionFlags,
    Header)
from typing import Iterable

filename = 'modified_siemens_mrd.bin'

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


# with BinaryMrdWriter(filename) as w:
#     h = Header()
#     w.write_header(h)
#     # w.write_data(acquisition_reader(r.read_data()))


with BinaryMrdReader(filename) as r:
    print('header', r.read_header())
