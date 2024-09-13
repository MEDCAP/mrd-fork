import numpy as np

'''
Example code to read and write custom field defined in model.yml
Code taken from: 
    https://microsoft.github.io/yardl/python/quickstart.html
    https://microsoft.github.io/yardl/reference/binary.html

Findings
- Need to Write and Read in the order of fields on model.yml
- Cannot skip writing or reading field, thus need to write an empty data and read it
Documentation: https://microsoft.github.io/yardl/matlab/language.html#protocols

- Datatypes are not automatically converted, need to convert it before writing
- End of sequence for cpp is already included in python as close() function
'''


from stream_test import (
    BinaryMyProtocolWriter,
    BinaryMyProtocolReader,
    Header,
    Sample,
    Point,
    DateTime,
    Fruits,
)

path = "test.bin"

def generate_sample():
    # yield Sample(data=[])
    yield Sample(data=[4,5,6])
    # optionalData will be set as None

with BinaryMyProtocolWriter(path) as w:
    # order of write must follow model.yml field declaration order
    w.write_header(Header(subject="test"))
    w.write_float_array(np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)) 
    w.write_samples(generate_sample())
    w.write_points([Point(x=1, y=2), Point(x=3, y=4), Point(x=5, y=6)])
    w.write_points([Point(x=700, y=800), Point(x=900, y=1000)])
    # enum
    fruit1 = Fruits.PEAR
    fruit2 = Fruits.BANANA
    fruit3 = Fruits.APPLE
    # end of stream already included?

with BinaryMyProtocolReader(path) as r:
    print(r.read_header())
    for f in r.read_float_array():
        print('f', f)
    for sample in r.read_samples():
        print('s', sample)
    for p in r.read_points():
        print('p', p)
    print('fruit', fruit1.name, fruit1.value)
    print('fruit', fruit2.name, fruit2.value)