# append mrd-fork/python/ to Path to import mrd module locally
from pathlib import Path    
import sys
path_root = Path(__file__).parents[2]   
sys.path.append(str(path_root))
import mrd
assert Path(mrd.__file__).parents[2] == Path(__file__).parents[3], \
    f"import source of mrd is not local: {Path(mrd.__file__)}"

filename = 'test_mrd.bin'    
with mrd.BinaryMrdReader(filename) as r:
    head = r.read_header()
    print(head.__dict__.keys())

    print('\n Data Stream:')
    data_stream = r.read_data()
    for item in data_stream:
        if isinstance(item, mrd.StreamItem.Pulse):
            print(item.value.__dict__.keys())
        elif isinstance(item, mrd.StreamItem.Gradient):
            print(item.value.__dict__.keys())
#     waveform_dict = {}
#     for item in data_stream:
#         if isinstance(item, mrd.StreamItem.WaveformUint32):
#             header_idx = waveid_idx_dict[item.value.waveform_id] # corresponding header idx
#             header = head.waveform_information[header_idx]       # corresponding header
#             waveform_name = header.waveform_name
#             user_parameters = header.user_parameters
#             user_param_long = user_parameters.user_parameter_long
#             user_param_double = user_parameters.user_parameter_double
#             user_param_string = user_parameters.user_parameter_string
            
#             scale_factor = user_param_double[0].value
#             zero_point = user_param_double[1].value
#             array_norm = user_param_double[2].value
#             waveform_data = dequantize(item.value.data, scale_factor, zero_point, array_norm)
#             waveform_dict[waveform_name] = waveform_data
#             channel_count = item.value.channels()
#             sample_size = item.value.number_of_samples()

#     pulse_shape = waveform_dict['pulse_shape']
#     gradient = waveform_dict['gradient']
#     gx = gradient[0, :]
#     gy = gradient[1, :]
#     gz = gradient[2, :]
#     B1 = waveform_dict['B1']
#     B1x = B1[0, :]
#     B1y = B1[1, :]
#     dt = 10
#     t = np.linspace(0, dt*sample_size, sample_size)
    
# # figure plot setting 
# fig, ax = plt.subplots()
# fig.subplots_adjust(right=0.85)
# ax.set_ylabel('gradients (T/m)')
# ax.yaxis.label.set_color('b')   # grad in blue
# ax.tick_params(axis='y', colors='b') 
# B1ax = ax.twinx()
# B1ax.set_ylabel('B1 (V)')   
# B1ax.yaxis.label.set_color('g')   # B1 in green
# B1ax.tick_params(axis='y', colors='g')

# # plot data
# B1ax.plot(t, B1x, color='g', linestyle='dashed', label='B1x_V')
# B1ax.plot(t, B1y, color='g', linestyle='dotted', label='B1y_V')
# ymax = 1.05*max(np.max(np.abs(B1x)), np.max(np.abs(B1y)))
# B1ax.set_ylim(bottom=-ymax,top=ymax)
# B1ax.legend(loc=4)
# ax.plot(t, gx, color='b',linestyle='dashed', label='gx:readout')
# ax.plot(t, gy, color='r',linestyle='dotted', label='gy:phase-encoding')
# ax.plot(t, gz, color='y',linestyle='dashdot', label='gz:slice-selection')
# ymax = 1.05*max(np.max(np.abs(gx)), np.max(np.abs(gy)), np.max(np.abs(gz)))
# ax.set_ylim(bottom=-ymax,top=ymax)
# ax.legend(loc=3)
# plt.show()
 
#     # counter = 0
#     data_stream = r.read_data()
#     # for item in data_stream:
#     #     data_keys = item.value.__dict__.keys()
#     #     # waveform
#     #     if isinstance(item, mrd.StreamItem.WaveformUint32):
#     #         for k in data_keys:
#     #             if k[0] == '_':
#     #                 continue
#     #             elif k=='data':
#     #                 print('key:', k, ' -data:', item.value.__dict__[k])
#     #                 # print shape of data
#     #                 print('key:', k, ' -shape:', item.value.__dict__[k].shape)
#     #                 counter += 1
#     #             elif k=='channels':
#     #                 counter+=1
#     #                 print('key:', k, ' -value:', item.value.__dict__[k])
#     #             else:
#     #                 continue
    
#     # image data but does not exist yet as this is pre-reconstruction
#     for item in data_stream:
#         if isinstance(item, (mrd.StreamItem.ImageComplexDouble,
#                              mrd.StreamItem.ImageComplexFloat,
#                              mrd.StreamItem.ImageDouble,
#                              mrd.StreamItem.ImageFloat,
#                              mrd.StreamItem.ImageInt,
#                              mrd.StreamItem.ImageUint,
#                              mrd.StreamItem.ImageUint16,
#                              mrd.StreamItem.ImageInt16)):
#             print('image')
#             print(item.value.__dict__.keys())
    
#     # # Acquisition data
#     # for item in data_stream:
#     #     print(item.value.__dict__.keys())
#     #     if isinstance(item, mrd.StreamItem.Acquisition):
#     #         for k in item.value.__dict__.keys():
#     #             if k[0] == '_':
#     #                 continue
#     #             if k=='acquisition_time_stamp':
#     #                 print('key:', k, item.value.__dict__[k])
#     #             else:
#     #                 print('key:', k, item.value.__dict__[k])