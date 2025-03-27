% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef EncodingLimitsType < handle
  properties
    kspace_encoding_step_0
    kspace_encoding_step_1
    kspace_encoding_step_2
    average
    slice
    contrast
    phase
    repetition
    set
    segment
    user_0
    user_1
    user_2
    user_3
    user_4
    user_5
    user_6
    user_7
  end

  methods
    function self = EncodingLimitsType(kwargs)
      arguments
        kwargs.kspace_encoding_step_0 = yardl.None;
        kwargs.kspace_encoding_step_1 = yardl.None;
        kwargs.kspace_encoding_step_2 = yardl.None;
        kwargs.average = yardl.None;
        kwargs.slice = yardl.None;
        kwargs.contrast = yardl.None;
        kwargs.phase = yardl.None;
        kwargs.repetition = yardl.None;
        kwargs.set = yardl.None;
        kwargs.segment = yardl.None;
        kwargs.user_0 = yardl.None;
        kwargs.user_1 = yardl.None;
        kwargs.user_2 = yardl.None;
        kwargs.user_3 = yardl.None;
        kwargs.user_4 = yardl.None;
        kwargs.user_5 = yardl.None;
        kwargs.user_6 = yardl.None;
        kwargs.user_7 = yardl.None;
      end
      self.kspace_encoding_step_0 = kwargs.kspace_encoding_step_0;
      self.kspace_encoding_step_1 = kwargs.kspace_encoding_step_1;
      self.kspace_encoding_step_2 = kwargs.kspace_encoding_step_2;
      self.average = kwargs.average;
      self.slice = kwargs.slice;
      self.contrast = kwargs.contrast;
      self.phase = kwargs.phase;
      self.repetition = kwargs.repetition;
      self.set = kwargs.set;
      self.segment = kwargs.segment;
      self.user_0 = kwargs.user_0;
      self.user_1 = kwargs.user_1;
      self.user_2 = kwargs.user_2;
      self.user_3 = kwargs.user_3;
      self.user_4 = kwargs.user_4;
      self.user_5 = kwargs.user_5;
      self.user_6 = kwargs.user_6;
      self.user_7 = kwargs.user_7;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.EncodingLimitsType") && ...
        isequal({self.kspace_encoding_step_0}, {other.kspace_encoding_step_0}) && ...
        isequal({self.kspace_encoding_step_1}, {other.kspace_encoding_step_1}) && ...
        isequal({self.kspace_encoding_step_2}, {other.kspace_encoding_step_2}) && ...
        isequal({self.average}, {other.average}) && ...
        isequal({self.slice}, {other.slice}) && ...
        isequal({self.contrast}, {other.contrast}) && ...
        isequal({self.phase}, {other.phase}) && ...
        isequal({self.repetition}, {other.repetition}) && ...
        isequal({self.set}, {other.set}) && ...
        isequal({self.segment}, {other.segment}) && ...
        isequal({self.user_0}, {other.user_0}) && ...
        isequal({self.user_1}, {other.user_1}) && ...
        isequal({self.user_2}, {other.user_2}) && ...
        isequal({self.user_3}, {other.user_3}) && ...
        isequal({self.user_4}, {other.user_4}) && ...
        isequal({self.user_5}, {other.user_5}) && ...
        isequal({self.user_6}, {other.user_6}) && ...
        isequal({self.user_7}, {other.user_7});
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end

    function res = isequal(self, other)
      res = all(eq(self, other));
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.EncodingLimitsType();
      if nargin == 0
        z = elem;
        return;
      end
      sz = [varargin{:}];
      if isscalar(sz)
        sz = [sz, sz];
      end
      z = reshape(repelem(elem, prod(sz)), sz);
    end
  end
end
