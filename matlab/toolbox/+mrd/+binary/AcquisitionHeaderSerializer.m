% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef AcquisitionHeaderSerializer < yardl.binary.RecordSerializer
  methods
    function self = AcquisitionHeaderSerializer()
      field_serializers{1} = yardl.binary.EnumSerializer('mrd.AcquisitionFlags', @mrd.AcquisitionFlags, yardl.binary.Uint64Serializer);
      field_serializers{2} = mrd.binary.EncodingCountersSerializer();
      field_serializers{3} = yardl.binary.Uint32Serializer;
      field_serializers{4} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{5} = yardl.binary.OptionalSerializer(yardl.binary.Uint64Serializer);
      field_serializers{6} = yardl.binary.VectorSerializer(yardl.binary.Uint64Serializer);
      field_serializers{7} = yardl.binary.VectorSerializer(yardl.binary.Uint32Serializer);
      field_serializers{8} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{9} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{10} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{11} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{12} = yardl.binary.OptionalSerializer(yardl.binary.Uint64Serializer);
      field_serializers{13} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{14} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{15} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{16} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{17} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{18} = yardl.binary.VectorSerializer(yardl.binary.Int32Serializer);
      field_serializers{19} = yardl.binary.VectorSerializer(yardl.binary.Float32Serializer);
      self@yardl.binary.RecordSerializer('mrd.AcquisitionHeader', field_serializers);
    end

    function write(self, outstream, value)
      arguments
        self
        outstream (1,1) yardl.binary.CodedOutputStream
        value (1,1) mrd.AcquisitionHeader
      end
      self.write_(outstream, value.flags, value.idx, value.measurement_uid, value.scan_counter, value.acquisition_time_stamp_ns, value.physiology_time_stamp_ns, value.channel_order, value.discard_pre, value.discard_post, value.center_sample, value.encoding_space_ref, value.sample_time_ns, value.position, value.read_dir, value.phase_dir, value.slice_dir, value.patient_table_position, value.user_int, value.user_float);
    end

    function value = read(self, instream)
      fields = self.read_(instream);
      value = mrd.AcquisitionHeader(flags=fields{1}, idx=fields{2}, measurement_uid=fields{3}, scan_counter=fields{4}, acquisition_time_stamp_ns=fields{5}, physiology_time_stamp_ns=fields{6}, channel_order=fields{7}, discard_pre=fields{8}, discard_post=fields{9}, center_sample=fields{10}, encoding_space_ref=fields{11}, sample_time_ns=fields{12}, position=fields{13}, read_dir=fields{14}, phase_dir=fields{15}, slice_dir=fields{16}, patient_table_position=fields{17}, user_int=fields{18}, user_float=fields{19});
    end
  end
end
