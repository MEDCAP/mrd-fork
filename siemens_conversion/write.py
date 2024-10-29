import mrd
import datetime

'''
Generate header and acquisition data
input:
    write_filename: name of the file to write to
'''
def generate(write_filename):
    ms = 64                 # matrix size
    fov = 30.0              # field of view in cm
    slice_thickness = 1     # slice thickness in cm
    oversampling = 1.3      # oversampling factor
    nkx = ms                # number of kx
    nky = oversampling * ms # number of ky: phase oversampling

    # Header object
    h = mrd.Header()
    '''
    * Values are optional. If not set, they will be set to None
    * Some values are extracted from Siemens scanner as sample data
    '''
    # subject_information schema defined at @types.py 249
    subject_info = mrd.SubjectInformationType()
    subject_info.patient_name = "Simulated Data"               # string
    subject_info.patient_weight_kg = float(70)                 # float
    subject_info.patient_height_m = float(1.75)                # float
    subject_info.patient_id = None                             # string
    subject_info.patient_birthdate = datetime.date(1990, 1, 1) # datetime
    subject_info.patient_gender = mrd.PatientGender.M          # PatientGender class defined at @types.py 244
    h.subject_information = subject_info    # assign subject_info to header

    # study_information schema defined at @types.py 290
    study_info = mrd.StudyInformationType()
    study_info.study_date = datetime.date(2024, 10, 29)     # datetime
    study_info.study_time = mrd.Time(hours=10, minutes=30)  # Time defined in @yardl_types.py 120
    study_info.study_id = None                              # string
    study_info.accession_number = None                      # int64
    study_info.referring_physician_name = None              # string
    study_info.study_description = "Simulated Data"         # string
    study_info.study_instance_uid = None                    # string
    study_info.body_part_examined = "Kidney"                # string
    h.study_information = study_info

    # measurement_information schema defined at @types.py 424
    meas_info = mrd.MeasurementInformationType()
    meas_info.measurement_id = "57146_95876468_95876477_173"    # string
    meas_info.series_date = datetime.date(2024, 10, 29)         # datetime
    meas_info.series_time = mrd.Time(hours=10, minutes=30)      # Time defined in @yardl_types.py 120
    meas_info.patient_position = mrd.PatientPosition.H_FS       # PatientPosition class defined at @types.py 339
    meas_info.relative_table_position = mrd.ThreeDimensionalFloat(x=0.0, y=0.0, z=0.0) # ThreeDimensionalFloat defined at @types.py 349
    meas_info.initial_series_number = 1                         # int64
    meas_info.protocol_name = "fa_spiral_dyn_fancy_v2_20230131" # string
    meas_info.series_description = "Simulated series"           # string
    meas_info.measurement_dependency = [mrd.MeasurementDependencyType(dependency_type='', measurement_id='')]     # MeasurmentDependencyType defined at @types.py 378
    meas_info.series_instance_uid_root = None                   # string
    meas_info.frame_of_reference_uid = None                     # string
    meas_info.reference_image_sequence = mrd.ReferenceImageSequenceType(reference_sop_instance_uid=None) # ReferenceImageSequenceType defined at @types.py 403
    h.measurement_information = meas_info

    # acquisition_system_information schema defined at @types.py 518
    sys_info = mrd.AcquisitionSystemInformationType()
    sys_info.system_vendor = "Siemens"              # string
    sys_info.system_model = "Avanto"                # string
    sys_info.system_field_strength_t = 1.5          # float32
    sys_info.relative_receiver_noise_bandwidth = 0.8# float32
    sys_info.receiver_channels = 1                  # uint32
    sys_info.coil_label = mrd.CoilLabel(coilNumber=3, coilName="XnoneCP2:1:Xe") # CoilLabel defined at @types.py 493
    sys_info.institution_name = "HUP"               # string
    sys_info.station_name = None                    # string
    sys_info.device_id = "57146"                    # string
    sys_info.device_serial_number = None            # string
    h.acquisition_system_information = sys_info

    # experimental_conditions
    exp = mrd.ExperimentalConditionsType()
    exp.h1resonance_frequency_hz = 17611981         # int64
    h.experimental_conditions = exp

    # encoded_space
    e = mrd.EncodingSpaceType()
    e.matrix_size = mrd.MatrixSizeType(x=nkx, y=nky, z=1) # MatrixSizeType defined at @types.py 596
    e.field_of_view_mm = mrd.FieldOfViewMm(x=oversampling*fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # recon_space
    r = mrd.EncodingSpaceType()
    r.matrix_size = mrd.MatrixSizeType(x=ms, y=ms, z=1) # MatrixSizeType defined at @types.py 596
    r.field_of_view_mm = mrd.FieldOfViewMm(x=fov, y=fov, z=slice_thickness) # FieldOfViewMm defined at @types.py 605
    # kspace_encoding_step_1
    limit1 = mrd.LimitType()
    limit1.minimum = 0  # uint32
    limit1.maximum = 19 # uint32
    limit1.center = 10  # uint32
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
    limit_rep = mrd.limittype()
    limit_rep.minimum = 0  
    limit_rep.maximum = 2024  
    limit_rep.center = 0
    # set
    limit_set = mrd.limittype()
    limit_set.minimum = 0  
    limit_set.maximum = 0  
    limit_set.center = 0
    # segment
    limit_sgm = mrd.limittype()
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
    enc.parallel_imaging = mrd.ParallelImagingType(acceleration_factor=mrd.AccelerationFactorType(kspace_encoding_step_1=1,
                                                                                                  kspace_encoding_step_2=1),
                                                   calibration_mode=mrd.CalibrationMode.OTHER,
                                                   interleaving_dimension=None,
                                                   multiband=None) # ParallelImagingType defined at @types.py 819
    enc.echo_train_length = None           # int64
    h.encoding.append(enc)  # h.encoding is a list of EncodingType
    
    # sequence_parameters
    seq = mrd.SequenceParametersType()
    seq.t_r = [14.899999618530273] # list of float32
    seq.t_e = [0.6200000047683716] # list of float32
    seq.t_i = [150.0]              # list of float32
    seq.flip_angle_deg = [3.5]     # list of float32
    seq.sequence_type = None       # string
    seq.echo_spacing = []          # list of float32
    seq.diffusion_dimension = None # DiffusionDimension defined at @types.py 1097
    seq.diffusion = []             # list of DiffusionType defined at @types.py 1142
    seq.diffusion_scheme = None    # string
    h.sequence_parameters = seq

    # user_parameters
    # WHATEVERY YOU WANT

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

    # write to header
    with mrd.BinaryMrdWriter(write_filename) as w:
        w.write_header(h)


# def generate_data() -> Generator[StreamItem, None, None]:
#     acq = Acquisition()
#     yield StreamItem.Acquisition(acq)

# def generate_image() -> Generator[StreamItem, None, None]:
#     image = Image()
#     yield StreamItem.ImageUint(image)

# def generate_waveform() -> Generator[StreamItem, None, None]:
#     for i in range(10):
#         waveform_data = np.array([[1, 2, 3],[4, 5, 6]], dtype=np.uint32)
#         waveform_time_stamp = i
#         waveform = Waveform[np.uint32](data=waveform_data, time_stamp=waveform_time_stamp)
#         yield StreamItem.WaveformUint32(waveform)


def main():
    write_filename = 'simulated_mrd.bin'
    generate(write_filename)

if __name__ == '__main__':
    main()