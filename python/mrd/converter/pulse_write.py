"""
Helper function to fill in pulse sequence from Siemens IDEA simulator 
"""
from scipy.io import loadmat
import numpy as np

import mrd

def parse_pulse_from_idea(pulse_amp_filename, pulse_phase_filename):
    '''
    Generate an mrd pulse sequence from Siemens IDEA simulator
    parameter:
        idea_file: Siemens IDEA simulator file
    return:
        pulse_sequence: mrd pulse object
    '''
    header = mrd.PulseHeader()
    header.pulse_time_stamp_ns = 0
    header.channel_order = [1]
    header.sample_time_ns = int(1e3)
    # header.pulse_calibration = []
    pulse = mrd.Pulse()
    pulse.head = header
    pulse.amplitude = loadmat(pulse_amp_filename)['data'].astype(np.float32)
    pulse.phase = loadmat(pulse_phase_filename)['data'].astype(np.float32)
    yield mrd.StreamItem.Pulse(pulse)