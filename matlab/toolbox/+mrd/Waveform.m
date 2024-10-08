% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef Waveform < handle
  properties
    flags
    measurement_uid
    scan_counter
    time_stamp
    sample_time_us
    waveform_id
    data
  end

  methods
    function self = Waveform(kwargs)
      arguments
        kwargs.flags = uint64(0);
        kwargs.measurement_uid = uint32(0);
        kwargs.scan_counter = uint32(0);
        kwargs.time_stamp = uint32(0);
        kwargs.sample_time_us = single(0);
        kwargs.waveform_id = uint32(0);
        kwargs.data;
      end
      self.flags = kwargs.flags;
      self.measurement_uid = kwargs.measurement_uid;
      self.scan_counter = kwargs.scan_counter;
      self.time_stamp = kwargs.time_stamp;
      self.sample_time_us = kwargs.sample_time_us;
      self.waveform_id = kwargs.waveform_id;
      if ~isfield(kwargs, "data")
        throw(yardl.TypeError("Missing required keyword argument 'data'"))
      end
      self.data = kwargs.data;
    end

    function res = channels(self)
      res = size(self.data, ndims(self.data)-(0));
      return
    end

    function res = number_of_samples(self)
      res = size(self.data, ndims(self.data)-(1));
      return
    end


    function res = eq(self, other)
      res = ...
        isa(other, "mrd.Waveform") && ...
        isequal(self.flags, other.flags) && ...
        isequal(self.measurement_uid, other.measurement_uid) && ...
        isequal(self.scan_counter, other.scan_counter) && ...
        isequal(self.time_stamp, other.time_stamp) && ...
        isequal(self.sample_time_us, other.sample_time_us) && ...
        isequal(self.waveform_id, other.waveform_id) && ...
        isequal(self.data, other.data);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

end
