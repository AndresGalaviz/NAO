# This is an autogenerated file. Do not edit

get_filename_component(_cur_dir ${CMAKE_CURRENT_LIST_FILE} PATH)
set(_root_dir "${_cur_dir}/../../../")
get_filename_component(ROOT_DIR ${_root_dir} ABSOLUTE)

 
set(ALFILE_INCLUDE_DIRS "${ROOT_DIR}/include;" CACHE STRING "" FORCE)
mark_as_advanced(ALFILE_INCLUDE_DIRS)
   

find_library(ALFILE_DEBUG_LIBRARY alfile_d)
find_library(ALFILE_LIBRARY       alfile)


if (ALFILE_DEBUG_LIBRARY)
  set(ALFILE_LIBRARIES optimized;${ALFILE_LIBRARY};debug;${ALFILE_DEBUG_LIBRARY})
else()
  set(ALFILE_LIBRARIES ${ALFILE_LIBRARY})
endif()

set(ALFILE_LIBRARIES ${ALFILE_LIBRARIES} CACHE INTERNAL "" FORCE)
 
include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ALFILE DEFAULT_MSG
  ALFILE_LIBRARIES
  ALFILE_INCLUDE_DIRS
)
set(ALFILE_PACKAGE_FOUND ${ALFILE_FOUND} CACHE INTERNAL "" FORCE)
 
set(ALFILE_DEPENDS "ALTOOLS;ALCORE;QI;BOOST_FILESYSTEM;BOOST_THREAD;BOOST_SYSTEM;PTHREAD;DL;ALERROR" CACHE INTERNAL "" FORCE)
 