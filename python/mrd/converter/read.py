import numpy as np

from pathlib import Path    # append mrd-fork/python/ to Path to import mrd module locally
import sys
path_root = Path(__file__).parents[2]   
sys.path.append(str(path_root))
import mrd  # local library mrd not from conda

filename = 'test_mrd.bin'    
with mrd.BinaryMrdReader(filename) as r:
    head = r.read_header()
    # list all available keys in the header
    print('Header fields: ', head.__dict__.keys())
    # field-key-value-param
    # for f in head.__dict__.keys():
    #     if head.__dict__[f] is None or not head.__dict__[f]:  # if field-value is None
    #         print('field:', f, ' -value:', head.__dict__[f])
    #         continue
    #     elif (isinstance(head.__dict__[f], list) and head.__dict__[f]):  # if field-value is a list, read the first element
    #         field = head.__dict__[f][0].__dict__
    #         keys = head.__dict__[f][0].__dict__.keys()
    #     else:   # if field-value is not None, read as dict
    #         field = head.__dict__[f].__dict__
    #         keys = head.__dict__[f].__dict__.keys()
    #     for k in keys:
    #         try:
    #             for p in field[k].__dict__.keys():
    #                 if p[0]=='_':
    #                     continue
    #                 else:
    #                     print('field:', f, ' -key:', k, ' -param:', p, ' -value:', field[k].__dict__[p])
    #         except:
    #             if isinstance(field[k], list):
    #                 for i in range(len(field[k])):
    #                     print('field:', f, ' -key:', k, ' -listvalue:', field[k][i])
    #             else:
    #                 print('field:', f, ' -key:', k, ' -value:', field[k])
    
    # # list all the keys available in the data
    
    # counter = 0
    data_stream = r.read_data()
    for item in data_stream:
        data_keys = item.value.__dict__.keys()
        print(data_keys)
        if isinstance(item, mrd.StreamItem.Pulse):
            print('pulse:', item.value.amplitude.shape)
            
        elif isinstance(item, (mrd.StreamItem.ImageFloat)):
            print('image')
            print(item.value.data.shape)

        elif isinstance(item, mrd.StreamItem.Acquisition):
            print('acquisition')
        # waveform
        elif isinstance(item, mrd.StreamItem.WaveformUint32):
            pass
