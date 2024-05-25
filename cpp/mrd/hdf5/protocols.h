// This file was generated by the "yardl" tool. DO NOT EDIT.

#pragma once
#include <array>
#include <complex>
#include <optional>
#include <variant>
#include <vector>

#include "../protocols.h"
#include "../types.h"
#include "../yardl/detail/hdf5/io.h"

namespace mrd::hdf5 {
// HDF5 writer for the Mrd protocol.
class MrdWriter : public mrd::MrdWriterBase, public yardl::hdf5::Hdf5Writer {
  public:
  MrdWriter(std::string path);

  protected:
  void WriteHeaderImpl(std::optional<mrd::Header> const& value) override;

  void WriteDataImpl(mrd::StreamItem const& value) override;

  void EndDataImpl() override;

  public:
  void Flush() override;

  private:
  std::unique_ptr<yardl::hdf5::UnionDatasetWriter<10>> data_dataset_state_;
};

// HDF5 reader for the Mrd protocol.
class MrdReader : public mrd::MrdReaderBase, public yardl::hdf5::Hdf5Reader {
  public:
  MrdReader(std::string path);

  void ReadHeaderImpl(std::optional<mrd::Header>& value) override;

  bool ReadDataImpl(mrd::StreamItem& value) override;

  private:
  std::unique_ptr<yardl::hdf5::UnionDatasetReader<10>> data_dataset_state_;
};

} // namespace mrd
