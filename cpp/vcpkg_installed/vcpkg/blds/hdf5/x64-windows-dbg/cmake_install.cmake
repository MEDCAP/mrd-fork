# Install script for directory: C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/pkgs/hdf5_x64-windows/debug")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "OFF")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/src/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/utils/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/hl/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/c++/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/hl/c++/cmake_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "configinstall" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/hdf5/hdf5-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/hdf5/hdf5-targets.cmake"
         "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/Export/b760cdf53cc4ab638d33cc787081df22/hdf5-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/hdf5/hdf5-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/hdf5/hdf5-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hdf5" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/Export/b760cdf53cc4ab638d33cc787081df22/hdf5-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hdf5" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/Export/b760cdf53cc4ab638d33cc787081df22/hdf5-targets-debug.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "configinstall" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hdf5" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/hdf5-config.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "configinstall" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hdf5" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/hdf5-config-version.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "libraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/src/libhdf5.settings")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "hdfdocuments" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hdf5/data" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/COPYING")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "hdfdocuments" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/hdf5/data" TYPE FILE FILES
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/release_docs/USING_HDF5_CMake.txt"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/release_docs/RELEASE.txt"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/release_docs/USING_HDF5_VS.txt"
    )
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
