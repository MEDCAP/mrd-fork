#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "hdf5::hdf5-shared" for configuration "Debug"
set_property(TARGET hdf5::hdf5-shared APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(hdf5::hdf5-shared PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib/hdf5_D.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin/hdf5_D.dll"
  )

list(APPEND _cmake_import_check_targets hdf5::hdf5-shared )
list(APPEND _cmake_import_check_files_for_hdf5::hdf5-shared "${_IMPORT_PREFIX}/lib/hdf5_D.lib" "${_IMPORT_PREFIX}/bin/hdf5_D.dll" )

# Import target "hdf5::hdf5_hl-shared" for configuration "Debug"
set_property(TARGET hdf5::hdf5_hl-shared APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(hdf5::hdf5_hl-shared PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib/hdf5_hl_D.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin/hdf5_hl_D.dll"
  )

list(APPEND _cmake_import_check_targets hdf5::hdf5_hl-shared )
list(APPEND _cmake_import_check_files_for_hdf5::hdf5_hl-shared "${_IMPORT_PREFIX}/lib/hdf5_hl_D.lib" "${_IMPORT_PREFIX}/bin/hdf5_hl_D.dll" )

# Import target "hdf5::hdf5_cpp-shared" for configuration "Debug"
set_property(TARGET hdf5::hdf5_cpp-shared APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(hdf5::hdf5_cpp-shared PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib/hdf5_cpp_D.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin/hdf5_cpp_D.dll"
  )

list(APPEND _cmake_import_check_targets hdf5::hdf5_cpp-shared )
list(APPEND _cmake_import_check_files_for_hdf5::hdf5_cpp-shared "${_IMPORT_PREFIX}/lib/hdf5_cpp_D.lib" "${_IMPORT_PREFIX}/bin/hdf5_cpp_D.dll" )

# Import target "hdf5::hdf5_hl_cpp-shared" for configuration "Debug"
set_property(TARGET hdf5::hdf5_hl_cpp-shared APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(hdf5::hdf5_hl_cpp-shared PROPERTIES
  IMPORTED_IMPLIB_DEBUG "${_IMPORT_PREFIX}/lib/hdf5_hl_cpp_D.lib"
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/bin/hdf5_hl_cpp_D.dll"
  )

list(APPEND _cmake_import_check_targets hdf5::hdf5_hl_cpp-shared )
list(APPEND _cmake_import_check_files_for_hdf5::hdf5_hl_cpp-shared "${_IMPORT_PREFIX}/lib/hdf5_hl_cpp_D.lib" "${_IMPORT_PREFIX}/bin/hdf5_hl_cpp_D.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
