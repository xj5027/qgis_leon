
// QGSCONFIG.H

#ifndef QGSCONFIG_H
#define QGSCONFIG_H

// Version must be specified according to
// <int>.<int>.<int>-<any text>.
// or else upgrading old project file will not work
// reliably.
// TODO QGIS 4: remove in favor of _QGIS_VERSION
#define VERSION "3.22.7-Białowieża"
#define _QGIS_VERSION "3.22.7-Białowieża"

//used in vim src/core/qgis.cpp
//The way below should work but it resolves to a number like 0110 which the compiler treats as octal I think
//because debuggin it out shows the decimal number 72 which results in incorrect version status.
//As a short term fix I (Tim) am defining the version in top level cmake. It would be good to
//reinstate this more generic approach below at some point though
//#define VERSION_INT 3227
// TODO QGIS 4: Remove in favor of _QGIS_VERSION_INT
#define VERSION_INT 32207
#define _QGIS_VERSION_INT 32207
#define ABISYM(x) x ## 32207
//used in main.cpp and anywhere else where the release name is needed
#define RELEASE_NAME "Białowieża"

#define QGIS_PLUGIN_SUBDIR "plugins"
#define QGIS_DATA_SUBDIR "."
#define QGIS_LIBEXEC_SUBDIR "."
#define QGIS_LIB_SUBDIR "lib"
#define QGIS_QML_SUBDIR "qml"
#define CMAKE_INSTALL_PREFIX "D:/qgis_install"
#define CMAKE_SOURCE_DIR "D:/QGIS"

#define QGIS_SERVER_MODULE_SUBDIR "server"

#if !defined(QSCINTILLA_VERSION_STR)
#define QSCINTILLA_VERSION_STR "2.13.1"
#endif

#if defined( __APPLE__ )
//used by Mac to find system or bundle resources relative to amount of bundling
#define QGIS_MACAPP_BUNDLE 
#endif

#define QT_PLUGINS_DIR "C:/OSGeo4W/apps/Qt5/plugins"

#define PYTHON_VERSION "3.9.5"
#define PYTHON_VERSION_MAJOR "3"
#define PYTHON_VERSION_MINOR "9"
#define PYTHON_VERSION_PATCH "5"

#define PROJ_VERSION_MAJOR 9
#define PROJ_VERSION_MINOR 0
#define PROJ_VERSION_PATCH 0

/* #undef USING_NMAKE */

/* #undef USING_NINJA */

#define HAVE_GUI

#define HAVE_SPATIALITE

#define HAVE_POSTGRESQL

/* #undef HAVE_ORACLE */

/* #undef HAVE_HANA */

/* #undef SERVER_SKIP_ECW */

/* #undef HAVE_SERVER_PYTHON_PLUGINS */

#define HAVE_OAUTH2_PLUGIN

#define HAVE_OPENCL
/* #undef OPENCL_USE_NEW_HEADER */

/* #undef ENABLE_MODELTEST */

/* #undef HAVE_3D */

#define HAVE_GSL

#define HAVE_GEOREFERENCER

#define USE_THREAD_LOCAL

/* #undef QGISDEBUG */

/* #undef HAVE_QUICK */

#define HAVE_QT5SERIALPORT

/* #undef HAVE_STATIC_PROVIDERS */

#define HAVE_EPT

/* #undef HAVE_PDAL */
#define PDAL_VERSION ""
#define PDAL_VERSION_MAJOR_INT 
#define PDAL_VERSION_MINOR_INT 
#define PDAL_VERSION_MAJOR ""
#define PDAL_VERSION_MINOR ""
#define PDAL_VERSION_MICRO ""

#define ENABLE_TESTS

#endif

