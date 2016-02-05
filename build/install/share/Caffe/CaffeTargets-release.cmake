#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "caffe" for configuration "Release"
set_property(TARGET caffe APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(caffe PROPERTIES
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "proto;proto;/home/zhenyang/local/lib/libboost_system.so;/home/zhenyang/local/lib/libboost_thread.so;/usr/lib/x86_64-linux-gnu/libpthread.so;-lpthread;/home/zhenyang/local/lib/libglog.so;/home/zhenyang/local/lib/libgflags.so;/home/zhenyang/local/lib/libprotobuf.so;-lpthread;/usr/lib/x86_64-linux-gnu/libhdf5_hl.so;/usr/lib/x86_64-linux-gnu/libhdf5.so;/home/zhenyang/local/lib/liblmdb.so;/home/zhenyang/local/lib/libleveldb.so;/home/zhenyang/local/lib/libsnappy.so;/usr/local/cuda-7.0/lib64/libcudart.so;/usr/local/cuda-7.0/lib64/libcurand.so;/usr/local/cuda-7.0/lib64/libcublas.so;/home/zhenyang/local/lib/libcudnn.so;opencv_core;opencv_highgui;opencv_imgproc;/usr/lib/liblapack_atlas.so;/usr/lib/libcblas.so;/usr/lib/libatlas.so;/home/zhenyang/anaconda/lib/libpython2.7.so;/home/zhenyang/local/lib/libboost_python.so;/home/zhenyang/local/lib/libmpi_cxx.so;/home/zhenyang/local/lib/libmpi.so"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libcaffe.so"
  IMPORTED_SONAME_RELEASE "libcaffe.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS caffe )
list(APPEND _IMPORT_CHECK_FILES_FOR_caffe "${_IMPORT_PREFIX}/lib/libcaffe.so" )

# Import target "proto" for configuration "Release"
set_property(TARGET proto APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(proto PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libproto.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS proto )
list(APPEND _IMPORT_CHECK_FILES_FOR_proto "${_IMPORT_PREFIX}/lib/libproto.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
