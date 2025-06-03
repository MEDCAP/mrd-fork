'''
Generate an MRD2+ file from Siemens dat file through mapvbvd
Each fields are filled with the helper functions imported
'''
import sys
import os
import numpy as np
import re
from typing import BinaryIO, Iterable, Union

from mapvbvd import mapVBVD

from pathlib import Path    # append mrd-fork/python/ to Path to import mrd module locally
import sys
path_root = Path(__file__).parents[2]   
sys.path.append(str(path_root))
import mrd
assert Path(mrd.__file__).parents[2] == Path(__file__).parents[3], \
    f"import source of mrd is not local: {Path(mrd.__file__)}"

from mrd.converter.header_write import parse_header_from_dat
from mrd.converter.pulse_write import parse_pulse_from_idea

# dat file to extract from
dat_filename  = "C:\\Users\\kento\\dev\\rawdata\\recon_siemens\\052825_liver_mrd1\\meas_MID00095_FID56528_c13_spspsp_BPAL_inj1_fasted.dat"
twixObj = mapVBVD(dat_filename)
hdr = twixObj.hdr['Meas']
# pulse sequence from Siemens IDEA simulator
pulse_amp_filename= "C:\\Users\\kento\\dev\\rawdata\\gradient_siemens\\RF-Signal (ch. 0, 1H, 123.2 MHz).mat"
pulse_phase_filename= "C:\\Users\\kento\\dev\\rawdata\\gradient_siemens\\Numeric Crystal Oscillator 1 Phase.mat"
# convert mapvbvd object to mrd object
h = parse_header_from_dat(hdr)

write_filename = 'test_mrd.bin'
with mrd.BinaryMrdWriter(write_filename) as w:
    w.write_header(h)   # save header information before write_data
    # write pulse sequence
    w.write_data(parse_pulse_from_idea(pulse_amp_filename, pulse_phase_filename))