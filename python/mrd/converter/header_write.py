"""
Helper function to read header from Siemens dat file through mapVBVD 
and fill in the corresponding fields in MRD header.
"""
import datetime

import mrd

def parse_header_from_dat(hdr):
    '''
    Generate an mrd header from Siemens dat file decoded with mapvbvd
    parameter:
        hdr: Siemens dat file header["Meas"] from mapvbvd
    return:
        h: mrd header object 
    '''
    h = mrd.Header()    # construct an empty header object

    # subject_information
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = hdr.PatientsName               # string
    subject_info.patient_weight_kg = hdr.flUsedPatientWeight   # float
    subject_info.patient_height_m = hdr.flPatientHeight / 1e3  # float
    subject_info.patient_id = hdr.PatientID                    # string
    subject_info.patient_birthdate = None                      # anomalized as string
    subject_info.patient_gender = mrd.PatientGender(int(hdr.PatientSex)) # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information
    study_info = mrd.StudyInformationType()
    date_str, time_str = hdr.PrepareTimestamp.split()
    study_info.study_date = datetime.date.fromisoformat(date_str) 
    study_info.study_time = mrd.Time.parse(time_str)  # nanoseconds since midnight
    study_info.study_id = hdr.StudyLoid
    # study_info.accession_number = int(hdr.AccessionNumber) if hdr.AccessionNumber else None
    # study_info.referring_physician_name = hdr.ReferringPhysician
    # study_info.study_description = hdr.StudyDescription
    # study_info.study_instance_uid = hdr.StudyInstanceUID
    study_info.body_part_examined = hdr.tBodyPartExamined
    h.study_information = study_info

    # measurement_information
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = str(hdr.MeasUid)
    datetime_str = hdr.PrepareTimestamp.split()
    meas_info.series_date = datetime.date.fromisoformat(datetime_str[0])
    meas_info.series_time = mrd.Time.parse(datetime_str[1])
    # meas_info.patient_position = mrd.PatientPosition[hdr.tPatientPosition]
    # meas_info.relative_table_position = []
    # meas_info.initial_series_number = None
    meas_info.protocol_name = hdr.tProtocolName
    meas_info.sequence_name = hdr.tSequenceFileName.split("\\")[1]
    # meas_info.series_description = None
    # meas_info.measurement_dependency = []
    # meas_info.series_instance_uid_root = None
    # meas_info.frame_of_reference_uid = None
    # meas_info.referenced_image_sequence = None
    h.measurement_information = meas_info

    # acquisition_system_information
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = hdr.Manufacturer
    sys_info.system_model = hdr.ManufacturersModelName
    sys_info.system_field_strength_t = hdr.flMagneticFieldStrength
    # sys_info.relative_receiver_noise_bandwidth = None
    sys_info.receiver_channels = int(hdr.iMaxNoOfUsedApplicationChannels)
    coil_number = [int(ch.replace("C", "")) for ch in hdr.atCoilSelectInfoText.split(";")]
    coil_name = hdr.TransmittingCoil
    sys_info.coil_label = [mrd.CoilLabelType(coil_number=i, coil_name=coil_name) for i in coil_number]
    sys_info.institution_name = hdr.InstitutionName
    sys_info.station_name = hdr.Ward
    # sys_info.device_id = None
    sys_info.device_serial_number = str(hdr.DeviceSerialNumber)
    h.acquisition_system_information = sys_info

    # experimental_conditions
    # exp = mrd.ExperimentalConditionsType()
    # exp.h1resonance_frequency_hz = 0
    # h.experimental_conditions = exp

    # Get encoding space parameters from header
    lines = hdr.iNoOfFourierLines   # interleaves
    turns = 4
    ms = int(lines * turns * 2)

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=ms, y=ms)  
    # e.field_of_view_mm = mrd.FieldOfViewMm(x=round(oversampling*fov), y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms) # MatrixSizeType defined at @types.py 596       
    # r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # # kspace_encoding_step_1
    # limit1 = mrd.LimitType()
    # limit1.minimum = 0
    # limit1.maximum = hdr.lPhaseEncodingLines - 1
    # limit1.center = hdr.lPhaseEncodingLines // 2
    # # kspace_encoding_step_2
    # limit2 = mrd.LimitType()
    # limit2.minimum = 0
    # limit2.maximum = 0
    # limit2.center = 0   
    # # average
    # limit_avg = mrd.LimitType()
    # limit_avg.minimum = 0
    # limit_avg.maximum = 0
    # limit_avg.center = 0
    # # slice
    # limit_slc = mrd.LimitType()
    # limit_slc.minimum = 0
    # limit_slc.maximum = 0
    # limit_slc.center = 0
    # # contrast
    # limit_cnt = mrd.LimitType()
    # limit_cnt.minimum = 0
    # limit_cnt.maximum = 0
    # limit_cnt.center = 0
    # # phase
    # limit_phs = mrd.LimitType()
    # limit_phs.minimum = 0
    # limit_phs.maximum = 0
    # limit_phs.center = 0
    # # repetition
    # limit_rep = mrd.LimitType()
    # limit_rep.minimum = 0
    # limit_rep.maximum = hdr.lRepetitions - 1
    # limit_rep.center = 0
    # # set
    # limit_set = mrd.LimitType()
    # limit_set.minimum = 0
    # limit_set.maximum = 0
    # limit_set.center = 0
    # # segment
    # limit_sgm = mrd.LimitType()
    # limit_sgm.minimum = 0
    # limit_sgm.maximum = 0
    # limit_sgm.center = 0
    # # encoding limits
    # limits = mrd.EncodingLimitsType()
    # limits.kspace_encoding_step_0 = None
    # limits.kspace_encoding_step_1 = limit1
    # limits.kspace_encoding_step_2 = limit2
    # limits.average = limit_avg
    # limits.slice = limit_slc
    # limits.contrast = limit_cnt
    # limits.phase = limit_phs
    # limits.repetition = limit_rep
    # limits.set = limit_set
    # limits.segment = limit_sgm
    # limits.user_0 = None
    # limits.user_1 = None
    # limits.user_2 = None
    # limits.user_3 = None
    # limits.user_4 = None
    # limits.user_5 = None
    # limits.user_6 = None
    # limits.user_7 = None
    # encoding
    enc = mrd.EncodingType()
    enc.encoded_space = e
    enc.recon_space = r
    # enc.encoding_limits = limits
    enc.trajectory = mrd.Trajectory.SPIRAL # Trajectory defined at @types.py 797
    enc.trajectory_description = None      # TrajectoryDescriptionType defined at @types.py 880
    # enc.parallel_imaging = mrd.ParallelImagingType(
    #     acceleration_factor=mrd.AccelerationFactorType(
    #         kspace_encoding_step_1=hdr.lAccelFactPE if hasattr(hdr, 'lAccelFactPE') else 1,
    #         kspace_encoding_step_2=hdr.lAccelFact3D if hasattr(hdr, 'lAccelFact3D') else 1
    #     ),
    #     calibration_mode=mrd.CalibrationMode.OTHER,
    #     interleaving_dimension=None,
    #     multiband=None
    # )
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType

    # sequence_parameters
    seq = mrd.SequenceParametersType()    
    seq.t_r = [float(x) / 1e3 for x in hdr.alTR.split()]  # Convert from us to ms
    seq.t_e = [float(x) / 1e3 for x in hdr.alTE.split()]  # Convert from us to ms
    # seq.t_i = [float(ti/1000.0) for ti in hdr.alTI if ti > 0]  # Convert from us to ms
    # seq.flip_angle_deg = [float(fa) for fa in hdr.adFlipAngleDegree if fa > 0]
    # seq.sequence_type = hdr.tSequenceString
    # seq.echo_spacing = []  # Not available in header
    # seq.diffusion_dimension = None  # Not a diffusion sequence
    # seq.diffusion = []
    # seq.diffusion_scheme = None
    h.sequence_parameters = seq

    # waveform_information
    # wave_info = mrd.WaveformInformationType()   # WaveformInformationType defined at @types.py 1286     
    # wave_info.waveform_name = 'ECG'             # string
    # wave_info.waveform_type = mrd.WaveformType.ECG # WaveformType defined at @types.py 1278
    # # UserParametersType defined at @types.py 1245
    # wave_info.user_parameters = mrd.UserParametersType(user_parameter_long=[],   # name: str, value: int64
    #                                                    user_parameter_double=[], # name: str, value: float64
    #                                                    user_parameter_string=[], # name: str, value: str
    #                                                    user_parameter_base64=[]) # name: str, value: str
    # h.waveform_information.append(wave_info)
    return h