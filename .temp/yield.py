import mrd

# Produce Acquisitions via a Python generator - simulating a stream
def generate_data():
    nreps = 2
    scan_counter = 0
    for _ in range(nreps):
        acq = mrd.Acquisition()
        acq.scan_counter = scan_counter
        scan_counter += 1
        yield mrd.StreamItem.Acquisition(acq)
    print('scan_counter:', scan_counter)


header = mrd.Header()
# Populate Header
# ...

with mrd.BinaryMrdWriter("test.bin") as w:
    w.write_header(header)
    w.write_data(generate_data())

with mrd.BinaryMrdReader("test.bin") as r:
    header = r.read_header()
    data_stream = r.read_data()
    for item in data_stream:
        data_keys = item.value.__dict__.keys()
        for k in data_keys:
            print('key:', k, ' -value:', item.value.__dict__[k])
        pass
