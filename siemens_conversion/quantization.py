import numpy as np

def quantize(array):
    '''
    Normalize and quantize array from float to uint32 to store as MRD format
    parameter:
        array: array in any float
    return:
        quantized_array: quantized array in uint32
        s: scalar factor
        z: zero point
        norm: norm of the input array to renormalize at dequantize
    '''
    if array.size == 0:
        raise Exception('Empty array to be quantized')
    norm = np.linalg.norm(array)
    array = array/norm if norm else array
    array_range = np.max(array) - np.min(array)
    uint32_max = np.iinfo(np.uint32).max                # maximum value of uint32
    uint32_min = np.iinfo(np.uint32).min                # minimum value of uint32
    if np.max(array) == np.min(array):                  # if array is constant set s to non-zero
        array_range = 1
    s = np.float64(array_range/(uint32_max-uint32_min)) # scale factor
    z = np.round((np.max(array)*uint32_min-np.min(array)*uint32_max)/array_range) # zero point
    quantized_array = np.round(array/s + z)
    quantized_array = np.clip(quantized_array, uint32_min, uint32_max) # clip within uint32 range
    return quantized_array.astype(np.uint32), s, z, norm    

def dequantize(quantized_array, s, z, norm):
    '''
    Return quantized array as float32  
    parameter:
        quantized_array: quantized array in uint32
        s: scalar factor
        z: zero point
        norm: norm of the input array to renormalize at dequantize
    return
        array: dequantized array in float32
    '''
    array = (quantized_array - z) * s
    array *= norm
    return array.astype(np.float32)