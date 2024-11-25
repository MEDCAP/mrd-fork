'''
Storing float32 into uint16 and restoring
'''
import numpy as np
import time

np.random.seed(0)
size = 10**6
input_a = np.random.normal(0, 33.33, size).astype(np.float32)

smallest_idx = np.where(input_a==np.min(np.abs(input_a)))
norm = np.linalg.norm(input_a)
a = input_a/norm
a_range = np.max(a) - np.min(a)
uint32_max = np.iinfo(np.uint32).max
uint32_min = np.iinfo(np.uint32).min

def quantization():
    # method1: quantization
    s = np.float64(a_range/uint32_max)
    z = np.round((np.max(a)*uint32_min- np.min(a)*uint32_max)/a_range)

    packed_a = np.clip(np.round(a/s + z), uint32_min, uint32_max)
    packed_a = packed_a.astype(np.uint32)

    unpacked_a = s * (packed_a - z)
    unpacked_a = unpacked_a.astype(np.float32)
    return unpacked_a

def packing():
    # method2: pack with our method: at max value, the division error gives overflow
    offset = np.float64(a) - np.float64(np.min(a))      # max(a) - min(a)
    temp = np.float64(uint32_max)+1
    packed_a = np.clip(np.float64(offset/a_range) * temp, uint32_min, uint32_max)  # double precision
    packed_a = packed_a.astype(np.uint32)

    unpacked_a = packed_a * a_range / temp + np.min(a) + a_range/(2*temp)
    unpacked_a = unpacked_a.astype(np.float32)
    return unpacked_a


if __name__ == '__main__':
    print('input', input_a)
    # method1
    start_time = time.time()
    unpacked_a = quantization()
    method1_time = time.time() - start_time
    print('method1', unpacked_a*norm)
    print('quantization error:', np.linalg.norm(unpacked_a*norm - input_a)/np.linalg.norm(input_a))
    print('method1 time:', method1_time)

    print('\n')
    # method2
    start_time = time.time()
    unpacked_a = packing()
    method2_time = time.time() - start_time
    print('method2', unpacked_a*norm)
    print('packing error:', np.linalg.norm(unpacked_a*norm - input_a)/np.linalg.norm(input_a))
    print('method2 time:', method2_time)
