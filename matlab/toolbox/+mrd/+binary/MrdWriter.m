% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef MrdWriter < yardl.binary.BinaryProtocolWriter & mrd.MrdWriterBase
  % Binary writer for the Mrd protocol
  properties (Access=protected)
    header_serializer
    data_serializer
  end

  methods
    function self = MrdWriter(filename)
      self@mrd.MrdWriterBase();
      self@yardl.binary.BinaryProtocolWriter(filename, mrd.MrdWriterBase.schema);
      self.header_serializer = yardl.binary.OptionalSerializer(mrd.binary.HeaderSerializer());
      self.data_serializer = yardl.binary.StreamSerializer(yardl.binary.UnionSerializer('mrd.StreamItem', {mrd.binary.AcquisitionSerializer(), mrd.binary.WaveformSerializer(yardl.binary.Uint32Serializer), mrd.binary.ImageSerializer(yardl.binary.Uint16Serializer), mrd.binary.ImageSerializer(yardl.binary.Int16Serializer), mrd.binary.ImageSerializer(yardl.binary.Uint32Serializer), mrd.binary.ImageSerializer(yardl.binary.Int32Serializer), mrd.binary.ImageSerializer(yardl.binary.Float32Serializer), mrd.binary.ImageSerializer(yardl.binary.Float64Serializer), mrd.binary.ImageSerializer(yardl.binary.Complexfloat32Serializer), mrd.binary.ImageSerializer(yardl.binary.Complexfloat64Serializer), mrd.binary.AcquisitionBucketSerializer(), mrd.binary.ReconDataSerializer(), yardl.binary.DynamicNDArraySerializer(yardl.binary.Complexfloat32Serializer), mrd.binary.ImageArraySerializer()}, {@mrd.StreamItem.Acquisition, @mrd.StreamItem.WaveformUint32, @mrd.StreamItem.ImageUint16, @mrd.StreamItem.ImageInt16, @mrd.StreamItem.ImageUint32, @mrd.StreamItem.ImageInt32, @mrd.StreamItem.ImageFloat, @mrd.StreamItem.ImageDouble, @mrd.StreamItem.ImageComplexFloat, @mrd.StreamItem.ImageComplexDouble, @mrd.StreamItem.AcquisitionBucket, @mrd.StreamItem.ReconData, @mrd.StreamItem.ArrayComplexFloat, @mrd.StreamItem.ImageArray}));
    end
  end

  methods (Access=protected)
    function write_header_(self, value)
      self.header_serializer.write(self.stream_, value);
    end

    function write_data_(self, value)
      self.data_serializer.write(self.stream_, value);
    end
  end
end
