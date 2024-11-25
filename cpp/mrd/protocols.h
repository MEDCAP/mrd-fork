// This file was generated by the "yardl" tool. DO NOT EDIT.

#pragma once
#include "types.h"

namespace mrd {
enum class Version {
  Current
};
// Abstract writer for the Mrd protocol.
// The MRD Protocol
class MrdWriterBase {
  public:
  // Ordinal 0.
  void WriteHeader(std::optional<mrd::Header> const& value);

  // Ordinal 1.
  // Call this method for each element of the `data` stream, then call `EndData() when done.`
  void WriteData(mrd::StreamItem const& value);

  // Ordinal 1.
  // Call this method to write many values to the `data` stream, then call `EndData()` when done.
  void WriteData(std::vector<mrd::StreamItem> const& values);

  // Marks the end of the `data` stream.
  void EndData();

  // Optionaly close this writer before destructing. Validates that all steps were completed.
  void Close();

  virtual ~MrdWriterBase() = default;

  // Flushes all buffered data.
  virtual void Flush() {}

  protected:
  virtual void WriteHeaderImpl(std::optional<mrd::Header> const& value) = 0;
  virtual void WriteDataImpl(mrd::StreamItem const& value) = 0;
  virtual void WriteDataImpl(std::vector<mrd::StreamItem> const& value);
  virtual void EndDataImpl() = 0;
  virtual void CloseImpl() {}

  static std::string schema_;

  static std::vector<std::string> previous_schemas_;

  static std::string SchemaFromVersion(Version version);

  private:
  uint8_t state_ = 0;

  friend class MrdReaderBase;
};

// Abstract reader for the Mrd protocol.
// The MRD Protocol
class MrdReaderBase {
  public:
  // Ordinal 0.
  void ReadHeader(std::optional<mrd::Header>& value);

  // Ordinal 1.
  [[nodiscard]] bool ReadData(mrd::StreamItem& value);

  // Ordinal 1.
  [[nodiscard]] bool ReadData(std::vector<mrd::StreamItem>& values);

  // Optionaly close this writer before destructing. Validates that all steps were completely read.
  void Close();

  void CopyTo(MrdWriterBase& writer, size_t data_buffer_size = 1);

  virtual ~MrdReaderBase() = default;

  protected:
  virtual void ReadHeaderImpl(std::optional<mrd::Header>& value) = 0;
  virtual bool ReadDataImpl(mrd::StreamItem& value) = 0;
  virtual bool ReadDataImpl(std::vector<mrd::StreamItem>& values);
  virtual void CloseImpl() {}
  static std::string schema_;

  static std::vector<std::string> previous_schemas_;

  static Version VersionFromSchema(const std::string& schema);

  private:
  uint8_t state_ = 0;
};

// Abstract writer for the MrdNoiseCovariance protocol.
// Protocol for serializing a noise covariance matrix
class MrdNoiseCovarianceWriterBase {
  public:
  // Ordinal 0.
  void WriteNoiseCovariance(mrd::NoiseCovariance const& value);

  // Optionaly close this writer before destructing. Validates that all steps were completed.
  void Close();

  virtual ~MrdNoiseCovarianceWriterBase() = default;

  // Flushes all buffered data.
  virtual void Flush() {}

  protected:
  virtual void WriteNoiseCovarianceImpl(mrd::NoiseCovariance const& value) = 0;
  virtual void CloseImpl() {}

  static std::string schema_;

  static std::vector<std::string> previous_schemas_;

  static std::string SchemaFromVersion(Version version);

  private:
  uint8_t state_ = 0;

  friend class MrdNoiseCovarianceReaderBase;
};

// Abstract reader for the MrdNoiseCovariance protocol.
// Protocol for serializing a noise covariance matrix
class MrdNoiseCovarianceReaderBase {
  public:
  // Ordinal 0.
  void ReadNoiseCovariance(mrd::NoiseCovariance& value);

  // Optionaly close this writer before destructing. Validates that all steps were completely read.
  void Close();

  void CopyTo(MrdNoiseCovarianceWriterBase& writer);

  virtual ~MrdNoiseCovarianceReaderBase() = default;

  protected:
  virtual void ReadNoiseCovarianceImpl(mrd::NoiseCovariance& value) = 0;
  virtual void CloseImpl() {}
  static std::string schema_;

  static std::vector<std::string> previous_schemas_;

  static Version VersionFromSchema(const std::string& schema);

  private:
  uint8_t state_ = 0;
};
} // namespace mrd
