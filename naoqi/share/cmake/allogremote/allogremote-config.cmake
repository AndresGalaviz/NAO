# This is an autogenerated file. Do not edit

get_filename_component(_cur_dir ${CMAKE_CURRENT_LIST_FILE} PATH)
set(_root_dir "${_cur_dir}/../../../")
get_filename_component(ROOT_DIR ${_root_dir} ABSOLUTE)

 
set(ALLOGREMOTE_INCLUDE_DIRS "${ROOT_DIR}/include;" CACHE STRING "" FORCE)
mark_as_advanced(ALLOGREMOTE_INCLUDE_DIRS)
   

find_library(ALLOGREMOTE_DEBUG_LIBRARY allogremote_d)
find_library(ALLOGREMOTE_LIBRARY       allogremote)


if (ALLOGREMOTE_DEBUG_LIBRARY)
  set(ALLOGREMOTE_LIBRARIES optimized;${ALLOGREMOTE_LIBRARY};debug;${ALLOGREMOTE_DEBUG_LIBRARY})
else()
  set(ALLOGREMOTE_LIBRARIES ${ALLOGREMOTE_LIBRARY})
endif()

set(ALLOGREMOTE_LIBRARIES ${ALLOGREMOTE_LIBRARIES} CACHE INTERNAL "" FORCE)
 
include(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(ALLOGREMOTE DEFAULT_MSG
  ALLOGREMOTE_LIBRARIES
  ALLOGREMOTE_INCLUDE_DIRS
)
set(ALLOGREMOTE_PACKAGE_FOUND ${ALLOGREMOTE_FOUND} CACHE INTERNAL "" FORCE)
 
set(ALLOGREMOTE_DEPENDS "QI;ZEROMQ;BOOST_FILESYSTEM;BOOST_THREAD;BOOST_SYSTEM;PTHREAD;DL;UUID;RT" CACHE INTERNAL "" FORCE)
 