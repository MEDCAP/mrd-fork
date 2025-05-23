% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef NoiseCovariance < handle
  properties
    % Comes from Header.acquisitionSystemInformation.coilLabel
    coil_labels
    % Comes from Header.acquisitionSystemInformation.relativeReceiverNoiseBandwidth
    receiver_noise_bandwidth
    % Comes from Acquisition.sampleTimeNs
    noise_dwell_time_ns
    % Number of samples used to compute matrix
    sample_count
    % Noise covariance matrix with dimensions [coil, coil]
    matrix
  end

  methods
    function self = NoiseCovariance(kwargs)
      arguments
        kwargs.coil_labels = mrd.CoilLabelType.empty();
        kwargs.receiver_noise_bandwidth = single(0);
        kwargs.noise_dwell_time_ns = uint64(0);
        kwargs.sample_count = uint64(0);
        kwargs.matrix = single.empty(0, 0);
      end
      self.coil_labels = kwargs.coil_labels;
      self.receiver_noise_bandwidth = kwargs.receiver_noise_bandwidth;
      self.noise_dwell_time_ns = kwargs.noise_dwell_time_ns;
      self.sample_count = kwargs.sample_count;
      self.matrix = kwargs.matrix;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.NoiseCovariance") && ...
        isequal(self.coil_labels, other.coil_labels) && ...
        isequal(self.receiver_noise_bandwidth, other.receiver_noise_bandwidth) && ...
        isequal(self.noise_dwell_time_ns, other.noise_dwell_time_ns) && ...
        isequal(self.sample_count, other.sample_count) && ...
        isequal(self.matrix, other.matrix);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.NoiseCovariance();
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
