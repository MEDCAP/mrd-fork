% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef SamplingDescription < handle
  properties
    encoded_fov
    recon_fov
    encoded_matrix
    recon_matrix
    sampling_limits
  end

  methods
    function self = SamplingDescription(kwargs)
      arguments
        kwargs.encoded_fov = mrd.FieldOfViewMm();
        kwargs.recon_fov = mrd.FieldOfViewMm();
        kwargs.encoded_matrix = mrd.MatrixSizeType();
        kwargs.recon_matrix = mrd.MatrixSizeType();
        kwargs.sampling_limits = mrd.SamplingLimits();
      end
      self.encoded_fov = kwargs.encoded_fov;
      self.recon_fov = kwargs.recon_fov;
      self.encoded_matrix = kwargs.encoded_matrix;
      self.recon_matrix = kwargs.recon_matrix;
      self.sampling_limits = kwargs.sampling_limits;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.SamplingDescription") && ...
        isequal(self.encoded_fov, other.encoded_fov) && ...
        isequal(self.recon_fov, other.recon_fov) && ...
        isequal(self.encoded_matrix, other.encoded_matrix) && ...
        isequal(self.recon_matrix, other.recon_matrix) && ...
        isequal(self.sampling_limits, other.sampling_limits);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.SamplingDescription();
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
