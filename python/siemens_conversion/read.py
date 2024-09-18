import mrd

filename = 'siemens_mrd.bin'

# Read the MRD file
with mrd.BinaryMrdReader(filename) as r:
    head = r.read_header()
    if head is None:
        raise Exception("Could not read header")
    print('fields: ', head.__dict__.keys())
    print('\n index: ', head.user_parameters.__dict__.keys(), '\n')
    # print('\n index: ', head.sequence_parameters, '\n')
    for f in head.__dict__.keys():
        if head.__dict__[f] is None:    # some field-value is None
            print('field:', f, ' -value:', head.__dict__[f])
            continue
        if isinstance(head.__dict__[f], list):  # encoding field is a list
            for k in head.__dict__[f][0].__dict__.keys():   # encoding field keys
                if head.__dict__[f][0].__dict__[k] is None:
                    print('field:', f, ' -key:', k, ' -value:', head.__dict__[f][0].__dict__[k])
                else:
                    for p in head.__dict__[f][0].__dict__[k].__dict__.keys():
                        # if field-key-param-value exists
                        if p[0] != '_':
                            print('field:', f, ' -key:', k, ' -param:', p, ' -value:', head.__dict__[f][0].__dict__[k].__dict__[p])
                        else:
                            # trajectory field only has field-key-value and the rest is class obj, type, etc.
                            print('field:', f, ' -key:', k, ' -value:', head.__dict__[f][0].__dict__[k])
                            break
        else:
            for k in head.__dict__[f].__dict__.keys():
                print('field:', f, ' -key:', k, ' -value:', head.__dict__[f].__dict__[k])
    data_stream = r.read_data()
    # for i in data_stream:
    #     pass

