include_directories(../)

add_executable(mrd_phantom mrd_phantom.cc shepp_logan_phantom.cc)
target_link_libraries(mrd_phantom mrd_generated fftw3f)

add_executable(mrd_hdf5_to_stream mrd_hdf5_to_stream.cc)
target_link_libraries(mrd_hdf5_to_stream mrd_generated)

add_executable(mrd_stream_to_hdf5 mrd_stream_to_hdf5.cc)
target_link_libraries(mrd_stream_to_hdf5 mrd_generated)

add_executable(mrd_stream_recon mrd_stream_recon.cc)
target_link_libraries(mrd_stream_recon fftw3f mrd_generated)

install(TARGETS
    mrd_hdf5_to_stream
    mrd_phantom
    mrd_stream_recon
    mrd_stream_to_hdf5
    DESTINATION bin)


find_package(ISMRMRD 1.13.4 REQUIRED)

if (ISMRMRD_FOUND)
  message(STATUS "ISMRMRD found: ${ISMRMRD_INCLUDE_DIR}")

  add_executable(ismrmrd_to_mrd ismrmrd_to_mrd.cc converters.cc)
  target_link_libraries(ismrmrd_to_mrd mrd_generated ISMRMRD::ISMRMRD)

  add_executable(mrd_to_ismrmrd mrd_to_ismrmrd.cc converters.cc)
  target_link_libraries(mrd_to_ismrmrd mrd_generated ISMRMRD::ISMRMRD)

  install(TARGETS ismrmrd_to_mrd mrd_to_ismrmrd DESTINATION bin)
else()
  message(STATUS "ISMRMRD not found. Skipping conversion tools.")
endif()


find_package(ImageMagick COMPONENTS Magick++)
find_package(fmt)

if (ImageMagick_FOUND AND fmt_FOUND)
  message(STATUS "ImageMagick and fmt found.")
  include_directories(${ImageMagick_INCLUDE_DIRS})

  add_executable(mrd_image_stream_to_png mrd_image_stream_to_png.cc)
  target_compile_options(mrd_image_stream_to_png PRIVATE "-DMAGICKCORE_QUANTUM_DEPTH=8" "-DMAGICKCORE_HDRI_ENABLE=0")
  target_link_libraries(mrd_image_stream_to_png mrd_generated ${ImageMagick_LIBRARIES} fmt::fmt)

  install(TARGETS mrd_image_stream_to_png DESTINATION bin)
else()
  message(STATUS "ImageMagick or fmt not found. Skipping mrd_image_stream_to_png.")
endif()
