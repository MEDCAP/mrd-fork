# Install script for directory: C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/hl/c++/src

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

if(CMAKE_INSTALL_COMPONENT STREQUAL "hlcppheaders" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/hl/c++/src/H5PacketTable.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "hlcpplibraries" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg]|[Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE FILE OPTIONAL FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/bin/hdf5_hl_cpp_D.pdb")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "hlcpplibraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY OPTIONAL FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/bin/hdf5_hl_cpp_D.lib")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "hlcpplibraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE SHARED_LIBRARY FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/bin/hdf5_hl_cpp_D.dll")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "hlcpplibraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/hdf5_hl_cpp.pc")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/hl/c++/src/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
