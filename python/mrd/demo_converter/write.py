'''
Generate an MRD2+ file from Siemens dat file 
Each fields are filled with the helper functions imported
'''
# set the path to \root\python directory to run code
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)
from mrd import BinaryMrdWriter
from mrd import types as mrd # import all types definition

# import helper functions to fill in each space
from write_header import generate_header

# read file from dat file
dat_filename = "meas_MID00070_FID50886_c13_sp3_timeOptimal_inj1.dat"
twixObj = mapVBVD(dat_filename)
hdr = twixObj.hdr['Meas']
# generate mrd.header from dat header
h = generate_header(hdr)

write_filename = 'test_mrd.bin'
with BinaryMrdWriter(write_filename) as w:
    w.write_header(h)   # save header information before write_data
    