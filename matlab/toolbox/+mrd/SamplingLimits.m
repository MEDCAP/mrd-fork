% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef SamplingLimits < handle
  % Sampled range along E0, E1, E2 (for asymmetric echo and partial fourier)
  properties
    kspace_encoding_step_0
    kspace_encoding_step_1
    kspace_encoding_step_2
  end

  methods
    function self = SamplingLimits(kwargs)
      arguments
        kwargs.kspace_encoding_step_0 = mrd.LimitType();
        kwargs.kspace_encoding_step_1 = mrd.LimitType();
        kwargs.kspace_encoding_step_2 = mrd.LimitType();
      end
      self.kspace_encoding_step_0 = kwargs.kspace_encoding_step_0;
      self.kspace_encoding_step_1 = kwargs.kspace_encoding_step_1;
      self.kspace_encoding_step_2 = kwargs.kspace_encoding_step_2;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.SamplingLimits") && ...
        isequal(self.kspace_encoding_step_0, other.kspace_encoding_step_0) && ...
        isequal(self.kspace_encoding_step_1, other.kspace_encoding_step_1) && ...
        isequal(self.kspace_encoding_step_2, other.kspace_encoding_step_2);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.SamplingLimits();
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
