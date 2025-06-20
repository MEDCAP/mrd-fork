"""
- Get acquisition data from mat file
- Get image data from mat file
- Get pulse sequence from Siemens IDEA simulator
- Write mrd stream item to file
"""
from scipy.io import loadmat
import numpy as np
from typing import Iterable

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
    # amplitude=(coils, samples), phase=(samples)
    pulse.amplitude = loadmat(pulse_amp_filename)['data'].astype(np.float32)
    pulse.phase = loadmat(pulse_phase_filename)['data'].astype(np.float32).flatten()
    yield mrd.StreamItem.Pulse(pulse)

def parse_image_from_mat(mat_filename):
    '''
    Extract image matrix from reconstructed mat file
    parameter:
        mat_filename: reconstructed mat file (channels, MSx, MSy, slices, measurements, metabolites)
    return:
        mrd.Image object
    '''
    # data shape=(channels, MSx, MSy, slices, measurements, metabolites)
    data = loadmat(mat_filename)['data']
    for islice in range(data.shape[3]):
        for imeas in range(data.shape[4]):
            for imet in range(data.shape[5]):
                image = abs(data[:, :, :, islice, imeas, imet]) # magnitude image
                [channels, MSx, MSy] = image.shape
                # ImageData dimensions=(channels, z, y, x)
                image = np.reshape(image, (channels, 1, MSy, MSx))  
                imghdr = mrd.ImageHeader(image_type=mrd.ImageType.MAGNITUDE)
                imghdr.slice = islice
                imghdr.image_index = imeas
                imghdr.contrast = imet
                mrd_image = mrd.Image[np.float64](head=imghdr, data=image, meta={})
                yield mrd_image

def stream_item(input: Iterable[mrd.Image[np.float64]]) -> Iterable[mrd.StreamItem]:
    for item in input:
        if isinstance(item, mrd.Image):
            yield mrd.StreamItem.ImageDouble(item)

def generate_data(pulse_amp_filename, pulse_phase_filename, mat_filename):
    yield from parse_pulse_from_idea(pulse_amp_filename, pulse_phase_filename)
    yield from stream_item(parse_image_from_mat(mat_filename))