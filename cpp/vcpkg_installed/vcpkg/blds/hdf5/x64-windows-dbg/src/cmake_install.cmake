# Install script for directory: C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src

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
  include("C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/src/H5FDsubfiling/cmake_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "headers" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/hdf5.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5api_adpt.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5encode.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5public.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Apublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5ACpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Cpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Dpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Epubgen.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Epublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5ESdevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5ESpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Fpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDcore.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDdevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDdirect.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDfamily.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDhdfs.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDlog.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDmirror.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDmpi.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDmpio.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDmulti.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDonion.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDros3.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDs3comms.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDsec2.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDsplitter.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDstdio.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDwindows.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDsubfiling/H5FDsubfiling.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5FDsubfiling/H5FDioc.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Gpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Idevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Ipublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Ldevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Lpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Mpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5MMpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Opublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Ppublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5PLextern.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5PLpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Rpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Spublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Tdevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Tpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5TSdevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5VLconnector.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5VLconnector_passthru.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5VLnative.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5VLpassthru.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5VLpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Zdevelop.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Zpublic.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5Epubgen.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5version.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/src/df5_1.14.6-3417ba69ef.clean/src/H5overflow.h"
    "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/src/H5pubconf.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "libraries" OR NOT CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg]|[Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE FILE OPTIONAL FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/bin/hdf5_D.pdb")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "libraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY OPTIONAL FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/bin/hdf5_D.lib")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "libraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE SHARED_LIBRARY FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/bin/hdf5_D.dll")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "libraries" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/CMakeFiles/hdf5.pc")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "C:/Users/kento/dev/mrd-fork/cpp/vcpkg_installed/vcpkg/blds/hdf5/x64-windows-dbg/src/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
