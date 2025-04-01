% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef ImageHeaderSerializer < yardl.binary.RecordSerializer
  methods
    function self = ImageHeaderSerializer()
      field_serializers{1} = yardl.binary.EnumSerializer('mrd.ImageFlags', @mrd.ImageFlags, yardl.binary.Uint64Serializer);
      field_serializers{2} = yardl.binary.Uint32Serializer;
      field_serializers{3} = yardl.binary.Uint32Serializer;
      field_serializers{4} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{5} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{6} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{7} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{8} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{9} = yardl.binary.FixedNDArraySerializer(yardl.binary.Float32Serializer, [3]);
      field_serializers{10} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{11} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{12} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{13} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{14} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{15} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{16} = yardl.binary.OptionalSerializer(yardl.binary.Uint64Serializer);
      field_serializers{17} = yardl.binary.VectorSerializer(yardl.binary.Uint64Serializer);
      field_serializers{18} = yardl.binary.EnumSerializer('mrd.ImageType', @mrd.ImageType, yardl.binary.Int32Serializer);
      field_serializers{19} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{20} = yardl.binary.OptionalSerializer(yardl.binary.Uint32Serializer);
      field_serializers{21} = yardl.binary.VectorSerializer(yardl.binary.Int32Serializer);
      field_serializers{22} = yardl.binary.VectorSerializer(yardl.binary.Float32Serializer);
      self@yardl.binary.RecordSerializer('mrd.ImageHeader', field_serializers);
    end

    function write(self, outstream, value)
      arguments
        self
        outstream (1,1) yardl.binary.CodedOutputStream
        value (1,1) mrd.ImageHeader
      end
      self.write_(outstream, value.flags, value.measurement_uid, value.measurement_freq, value.field_of_view, value.position, value.col_dir, value.line_dir, value.slice_dir, value.patient_table_position, value.average, value.slice, value.contrast, value.phase, value.repetition, value.set, value.acquisition_time_stamp_ns, value.physiology_time_stamp_ns, value.image_type, value.image_index, value.image_series_index, value.user_int, value.user_float);
    end

    function value = read(self, instream)
      fields = self.read_(instream);
      value = mrd.ImageHeader(flags=fields{1}, measurement_uid=fields{2}, measurement_freq=fields{3}, field_of_view=fields{4}, position=fields{5}, col_dir=fields{6}, line_dir=fields{7}, slice_dir=fields{8}, patient_table_position=fields{9}, average=fields{10}, slice=fields{11}, contrast=fields{12}, phase=fields{13}, repetition=fields{14}, set=fields{15}, acquisition_time_stamp_ns=fields{16}, physiology_time_stamp_ns=fields{17}, image_type=fields{18}, image_index=fields{19}, image_series_index=fields{20}, user_int=fields{21}, user_float=fields{22});
    end
  end
end
