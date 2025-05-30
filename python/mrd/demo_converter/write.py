from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)
from mrd import BinaryMrdWriter
from mrd import types as mrd # import all types definition
from mapvbvd import mapVBVD

def generate_header(dat_hdr):
    h = mrd.Header()

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeighWt        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info 

    return h

if __name__ == '__main__':
    # read file from dat file
    dat_filename = "meas_MID00070_FID50886_c13_sp3_timeOptimal_inj1.dat"
    twixObj = mapVBVD(dat_filename)
    hdr = twixObj.hdr['Meas']
    # generate mrd.header from dat header
    h = generate_header(hdr)

    write_filename = 'test_mrd.bin'
    with BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data
