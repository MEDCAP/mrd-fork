"""
Helper function to fill acquisition fields from twixFile object 
"""
import os
from typing import Iterable
from scipy.io import loadmat
import numpy as np
from mapvbvd import mapVBVD

import mrd

def parse_acq_from_twix(twixFile: mapVBVD) -> Iterable[mrd.Acquisition]:
    '''
    Generate an mrd acquisition object from twixFile object
    parameter:
        twixFile: twixFile object
    return
        acq: mrd acquisition object
    '''
    acq = mrd.Acquisition()
    acq.data.resize(())
    