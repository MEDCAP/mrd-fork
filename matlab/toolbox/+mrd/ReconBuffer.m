% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef ReconBuffer < handle
  properties
    % Buffered Acquisition data
    data
    % Buffered Trajectory data
    trajectory
    % Buffered Density weights
    density
    % Buffered AcquisitionHeaders
    headers
    % Sampling details for these Acquisitions
    sampling
  end

  methods
    function self = ReconBuffer(kwargs)
      arguments
        kwargs.data = single.empty(0, 0, 0, 0, 0, 0, 0);
        kwargs.trajectory = single.empty(0, 0, 0, 0, 0, 0, 0);
        kwargs.density = yardl.None;
        kwargs.headers = mrd.AcquisitionHeader.empty(0, 0, 0, 0, 0);
        kwargs.sampling = mrd.SamplingDescription();
      end
      self.data = kwargs.data;
      self.trajectory = kwargs.trajectory;
      self.density = kwargs.density;
      self.headers = kwargs.headers;
      self.sampling = kwargs.sampling;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.ReconBuffer") && ...
        isequal(self.data, other.data) && ...
        isequal(self.trajectory, other.trajectory) && ...
        isequal(self.density, other.density) && ...
        isequal(self.headers, other.headers) && ...
        isequal(self.sampling, other.sampling);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.ReconBuffer();
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