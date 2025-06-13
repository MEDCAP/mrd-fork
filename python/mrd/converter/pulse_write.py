"""
Helper function to fill in pulse and gradient fields from Siemens IDEA simulator 
"""
import os
from typing import Iterable
from scipy.io import loadmat
import numpy as np

import mrd

def parse_pulse_from_idea(dirpath: str) -> Iterable[mrd.Pulse]:
    '''
    Generate an mrd pulse sequence from Siemens IDEA simulator
    parameter:
        dirpath: directory path where pulse mat files stored
        assuming that all files are stored in the same directory with filenames
        set as field names from Siemens IDEA simulator
    return:
        pulse_sequence: mrd pulse object
    '''
    header = mrd.PulseHeader()
    header.pulse_time_stamp_ns = 0
    header.channel_order = [1]
    header.sample_time_ns = 1000    # 10us extracted every 10rows from simulator
    # header.pulse_calibration = []
    pulse = mrd.Pulse()
    pulse.head = header
    pulse_amp_filename = os.path.join(dirpath, "RF-Signal (ch. 0, 1H, 123.2 MHz).mat")
    pulse_phase_filename = os.path.join(dirpath, "Numeric Crystal Oscillator 1 Phase.mat")
    pulse.amplitude = loadmat(pulse_amp_filename)['data'].astype(np.float32)
    pulse.phase = loadmat(pulse_phase_filename)['data'].astype(np.float32)
    yield mrd.StreamItem.Pulse(pulse)

def parse_gradient_from_idea(dirpath: str) -> Iterable[mrd.Gradient]:
    '''
    Parse gradient from Siemens IDEA simulator and return mrd gradient object as stream
    parameter:
        dirpath: directory with gradient mat files stored
    return:
        gradient_sequence: mrd gradient object
    '''
    header = mrd.GradientHeader()
    header.gradient_time_stamp_ns = 0
    header.gradient_sample_time_ns = 1000
    gradient = mrd.Gradient()
    gradient.head = header
    gx_filepath = os.path.join(dirpath, "X Gradient (GPA 0).mat")
    gy_filepath = os.path.join(dirpath, "Y Gradient (GPA 0).mat")
    gz_filepath = os.path.join(dirpath, "Z Gradient (GPA 0).mat")
   # squeeze mat files (1, samples)
    gradient.rl = loadmat(gx_filepath)['data'].astype(np.float32).squeeze()
    gradient.ap = loadmat(gy_filepath)['data'].astype(np.float32).squeeze()
    gradient.fh = loadmat(gz_filepath)['data'].astype(np.float32).squeeze()
    yield mrd.StreamItem.Gradient(gradient)