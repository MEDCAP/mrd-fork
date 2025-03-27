% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef AccelerationFactorType < handle
  properties
    kspace_encoding_step_1
    kspace_encoding_step_2
  end

  methods
    function self = AccelerationFactorType(kwargs)
      arguments
        kwargs.kspace_encoding_step_1 = uint32(0);
        kwargs.kspace_encoding_step_2 = uint32(0);
      end
      self.kspace_encoding_step_1 = kwargs.kspace_encoding_step_1;
      self.kspace_encoding_step_2 = kwargs.kspace_encoding_step_2;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.AccelerationFactorType") && ...
        isequal({self.kspace_encoding_step_1}, {other.kspace_encoding_step_1}) && ...
        isequal({self.kspace_encoding_step_2}, {other.kspace_encoding_step_2});
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
      elem = mrd.AccelerationFactorType();
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
