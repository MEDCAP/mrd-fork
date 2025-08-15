import numpy as np
import argparse

from pathlib import Path    # append mrd-fork/python/ to Path to import mrd module locally
import sys
path_root = Path(__file__).parents[2]   
sys.path.insert(0, str(path_root))  # Insert at beginning to prioritize local version
import mrd  # local library mrd not from conda

import time

def read_mrd(filename):
    # Method 1: Raw byte reading
    # start_time = time.time()
    # with open(filename, 'rb') as file:
    #     data = file.read(10096)
    #     print(data)

    # Method 2: MRD Reader
    # start_time = time.time()
    with mrd.BinaryMrdReader(filename) as r:
        head = r.read_header()
        # list all available keys in the header
        print('Header fields: ', head.__dict__.keys())
        print(head.encoding)
    #     # field-key-value-param
    #     for f in head.__dict__.keys():
    #         if f == "study_information":
    #             print(head.__dict__[f])
            # if head.__dict__[f] is None or not head.__dict__[f]:  # if field-value is None
            #     print('field:', f, ' -value:', head.__dict__[f])
            #     continue
            # elif (isinstance(head.__dict__[f], list) and head.__dict__[f]):  # if field-value is a list, read the first element
            #     field = head.__dict__[f][0].__dict__
            #     keys = head.__dict__[f][0].__dict__.keys()
            # else:   # if field-value is not None, read as dict
            #     field = head.__dict__[f].__dict__
            #     keys = head.__dict__[f].__dict__.keys()
            # for k in keys:
            #     try:
            #         for p in field[k].__dict__.keys():
            #             if p[0]=='_':
            #                 continue
            #             else:
            #                 print('field:', f, ' -key:', k, ' -param:', p, ' -value:', field[k].__dict__[p])
            #     except:
            #         if isinstance(field[k], list):
            #             for i in range(len(field[k])):
            #                 print('field:', f, ' -key:', k, ' -listvalue:', field[k][i])
            #         else:
            #             print('field:', f, ' -key:', k, ' -value:', field[k])
        
        # # list all the keys available in the data
        
        # counter = 0
        data_stream = r.read_data()
        acq_counter = 0
        img_counter = 0
        wf_counter = 0
        for item in data_stream:
            if isinstance(item, mrd.StreamItem.Acquisition):
                acq_counter += 1
                print("acquisition", item.value.data.shape)
            elif isinstance(item, mrd.StreamItem.ImageFloat):
                img_counter += 1
                print("image", item.value.data.shape)
                print('meas', item.value.head.repetition)
                print('slice', item.value.head.slice)
                print('metabolite', item.value.head.measurement_freq)
            elif isinstance(item, mrd.StreamItem.WaveformUint32):
                wf_counter += 1
                print("waveform", item.value.data.shape)
        print("acq_counter", acq_counter)
        print("img_counter", img_counter)
        print("wf_counter", wf_counter)

        # for item in data_stream:
        #     data_keys = item.value.__dict__.keys()
            # if isinstance(item, mrd.StreamItem.Pulse):
            #     print('pulse:', item.value.amplitude.shape)
                
            # elif isinstance(item, (mrd.StreamItem.ImageFloat)):
            #     print('image')
            #     print(item.value.data.shape)

            # elif isinstance(item, mrd.StreamItem.Acquisition):
            #     print('acquisition')
            #     print(item.value.data.shape)
            #     print(item.value.phase.shape)
            # elif isinstance(item, mrd.StreamItem.Gradient):
            #     print('gradient')
            #     print(item.value.rl.shape)
            #     print(item.value.ap.shape)
            #     print(item.value.fh.shape)
            # # waveform
            # elif isinstance(item, mrd.StreamItem.WaveformUint32):
            #     pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="read mrd2+ file")
    parser.add_argument('-f', '--file', type=str, required=False, help="File to read")
    args = parser.parse_args()
    read_mrd(args.file)