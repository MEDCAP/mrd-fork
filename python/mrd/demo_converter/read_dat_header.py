import numpy as np
from matplotlib import pyplot as plt 
from mapvbvd import mapVBVD


vbfile = "../rawdata/meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(vbfile)

output = []
for k in twixObj.hdr["Meas"].keys():
    if "timestamp" in k.lower():
        output.append({k: twixObj.hdr["Meas"][k]})
    if twixObj.hdr["Meas"][k] == "":
        continue
print(output)