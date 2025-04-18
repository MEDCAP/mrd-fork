% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef WaveformSerializer < yardl.binary.RecordSerializer
  methods
    function self = WaveformSerializer(t_serializer)
      field_serializers{1} = yardl.binary.Uint64Serializer;
      field_serializers{2} = yardl.binary.Uint32Serializer;
      field_serializers{3} = yardl.binary.Uint32Serializer;
      field_serializers{4} = yardl.binary.Uint64Serializer;
      field_serializers{5} = yardl.binary.Uint64Serializer;
      field_serializers{6} = yardl.binary.Uint32Serializer;
      field_serializers{7} = yardl.binary.NDArraySerializer(t_serializer, 2);
      self@yardl.binary.RecordSerializer('mrd.Waveform', field_serializers);
    end

    function write(self, outstream, value)
      arguments
        self
        outstream (1,1) yardl.binary.CodedOutputStream
        value (1,1) mrd.Waveform
      end
      self.write_(outstream, value.flags, value.measurement_uid, value.scan_counter, value.time_stamp_ns, value.sample_time_ns, value.waveform_id, value.data);
    end

    function value = read(self, instream)
      fields = self.read_(instream);
      value = mrd.Waveform(flags=fields{1}, measurement_uid=fields{2}, scan_counter=fields{3}, time_stamp_ns=fields{4}, sample_time_ns=fields{5}, waveform_id=fields{6}, data=fields{7});
    end
  end
end
