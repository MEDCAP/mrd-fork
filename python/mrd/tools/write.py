import datetime
import numpy as np
import os
from mapvbvd import mapVBVD
import mrd

# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as n-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data-import datetime
import numpy as np
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_datap
import os
from mapvbvd import mapVBVD

# import readers writers class from yardl generated python files
from binary import BinaryMrdWriter
from .. import types as mrd # import all types definition


# decode dat file with mapvbvd
dat_filename = "meas_MID01060_FID23027_c13_spspsp_BPAL_inj2.dat"
twixObj = mapVBVD(dat_filename)

# add header
def generate_header(hdr, target_filename):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    * Values can be set to None
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
        target_filename: mrd filename to be generated
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.tPatientName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight        # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = hdr.PatientBirthDay       # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.lPatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    year, month, day = map(int, hdr.StudyDate.split('-'))
    study_info.study_date = datetime.date(year, month, day)
    study_info.study_time = mrd.Time(int(hdr.StudyTime * 1e9))  # Convert to nanoseconds
    study_info.study_id = hdr.StudyID
    study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    study_info.referring_physician_name = hdr.ReferringPhysician
    study_info.study_description = hdr.StudyDescription
    study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.BodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = hdr.DeviceSerialNumber
    year, month, day = map(int, hdr.SeriesDate.split('-'))
    meas_info.series_date = datetime.date(year, month, day)
    meas_info.series_time = mrd.Time(int(hdr.SeriesTime * 1e9))
    meas_info.patient_position = mrd.PatientPosition[hdr.PatientPosition]
    meas_info.initial_series_number = int(hdr.SeriesNumber)
    meas_info.protocol_name = hdr.ProtocolName
    meas_info.series_description = hdr.SeriesDescription
    meas_info.measurement_dependency = []  # Fill if dependencies exist
    meas_info.series_instance_uid_root = hdr.SeriesInstanceUIDRoot
    meas_info.frame_of_reference_uid = hdr.FrameOfReferenceUID
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.ManufacturerName
    sys_info.system_model = hdr.DeviceModel
    sys_info.system_field_strength_t = float(hdr.FieldStrength)
    sys_info.relative_receiver_noise_bandwidth = 0.8  # Default value
    sys_info.receiver_channels = hdr.iMaxNoOfRxChannels
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.StationName
    sys_info.device_serial_number = hdr.DeviceSerialNumber
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = int(hdr.Frequency)
    h.experimental_conditions = exp

    # Get encoding space parameters from header
    nkx = hdr.iNoOfFourierColumns  # Number of columns (500)
    nky = hdr.iNoOfFourierLines    # Number of lines (4)
    ms = hdr.lBaseResolution      # Base resolution (500)
    fov = hdr.lPhaseEncodingLines * hdr.dPhaseResolution  # FOV in phase direction
    slice_thickness = hdr.dThickness if hasattr(hdr, 'dThickness') else 5.0  # Default to 5mm if not specified
    oversampling = hdr.iNoOfFourierColumns / hdr.iMaxNoOfColumns if hdr.iMaxNoOfColumns > 0 else 1.0    

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596     
    e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596       
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0
    limit1.maximum = hdr.lPhaseEncodingLines - 1
    limit1.center = hdr.lPhaseEncodingLines // 2
    # kspace_encoding_step_2
    limit2 = mrd.LimitType()
    limit2.minimum = 0
    limit2.maximum = 0
    limit2.center = 0   
    # average
    limit_avg = mrd.LimitType()
    limit_avg.minimum = 0
    limit_avg.maximum = 0
    limit_avg.center = 0
    # slice
    limit_slc = mrd.LimitType()
    limit_slc.minimum = 0
    limit_slc.maximum = 0
    limit_slc.center = 0
    # contrast
    limit_cnt = mrd.LimitType()
    limit_cnt.minimum = 0
    limit_cnt.maximum = 0
    limit_cnt.center = 0
    # phase
    limit_phs = mrd.LimitType()
    limit_phs.minimum = 0
    limit_phs.maximum = 0
    limit_phs.center = 0
    # repetition
    limit_rep = mrd.LimitType()
    limit_rep.minimum = 0
    limit_rep.maximum = hdr.lRepetitions - 1
    limit_rep.center = 0
    # set
    limit_set = mrd.LimitType()
    limit_set.minimum = 0
    limit_set.maximum = 0
    limit_set.center = 0
    # segment
    limit_sgm = mrd.LimitType()
    limit_sgm.minimum = 0
    limit_sgm.maximum = 0
    limit_sgm.center = 0
    # encoding limits
    limits = mrd.EncodingLimitsType()
    limits.kspace_encoding_step_0 = None
    limits.kspace_encoding_step_1 = limit1
    limits.kspace_encoding_step_2 = limit2
    limits.average = limit_avg
    limits.slice = limit_slc
    limits.contrast = limit_cnt
    limits.phase = limit_phs
    limits.repetition = limit_rep
    limits.set = limit_set
    limits.segment = limit_sgm
    limits.user_0 = None
    limits.user_1 = None
    limits.user_2 = None
    limits.user_3 = None
    limits.user_4 = None
    limits.user_5 = None
    limits.user_6 = None
    limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    enc.parallel_imaging = mrd.ParallelImagingType(
        acceleration_factor=mrd.AccelerationFactorType(
            kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
            kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
        ),
        calibration_mode=mrd.CalibrationMode.OTHER,
        interleaving_dimension=None,
        multiband=None
    )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [float(hdr.lTR/1000.0)]  # Convert from us to ms
    seq.t_e = [float(te/1000.0) for te in hdr.alTE if te > 0]  # Convert from us to ms
    seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    seq.sequence_type = hdr.tSequenceString
    seq.echo_spacing = []  # Not available in header
    seq.diffusion_dimension = None  # Not a diffusion sequence
    seq.diffusion = []
    seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    wave_info.waveform_name = 'ECG'             # string
    wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # UserParametersType defined at @types.py 1245
    wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
                                                       user_parameter_double=[], # name: str, value: float64
                                                       user_parameter_string=[], # name: str, value: str
                                                       user_parameter_base64=[]) # name: str, value: str
    h.waveform_information.append(wave_info)
    return h


if __name__ == '__main__':
    dir = 'data'
    write_filename = 'simulated_mrd.bin'
    write_filename = os.path.join(dir, write_filename)
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)   # save header information before write_data