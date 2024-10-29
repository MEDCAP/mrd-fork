import sys
sys.path.append('..')
from python.mrd import (
    BinaryMrdReader,
    StreamItem,
    MrdReaderBase)

# change filename below to read different files
# filename = 'empty_mrd.bin'      # mrd file with empty fields
filename = 'siemens_mrd.bin'    # mrd file converted from siemens raw data
# filename = 'simulated_mrd.bin'  # mrd file with simulated data

with BinaryMrdReader(filename) as r:
    # read header values
    head = r.read_header()
    if head is None:
        raise Exception("Could not read header")

    print('fields: ', head.__dict__.keys())
    # field-key-value-param
    for f in head.__dict__.keys():
        if head.__dict__[f] is None or not head.__dict__[f]:  # if field-value is None
            print('field:', f, ' -value:', head.__dict__[f])
            continue
        elif (isinstance(head.__dict__[f], list) and head.__dict__[f]):  # if field-value is a list, read the first element
            field = head.__dict__[f][0].__dict__
            keys = head.__dict__[f][0].__dict__.keys()
        else:   # if field-value is not None, read as dict
            field = head.__dict__[f].__dict__
            keys = head.__dict__[f].__dict__.keys()
        for k in keys:
            try:
                for p in field[k].__dict__.keys():
                    if p[0]=='_':
                        continue
                    else:
                        print('field:', f, ' -key:', k, ' -param:', p, ' -value:', field[k].__dict__[p])
            except:
                if isinstance(field[k], list):
                    for i in range(len(field[k])):
                        print('field:', f, ' -key:', k, ' -listvalue:', field[k][i])
                else:
                    print('field:', f, ' -key:', k, ' -value:', field[k])

    print('\n Data Stream:')
    data_stream = r.read_data()
    counter = 0
    # waveform data
    for item in data_stream:
        if isinstance(item, StreamItem.WaveformUint32):
            for k in item.value.__dict__.keys():
                if k[0] == '_':
                    continue
                elif k=='data':
                    print('key:', k, ' -data:', item.value.__dict__[k])
                    # print shape of data
                    # print('key:', k, ' -shape:', item.value.__dict__[k].shape)
                    continue
                elif k=='time_stamp':
                    print('key:', k, ' -value:', item.value.__dict__[k])

#     # image data but does not exist yet as this is pre-reconstruction
#     # for item in data_stream:
#     #     break
#     #     if isinstance(item, (mrd.StreamItem.ImageComplexDouble,
#     #                          mrd.StreamItem.ImageComplexFloat,
#     #                          mrd.StreamItem.ImageDouble,
#     #                          mrd.StreamItem.ImageFloat,
#     #                          mrd.StreamItem.ImageInt,
#     #                          mrd.StreamItem.ImageUint,
#     #                          mrd.StreamItem.ImageUint16,
#     #                          mrd.StreamItem.ImageInt16)):
#     #         print('image')
#     #         print(item.value.__dict__.keys())
    
    # # Acquisition data
    # for item in data_stream:
    #     print(item.value.__dict__.keys())
    #     if isinstance(item, StreamItem.Acquisition):

    #         for k in item.value.__dict__.keys():
    #             if k[0] == '_':
    #                 continue
    #             if k=='acquisition_time_stamp':
    #                 print('key:', k, item.value.__dict__[k])
    #             # if k=='user_float':
    #             #     print('key:', k, item.value.__dict__[k])