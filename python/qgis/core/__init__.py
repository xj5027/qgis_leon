# -*- coding: utf-8 -*-

"""
***************************************************************************
    __init__.py
    ---------------------
    Date                 : May 2014
    Copyright            : (C) 2014 by Nathan Woodrow
    Email                : woodrow dot nathan at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Nathan Woodrow'
__date__ = 'May 2014'
__copyright__ = '(C) 2014, Nathan Woodrow'

from qgis.PyQt.QtCore import NULL
from qgis._core import *

from .additions.edit import edit, QgsEditError
from .additions.fromfunction import fromFunction
from .additions.metaenum import metaEnumFromType, metaEnumFromValue
from .additions.processing import processing_output_layer_repr, processing_source_repr
from .additions.projectdirtyblocker import ProjectDirtyBlocker
from .additions.providermetadata import PyProviderMetadata
from .additions.qgsfeature import mapping_feature
from .additions.qgsfunction import register_function, qgsfunction
from .additions.qgsgeometry import _geometryNonZero, mapping_geometry
from .additions.qgssettings import _qgssettings_enum_value, _qgssettings_set_enum_value, _qgssettings_flag_value
from .additions.qgssettingsentry import PyQgsSettingsEntryEnumFlag
from .additions.qgstaskwrapper import QgsTaskWrapper
from .additions.readwritecontextentercategory import ReadWriteContextEnterCategory
from .additions.runtimeprofiler import ScopedRuntimeProfileContextManager
from .additions.validitycheck import check
from .additions.ranges import datetime_range_repr, date_range_repr

# Injections into classes
QgsFeature.__geo_interface__ = property(mapping_feature)
QgsGeometry.__bool__ = _geometryNonZero
QgsGeometry.__geo_interface__ = property(mapping_geometry)
QgsGeometry.__nonzero__ = _geometryNonZero
QgsProcessingFeatureSourceDefinition.__repr__ = processing_source_repr
QgsProcessingOutputLayerDefinition.__repr__ = processing_output_layer_repr
QgsProject.blockDirtying = ProjectDirtyBlocker
QgsReadWriteContext.enterCategory = ReadWriteContextEnterCategory
QgsRuntimeProfiler.profile = ScopedRuntimeProfileContextManager
QgsSettings.enumValue = _qgssettings_enum_value
QgsSettings.setEnumValue = _qgssettings_set_enum_value
QgsSettings.flagValue = _qgssettings_flag_value
QgsTask.fromFunction = fromFunction
QgsDateTimeRange.__repr__ = datetime_range_repr
QgsDateRange.__repr__ = date_range_repr

# Classes patched
QgsSettingsEntryEnumFlag = PyQgsSettingsEntryEnumFlag

# Classes patched using a derived class
QgsProviderMetadata = PyProviderMetadata

# monkey patch deprecated enum values to maintain API
# TODO - remove for QGIS 4.0
QgsMarkerLineSymbolLayer.Interval = QgsTemplatedLineSymbolLayerBase.Interval
QgsMarkerLineSymbolLayer.Vertex = QgsTemplatedLineSymbolLayerBase.Vertex
QgsMarkerLineSymbolLayer.LastVertex = QgsTemplatedLineSymbolLayerBase.LastVertex
QgsMarkerLineSymbolLayer.FirstVertex = QgsTemplatedLineSymbolLayerBase.FirstVertex
QgsMarkerLineSymbolLayer.CentralPoint = QgsTemplatedLineSymbolLayerBase.CentralPoint
QgsMarkerLineSymbolLayer.CurvePoint = QgsTemplatedLineSymbolLayerBase.CurvePoint

QgsVectorLayer.VertexMarkerType = Qgis.VertexMarkerType
QgsVectorLayer.SemiTransparentCircle = Qgis.VertexMarkerType.SemiTransparentCircle
QgsVectorLayer.SemiTransparentCircle.is_monkey_patched = True
QgsVectorLayer.SemiTransparentCircle.__doc__ = "Semi-transparent circle marker"
QgsVectorLayer.Cross = Qgis.VertexMarkerType.Cross
QgsVectorLayer.Cross.is_monkey_patched = True
QgsVectorLayer.Cross.__doc__ = "Cross marker"
QgsVectorLayer.NoMarker = Qgis.VertexMarkerType.NoMarker
QgsVectorLayer.NoMarker.is_monkey_patched = True
QgsVectorLayer.NoMarker.__doc__ = "No marker"

QgsSymbol.RenderHints = Qgis.SymbolRenderHints
QgsSymbol.PreviewFlags = Qgis.SymbolPreviewFlags
QgsDataItem.Capabilities = Qgis.BrowserItemCapabilities
QgsGeometry.ValidityFlags = Qgis.GeometryValidityFlags

# Monkey patch static const "QgsDataProvider.SUBLAYER_SEPARATOR" which was removed for QGIS 3.12
QgsDataProvider.SUBLAYER_SEPARATOR = QgsDataProvider.sublayerSeparator()

# Monkey patch Qgis vars
Qgis.QGIS_VERSION = Qgis.version()
Qgis.QGIS_VERSION_INT = Qgis.versionInt()
Qgis.QGIS_RELEASE_NAME = Qgis.releaseName()

GEOWKT = geoWkt()
PROJECT_SCALES = Qgis.defaultProjectScales()
GEOPROJ4 = geoProj4()
GEO_EPSG_CRS_AUTHID = geoEpsgCrsAuthId()
GEO_NONE = geoNone()
"""
This folder is completed using sipify.pl script
It is not aimed to be manually edited
"""
# The following has been generated automatically from src/core/qgis.h
QgsMapLayer.LayerType = QgsMapLayerType
# monkey patching scoped based enum
QgsMapLayer.VectorLayer = QgsMapLayerType.VectorLayer
QgsMapLayer.VectorLayer.is_monkey_patched = True
QgsMapLayer.VectorLayer.__doc__ = ""
QgsMapLayer.RasterLayer = QgsMapLayerType.RasterLayer
QgsMapLayer.RasterLayer.is_monkey_patched = True
QgsMapLayer.RasterLayer.__doc__ = ""
QgsMapLayer.PluginLayer = QgsMapLayerType.PluginLayer
QgsMapLayer.PluginLayer.is_monkey_patched = True
QgsMapLayer.PluginLayer.__doc__ = ""
QgsMapLayer.MeshLayer = QgsMapLayerType.MeshLayer
QgsMapLayer.MeshLayer.is_monkey_patched = True
QgsMapLayer.MeshLayer.__doc__ = "Added in 3.2"
QgsMapLayer.VectorTileLayer = QgsMapLayerType.VectorTileLayer
QgsMapLayer.VectorTileLayer.is_monkey_patched = True
QgsMapLayer.VectorTileLayer.__doc__ = "Added in 3.14"
QgsMapLayer.AnnotationLayer = QgsMapLayerType.AnnotationLayer
QgsMapLayer.AnnotationLayer.is_monkey_patched = True
QgsMapLayer.AnnotationLayer.__doc__ = "Contains freeform, georeferenced annotations. Added in QGIS 3.16"
QgsMapLayer.PointCloudLayer = QgsMapLayerType.PointCloudLayer
QgsMapLayer.PointCloudLayer.is_monkey_patched = True
QgsMapLayer.PointCloudLayer.__doc__ = "Added in 3.18"
QgsMapLayerType.__doc__ = 'Types of layers that can be added to a map\n\n.. versionadded:: 3.8\n\n' + '* ``VectorLayer``: ' + QgsMapLayerType.VectorLayer.__doc__ + '\n' + '* ``RasterLayer``: ' + QgsMapLayerType.RasterLayer.__doc__ + '\n' + '* ``PluginLayer``: ' + QgsMapLayerType.PluginLayer.__doc__ + '\n' + '* ``MeshLayer``: ' + QgsMapLayerType.MeshLayer.__doc__ + '\n' + '* ``VectorTileLayer``: ' + QgsMapLayerType.VectorTileLayer.__doc__ + '\n' + '* ``AnnotationLayer``: ' + QgsMapLayerType.AnnotationLayer.__doc__ + '\n' + '* ``PointCloudLayer``: ' + QgsMapLayerType.PointCloudLayer.__doc__
# --
Qgis.MessageLevel.baseClass = Qgis
# monkey patching scoped based enum
Qgis.UnknownDataType = Qgis.DataType.UnknownDataType
Qgis.UnknownDataType.is_monkey_patched = True
Qgis.UnknownDataType.__doc__ = "Unknown or unspecified type"
Qgis.Byte = Qgis.DataType.Byte
Qgis.Byte.is_monkey_patched = True
Qgis.Byte.__doc__ = "Eight bit unsigned integer (quint8)"
Qgis.UInt16 = Qgis.DataType.UInt16
Qgis.UInt16.is_monkey_patched = True
Qgis.UInt16.__doc__ = "Sixteen bit unsigned integer (quint16)"
Qgis.Int16 = Qgis.DataType.Int16
Qgis.Int16.is_monkey_patched = True
Qgis.Int16.__doc__ = "Sixteen bit signed integer (qint16)"
Qgis.UInt32 = Qgis.DataType.UInt32
Qgis.UInt32.is_monkey_patched = True
Qgis.UInt32.__doc__ = "Thirty two bit unsigned integer (quint32)"
Qgis.Int32 = Qgis.DataType.Int32
Qgis.Int32.is_monkey_patched = True
Qgis.Int32.__doc__ = "Thirty two bit signed integer (qint32)"
Qgis.Float32 = Qgis.DataType.Float32
Qgis.Float32.is_monkey_patched = True
Qgis.Float32.__doc__ = "Thirty two bit floating point (float)"
Qgis.Float64 = Qgis.DataType.Float64
Qgis.Float64.is_monkey_patched = True
Qgis.Float64.__doc__ = "Sixty four bit floating point (double)"
Qgis.CInt16 = Qgis.DataType.CInt16
Qgis.CInt16.is_monkey_patched = True
Qgis.CInt16.__doc__ = "Complex Int16"
Qgis.CInt32 = Qgis.DataType.CInt32
Qgis.CInt32.is_monkey_patched = True
Qgis.CInt32.__doc__ = "Complex Int32"
Qgis.CFloat32 = Qgis.DataType.CFloat32
Qgis.CFloat32.is_monkey_patched = True
Qgis.CFloat32.__doc__ = "Complex Float32"
Qgis.CFloat64 = Qgis.DataType.CFloat64
Qgis.CFloat64.is_monkey_patched = True
Qgis.CFloat64.__doc__ = "Complex Float64"
Qgis.ARGB32 = Qgis.DataType.ARGB32
Qgis.ARGB32.is_monkey_patched = True
Qgis.ARGB32.__doc__ = "Color, alpha, red, green, blue, 4 bytes the same as QImage::Format_ARGB32"
Qgis.ARGB32_Premultiplied = Qgis.DataType.ARGB32_Premultiplied
Qgis.ARGB32_Premultiplied.is_monkey_patched = True
Qgis.ARGB32_Premultiplied.__doc__ = "Color, alpha, red, green, blue, 4 bytes  the same as QImage::Format_ARGB32_Premultiplied"
Qgis.DataType.__doc__ = 'Raster data types.\nThis is modified and extended copy of GDALDataType.\n\n' + '* ``UnknownDataType``: ' + Qgis.DataType.UnknownDataType.__doc__ + '\n' + '* ``Byte``: ' + Qgis.DataType.Byte.__doc__ + '\n' + '* ``UInt16``: ' + Qgis.DataType.UInt16.__doc__ + '\n' + '* ``Int16``: ' + Qgis.DataType.Int16.__doc__ + '\n' + '* ``UInt32``: ' + Qgis.DataType.UInt32.__doc__ + '\n' + '* ``Int32``: ' + Qgis.DataType.Int32.__doc__ + '\n' + '* ``Float32``: ' + Qgis.DataType.Float32.__doc__ + '\n' + '* ``Float64``: ' + Qgis.DataType.Float64.__doc__ + '\n' + '* ``CInt16``: ' + Qgis.DataType.CInt16.__doc__ + '\n' + '* ``CInt32``: ' + Qgis.DataType.CInt32.__doc__ + '\n' + '* ``CFloat32``: ' + Qgis.DataType.CFloat32.__doc__ + '\n' + '* ``CFloat64``: ' + Qgis.DataType.CFloat64.__doc__ + '\n' + '* ``ARGB32``: ' + Qgis.DataType.ARGB32.__doc__ + '\n' + '* ``ARGB32_Premultiplied``: ' + Qgis.DataType.ARGB32_Premultiplied.__doc__
# --
Qgis.DataType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.Never = Qgis.PythonMacroMode.Never
Qgis.Never.is_monkey_patched = True
Qgis.Never.__doc__ = "Macros are never run"
Qgis.Ask = Qgis.PythonMacroMode.Ask
Qgis.Ask.is_monkey_patched = True
Qgis.Ask.__doc__ = "User is prompt before running"
Qgis.SessionOnly = Qgis.PythonMacroMode.SessionOnly
Qgis.SessionOnly.is_monkey_patched = True
Qgis.SessionOnly.__doc__ = "Only during this session"
Qgis.Always = Qgis.PythonMacroMode.Always
Qgis.Always.is_monkey_patched = True
Qgis.Always.__doc__ = "Macros are always run"
Qgis.NotForThisSession = Qgis.PythonMacroMode.NotForThisSession
Qgis.NotForThisSession.is_monkey_patched = True
Qgis.NotForThisSession.__doc__ = "Macros will not be run for this session"
Qgis.PythonMacroMode.__doc__ = 'Authorisation to run Python Macros\n\n.. versionadded:: 3.10\n\n' + '* ``Never``: ' + Qgis.PythonMacroMode.Never.__doc__ + '\n' + '* ``Ask``: ' + Qgis.PythonMacroMode.Ask.__doc__ + '\n' + '* ``SessionOnly``: ' + Qgis.PythonMacroMode.SessionOnly.__doc__ + '\n' + '* ``Always``: ' + Qgis.PythonMacroMode.Always.__doc__ + '\n' + '* ``NotForThisSession``: ' + Qgis.PythonMacroMode.NotForThisSession.__doc__
# --
Qgis.PythonMacroMode.baseClass = Qgis
QgsVectorDataProvider.FeatureCountState = Qgis.FeatureCountState
# monkey patching scoped based enum
QgsVectorDataProvider.Uncounted = Qgis.FeatureCountState.Uncounted
QgsVectorDataProvider.Uncounted.is_monkey_patched = True
QgsVectorDataProvider.Uncounted.__doc__ = "Feature count not yet computed"
QgsVectorDataProvider.UnknownCount = Qgis.FeatureCountState.UnknownCount
QgsVectorDataProvider.UnknownCount.is_monkey_patched = True
QgsVectorDataProvider.UnknownCount.__doc__ = "Provider returned an unknown feature count"
Qgis.FeatureCountState.__doc__ = 'Enumeration of feature count states\n\n.. versionadded:: 3.20\n\n' + '* ``Uncounted``: ' + Qgis.FeatureCountState.Uncounted.__doc__ + '\n' + '* ``UnknownCount``: ' + Qgis.FeatureCountState.UnknownCount.__doc__
# --
Qgis.FeatureCountState.baseClass = Qgis
QgsSymbol.SymbolType = Qgis.SymbolType
# monkey patching scoped based enum
QgsSymbol.Marker = Qgis.SymbolType.Marker
QgsSymbol.Marker.is_monkey_patched = True
QgsSymbol.Marker.__doc__ = "Marker symbol"
QgsSymbol.Line = Qgis.SymbolType.Line
QgsSymbol.Line.is_monkey_patched = True
QgsSymbol.Line.__doc__ = "Line symbol"
QgsSymbol.Fill = Qgis.SymbolType.Fill
QgsSymbol.Fill.is_monkey_patched = True
QgsSymbol.Fill.__doc__ = "Fill symbol"
QgsSymbol.Hybrid = Qgis.SymbolType.Hybrid
QgsSymbol.Hybrid.is_monkey_patched = True
QgsSymbol.Hybrid.__doc__ = "Hybrid symbol"
Qgis.SymbolType.__doc__ = 'Symbol types\n\n.. versionadded:: 3.20\n\n' + '* ``Marker``: ' + Qgis.SymbolType.Marker.__doc__ + '\n' + '* ``Line``: ' + Qgis.SymbolType.Line.__doc__ + '\n' + '* ``Fill``: ' + Qgis.SymbolType.Fill.__doc__ + '\n' + '* ``Hybrid``: ' + Qgis.SymbolType.Hybrid.__doc__
# --
Qgis.SymbolType.baseClass = Qgis
QgsSymbol.ScaleMethod = Qgis.ScaleMethod
# monkey patching scoped based enum
QgsSymbol.ScaleArea = Qgis.ScaleMethod.ScaleArea
QgsSymbol.ScaleArea.is_monkey_patched = True
QgsSymbol.ScaleArea.__doc__ = "Calculate scale by the area"
QgsSymbol.ScaleDiameter = Qgis.ScaleMethod.ScaleDiameter
QgsSymbol.ScaleDiameter.is_monkey_patched = True
QgsSymbol.ScaleDiameter.__doc__ = "Calculate scale by the diameter"
Qgis.ScaleMethod.__doc__ = 'Scale methods\n\n.. versionadded:: 3.20\n\n' + '* ``ScaleArea``: ' + Qgis.ScaleMethod.ScaleArea.__doc__ + '\n' + '* ``ScaleDiameter``: ' + Qgis.ScaleMethod.ScaleDiameter.__doc__
# --
Qgis.ScaleMethod.baseClass = Qgis
QgsSymbol.RenderHint = Qgis.SymbolRenderHint
# monkey patching scoped based enum
QgsSymbol.DynamicRotation = Qgis.SymbolRenderHint.DynamicRotation
QgsSymbol.DynamicRotation.is_monkey_patched = True
QgsSymbol.DynamicRotation.__doc__ = "Rotation of symbol may be changed during rendering and symbol should not be cached"
Qgis.SymbolRenderHint.__doc__ = 'Flags controlling behavior of symbols during rendering\n\n.. versionadded:: 3.20\n\n' + '* ``DynamicRotation``: ' + Qgis.SymbolRenderHint.DynamicRotation.__doc__
# --
Qgis.SymbolRenderHint.baseClass = Qgis
QgsSymbol.RenderHints = Qgis.SymbolRenderHints
# monkey patching scoped based enum
Qgis.SymbolFlag.RendererShouldUseSymbolLevels.__doc__ = "If present, indicates that a QgsFeatureRenderer using the symbol should use symbol levels for best results"
Qgis.SymbolFlag.__doc__ = 'Flags controlling behavior of symbols\n\n.. versionadded:: 3.20\n\n' + '* ``RendererShouldUseSymbolLevels``: ' + Qgis.SymbolFlag.RendererShouldUseSymbolLevels.__doc__
# --
Qgis.SymbolFlag.baseClass = Qgis
QgsSymbol.PreviewFlag = Qgis.SymbolPreviewFlag
# monkey patching scoped based enum
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols = Qgis.SymbolPreviewFlag.FlagIncludeCrosshairsForMarkerSymbols
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols.is_monkey_patched = True
QgsSymbol.FlagIncludeCrosshairsForMarkerSymbols.__doc__ = "Include a crosshairs reference image in the background of marker symbol previews"
Qgis.SymbolPreviewFlag.__doc__ = 'Flags for controlling how symbol preview images are generated.\n\n.. versionadded:: 3.20\n\n' + '* ``FlagIncludeCrosshairsForMarkerSymbols``: ' + Qgis.SymbolPreviewFlag.FlagIncludeCrosshairsForMarkerSymbols.__doc__
# --
Qgis.SymbolPreviewFlag.baseClass = Qgis
QgsSymbol.SymbolPreviewFlags = Qgis.SymbolPreviewFlags
# monkey patching scoped based enum
Qgis.SymbolLayerFlag.DisableFeatureClipping.__doc__ = "If present, indicates that features should never be clipped to the map extent during rendering"
Qgis.SymbolLayerFlag.__doc__ = 'Flags controlling behavior of symbol layers\n\n.. versionadded:: 3.22\n\n' + '* ``DisableFeatureClipping``: ' + Qgis.SymbolLayerFlag.DisableFeatureClipping.__doc__
# --
Qgis.SymbolLayerFlag.baseClass = Qgis
QgsDataItem.Type = Qgis.BrowserItemType
# monkey patching scoped based enum
QgsDataItem.Collection = Qgis.BrowserItemType.Collection
QgsDataItem.Collection.is_monkey_patched = True
QgsDataItem.Collection.__doc__ = "A collection of items"
QgsDataItem.Directory = Qgis.BrowserItemType.Directory
QgsDataItem.Directory.is_monkey_patched = True
QgsDataItem.Directory.__doc__ = "Represents a file directory"
QgsDataItem.Layer = Qgis.BrowserItemType.Layer
QgsDataItem.Layer.is_monkey_patched = True
QgsDataItem.Layer.__doc__ = "Represents a map layer"
QgsDataItem.Error = Qgis.BrowserItemType.Error
QgsDataItem.Error.is_monkey_patched = True
QgsDataItem.Error.__doc__ = "Contains an error message"
QgsDataItem.Favorites = Qgis.BrowserItemType.Favorites
QgsDataItem.Favorites.is_monkey_patched = True
QgsDataItem.Favorites.__doc__ = "Represents a favorite item"
QgsDataItem.Project = Qgis.BrowserItemType.Project
QgsDataItem.Project.is_monkey_patched = True
QgsDataItem.Project.__doc__ = "Represents a QGIS project"
QgsDataItem.Custom = Qgis.BrowserItemType.Custom
QgsDataItem.Custom.is_monkey_patched = True
QgsDataItem.Custom.__doc__ = "Custom item type"
QgsDataItem.Fields = Qgis.BrowserItemType.Fields
QgsDataItem.Fields.is_monkey_patched = True
QgsDataItem.Fields.__doc__ = "Collection of fields"
QgsDataItem.Field = Qgis.BrowserItemType.Field
QgsDataItem.Field.is_monkey_patched = True
QgsDataItem.Field.__doc__ = "Vector layer field"
Qgis.BrowserItemType.__doc__ = 'Browser item types.\n\n.. versionadded:: 3.20\n\n' + '* ``Collection``: ' + Qgis.BrowserItemType.Collection.__doc__ + '\n' + '* ``Directory``: ' + Qgis.BrowserItemType.Directory.__doc__ + '\n' + '* ``Layer``: ' + Qgis.BrowserItemType.Layer.__doc__ + '\n' + '* ``Error``: ' + Qgis.BrowserItemType.Error.__doc__ + '\n' + '* ``Favorites``: ' + Qgis.BrowserItemType.Favorites.__doc__ + '\n' + '* ``Project``: ' + Qgis.BrowserItemType.Project.__doc__ + '\n' + '* ``Custom``: ' + Qgis.BrowserItemType.Custom.__doc__ + '\n' + '* ``Fields``: ' + Qgis.BrowserItemType.Fields.__doc__ + '\n' + '* ``Field``: ' + Qgis.BrowserItemType.Field.__doc__
# --
Qgis.BrowserItemType.baseClass = Qgis
QgsDataItem.State = Qgis.BrowserItemState
# monkey patching scoped based enum
QgsDataItem.NotPopulated = Qgis.BrowserItemState.NotPopulated
QgsDataItem.NotPopulated.is_monkey_patched = True
QgsDataItem.NotPopulated.__doc__ = "Children not yet created"
QgsDataItem.Populating = Qgis.BrowserItemState.Populating
QgsDataItem.Populating.is_monkey_patched = True
QgsDataItem.Populating.__doc__ = "Creating children in separate thread (populating or refreshing)"
QgsDataItem.Populated = Qgis.BrowserItemState.Populated
QgsDataItem.Populated.is_monkey_patched = True
QgsDataItem.Populated.__doc__ = "Children created"
Qgis.BrowserItemState.__doc__ = 'Browser item states.\n\n.. versionadded:: 3.20\n\n' + '* ``NotPopulated``: ' + Qgis.BrowserItemState.NotPopulated.__doc__ + '\n' + '* ``Populating``: ' + Qgis.BrowserItemState.Populating.__doc__ + '\n' + '* ``Populated``: ' + Qgis.BrowserItemState.Populated.__doc__
# --
Qgis.BrowserItemState.baseClass = Qgis
QgsDataItem.Capability = Qgis.BrowserItemCapability
# monkey patching scoped based enum
QgsDataItem.NoCapabilities = Qgis.BrowserItemCapability.NoCapabilities
QgsDataItem.NoCapabilities.is_monkey_patched = True
QgsDataItem.NoCapabilities.__doc__ = "Item has no capabilities"
QgsDataItem.SetCrs = Qgis.BrowserItemCapability.SetCrs
QgsDataItem.SetCrs.is_monkey_patched = True
QgsDataItem.SetCrs.__doc__ = "Can set CRS on layer or group of layers. \deprecated since QGIS 3.6 -- no longer used by QGIS and will be removed in QGIS 4.0"
QgsDataItem.Fertile = Qgis.BrowserItemCapability.Fertile
QgsDataItem.Fertile.is_monkey_patched = True
QgsDataItem.Fertile.__doc__ = "Can create children. Even items without this capability may have children, but cannot create them, it means that children are created by item ancestors."
QgsDataItem.Fast = Qgis.BrowserItemCapability.Fast
QgsDataItem.Fast.is_monkey_patched = True
QgsDataItem.Fast.__doc__ = "CreateChildren() is fast enough to be run in main thread when refreshing items, most root items (wms,wfs,wcs,postgres...) are considered fast because they are reading data only from QgsSettings"
QgsDataItem.Collapse = Qgis.BrowserItemCapability.Collapse
QgsDataItem.Collapse.is_monkey_patched = True
QgsDataItem.Collapse.__doc__ = "The collapse/expand status for this items children should be ignored in order to avoid undesired network connections (wms etc.)"
QgsDataItem.Rename = Qgis.BrowserItemCapability.Rename
QgsDataItem.Rename.is_monkey_patched = True
QgsDataItem.Rename.__doc__ = "Item can be renamed"
QgsDataItem.Delete = Qgis.BrowserItemCapability.Delete
QgsDataItem.Delete.is_monkey_patched = True
QgsDataItem.Delete.__doc__ = "Item can be deleted"
QgsDataItem.ItemRepresentsFile = Qgis.BrowserItemCapability.ItemRepresentsFile
QgsDataItem.ItemRepresentsFile.is_monkey_patched = True
QgsDataItem.ItemRepresentsFile.__doc__ = "Item's path() directly represents a file on disk (since QGIS 3.22)"
Qgis.BrowserItemCapability.__doc__ = 'Browser item capabilities.\n\n.. versionadded:: 3.20\n\n' + '* ``NoCapabilities``: ' + Qgis.BrowserItemCapability.NoCapabilities.__doc__ + '\n' + '* ``SetCrs``: ' + Qgis.BrowserItemCapability.SetCrs.__doc__ + '\n' + '* ``Fertile``: ' + Qgis.BrowserItemCapability.Fertile.__doc__ + '\n' + '* ``Fast``: ' + Qgis.BrowserItemCapability.Fast.__doc__ + '\n' + '* ``Collapse``: ' + Qgis.BrowserItemCapability.Collapse.__doc__ + '\n' + '* ``Rename``: ' + Qgis.BrowserItemCapability.Rename.__doc__ + '\n' + '* ``Delete``: ' + Qgis.BrowserItemCapability.Delete.__doc__ + '\n' + '* ``ItemRepresentsFile``: ' + Qgis.BrowserItemCapability.ItemRepresentsFile.__doc__
# --
Qgis.BrowserItemCapability.baseClass = Qgis
QgsDataItem.Capabilities = Qgis.BrowserItemCapabilities
QgsLayerItem.LayerType = Qgis.BrowserLayerType
# monkey patching scoped based enum
QgsLayerItem.NoType = Qgis.BrowserLayerType.NoType
QgsLayerItem.NoType.is_monkey_patched = True
QgsLayerItem.NoType.__doc__ = "No type"
QgsLayerItem.Vector = Qgis.BrowserLayerType.Vector
QgsLayerItem.Vector.is_monkey_patched = True
QgsLayerItem.Vector.__doc__ = "Generic vector layer"
QgsLayerItem.Raster = Qgis.BrowserLayerType.Raster
QgsLayerItem.Raster.is_monkey_patched = True
QgsLayerItem.Raster.__doc__ = "Raster layer"
QgsLayerItem.Point = Qgis.BrowserLayerType.Point
QgsLayerItem.Point.is_monkey_patched = True
QgsLayerItem.Point.__doc__ = "Vector point layer"
QgsLayerItem.Line = Qgis.BrowserLayerType.Line
QgsLayerItem.Line.is_monkey_patched = True
QgsLayerItem.Line.__doc__ = "Vector line layer"
QgsLayerItem.Polygon = Qgis.BrowserLayerType.Polygon
QgsLayerItem.Polygon.is_monkey_patched = True
QgsLayerItem.Polygon.__doc__ = "Vector polygon layer"
QgsLayerItem.TableLayer = Qgis.BrowserLayerType.TableLayer
QgsLayerItem.TableLayer.is_monkey_patched = True
QgsLayerItem.TableLayer.__doc__ = "Vector non-spatial layer"
QgsLayerItem.Database = Qgis.BrowserLayerType.Database
QgsLayerItem.Database.is_monkey_patched = True
QgsLayerItem.Database.__doc__ = "Database layer"
QgsLayerItem.Table = Qgis.BrowserLayerType.Table
QgsLayerItem.Table.is_monkey_patched = True
QgsLayerItem.Table.__doc__ = "Database table"
QgsLayerItem.Plugin = Qgis.BrowserLayerType.Plugin
QgsLayerItem.Plugin.is_monkey_patched = True
QgsLayerItem.Plugin.__doc__ = "Plugin based layer"
QgsLayerItem.Mesh = Qgis.BrowserLayerType.Mesh
QgsLayerItem.Mesh.is_monkey_patched = True
QgsLayerItem.Mesh.__doc__ = "Mesh layer"
QgsLayerItem.VectorTile = Qgis.BrowserLayerType.VectorTile
QgsLayerItem.VectorTile.is_monkey_patched = True
QgsLayerItem.VectorTile.__doc__ = "Vector tile layer"
QgsLayerItem.PointCloud = Qgis.BrowserLayerType.PointCloud
QgsLayerItem.PointCloud.is_monkey_patched = True
QgsLayerItem.PointCloud.__doc__ = "Point cloud layer"
Qgis.BrowserLayerType.__doc__ = 'Browser item layer types\n\n.. versionadded:: 3.20\n\n' + '* ``NoType``: ' + Qgis.BrowserLayerType.NoType.__doc__ + '\n' + '* ``Vector``: ' + Qgis.BrowserLayerType.Vector.__doc__ + '\n' + '* ``Raster``: ' + Qgis.BrowserLayerType.Raster.__doc__ + '\n' + '* ``Point``: ' + Qgis.BrowserLayerType.Point.__doc__ + '\n' + '* ``Line``: ' + Qgis.BrowserLayerType.Line.__doc__ + '\n' + '* ``Polygon``: ' + Qgis.BrowserLayerType.Polygon.__doc__ + '\n' + '* ``TableLayer``: ' + Qgis.BrowserLayerType.TableLayer.__doc__ + '\n' + '* ``Database``: ' + Qgis.BrowserLayerType.Database.__doc__ + '\n' + '* ``Table``: ' + Qgis.BrowserLayerType.Table.__doc__ + '\n' + '* ``Plugin``: ' + Qgis.BrowserLayerType.Plugin.__doc__ + '\n' + '* ``Mesh``: ' + Qgis.BrowserLayerType.Mesh.__doc__ + '\n' + '* ``VectorTile``: ' + Qgis.BrowserLayerType.VectorTile.__doc__ + '\n' + '* ``PointCloud``: ' + Qgis.BrowserLayerType.PointCloud.__doc__
# --
Qgis.BrowserLayerType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.BrowserDirectoryMonitoring.Default.__doc__ = "Use default logic to determine whether directory should be monitored"
Qgis.BrowserDirectoryMonitoring.NeverMonitor.__doc__ = "Never monitor the directory, regardless of the default logic"
Qgis.BrowserDirectoryMonitoring.AlwaysMonitor.__doc__ = "Always monitor the directory, regardless of the default logic"
Qgis.BrowserDirectoryMonitoring.__doc__ = 'Browser directory item monitoring switches.\n\n.. versionadded:: 3.20\n\n' + '* ``Default``: ' + Qgis.BrowserDirectoryMonitoring.Default.__doc__ + '\n' + '* ``NeverMonitor``: ' + Qgis.BrowserDirectoryMonitoring.NeverMonitor.__doc__ + '\n' + '* ``AlwaysMonitor``: ' + Qgis.BrowserDirectoryMonitoring.AlwaysMonitor.__doc__
# --
Qgis.BrowserDirectoryMonitoring.baseClass = Qgis
# monkey patching scoped based enum
Qgis.HttpMethod.Get.__doc__ = "GET method"
Qgis.HttpMethod.Post.__doc__ = "POST method"
Qgis.HttpMethod.__doc__ = 'Different methods of HTTP requests\n\n.. versionadded:: 3.22\n\n' + '* ``Get``: ' + Qgis.HttpMethod.Get.__doc__ + '\n' + '* ``Post``: ' + Qgis.HttpMethod.Post.__doc__
# --
Qgis.HttpMethod.baseClass = Qgis
QgsVectorLayerExporter.ExportError = Qgis.VectorExportResult
# monkey patching scoped based enum
QgsVectorLayerExporter.NoError = Qgis.VectorExportResult.Success
QgsVectorLayerExporter.NoError.is_monkey_patched = True
QgsVectorLayerExporter.NoError.__doc__ = "No errors were encountered"
QgsVectorLayerExporter.ErrCreateDataSource = Qgis.VectorExportResult.ErrorCreatingDataSource
QgsVectorLayerExporter.ErrCreateDataSource.is_monkey_patched = True
QgsVectorLayerExporter.ErrCreateDataSource.__doc__ = "Could not create the destination data source"
QgsVectorLayerExporter.ErrCreateLayer = Qgis.VectorExportResult.ErrorCreatingLayer
QgsVectorLayerExporter.ErrCreateLayer.is_monkey_patched = True
QgsVectorLayerExporter.ErrCreateLayer.__doc__ = "Could not create destination layer"
QgsVectorLayerExporter.ErrAttributeTypeUnsupported = Qgis.VectorExportResult.ErrorAttributeTypeUnsupported
QgsVectorLayerExporter.ErrAttributeTypeUnsupported.is_monkey_patched = True
QgsVectorLayerExporter.ErrAttributeTypeUnsupported.__doc__ = "Source layer has an attribute type which could not be handled by destination"
QgsVectorLayerExporter.ErrAttributeCreationFailed = Qgis.VectorExportResult.ErrorAttributeCreationFailed
QgsVectorLayerExporter.ErrAttributeCreationFailed.is_monkey_patched = True
QgsVectorLayerExporter.ErrAttributeCreationFailed.__doc__ = "Destination provider was unable to create an attribute"
QgsVectorLayerExporter.ErrProjection = Qgis.VectorExportResult.ErrorProjectingFeatures
QgsVectorLayerExporter.ErrProjection.is_monkey_patched = True
QgsVectorLayerExporter.ErrProjection.__doc__ = "An error occurred while reprojecting features to destination CRS"
QgsVectorLayerExporter.ErrFeatureWriteFailed = Qgis.VectorExportResult.ErrorFeatureWriteFailed
QgsVectorLayerExporter.ErrFeatureWriteFailed.is_monkey_patched = True
QgsVectorLayerExporter.ErrFeatureWriteFailed.__doc__ = "An error occurred while writing a feature to the destination"
QgsVectorLayerExporter.ErrInvalidLayer = Qgis.VectorExportResult.ErrorInvalidLayer
QgsVectorLayerExporter.ErrInvalidLayer.is_monkey_patched = True
QgsVectorLayerExporter.ErrInvalidLayer.__doc__ = "Could not access newly created destination layer"
QgsVectorLayerExporter.ErrInvalidProvider = Qgis.VectorExportResult.ErrorInvalidProvider
QgsVectorLayerExporter.ErrInvalidProvider.is_monkey_patched = True
QgsVectorLayerExporter.ErrInvalidProvider.__doc__ = "Could not find a matching provider key"
QgsVectorLayerExporter.ErrProviderUnsupportedFeature = Qgis.VectorExportResult.ErrorProviderUnsupportedFeature
QgsVectorLayerExporter.ErrProviderUnsupportedFeature.is_monkey_patched = True
QgsVectorLayerExporter.ErrProviderUnsupportedFeature.__doc__ = "Provider does not support creation of empty layers"
QgsVectorLayerExporter.ErrConnectionFailed = Qgis.VectorExportResult.ErrorConnectionFailed
QgsVectorLayerExporter.ErrConnectionFailed.is_monkey_patched = True
QgsVectorLayerExporter.ErrConnectionFailed.__doc__ = "Could not connect to destination"
QgsVectorLayerExporter.ErrUserCanceled = Qgis.VectorExportResult.UserCanceled
QgsVectorLayerExporter.ErrUserCanceled.is_monkey_patched = True
QgsVectorLayerExporter.ErrUserCanceled.__doc__ = "User canceled the export"
Qgis.VectorExportResult.__doc__ = 'Vector layer export result codes.\n\n.. versionadded:: 3.20\n\n' + '* ``NoError``: ' + Qgis.VectorExportResult.Success.__doc__ + '\n' + '* ``ErrCreateDataSource``: ' + Qgis.VectorExportResult.ErrorCreatingDataSource.__doc__ + '\n' + '* ``ErrCreateLayer``: ' + Qgis.VectorExportResult.ErrorCreatingLayer.__doc__ + '\n' + '* ``ErrAttributeTypeUnsupported``: ' + Qgis.VectorExportResult.ErrorAttributeTypeUnsupported.__doc__ + '\n' + '* ``ErrAttributeCreationFailed``: ' + Qgis.VectorExportResult.ErrorAttributeCreationFailed.__doc__ + '\n' + '* ``ErrProjection``: ' + Qgis.VectorExportResult.ErrorProjectingFeatures.__doc__ + '\n' + '* ``ErrFeatureWriteFailed``: ' + Qgis.VectorExportResult.ErrorFeatureWriteFailed.__doc__ + '\n' + '* ``ErrInvalidLayer``: ' + Qgis.VectorExportResult.ErrorInvalidLayer.__doc__ + '\n' + '* ``ErrInvalidProvider``: ' + Qgis.VectorExportResult.ErrorInvalidProvider.__doc__ + '\n' + '* ``ErrProviderUnsupportedFeature``: ' + Qgis.VectorExportResult.ErrorProviderUnsupportedFeature.__doc__ + '\n' + '* ``ErrConnectionFailed``: ' + Qgis.VectorExportResult.ErrorConnectionFailed.__doc__ + '\n' + '* ``ErrUserCanceled``: ' + Qgis.VectorExportResult.UserCanceled.__doc__
# --
Qgis.VectorExportResult.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SqlLayerDefinitionCapability.SubsetStringFilter.__doc__ = "SQL layer definition supports subset string filter"
Qgis.SqlLayerDefinitionCapability.GeometryColumn.__doc__ = "SQL layer definition supports geometry column"
Qgis.SqlLayerDefinitionCapability.PrimaryKeys.__doc__ = "SQL layer definition supports primary keys"
Qgis.SqlLayerDefinitionCapability.UnstableFeatureIds.__doc__ = "SQL layer definition supports disabling select at id"
Qgis.SqlLayerDefinitionCapability.__doc__ = 'SqlLayerDefinitionCapability enum lists the arguments supported by the provider when creating SQL query layers.\n\n.. versionadded:: 3.22\n\n' + '* ``SubsetStringFilter``: ' + Qgis.SqlLayerDefinitionCapability.SubsetStringFilter.__doc__ + '\n' + '* ``GeometryColumn``: ' + Qgis.SqlLayerDefinitionCapability.GeometryColumn.__doc__ + '\n' + '* ``PrimaryKeys``: ' + Qgis.SqlLayerDefinitionCapability.PrimaryKeys.__doc__ + '\n' + '* ``UnstableFeatureIds``: ' + Qgis.SqlLayerDefinitionCapability.UnstableFeatureIds.__doc__
# --
Qgis.SqlLayerDefinitionCapability.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SqlKeywordCategory.Keyword.__doc__ = "SQL keyword"
Qgis.SqlKeywordCategory.Constant.__doc__ = "SQL constant"
Qgis.SqlKeywordCategory.Function.__doc__ = "SQL generic function"
Qgis.SqlKeywordCategory.Geospatial.__doc__ = "SQL spatial function"
Qgis.SqlKeywordCategory.Operator.__doc__ = "SQL operator"
Qgis.SqlKeywordCategory.Math.__doc__ = "SQL math function"
Qgis.SqlKeywordCategory.Aggregate.__doc__ = "SQL aggregate function"
Qgis.SqlKeywordCategory.String.__doc__ = "SQL string function"
Qgis.SqlKeywordCategory.Identifier.__doc__ = "SQL identifier"
Qgis.SqlKeywordCategory.__doc__ = 'SqlKeywordCategory enum represents the categories of the SQL keywords used by the SQL query editor.\n\n.. note::\n\n   The category has currently no usage, but it was planned for future uses.\n\n.. versionadded:: 3.22\n\n' + '* ``Keyword``: ' + Qgis.SqlKeywordCategory.Keyword.__doc__ + '\n' + '* ``Constant``: ' + Qgis.SqlKeywordCategory.Constant.__doc__ + '\n' + '* ``Function``: ' + Qgis.SqlKeywordCategory.Function.__doc__ + '\n' + '* ``Geospatial``: ' + Qgis.SqlKeywordCategory.Geospatial.__doc__ + '\n' + '* ``Operator``: ' + Qgis.SqlKeywordCategory.Operator.__doc__ + '\n' + '* ``Math``: ' + Qgis.SqlKeywordCategory.Math.__doc__ + '\n' + '* ``Aggregate``: ' + Qgis.SqlKeywordCategory.Aggregate.__doc__ + '\n' + '* ``String``: ' + Qgis.SqlKeywordCategory.String.__doc__ + '\n' + '* ``Identifier``: ' + Qgis.SqlKeywordCategory.Identifier.__doc__
# --
Qgis.SqlKeywordCategory.baseClass = Qgis
# monkey patching scoped based enum
Qgis.DriveType.Unknown.__doc__ = "Unknown type"
Qgis.DriveType.Invalid.__doc__ = "Invalid path"
Qgis.DriveType.Removable.__doc__ = "Removable drive"
Qgis.DriveType.Fixed.__doc__ = "Fixed drive"
Qgis.DriveType.Remote.__doc__ = "Remote drive"
Qgis.DriveType.CdRom.__doc__ = "CD-ROM"
Qgis.DriveType.RamDisk.__doc__ = "RAM disk"
Qgis.DriveType.__doc__ = 'Drive types\n\n.. versionadded:: 3.20\n\n' + '* ``Unknown``: ' + Qgis.DriveType.Unknown.__doc__ + '\n' + '* ``Invalid``: ' + Qgis.DriveType.Invalid.__doc__ + '\n' + '* ``Removable``: ' + Qgis.DriveType.Removable.__doc__ + '\n' + '* ``Fixed``: ' + Qgis.DriveType.Fixed.__doc__ + '\n' + '* ``Remote``: ' + Qgis.DriveType.Remote.__doc__ + '\n' + '* ``CdRom``: ' + Qgis.DriveType.CdRom.__doc__ + '\n' + '* ``RamDisk``: ' + Qgis.DriveType.RamDisk.__doc__
# --
Qgis.DriveType.baseClass = Qgis
QgsNetworkContentFetcherRegistry.FetchingMode = Qgis.ActionStart
# monkey patching scoped based enum
QgsNetworkContentFetcherRegistry.DownloadLater = Qgis.ActionStart.Deferred
QgsNetworkContentFetcherRegistry.DownloadLater.is_monkey_patched = True
QgsNetworkContentFetcherRegistry.DownloadLater.__doc__ = "Do not start immediately the action"
QgsNetworkContentFetcherRegistry.DownloadImmediately = Qgis.ActionStart.Immediate
QgsNetworkContentFetcherRegistry.DownloadImmediately.is_monkey_patched = True
QgsNetworkContentFetcherRegistry.DownloadImmediately.__doc__ = "Action will start immediately"
Qgis.ActionStart.__doc__ = 'Enum to determine when an operation would begin\n\n.. versionadded:: 3.22\n\n' + '* ``DownloadLater``: ' + Qgis.ActionStart.Deferred.__doc__ + '\n' + '* ``DownloadImmediately``: ' + Qgis.ActionStart.Immediate.__doc__
# --
Qgis.ActionStart.baseClass = Qgis
# monkey patching scoped based enum
Qgis.UnplacedLabelVisibility.FollowEngineSetting.__doc__ = "Respect the label engine setting"
Qgis.UnplacedLabelVisibility.NeverShow.__doc__ = "Never show unplaced labels, regardless of the engine setting"
Qgis.UnplacedLabelVisibility.__doc__ = 'Unplaced label visibility.\n\n.. versionadded:: 3.20\n\n' + '* ``FollowEngineSetting``: ' + Qgis.UnplacedLabelVisibility.FollowEngineSetting.__doc__ + '\n' + '* ``NeverShow``: ' + Qgis.UnplacedLabelVisibility.NeverShow.__doc__
# --
Qgis.UnplacedLabelVisibility.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SublayerQueryFlag.FastScan.__doc__ = "Indicates that the provider must scan for sublayers using the fastest possible approach -- e.g. by first checking that a uri has an extension which is known to be readable by the provider"
Qgis.SublayerQueryFlag.ResolveGeometryType.__doc__ = "Attempt to resolve the geometry type for vector sublayers"
Qgis.SublayerQueryFlag.CountFeatures.__doc__ = "Count features in vector sublayers"
Qgis.SublayerQueryFlag.IncludeSystemTables.__doc__ = "Include system or internal tables (these are not included by default)"
Qgis.SublayerQueryFlag.__doc__ = 'Flags which control how data providers will scan for sublayers in a dataset.\n\n.. versionadded:: 3.22\n\n' + '* ``FastScan``: ' + Qgis.SublayerQueryFlag.FastScan.__doc__ + '\n' + '* ``ResolveGeometryType``: ' + Qgis.SublayerQueryFlag.ResolveGeometryType.__doc__ + '\n' + '* ``CountFeatures``: ' + Qgis.SublayerQueryFlag.CountFeatures.__doc__ + '\n' + '* ``IncludeSystemTables``: ' + Qgis.SublayerQueryFlag.IncludeSystemTables.__doc__
# --
Qgis.SublayerQueryFlag.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SublayerFlag.SystemTable.__doc__ = "Sublayer is a system or internal table, which should be hidden by default"
Qgis.SublayerFlag.__doc__ = 'Flags which reflect the properties of sublayers in a dataset.\n\n.. versionadded:: 3.22\n\n' + '* ``SystemTable``: ' + Qgis.SublayerFlag.SystemTable.__doc__
# --
Qgis.SublayerFlag.baseClass = Qgis
QgsRasterPipe.Role = Qgis.RasterPipeInterfaceRole
# monkey patching scoped based enum
QgsRasterPipe.UnknownRole = Qgis.RasterPipeInterfaceRole.Unknown
QgsRasterPipe.UnknownRole.is_monkey_patched = True
QgsRasterPipe.UnknownRole.__doc__ = "Unknown role"
QgsRasterPipe.ProviderRole = Qgis.RasterPipeInterfaceRole.Provider
QgsRasterPipe.ProviderRole.is_monkey_patched = True
QgsRasterPipe.ProviderRole.__doc__ = "Data provider role"
QgsRasterPipe.RendererRole = Qgis.RasterPipeInterfaceRole.Renderer
QgsRasterPipe.RendererRole.is_monkey_patched = True
QgsRasterPipe.RendererRole.__doc__ = "Raster renderer role"
QgsRasterPipe.BrightnessRole = Qgis.RasterPipeInterfaceRole.Brightness
QgsRasterPipe.BrightnessRole.is_monkey_patched = True
QgsRasterPipe.BrightnessRole.__doc__ = "Brightness filter role"
QgsRasterPipe.ResamplerRole = Qgis.RasterPipeInterfaceRole.Resampler
QgsRasterPipe.ResamplerRole.is_monkey_patched = True
QgsRasterPipe.ResamplerRole.__doc__ = "Resampler role"
QgsRasterPipe.ProjectorRole = Qgis.RasterPipeInterfaceRole.Projector
QgsRasterPipe.ProjectorRole.is_monkey_patched = True
QgsRasterPipe.ProjectorRole.__doc__ = "Projector role"
QgsRasterPipe.NullerRole = Qgis.RasterPipeInterfaceRole.Nuller
QgsRasterPipe.NullerRole.is_monkey_patched = True
QgsRasterPipe.NullerRole.__doc__ = "Raster nuller role"
QgsRasterPipe.HueSaturationRole = Qgis.RasterPipeInterfaceRole.HueSaturation
QgsRasterPipe.HueSaturationRole.is_monkey_patched = True
QgsRasterPipe.HueSaturationRole.__doc__ = "Hue/saturation filter role (also applies grayscale/color inversion)"
Qgis.RasterPipeInterfaceRole.__doc__ = 'Raster pipe interface roles.\n\n.. versionadded:: 3.22\n\n' + '* ``UnknownRole``: ' + Qgis.RasterPipeInterfaceRole.Unknown.__doc__ + '\n' + '* ``ProviderRole``: ' + Qgis.RasterPipeInterfaceRole.Provider.__doc__ + '\n' + '* ``RendererRole``: ' + Qgis.RasterPipeInterfaceRole.Renderer.__doc__ + '\n' + '* ``BrightnessRole``: ' + Qgis.RasterPipeInterfaceRole.Brightness.__doc__ + '\n' + '* ``ResamplerRole``: ' + Qgis.RasterPipeInterfaceRole.Resampler.__doc__ + '\n' + '* ``ProjectorRole``: ' + Qgis.RasterPipeInterfaceRole.Projector.__doc__ + '\n' + '* ``NullerRole``: ' + Qgis.RasterPipeInterfaceRole.Nuller.__doc__ + '\n' + '* ``HueSaturationRole``: ' + Qgis.RasterPipeInterfaceRole.HueSaturation.__doc__
# --
Qgis.RasterPipeInterfaceRole.baseClass = Qgis
QgsRasterPipe.ResamplingStage = Qgis.RasterResamplingStage
# monkey patching scoped based enum
QgsRasterPipe.ResampleFilter = Qgis.RasterResamplingStage.ResampleFilter
QgsRasterPipe.ResampleFilter.is_monkey_patched = True
QgsRasterPipe.ResampleFilter.__doc__ = ""
QgsRasterPipe.Provider = Qgis.RasterResamplingStage.Provider
QgsRasterPipe.Provider.is_monkey_patched = True
QgsRasterPipe.Provider.__doc__ = ""
Qgis.RasterResamplingStage.__doc__ = 'Stage at which raster resampling occurs.\n\n.. versionadded:: 3.22\n\n' + '* ``ResampleFilter``: ' + Qgis.RasterResamplingStage.ResampleFilter.__doc__ + '\n' + '* ``Provider``: ' + Qgis.RasterResamplingStage.Provider.__doc__
# --
Qgis.RasterResamplingStage.baseClass = Qgis
# monkey patching scoped based enum
Qgis.MeshEditingErrorType.NoError.__doc__ = "No type"
Qgis.MeshEditingErrorType.InvalidFace.__doc__ = "An error occurs due to an invalid face (for example, vertex indexes are unordered)"
Qgis.MeshEditingErrorType.TooManyVerticesInFace.__doc__ = "A face has more vertices than the maximum number supported per face"
Qgis.MeshEditingErrorType.FlatFace.__doc__ = "A flat face is present"
Qgis.MeshEditingErrorType.UniqueSharedVertex.__doc__ = "A least two faces share only one vertices"
Qgis.MeshEditingErrorType.InvalidVertex.__doc__ = "An error occurs due to an invalid vertex (for example, vertex index is out of range the available vertex)"
Qgis.MeshEditingErrorType.ManifoldFace.__doc__ = "ManifoldFace"
Qgis.MeshEditingErrorType.__doc__ = 'Type of error that can occur during mesh frame editing.\n\n.. versionadded:: 3.22\n\n' + '* ``NoError``: ' + Qgis.MeshEditingErrorType.NoError.__doc__ + '\n' + '* ``InvalidFace``: ' + Qgis.MeshEditingErrorType.InvalidFace.__doc__ + '\n' + '* ``TooManyVerticesInFace``: ' + Qgis.MeshEditingErrorType.TooManyVerticesInFace.__doc__ + '\n' + '* ``FlatFace``: ' + Qgis.MeshEditingErrorType.FlatFace.__doc__ + '\n' + '* ``UniqueSharedVertex``: ' + Qgis.MeshEditingErrorType.UniqueSharedVertex.__doc__ + '\n' + '* ``InvalidVertex``: ' + Qgis.MeshEditingErrorType.InvalidVertex.__doc__ + '\n' + '* ``ManifoldFace``: ' + Qgis.MeshEditingErrorType.ManifoldFace.__doc__
# --
Qgis.MeshEditingErrorType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FilePathType.Absolute.__doc__ = "Absolute path"
Qgis.FilePathType.Relative.__doc__ = "Relative path"
Qgis.FilePathType.__doc__ = 'File path types.\n\n.. versionadded:: 3.22\n\n' + '* ``Absolute``: ' + Qgis.FilePathType.Absolute.__doc__ + '\n' + '* ``Relative``: ' + Qgis.FilePathType.Relative.__doc__
# --
Qgis.FilePathType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SublayerPromptMode.AlwaysAsk.__doc__ = "Always ask users to select from available sublayers, if sublayers are present"
Qgis.SublayerPromptMode.AskExcludingRasterBands.__doc__ = "Ask users to select from available sublayers, unless only raster bands are present"
Qgis.SublayerPromptMode.NeverAskSkip.__doc__ = "Never ask users to select sublayers, instead don't load anything"
Qgis.SublayerPromptMode.NeverAskLoadAll.__doc__ = "Never ask users to select sublayers, instead automatically load all available sublayers"
Qgis.SublayerPromptMode.__doc__ = 'Specifies how to handle layer sources with multiple sublayers.\n\n.. versionadded:: 3.22\n\n' + '* ``AlwaysAsk``: ' + Qgis.SublayerPromptMode.AlwaysAsk.__doc__ + '\n' + '* ``AskExcludingRasterBands``: ' + Qgis.SublayerPromptMode.AskExcludingRasterBands.__doc__ + '\n' + '* ``NeverAskSkip``: ' + Qgis.SublayerPromptMode.NeverAskSkip.__doc__ + '\n' + '* ``NeverAskLoadAll``: ' + Qgis.SublayerPromptMode.NeverAskLoadAll.__doc__
# --
Qgis.SublayerPromptMode.baseClass = Qgis
QgsVectorLayer.SelectBehavior = Qgis.SelectBehavior
# monkey patching scoped based enum
QgsVectorLayer.SetSelection = Qgis.SelectBehavior.SetSelection
QgsVectorLayer.SetSelection.is_monkey_patched = True
QgsVectorLayer.SetSelection.__doc__ = "Set selection, removing any existing selection"
QgsVectorLayer.AddToSelection = Qgis.SelectBehavior.AddToSelection
QgsVectorLayer.AddToSelection.is_monkey_patched = True
QgsVectorLayer.AddToSelection.__doc__ = "Add selection to current selection"
QgsVectorLayer.IntersectSelection = Qgis.SelectBehavior.IntersectSelection
QgsVectorLayer.IntersectSelection.is_monkey_patched = True
QgsVectorLayer.IntersectSelection.__doc__ = "Modify current selection to include only select features which match"
QgsVectorLayer.RemoveFromSelection = Qgis.SelectBehavior.RemoveFromSelection
QgsVectorLayer.RemoveFromSelection.is_monkey_patched = True
QgsVectorLayer.RemoveFromSelection.__doc__ = "Remove from current selection"
Qgis.SelectBehavior.__doc__ = 'Specifies how a selection should be applied.\n\n.. versionadded:: 3.22\n\n' + '* ``SetSelection``: ' + Qgis.SelectBehavior.SetSelection.__doc__ + '\n' + '* ``AddToSelection``: ' + Qgis.SelectBehavior.AddToSelection.__doc__ + '\n' + '* ``IntersectSelection``: ' + Qgis.SelectBehavior.IntersectSelection.__doc__ + '\n' + '* ``RemoveFromSelection``: ' + Qgis.SelectBehavior.RemoveFromSelection.__doc__
# --
Qgis.SelectBehavior.baseClass = Qgis
QgsVectorLayer.EditResult = Qgis.VectorEditResult
# monkey patching scoped based enum
QgsVectorLayer.Success = Qgis.VectorEditResult.Success
QgsVectorLayer.Success.is_monkey_patched = True
QgsVectorLayer.Success.__doc__ = "Edit operation was successful"
QgsVectorLayer.EmptyGeometry = Qgis.VectorEditResult.EmptyGeometry
QgsVectorLayer.EmptyGeometry.is_monkey_patched = True
QgsVectorLayer.EmptyGeometry.__doc__ = "Edit operation resulted in an empty geometry"
QgsVectorLayer.EditFailed = Qgis.VectorEditResult.EditFailed
QgsVectorLayer.EditFailed.is_monkey_patched = True
QgsVectorLayer.EditFailed.__doc__ = "Edit operation failed"
QgsVectorLayer.FetchFeatureFailed = Qgis.VectorEditResult.FetchFeatureFailed
QgsVectorLayer.FetchFeatureFailed.is_monkey_patched = True
QgsVectorLayer.FetchFeatureFailed.__doc__ = "Unable to fetch requested feature"
QgsVectorLayer.InvalidLayer = Qgis.VectorEditResult.InvalidLayer
QgsVectorLayer.InvalidLayer.is_monkey_patched = True
QgsVectorLayer.InvalidLayer.__doc__ = "Edit failed due to invalid layer"
Qgis.VectorEditResult.__doc__ = 'Specifies the result of a vector layer edit operation\n\n.. versionadded:: 3.22\n\n' + '* ``Success``: ' + Qgis.VectorEditResult.Success.__doc__ + '\n' + '* ``EmptyGeometry``: ' + Qgis.VectorEditResult.EmptyGeometry.__doc__ + '\n' + '* ``EditFailed``: ' + Qgis.VectorEditResult.EditFailed.__doc__ + '\n' + '* ``FetchFeatureFailed``: ' + Qgis.VectorEditResult.FetchFeatureFailed.__doc__ + '\n' + '* ``InvalidLayer``: ' + Qgis.VectorEditResult.InvalidLayer.__doc__
# --
Qgis.VectorEditResult.baseClass = Qgis
QgsSymbolLayerUtils.VertexMarkerType = Qgis.VertexMarkerType
# monkey patching scoped based enum
QgsSymbolLayerUtils.SemiTransparentCircle = Qgis.VertexMarkerType.SemiTransparentCircle
QgsSymbolLayerUtils.SemiTransparentCircle.is_monkey_patched = True
QgsSymbolLayerUtils.SemiTransparentCircle.__doc__ = "Semi-transparent circle marker"
QgsSymbolLayerUtils.Cross = Qgis.VertexMarkerType.Cross
QgsSymbolLayerUtils.Cross.is_monkey_patched = True
QgsSymbolLayerUtils.Cross.__doc__ = "Cross marker"
QgsSymbolLayerUtils.NoMarker = Qgis.VertexMarkerType.NoMarker
QgsSymbolLayerUtils.NoMarker.is_monkey_patched = True
QgsSymbolLayerUtils.NoMarker.__doc__ = "No marker"
Qgis.VertexMarkerType.__doc__ = 'Editing vertex markers, used for showing vertices during a edit operation.\n\n.. versionadded:: 3.22\n\n' + '* ``SemiTransparentCircle``: ' + Qgis.VertexMarkerType.SemiTransparentCircle.__doc__ + '\n' + '* ``Cross``: ' + Qgis.VertexMarkerType.Cross.__doc__ + '\n' + '* ``NoMarker``: ' + Qgis.VertexMarkerType.NoMarker.__doc__
# --
Qgis.VertexMarkerType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.ContentStatus.NotStarted.__doc__ = "Content fetching/storing has not started yet"
Qgis.ContentStatus.Running.__doc__ = "Content fetching/storing is in progress"
Qgis.ContentStatus.Finished.__doc__ = "Content fetching/storing is finished and successful"
Qgis.ContentStatus.Failed.__doc__ = "Content fetching/storing has failed"
Qgis.ContentStatus.Canceled.__doc__ = "Content fetching/storing has been canceled"
Qgis.ContentStatus.__doc__ = 'Status for fetched or stored content\n\n.. versionadded:: 3.22\n\n' + '* ``NotStarted``: ' + Qgis.ContentStatus.NotStarted.__doc__ + '\n' + '* ``Running``: ' + Qgis.ContentStatus.Running.__doc__ + '\n' + '* ``Finished``: ' + Qgis.ContentStatus.Finished.__doc__ + '\n' + '* ``Failed``: ' + Qgis.ContentStatus.Failed.__doc__ + '\n' + '* ``Canceled``: ' + Qgis.ContentStatus.Canceled.__doc__
# --
Qgis.ContentStatus.baseClass = Qgis
# monkey patching scoped based enum
Qgis.GpsQualityIndicator.Unknown.__doc__ = "Unknown"
Qgis.GpsQualityIndicator.Invalid.__doc__ = "Invalid"
Qgis.GpsQualityIndicator.GPS.__doc__ = "Standalone"
Qgis.GpsQualityIndicator.DGPS.__doc__ = "Differential GPS"
Qgis.GpsQualityIndicator.PPS.__doc__ = "PPS"
Qgis.GpsQualityIndicator.RTK.__doc__ = "Real-time-kynematic"
Qgis.GpsQualityIndicator.FloatRTK.__doc__ = "Float real-time-kynematic"
Qgis.GpsQualityIndicator.Estimated.__doc__ = "Estimated"
Qgis.GpsQualityIndicator.Manual.__doc__ = "Manual input mode"
Qgis.GpsQualityIndicator.Simulation.__doc__ = "Simulation mode"
Qgis.GpsQualityIndicator.__doc__ = 'GPS signal quality indicator\n\n.. versionadded:: 3.22.6\n\n' + '* ``Unknown``: ' + Qgis.GpsQualityIndicator.Unknown.__doc__ + '\n' + '* ``Invalid``: ' + Qgis.GpsQualityIndicator.Invalid.__doc__ + '\n' + '* ``GPS``: ' + Qgis.GpsQualityIndicator.GPS.__doc__ + '\n' + '* ``DGPS``: ' + Qgis.GpsQualityIndicator.DGPS.__doc__ + '\n' + '* ``PPS``: ' + Qgis.GpsQualityIndicator.PPS.__doc__ + '\n' + '* ``RTK``: ' + Qgis.GpsQualityIndicator.RTK.__doc__ + '\n' + '* ``FloatRTK``: ' + Qgis.GpsQualityIndicator.FloatRTK.__doc__ + '\n' + '* ``Estimated``: ' + Qgis.GpsQualityIndicator.Estimated.__doc__ + '\n' + '* ``Manual``: ' + Qgis.GpsQualityIndicator.Manual.__doc__ + '\n' + '* ``Simulation``: ' + Qgis.GpsQualityIndicator.Simulation.__doc__
# --
Qgis.GpsQualityIndicator.baseClass = Qgis
# monkey patching scoped based enum
Qgis.BabelFormatCapability.Import.__doc__ = "Format supports importing"
Qgis.BabelFormatCapability.Export.__doc__ = "Format supports exporting"
Qgis.BabelFormatCapability.Waypoints.__doc__ = "Format supports waypoints"
Qgis.BabelFormatCapability.Routes.__doc__ = "Format supports routes"
Qgis.BabelFormatCapability.Tracks.__doc__ = "Format supports tracks"
Qgis.BabelFormatCapability.__doc__ = 'Babel GPS format capabilities.\n\n.. versionadded:: 3.22\n\n' + '* ``Import``: ' + Qgis.BabelFormatCapability.Import.__doc__ + '\n' + '* ``Export``: ' + Qgis.BabelFormatCapability.Export.__doc__ + '\n' + '* ``Waypoints``: ' + Qgis.BabelFormatCapability.Waypoints.__doc__ + '\n' + '* ``Routes``: ' + Qgis.BabelFormatCapability.Routes.__doc__ + '\n' + '* ``Tracks``: ' + Qgis.BabelFormatCapability.Tracks.__doc__
# --
Qgis.BabelFormatCapability.baseClass = Qgis
# monkey patching scoped based enum
Qgis.BabelCommandFlag.QuoteFilePaths.__doc__ = "File paths should be enclosed in quotations and escaped"
Qgis.BabelCommandFlag.__doc__ = 'Babel command flags, which control how commands and arguments\nare generated for executing GPSBabel processes.\n\n.. versionadded:: 3.22\n\n' + '* ``QuoteFilePaths``: ' + Qgis.BabelCommandFlag.QuoteFilePaths.__doc__
# --
Qgis.BabelCommandFlag.baseClass = Qgis
# monkey patching scoped based enum
Qgis.GpsFeatureType.Waypoint.__doc__ = "Waypoint"
Qgis.GpsFeatureType.Route.__doc__ = "Route"
Qgis.GpsFeatureType.Track.__doc__ = "Track"
Qgis.GpsFeatureType.__doc__ = 'GPS feature types.\n\n.. versionadded:: 3.22\n\n' + '* ``Waypoint``: ' + Qgis.GpsFeatureType.Waypoint.__doc__ + '\n' + '* ``Route``: ' + Qgis.GpsFeatureType.Route.__doc__ + '\n' + '* ``Track``: ' + Qgis.GpsFeatureType.Track.__doc__
# --
Qgis.GpsFeatureType.baseClass = Qgis
QgsGeometry.OperationResult = Qgis.GeometryOperationResult
# monkey patching scoped based enum
QgsGeometry.Success = Qgis.GeometryOperationResult.Success
QgsGeometry.Success.is_monkey_patched = True
QgsGeometry.Success.__doc__ = "Operation succeeded"
QgsGeometry.NothingHappened = Qgis.GeometryOperationResult.NothingHappened
QgsGeometry.NothingHappened.is_monkey_patched = True
QgsGeometry.NothingHappened.__doc__ = "Nothing happened, without any error"
QgsGeometry.InvalidBaseGeometry = Qgis.GeometryOperationResult.InvalidBaseGeometry
QgsGeometry.InvalidBaseGeometry.is_monkey_patched = True
QgsGeometry.InvalidBaseGeometry.__doc__ = "The base geometry on which the operation is done is invalid or empty"
QgsGeometry.InvalidInputGeometryType = Qgis.GeometryOperationResult.InvalidInputGeometryType
QgsGeometry.InvalidInputGeometryType.is_monkey_patched = True
QgsGeometry.InvalidInputGeometryType.__doc__ = "The input geometry (ring, part, split line, etc.) has not the correct geometry type"
QgsGeometry.SelectionIsEmpty = Qgis.GeometryOperationResult.SelectionIsEmpty
QgsGeometry.SelectionIsEmpty.is_monkey_patched = True
QgsGeometry.SelectionIsEmpty.__doc__ = "No features were selected"
QgsGeometry.SelectionIsGreaterThanOne = Qgis.GeometryOperationResult.SelectionIsGreaterThanOne
QgsGeometry.SelectionIsGreaterThanOne.is_monkey_patched = True
QgsGeometry.SelectionIsGreaterThanOne.__doc__ = "More than one features were selected"
QgsGeometry.GeometryEngineError = Qgis.GeometryOperationResult.GeometryEngineError
QgsGeometry.GeometryEngineError.is_monkey_patched = True
QgsGeometry.GeometryEngineError.__doc__ = "Geometry engine misses a method implemented or an error occurred in the geometry engine"
QgsGeometry.LayerNotEditable = Qgis.GeometryOperationResult.LayerNotEditable
QgsGeometry.LayerNotEditable.is_monkey_patched = True
QgsGeometry.LayerNotEditable.__doc__ = "Cannot edit layer"
QgsGeometry.AddPartSelectedGeometryNotFound = Qgis.GeometryOperationResult.AddPartSelectedGeometryNotFound
QgsGeometry.AddPartSelectedGeometryNotFound.is_monkey_patched = True
QgsGeometry.AddPartSelectedGeometryNotFound.__doc__ = "The selected geometry cannot be found"
QgsGeometry.AddPartNotMultiGeometry = Qgis.GeometryOperationResult.AddPartNotMultiGeometry
QgsGeometry.AddPartNotMultiGeometry.is_monkey_patched = True
QgsGeometry.AddPartNotMultiGeometry.__doc__ = "The source geometry is not multi"
QgsGeometry.AddRingNotClosed = Qgis.GeometryOperationResult.AddRingNotClosed
QgsGeometry.AddRingNotClosed.is_monkey_patched = True
QgsGeometry.AddRingNotClosed.__doc__ = "The input ring is not closed"
QgsGeometry.AddRingNotValid = Qgis.GeometryOperationResult.AddRingNotValid
QgsGeometry.AddRingNotValid.is_monkey_patched = True
QgsGeometry.AddRingNotValid.__doc__ = "The input ring is not valid"
QgsGeometry.AddRingCrossesExistingRings = Qgis.GeometryOperationResult.AddRingCrossesExistingRings
QgsGeometry.AddRingCrossesExistingRings.is_monkey_patched = True
QgsGeometry.AddRingCrossesExistingRings.__doc__ = "The input ring crosses existing rings (it is not disjoint)"
QgsGeometry.AddRingNotInExistingFeature = Qgis.GeometryOperationResult.AddRingNotInExistingFeature
QgsGeometry.AddRingNotInExistingFeature.is_monkey_patched = True
QgsGeometry.AddRingNotInExistingFeature.__doc__ = "The input ring doesn't have any existing ring to fit into"
QgsGeometry.SplitCannotSplitPoint = Qgis.GeometryOperationResult.SplitCannotSplitPoint
QgsGeometry.SplitCannotSplitPoint.is_monkey_patched = True
QgsGeometry.SplitCannotSplitPoint.__doc__ = "Cannot split points"
Qgis.GeometryOperationResult.__doc__ = 'Split features */\n\n' + '* ``Success``: ' + Qgis.GeometryOperationResult.Success.__doc__ + '\n' + '* ``NothingHappened``: ' + Qgis.GeometryOperationResult.NothingHappened.__doc__ + '\n' + '* ``InvalidBaseGeometry``: ' + Qgis.GeometryOperationResult.InvalidBaseGeometry.__doc__ + '\n' + '* ``InvalidInputGeometryType``: ' + Qgis.GeometryOperationResult.InvalidInputGeometryType.__doc__ + '\n' + '* ``SelectionIsEmpty``: ' + Qgis.GeometryOperationResult.SelectionIsEmpty.__doc__ + '\n' + '* ``SelectionIsGreaterThanOne``: ' + Qgis.GeometryOperationResult.SelectionIsGreaterThanOne.__doc__ + '\n' + '* ``GeometryEngineError``: ' + Qgis.GeometryOperationResult.GeometryEngineError.__doc__ + '\n' + '* ``LayerNotEditable``: ' + Qgis.GeometryOperationResult.LayerNotEditable.__doc__ + '\n' + '* ``AddPartSelectedGeometryNotFound``: ' + Qgis.GeometryOperationResult.AddPartSelectedGeometryNotFound.__doc__ + '\n' + '* ``AddPartNotMultiGeometry``: ' + Qgis.GeometryOperationResult.AddPartNotMultiGeometry.__doc__ + '\n' + '* ``AddRingNotClosed``: ' + Qgis.GeometryOperationResult.AddRingNotClosed.__doc__ + '\n' + '* ``AddRingNotValid``: ' + Qgis.GeometryOperationResult.AddRingNotValid.__doc__ + '\n' + '* ``AddRingCrossesExistingRings``: ' + Qgis.GeometryOperationResult.AddRingCrossesExistingRings.__doc__ + '\n' + '* ``AddRingNotInExistingFeature``: ' + Qgis.GeometryOperationResult.AddRingNotInExistingFeature.__doc__ + '\n' + '* ``SplitCannotSplitPoint``: ' + Qgis.GeometryOperationResult.SplitCannotSplitPoint.__doc__
# --
Qgis.GeometryOperationResult.baseClass = Qgis
QgsGeometry.ValidityFlag = Qgis.GeometryValidityFlag
# monkey patching scoped based enum
QgsGeometry.FlagAllowSelfTouchingHoles = Qgis.GeometryValidityFlag.AllowSelfTouchingHoles
QgsGeometry.FlagAllowSelfTouchingHoles.is_monkey_patched = True
QgsGeometry.FlagAllowSelfTouchingHoles.__doc__ = "Indicates that self-touching holes are permitted. OGC validity states that self-touching holes are NOT permitted, whilst other vendor validity checks (e.g. ESRI) permit self-touching holes."
Qgis.GeometryValidityFlag.__doc__ = 'Geometry validity check flags.\n\n.. versionadded:: 3.22\n\n' + '* ``FlagAllowSelfTouchingHoles``: ' + Qgis.GeometryValidityFlag.AllowSelfTouchingHoles.__doc__
# --
QgsGeometry.ValidityFlags = Qgis.GeometryValidityFlags
Qgis.GeometryValidityFlag.baseClass = Qgis
QgsGeometry.ValidationMethod = Qgis.GeometryValidationEngine
# monkey patching scoped based enum
QgsGeometry.ValidatorQgisInternal = Qgis.GeometryValidationEngine.QgisInternal
QgsGeometry.ValidatorQgisInternal.is_monkey_patched = True
QgsGeometry.ValidatorQgisInternal.__doc__ = "Use internal QgsGeometryValidator method"
QgsGeometry.ValidatorGeos = Qgis.GeometryValidationEngine.Geos
QgsGeometry.ValidatorGeos.is_monkey_patched = True
QgsGeometry.ValidatorGeos.__doc__ = "Use GEOS validation methods"
Qgis.GeometryValidationEngine.__doc__ = 'Available engines for validating geometries.\n\n.. versionadded:: 3.22\n\n' + '* ``ValidatorQgisInternal``: ' + Qgis.GeometryValidationEngine.QgisInternal.__doc__ + '\n' + '* ``ValidatorGeos``: ' + Qgis.GeometryValidationEngine.Geos.__doc__
# --
Qgis.GeometryValidationEngine.baseClass = Qgis
QgsGeometry.BufferSide = Qgis.BufferSide
# monkey patching scoped based enum
QgsGeometry.SideLeft = Qgis.BufferSide.Left
QgsGeometry.SideLeft.is_monkey_patched = True
QgsGeometry.SideLeft.__doc__ = "Buffer to left of line"
QgsGeometry.SideRight = Qgis.BufferSide.Right
QgsGeometry.SideRight.is_monkey_patched = True
QgsGeometry.SideRight.__doc__ = "Buffer to right of line"
Qgis.BufferSide.__doc__ = 'Side of line to buffer.\n\n.. versionadded:: 3.22\n\n' + '* ``SideLeft``: ' + Qgis.BufferSide.Left.__doc__ + '\n' + '* ``SideRight``: ' + Qgis.BufferSide.Right.__doc__
# --
Qgis.BufferSide.baseClass = Qgis
QgsGeometry.EndCapStyle = Qgis.EndCapStyle
# monkey patching scoped based enum
QgsGeometry.CapRound = Qgis.EndCapStyle.Round
QgsGeometry.CapRound.is_monkey_patched = True
QgsGeometry.CapRound.__doc__ = "Round cap"
QgsGeometry.CapFlat = Qgis.EndCapStyle.Flat
QgsGeometry.CapFlat.is_monkey_patched = True
QgsGeometry.CapFlat.__doc__ = "Flat cap (in line with start/end of line)"
QgsGeometry.CapSquare = Qgis.EndCapStyle.Square
QgsGeometry.CapSquare.is_monkey_patched = True
QgsGeometry.CapSquare.__doc__ = "Square cap (extends past start/end of line by buffer distance)"
Qgis.EndCapStyle.__doc__ = 'End cap styles for buffers.\n\n.. versionadded:: 3.22\n\n' + '* ``CapRound``: ' + Qgis.EndCapStyle.Round.__doc__ + '\n' + '* ``CapFlat``: ' + Qgis.EndCapStyle.Flat.__doc__ + '\n' + '* ``CapSquare``: ' + Qgis.EndCapStyle.Square.__doc__
# --
Qgis.EndCapStyle.baseClass = Qgis
QgsGeometry.JoinStyle = Qgis.JoinStyle
# monkey patching scoped based enum
QgsGeometry.JoinStyleRound = Qgis.JoinStyle.Round
QgsGeometry.JoinStyleRound.is_monkey_patched = True
QgsGeometry.JoinStyleRound.__doc__ = "Use rounded joins"
QgsGeometry.JoinStyleMiter = Qgis.JoinStyle.Miter
QgsGeometry.JoinStyleMiter.is_monkey_patched = True
QgsGeometry.JoinStyleMiter.__doc__ = "Use mitered joins"
QgsGeometry.JoinStyleBevel = Qgis.JoinStyle.Bevel
QgsGeometry.JoinStyleBevel.is_monkey_patched = True
QgsGeometry.JoinStyleBevel.__doc__ = "Use beveled joins"
Qgis.JoinStyle.__doc__ = 'Join styles for buffers.\n\n.. versionadded:: 3.22\n\n' + '* ``JoinStyleRound``: ' + Qgis.JoinStyle.Round.__doc__ + '\n' + '* ``JoinStyleMiter``: ' + Qgis.JoinStyle.Miter.__doc__ + '\n' + '* ``JoinStyleBevel``: ' + Qgis.JoinStyle.Bevel.__doc__
# --
Qgis.JoinStyle.baseClass = Qgis
# monkey patching scoped based enum
Qgis.SpatialFilterType.NoFilter.__doc__ = "No spatial filtering of features"
Qgis.SpatialFilterType.BoundingBox.__doc__ = "Filter using a bounding box"
Qgis.SpatialFilterType.DistanceWithin.__doc__ = "Filter by distance to reference geometry"
Qgis.SpatialFilterType.__doc__ = 'Feature request spatial filter types.\n\n.. versionadded:: 3.22\n\n' + '* ``NoFilter``: ' + Qgis.SpatialFilterType.NoFilter.__doc__ + '\n' + '* ``BoundingBox``: ' + Qgis.SpatialFilterType.BoundingBox.__doc__ + '\n' + '* ``DistanceWithin``: ' + Qgis.SpatialFilterType.DistanceWithin.__doc__
# --
Qgis.SpatialFilterType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.FileOperationFlag.IncludeMetadataFile.__doc__ = "Indicates that any associated .qmd metadata file should be included with the operation"
Qgis.FileOperationFlag.IncludeStyleFile.__doc__ = "Indicates that any associated .qml styling file should be included with the operation"
Qgis.FileOperationFlag.__doc__ = 'File operation flags.\n\n.. versionadded:: 3.22\n\n' + '* ``IncludeMetadataFile``: ' + Qgis.FileOperationFlag.IncludeMetadataFile.__doc__ + '\n' + '* ``IncludeStyleFile``: ' + Qgis.FileOperationFlag.IncludeStyleFile.__doc__
# --
Qgis.FileOperationFlag.baseClass = Qgis
# monkey patching scoped based enum
Qgis.MapLayerProperty.UsersCannotToggleEditing.__doc__ = "Indicates that users are not allowed to toggle editing for this layer. Note that this does not imply that the layer is non-editable (see isEditable(), supportsEditing() ), rather that the editable status of the layer cannot be changed by users manually. Since QGIS 3.22."
Qgis.MapLayerProperty.__doc__ = 'Generic map layer properties.\n\n.. versionadded:: 3.22\n\n' + '* ``UsersCannotToggleEditing``: ' + Qgis.MapLayerProperty.UsersCannotToggleEditing.__doc__
# --
Qgis.MapLayerProperty.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AnnotationItemFlag.ScaleDependentBoundingBox.__doc__ = "Item's bounding box will vary depending on map scale"
Qgis.AnnotationItemFlag.__doc__ = 'Flags for annotation items.\n\n.. versionadded:: 3.22\n\n' + '* ``ScaleDependentBoundingBox``: ' + Qgis.AnnotationItemFlag.ScaleDependentBoundingBox.__doc__
# --
Qgis.AnnotationItemFlag.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AnnotationItemGuiFlag.FlagNoCreationTools.__doc__ = "Do not show item creation tools for the item type"
Qgis.AnnotationItemGuiFlag.__doc__ = 'Flags for controlling how an annotation item behaves in the GUI.\n\n.. versionadded:: 3.22\n\n' + '* ``FlagNoCreationTools``: ' + Qgis.AnnotationItemGuiFlag.FlagNoCreationTools.__doc__
# --
Qgis.AnnotationItemGuiFlag.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AnnotationItemNodeType.VertexHandle.__doc__ = "Node is a handle for manipulating vertices"
Qgis.AnnotationItemNodeType.__doc__ = 'Annotation item node types.\n\n.. versionadded:: 3.22\n\n' + '* ``VertexHandle``: ' + Qgis.AnnotationItemNodeType.VertexHandle.__doc__
# --
Qgis.AnnotationItemNodeType.baseClass = Qgis
# monkey patching scoped based enum
Qgis.AnnotationItemEditOperationResult.Success.__doc__ = "Item was modified successfully"
Qgis.AnnotationItemEditOperationResult.Invalid.__doc__ = "Operation has invalid parameters for the item, no change occurred"
Qgis.AnnotationItemEditOperationResult.ItemCleared.__doc__ = "The operation results in the item being cleared, and the item should be removed from the layer as a result"
Qgis.AnnotationItemEditOperationResult.__doc__ = 'Results from an edit operation on an annotation item.\n\n.. versionadded:: 3.22\n\n' + '* ``Success``: ' + Qgis.AnnotationItemEditOperationResult.Success.__doc__ + '\n' + '* ``Invalid``: ' + Qgis.AnnotationItemEditOperationResult.Invalid.__doc__ + '\n' + '* ``ItemCleared``: ' + Qgis.AnnotationItemEditOperationResult.ItemCleared.__doc__
# --
Qgis.AnnotationItemEditOperationResult.baseClass = Qgis
QgsVectorLayerTemporalProperties.TemporalMode = Qgis.VectorTemporalMode
# monkey patching scoped based enum
QgsVectorLayerTemporalProperties.ModeFixedTemporalRange = Qgis.VectorTemporalMode.FixedTemporalRange
QgsVectorLayerTemporalProperties.ModeFixedTemporalRange.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFixedTemporalRange.__doc__ = "Mode when temporal properties have fixed start and end datetimes."
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeInstantFromField = Qgis.VectorTemporalMode.FeatureDateTimeInstantFromField
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeInstantFromField.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeInstantFromField.__doc__ = "Mode when features have a datetime instant taken from a single field"
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromFields = Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromFields
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromFields.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromFields.__doc__ = "Mode when features have separate fields for start and end times"
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndDurationFromFields = Qgis.VectorTemporalMode.FeatureDateTimeStartAndDurationFromFields
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndDurationFromFields.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndDurationFromFields.__doc__ = "Mode when features have a field for start time and a field for event duration"
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromExpressions = Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromExpressions
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromExpressions.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeFeatureDateTimeStartAndEndFromExpressions.__doc__ = "Mode when features use expressions for start and end times"
QgsVectorLayerTemporalProperties.ModeRedrawLayerOnly = Qgis.VectorTemporalMode.RedrawLayerOnly
QgsVectorLayerTemporalProperties.ModeRedrawLayerOnly.is_monkey_patched = True
QgsVectorLayerTemporalProperties.ModeRedrawLayerOnly.__doc__ = "Redraw the layer when temporal range changes, but don't apply any filtering. Useful when symbology or rule based renderer expressions depend on the time range."
Qgis.VectorTemporalMode.__doc__ = 'Vector layer temporal feature modes\n\n.. versionadded:: 3.22\n\n' + '* ``ModeFixedTemporalRange``: ' + Qgis.VectorTemporalMode.FixedTemporalRange.__doc__ + '\n' + '* ``ModeFeatureDateTimeInstantFromField``: ' + Qgis.VectorTemporalMode.FeatureDateTimeInstantFromField.__doc__ + '\n' + '* ``ModeFeatureDateTimeStartAndEndFromFields``: ' + Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromFields.__doc__ + '\n' + '* ``ModeFeatureDateTimeStartAndDurationFromFields``: ' + Qgis.VectorTemporalMode.FeatureDateTimeStartAndDurationFromFields.__doc__ + '\n' + '* ``ModeFeatureDateTimeStartAndEndFromExpressions``: ' + Qgis.VectorTemporalMode.FeatureDateTimeStartAndEndFromExpressions.__doc__ + '\n' + '* ``ModeRedrawLayerOnly``: ' + Qgis.VectorTemporalMode.RedrawLayerOnly.__doc__
# --
Qgis.VectorTemporalMode.baseClass = Qgis
# monkey patching scoped based enum
Qgis.VectorTemporalLimitMode.IncludeBeginExcludeEnd.__doc__ = "Default mode: include the Begin limit, but exclude the End limit"
Qgis.VectorTemporalLimitMode.IncludeBeginIncludeEnd.__doc__ = "Mode to include both limits of the filtering timeframe"
Qgis.VectorTemporalLimitMode.__doc__ = 'Mode for the handling of the limits of the filtering timeframe for vector features\n\n.. versionadded:: 3.22\n\n' + '* ``IncludeBeginExcludeEnd``: ' + Qgis.VectorTemporalLimitMode.IncludeBeginExcludeEnd.__doc__ + '\n' + '* ``IncludeBeginIncludeEnd``: ' + Qgis.VectorTemporalLimitMode.IncludeBeginIncludeEnd.__doc__
# --
Qgis.VectorTemporalLimitMode.baseClass = Qgis
QgsVectorDataProviderTemporalCapabilities.TemporalMode = Qgis.VectorDataProviderTemporalMode
# monkey patching scoped based enum
QgsVectorDataProviderTemporalCapabilities.ProviderHasFixedTemporalRange = Qgis.VectorDataProviderTemporalMode.HasFixedTemporalRange
QgsVectorDataProviderTemporalCapabilities.ProviderHasFixedTemporalRange.is_monkey_patched = True
QgsVectorDataProviderTemporalCapabilities.ProviderHasFixedTemporalRange.__doc__ = "Entire dataset from provider has a fixed start and end datetime."
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeInstantInField = Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeInstantInField
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeInstantInField.is_monkey_patched = True
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeInstantInField.__doc__ = "Dataset has feature datetime instants stored in a single field"
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeStartAndEndInSeparateFields = Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeStartAndEndInSeparateFields
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeStartAndEndInSeparateFields.is_monkey_patched = True
QgsVectorDataProviderTemporalCapabilities.ProviderStoresFeatureDateTimeStartAndEndInSeparateFields.__doc__ = "Dataset stores feature start and end datetimes in separate fields"
Qgis.VectorDataProviderTemporalMode.__doc__ = 'Vector data provider temporal handling modes.\n\n.. versionadded:: 3.22\n\n' + '* ``ProviderHasFixedTemporalRange``: ' + Qgis.VectorDataProviderTemporalMode.HasFixedTemporalRange.__doc__ + '\n' + '* ``ProviderStoresFeatureDateTimeInstantInField``: ' + Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeInstantInField.__doc__ + '\n' + '* ``ProviderStoresFeatureDateTimeStartAndEndInSeparateFields``: ' + Qgis.VectorDataProviderTemporalMode.StoresFeatureDateTimeStartAndEndInSeparateFields.__doc__
# --
Qgis.VectorDataProviderTemporalMode.baseClass = Qgis
QgsRasterLayerTemporalProperties.TemporalMode = Qgis.RasterTemporalMode
# monkey patching scoped based enum
QgsRasterLayerTemporalProperties.ModeFixedTemporalRange = Qgis.RasterTemporalMode.FixedTemporalRange
QgsRasterLayerTemporalProperties.ModeFixedTemporalRange.is_monkey_patched = True
QgsRasterLayerTemporalProperties.ModeFixedTemporalRange.__doc__ = "Mode when temporal properties have fixed start and end datetimes."
QgsRasterLayerTemporalProperties.ModeTemporalRangeFromDataProvider = Qgis.RasterTemporalMode.TemporalRangeFromDataProvider
QgsRasterLayerTemporalProperties.ModeTemporalRangeFromDataProvider.is_monkey_patched = True
QgsRasterLayerTemporalProperties.ModeTemporalRangeFromDataProvider.__doc__ = "Mode when raster layer delegates temporal range handling to the dataprovider."
QgsRasterLayerTemporalProperties.ModeRedrawLayerOnly = Qgis.RasterTemporalMode.RedrawLayerOnly
QgsRasterLayerTemporalProperties.ModeRedrawLayerOnly.is_monkey_patched = True
QgsRasterLayerTemporalProperties.ModeRedrawLayerOnly.__doc__ = "Redraw the layer when temporal range changes, but don't apply any filtering. Useful when raster symbology expressions depend on the time range. (since QGIS 3.22)"
Qgis.RasterTemporalMode.__doc__ = 'Raster layer temporal modes\n\n.. versionadded:: 3.22\n\n' + '* ``ModeFixedTemporalRange``: ' + Qgis.RasterTemporalMode.FixedTemporalRange.__doc__ + '\n' + '* ``ModeTemporalRangeFromDataProvider``: ' + Qgis.RasterTemporalMode.TemporalRangeFromDataProvider.__doc__ + '\n' + '* ``ModeRedrawLayerOnly``: ' + Qgis.RasterTemporalMode.RedrawLayerOnly.__doc__
# --
Qgis.RasterTemporalMode.baseClass = Qgis
QgsRasterDataProviderTemporalCapabilities.IntervalHandlingMethod = Qgis.TemporalIntervalMatchMethod
# monkey patching scoped based enum
QgsRasterDataProviderTemporalCapabilities.MatchUsingWholeRange = Qgis.TemporalIntervalMatchMethod.MatchUsingWholeRange
QgsRasterDataProviderTemporalCapabilities.MatchUsingWholeRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.MatchUsingWholeRange.__doc__ = "Use an exact match to the whole temporal range"
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingStartOfRange = Qgis.TemporalIntervalMatchMethod.MatchExactUsingStartOfRange
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingStartOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingStartOfRange.__doc__ = "Match the start of the temporal range to a corresponding layer or band, and only use exact matching results"
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingEndOfRange = Qgis.TemporalIntervalMatchMethod.MatchExactUsingEndOfRange
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingEndOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.MatchExactUsingEndOfRange.__doc__ = "Match the end of the temporal range to a corresponding layer or band, and only use exact matching results"
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToStartOfRange = Qgis.TemporalIntervalMatchMethod.FindClosestMatchToStartOfRange
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToStartOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToStartOfRange.__doc__ = "Match the start of the temporal range to the least previous closest datetime."
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToEndOfRange = Qgis.TemporalIntervalMatchMethod.FindClosestMatchToEndOfRange
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToEndOfRange.is_monkey_patched = True
QgsRasterDataProviderTemporalCapabilities.FindClosestMatchToEndOfRange.__doc__ = "Match the end of the temporal range to the least previous closest datetime."
Qgis.TemporalIntervalMatchMethod.__doc__ = 'Method to use when resolving a temporal range to a data provider layer or band.\n\n.. versionadded:: 3.22\n\n' + '* ``MatchUsingWholeRange``: ' + Qgis.TemporalIntervalMatchMethod.MatchUsingWholeRange.__doc__ + '\n' + '* ``MatchExactUsingStartOfRange``: ' + Qgis.TemporalIntervalMatchMethod.MatchExactUsingStartOfRange.__doc__ + '\n' + '* ``MatchExactUsingEndOfRange``: ' + Qgis.TemporalIntervalMatchMethod.MatchExactUsingEndOfRange.__doc__ + '\n' + '* ``FindClosestMatchToStartOfRange``: ' + Qgis.TemporalIntervalMatchMethod.FindClosestMatchToStartOfRange.__doc__ + '\n' + '* ``FindClosestMatchToEndOfRange``: ' + Qgis.TemporalIntervalMatchMethod.FindClosestMatchToEndOfRange.__doc__
# --
Qgis.TemporalIntervalMatchMethod.baseClass = Qgis
QgsCoordinateTransform.TransformDirection = Qgis.TransformDirection
# monkey patching scoped based enum
QgsCoordinateTransform.ForwardTransform = Qgis.TransformDirection.Forward
QgsCoordinateTransform.ForwardTransform.is_monkey_patched = True
QgsCoordinateTransform.ForwardTransform.__doc__ = "Forward transform (from source to destination)"
QgsCoordinateTransform.ReverseTransform = Qgis.TransformDirection.Reverse
QgsCoordinateTransform.ReverseTransform.is_monkey_patched = True
QgsCoordinateTransform.ReverseTransform.__doc__ = "Reverse/inverse transform (from destination to source)"
Qgis.TransformDirection.__doc__ = 'Indicates the direction (forward or inverse) of a transform.\n\n.. versionadded:: 3.22\n\n' + '* ``ForwardTransform``: ' + Qgis.TransformDirection.Forward.__doc__ + '\n' + '* ``ReverseTransform``: ' + Qgis.TransformDirection.Reverse.__doc__
# --
Qgis.TransformDirection.baseClass = Qgis
QgsMapSettings.Flag = Qgis.MapSettingsFlag
# monkey patching scoped based enum
QgsMapSettings.Antialiasing = Qgis.MapSettingsFlag.Antialiasing
QgsMapSettings.Antialiasing.is_monkey_patched = True
QgsMapSettings.Antialiasing.__doc__ = "Enable anti-aliasing for map rendering"
QgsMapSettings.DrawEditingInfo = Qgis.MapSettingsFlag.DrawEditingInfo
QgsMapSettings.DrawEditingInfo.is_monkey_patched = True
QgsMapSettings.DrawEditingInfo.__doc__ = "Enable drawing of vertex markers for layers in editing mode"
QgsMapSettings.ForceVectorOutput = Qgis.MapSettingsFlag.ForceVectorOutput
QgsMapSettings.ForceVectorOutput.is_monkey_patched = True
QgsMapSettings.ForceVectorOutput.__doc__ = "Vector graphics should not be cached and drawn as raster images"
QgsMapSettings.UseAdvancedEffects = Qgis.MapSettingsFlag.UseAdvancedEffects
QgsMapSettings.UseAdvancedEffects.is_monkey_patched = True
QgsMapSettings.UseAdvancedEffects.__doc__ = "Enable layer opacity and blending effects"
QgsMapSettings.DrawLabeling = Qgis.MapSettingsFlag.DrawLabeling
QgsMapSettings.DrawLabeling.is_monkey_patched = True
QgsMapSettings.DrawLabeling.__doc__ = "Enable drawing of labels on top of the map"
QgsMapSettings.UseRenderingOptimization = Qgis.MapSettingsFlag.UseRenderingOptimization
QgsMapSettings.UseRenderingOptimization.is_monkey_patched = True
QgsMapSettings.UseRenderingOptimization.__doc__ = "Enable vector simplification and other rendering optimizations"
QgsMapSettings.DrawSelection = Qgis.MapSettingsFlag.DrawSelection
QgsMapSettings.DrawSelection.is_monkey_patched = True
QgsMapSettings.DrawSelection.__doc__ = "Whether vector selections should be shown in the rendered map"
QgsMapSettings.DrawSymbolBounds = Qgis.MapSettingsFlag.DrawSymbolBounds
QgsMapSettings.DrawSymbolBounds.is_monkey_patched = True
QgsMapSettings.DrawSymbolBounds.__doc__ = "Draw bounds of symbols (for debugging/testing)"
QgsMapSettings.RenderMapTile = Qgis.MapSettingsFlag.RenderMapTile
QgsMapSettings.RenderMapTile.is_monkey_patched = True
QgsMapSettings.RenderMapTile.__doc__ = "Draw map such that there are no problems between adjacent tiles"
QgsMapSettings.RenderPartialOutput = Qgis.MapSettingsFlag.RenderPartialOutput
QgsMapSettings.RenderPartialOutput.is_monkey_patched = True
QgsMapSettings.RenderPartialOutput.__doc__ = "Whether to make extra effort to update map image with partially rendered layers (better for interactive map canvas). Added in QGIS 3.0"
QgsMapSettings.RenderPreviewJob = Qgis.MapSettingsFlag.RenderPreviewJob
QgsMapSettings.RenderPreviewJob.is_monkey_patched = True
QgsMapSettings.RenderPreviewJob.__doc__ = "Render is a 'canvas preview' render, and shortcuts should be taken to ensure fast rendering"
QgsMapSettings.RenderBlocking = Qgis.MapSettingsFlag.RenderBlocking
QgsMapSettings.RenderBlocking.is_monkey_patched = True
QgsMapSettings.RenderBlocking.__doc__ = "Render and load remote sources in the same thread to ensure rendering remote sources (svg and images). WARNING: this flag must NEVER be used from GUI based applications (like the main QGIS application) or crashes will result. Only for use in external scripts or QGIS server."
QgsMapSettings.LosslessImageRendering = Qgis.MapSettingsFlag.LosslessImageRendering
QgsMapSettings.LosslessImageRendering.is_monkey_patched = True
QgsMapSettings.LosslessImageRendering.__doc__ = "Render images losslessly whenever possible, instead of the default lossy jpeg rendering used for some destination devices (e.g. PDF). This flag only works with builds based on Qt 5.13 or later."
QgsMapSettings.Render3DMap = Qgis.MapSettingsFlag.Render3DMap
QgsMapSettings.Render3DMap.is_monkey_patched = True
QgsMapSettings.Render3DMap.__doc__ = "Render is for a 3D map"
Qgis.MapSettingsFlag.__doc__ = 'Flags which adjust the way maps are rendered.\n\n.. versionadded:: 3.22\n\n' + '* ``Antialiasing``: ' + Qgis.MapSettingsFlag.Antialiasing.__doc__ + '\n' + '* ``DrawEditingInfo``: ' + Qgis.MapSettingsFlag.DrawEditingInfo.__doc__ + '\n' + '* ``ForceVectorOutput``: ' + Qgis.MapSettingsFlag.ForceVectorOutput.__doc__ + '\n' + '* ``UseAdvancedEffects``: ' + Qgis.MapSettingsFlag.UseAdvancedEffects.__doc__ + '\n' + '* ``DrawLabeling``: ' + Qgis.MapSettingsFlag.DrawLabeling.__doc__ + '\n' + '* ``UseRenderingOptimization``: ' + Qgis.MapSettingsFlag.UseRenderingOptimization.__doc__ + '\n' + '* ``DrawSelection``: ' + Qgis.MapSettingsFlag.DrawSelection.__doc__ + '\n' + '* ``DrawSymbolBounds``: ' + Qgis.MapSettingsFlag.DrawSymbolBounds.__doc__ + '\n' + '* ``RenderMapTile``: ' + Qgis.MapSettingsFlag.RenderMapTile.__doc__ + '\n' + '* ``RenderPartialOutput``: ' + Qgis.MapSettingsFlag.RenderPartialOutput.__doc__ + '\n' + '* ``RenderPreviewJob``: ' + Qgis.MapSettingsFlag.RenderPreviewJob.__doc__ + '\n' + '* ``RenderBlocking``: ' + Qgis.MapSettingsFlag.RenderBlocking.__doc__ + '\n' + '* ``LosslessImageRendering``: ' + Qgis.MapSettingsFlag.LosslessImageRendering.__doc__ + '\n' + '* ``Render3DMap``: ' + Qgis.MapSettingsFlag.Render3DMap.__doc__
# --
QgsMapSettings.Flags = Qgis.MapSettingsFlags
Qgis.MapSettingsFlag.baseClass = Qgis
QgsRenderContext.Flag = Qgis.RenderContextFlag
# monkey patching scoped based enum
QgsRenderContext.DrawEditingInfo = Qgis.RenderContextFlag.DrawEditingInfo
QgsRenderContext.DrawEditingInfo.is_monkey_patched = True
QgsRenderContext.DrawEditingInfo.__doc__ = "Enable drawing of vertex markers for layers in editing mode"
QgsRenderContext.ForceVectorOutput = Qgis.RenderContextFlag.ForceVectorOutput
QgsRenderContext.ForceVectorOutput.is_monkey_patched = True
QgsRenderContext.ForceVectorOutput.__doc__ = "Vector graphics should not be cached and drawn as raster images"
QgsRenderContext.UseAdvancedEffects = Qgis.RenderContextFlag.UseAdvancedEffects
QgsRenderContext.UseAdvancedEffects.is_monkey_patched = True
QgsRenderContext.UseAdvancedEffects.__doc__ = "Enable layer opacity and blending effects"
QgsRenderContext.UseRenderingOptimization = Qgis.RenderContextFlag.UseRenderingOptimization
QgsRenderContext.UseRenderingOptimization.is_monkey_patched = True
QgsRenderContext.UseRenderingOptimization.__doc__ = "Enable vector simplification and other rendering optimizations"
QgsRenderContext.DrawSelection = Qgis.RenderContextFlag.DrawSelection
QgsRenderContext.DrawSelection.is_monkey_patched = True
QgsRenderContext.DrawSelection.__doc__ = "Whether vector selections should be shown in the rendered map"
QgsRenderContext.DrawSymbolBounds = Qgis.RenderContextFlag.DrawSymbolBounds
QgsRenderContext.DrawSymbolBounds.is_monkey_patched = True
QgsRenderContext.DrawSymbolBounds.__doc__ = "Draw bounds of symbols (for debugging/testing)"
QgsRenderContext.RenderMapTile = Qgis.RenderContextFlag.RenderMapTile
QgsRenderContext.RenderMapTile.is_monkey_patched = True
QgsRenderContext.RenderMapTile.__doc__ = "Draw map such that there are no problems between adjacent tiles"
QgsRenderContext.Antialiasing = Qgis.RenderContextFlag.Antialiasing
QgsRenderContext.Antialiasing.is_monkey_patched = True
QgsRenderContext.Antialiasing.__doc__ = "Use antialiasing while drawing"
QgsRenderContext.RenderPartialOutput = Qgis.RenderContextFlag.RenderPartialOutput
QgsRenderContext.RenderPartialOutput.is_monkey_patched = True
QgsRenderContext.RenderPartialOutput.__doc__ = "Whether to make extra effort to update map image with partially rendered layers (better for interactive map canvas). Added in QGIS 3.0"
QgsRenderContext.RenderPreviewJob = Qgis.RenderContextFlag.RenderPreviewJob
QgsRenderContext.RenderPreviewJob.is_monkey_patched = True
QgsRenderContext.RenderPreviewJob.__doc__ = "Render is a 'canvas preview' render, and shortcuts should be taken to ensure fast rendering"
QgsRenderContext.RenderBlocking = Qgis.RenderContextFlag.RenderBlocking
QgsRenderContext.RenderBlocking.is_monkey_patched = True
QgsRenderContext.RenderBlocking.__doc__ = "Render and load remote sources in the same thread to ensure rendering remote sources (svg and images). WARNING: this flag must NEVER be used from GUI based applications (like the main QGIS application) or crashes will result. Only for use in external scripts or QGIS server."
QgsRenderContext.RenderSymbolPreview = Qgis.RenderContextFlag.RenderSymbolPreview
QgsRenderContext.RenderSymbolPreview.is_monkey_patched = True
QgsRenderContext.RenderSymbolPreview.__doc__ = "The render is for a symbol preview only and map based properties may not be available, so care should be taken to handle map unit based sizes in an appropriate way."
QgsRenderContext.LosslessImageRendering = Qgis.RenderContextFlag.LosslessImageRendering
QgsRenderContext.LosslessImageRendering.is_monkey_patched = True
QgsRenderContext.LosslessImageRendering.__doc__ = "Render images losslessly whenever possible, instead of the default lossy jpeg rendering used for some destination devices (e.g. PDF). This flag only works with builds based on Qt 5.13 or later."
QgsRenderContext.ApplyScalingWorkaroundForTextRendering = Qgis.RenderContextFlag.ApplyScalingWorkaroundForTextRendering
QgsRenderContext.ApplyScalingWorkaroundForTextRendering.is_monkey_patched = True
QgsRenderContext.ApplyScalingWorkaroundForTextRendering.__doc__ = "Whether a scaling workaround designed to stablise the rendering of small font sizes (or for painters scaled out by a large amount) when rendering text. Generally this is recommended, but it may incur some performance cost."
QgsRenderContext.Render3DMap = Qgis.RenderContextFlag.Render3DMap
QgsRenderContext.Render3DMap.is_monkey_patched = True
QgsRenderContext.Render3DMap.__doc__ = "Render is for a 3D map"
QgsRenderContext.ApplyClipAfterReprojection = Qgis.RenderContextFlag.ApplyClipAfterReprojection
QgsRenderContext.ApplyClipAfterReprojection.is_monkey_patched = True
QgsRenderContext.ApplyClipAfterReprojection.__doc__ = "Feature geometry clipping to mapExtent() must be performed after the geometries are transformed using coordinateTransform(). Usually feature geometry clipping occurs using the extent() in the layer's CRS prior to geometry transformation, but in some cases when extent() could not be accurately calculated it is necessary to clip geometries to mapExtent() AFTER transforming them using coordinateTransform()."
QgsRenderContext.RenderingSubSymbol = Qgis.RenderContextFlag.RenderingSubSymbol
QgsRenderContext.RenderingSubSymbol.is_monkey_patched = True
QgsRenderContext.RenderingSubSymbol.__doc__ = "Set whenever a sub-symbol of a parent symbol is currently being rendered. Can be used during symbol and symbol layer rendering to determine whether the symbol being rendered is a subsymbol. (Since QGIS 3.24)"
Qgis.RenderContextFlag.__doc__ = 'Flags which affect rendering operations.\n\n.. versionadded:: 3.22\n\n' + '* ``DrawEditingInfo``: ' + Qgis.RenderContextFlag.DrawEditingInfo.__doc__ + '\n' + '* ``ForceVectorOutput``: ' + Qgis.RenderContextFlag.ForceVectorOutput.__doc__ + '\n' + '* ``UseAdvancedEffects``: ' + Qgis.RenderContextFlag.UseAdvancedEffects.__doc__ + '\n' + '* ``UseRenderingOptimization``: ' + Qgis.RenderContextFlag.UseRenderingOptimization.__doc__ + '\n' + '* ``DrawSelection``: ' + Qgis.RenderContextFlag.DrawSelection.__doc__ + '\n' + '* ``DrawSymbolBounds``: ' + Qgis.RenderContextFlag.DrawSymbolBounds.__doc__ + '\n' + '* ``RenderMapTile``: ' + Qgis.RenderContextFlag.RenderMapTile.__doc__ + '\n' + '* ``Antialiasing``: ' + Qgis.RenderContextFlag.Antialiasing.__doc__ + '\n' + '* ``RenderPartialOutput``: ' + Qgis.RenderContextFlag.RenderPartialOutput.__doc__ + '\n' + '* ``RenderPreviewJob``: ' + Qgis.RenderContextFlag.RenderPreviewJob.__doc__ + '\n' + '* ``RenderBlocking``: ' + Qgis.RenderContextFlag.RenderBlocking.__doc__ + '\n' + '* ``RenderSymbolPreview``: ' + Qgis.RenderContextFlag.RenderSymbolPreview.__doc__ + '\n' + '* ``LosslessImageRendering``: ' + Qgis.RenderContextFlag.LosslessImageRendering.__doc__ + '\n' + '* ``ApplyScalingWorkaroundForTextRendering``: ' + Qgis.RenderContextFlag.ApplyScalingWorkaroundForTextRendering.__doc__ + '\n' + '* ``Render3DMap``: ' + Qgis.RenderContextFlag.Render3DMap.__doc__ + '\n' + '* ``ApplyClipAfterReprojection``: ' + Qgis.RenderContextFlag.ApplyClipAfterReprojection.__doc__ + '\n' + '* ``RenderingSubSymbol``: ' + Qgis.RenderContextFlag.RenderingSubSymbol.__doc__
# --
QgsRenderContext.Flags = Qgis.RenderContextFlags
Qgis.RenderContextFlag.baseClass = Qgis
QgsRenderContext.TextRenderFormat = Qgis.TextRenderFormat
# monkey patching scoped based enum
QgsRenderContext.TextFormatAlwaysOutlines = Qgis.TextRenderFormat.AlwaysOutlines
QgsRenderContext.TextFormatAlwaysOutlines.is_monkey_patched = True
QgsRenderContext.TextFormatAlwaysOutlines.__doc__ = "Always render text using path objects (AKA outlines/curves). This setting guarantees the best quality rendering, even when using a raster paint surface (where sub-pixel path based text rendering is superior to sub-pixel text-based rendering). The downside is that text is converted to paths only, so users cannot open created vector outputs for post-processing in other applications and retain text editability.  This setting also guarantees complete compatibility with the full range of formatting options available through QgsTextRenderer and QgsTextFormat, some of which may not be possible to reproduce when using a vector-based paint surface and TextFormatAlwaysText mode. A final benefit to this setting is that vector exports created using text as outlines do not require all users to have the original fonts installed in order to display the text in its original style."
QgsRenderContext.TextFormatAlwaysText = Qgis.TextRenderFormat.AlwaysText
QgsRenderContext.TextFormatAlwaysText.is_monkey_patched = True
QgsRenderContext.TextFormatAlwaysText.__doc__ = "Always render text as text objects. While this mode preserves text objects as text for post-processing in external vector editing applications, it can result in rendering artifacts or poor quality rendering, depending on the text format settings. Even with raster based paint devices, TextFormatAlwaysText can result in inferior rendering quality to TextFormatAlwaysOutlines. When rendering using TextFormatAlwaysText to a vector based device (e.g. PDF or SVG), care must be taken to ensure that the required fonts are available to users when opening the created files, or default fallback fonts will be used to display the output instead. (Although PDF exports MAY automatically embed some fonts when possible, depending on the user's platform)."
Qgis.TextRenderFormat.__doc__ = 'Options for rendering text.\n\n.. versionadded:: 3.22\n\n' + '* ``TextFormatAlwaysOutlines``: ' + Qgis.TextRenderFormat.AlwaysOutlines.__doc__ + '\n' + '* ``TextFormatAlwaysText``: ' + Qgis.TextRenderFormat.AlwaysText.__doc__
# --
Qgis.TextRenderFormat.baseClass = Qgis
# monkey patching scoped based enum
Qgis.RenderSubcomponentProperty.Generic.__doc__ = "Generic subcomponent property"
Qgis.RenderSubcomponentProperty.ShadowOffset.__doc__ = "Shadow offset"
Qgis.RenderSubcomponentProperty.BlurSize.__doc__ = "Blur size"
Qgis.RenderSubcomponentProperty.GlowSpread.__doc__ = "Glow spread size"
Qgis.RenderSubcomponentProperty.__doc__ = 'Rendering subcomponent properties.\n\n.. versionadded:: 3.22\n\n' + '* ``Generic``: ' + Qgis.RenderSubcomponentProperty.Generic.__doc__ + '\n' + '* ``ShadowOffset``: ' + Qgis.RenderSubcomponentProperty.ShadowOffset.__doc__ + '\n' + '* ``BlurSize``: ' + Qgis.RenderSubcomponentProperty.BlurSize.__doc__ + '\n' + '* ``GlowSpread``: ' + Qgis.RenderSubcomponentProperty.GlowSpread.__doc__
# --
Qgis.RenderSubcomponentProperty.baseClass = Qgis
QgsVertexId.VertexType = Qgis.VertexType
# monkey patching scoped based enum
QgsVertexId.SegmentVertex = Qgis.VertexType.Segment
QgsVertexId.SegmentVertex.is_monkey_patched = True
QgsVertexId.SegmentVertex.__doc__ = "The actual start or end point of a segment"
QgsVertexId.CurveVertex = Qgis.VertexType.Curve
QgsVertexId.CurveVertex.is_monkey_patched = True
QgsVertexId.CurveVertex.__doc__ = "An intermediate point on a segment defining the curvature of the segment"
Qgis.VertexType.__doc__ = 'Types of vertex.\n\n.. versionadded:: 3.22\n\n' + '* ``SegmentVertex``: ' + Qgis.VertexType.Segment.__doc__ + '\n' + '* ``CurveVertex``: ' + Qgis.VertexType.Curve.__doc__
# --
Qgis.VertexType.baseClass = Qgis
# The following has been generated automatically from src/core/providers/qgsabstractdatabaseproviderconnection.h
QgsAbstractDatabaseProviderConnection.TableFlag.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.TableFlags.baseClass = QgsAbstractDatabaseProviderConnection
TableFlags = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
QgsAbstractDatabaseProviderConnection.Capability.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.Capabilities.baseClass = QgsAbstractDatabaseProviderConnection
Capabilities = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
QgsAbstractDatabaseProviderConnection.GeometryColumnCapability.baseClass = QgsAbstractDatabaseProviderConnection
QgsAbstractDatabaseProviderConnection.GeometryColumnCapabilities.baseClass = QgsAbstractDatabaseProviderConnection
GeometryColumnCapabilities = QgsAbstractDatabaseProviderConnection  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geometry/qgsabstractgeometry.h
QgsAbstractGeometry.SegmentationToleranceType.baseClass = QgsAbstractGeometry
# The following has been generated automatically from src/core/annotations/qgsannotationitemeditoperation.h
# monkey patching scoped based enum
QgsAbstractAnnotationItemEditOperation.Type.MoveNode.__doc__ = "Move a node"
QgsAbstractAnnotationItemEditOperation.Type.DeleteNode.__doc__ = "Delete a node"
QgsAbstractAnnotationItemEditOperation.Type.AddNode.__doc__ = "Add a node"
QgsAbstractAnnotationItemEditOperation.Type.TranslateItem.__doc__ = "Translate (move) an item"
QgsAbstractAnnotationItemEditOperation.Type.__doc__ = 'Operation type\n\n' + '* ``MoveNode``: ' + QgsAbstractAnnotationItemEditOperation.Type.MoveNode.__doc__ + '\n' + '* ``DeleteNode``: ' + QgsAbstractAnnotationItemEditOperation.Type.DeleteNode.__doc__ + '\n' + '* ``AddNode``: ' + QgsAbstractAnnotationItemEditOperation.Type.AddNode.__doc__ + '\n' + '* ``TranslateItem``: ' + QgsAbstractAnnotationItemEditOperation.Type.TranslateItem.__doc__
# --
# The following has been generated automatically from src/core/editform/qgsattributeeditorrelation.h
QgsAttributeEditorRelation.Button.baseClass = QgsAttributeEditorRelation
QgsAttributeEditorRelation.Buttons.baseClass = QgsAttributeEditorRelation
Buttons = QgsAttributeEditorRelation  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/auth/qgsauthmanager.h
QgsAuthManager.MessageLevel.baseClass = QgsAuthManager
# The following has been generated automatically from src/core/qgsdatasourceuri.h
QgsDataSourceUri.SslMode.baseClass = QgsDataSourceUri
# The following has been generated automatically from src/core/qgsdefaultvalue.h
QgsDefaultValue.__bool__ = lambda self: self.isValid()
# The following has been generated automatically from src/core/dxf/qgsdxfexport.h
# monkey patching scoped based enum
QgsDxfExport.ExportResult.Success.__doc__ = "Successful export"
QgsDxfExport.ExportResult.InvalidDeviceError.__doc__ = "Invalid device error"
QgsDxfExport.ExportResult.DeviceNotWritableError.__doc__ = "Device not writable error"
QgsDxfExport.ExportResult.EmptyExtentError.__doc__ = "Empty extent, no extent given and no extent could be derived from layers"
QgsDxfExport.ExportResult.__doc__ = 'The result of an export as dxf operation\n\n.. versionadded:: 3.10.1\n\n' + '* ``Success``: ' + QgsDxfExport.ExportResult.Success.__doc__ + '\n' + '* ``InvalidDeviceError``: ' + QgsDxfExport.ExportResult.InvalidDeviceError.__doc__ + '\n' + '* ``DeviceNotWritableError``: ' + QgsDxfExport.ExportResult.DeviceNotWritableError.__doc__ + '\n' + '* ``EmptyExtentError``: ' + QgsDxfExport.ExportResult.EmptyExtentError.__doc__
# --
# monkey patching scoped based enum
QgsDxfExport.VAlign.VBaseLine.__doc__ = "Top (0)"
QgsDxfExport.VAlign.VBottom.__doc__ = "Bottom (1)"
QgsDxfExport.VAlign.VMiddle.__doc__ = "Middle (2)"
QgsDxfExport.VAlign.VTop.__doc__ = "Top (3)"
QgsDxfExport.VAlign.Undefined.__doc__ = "Undefined"
QgsDxfExport.VAlign.__doc__ = 'Vertical alignments.\n\n' + '* ``VBaseLine``: ' + QgsDxfExport.VAlign.VBaseLine.__doc__ + '\n' + '* ``VBottom``: ' + QgsDxfExport.VAlign.VBottom.__doc__ + '\n' + '* ``VMiddle``: ' + QgsDxfExport.VAlign.VMiddle.__doc__ + '\n' + '* ``VTop``: ' + QgsDxfExport.VAlign.VTop.__doc__ + '\n' + '* ``Undefined``: ' + QgsDxfExport.VAlign.Undefined.__doc__
# --
# monkey patching scoped based enum
QgsDxfExport.HAlign.HLeft.__doc__ = "Left (0)"
QgsDxfExport.HAlign.HCenter.__doc__ = "Centered (1)"
QgsDxfExport.HAlign.HRight.__doc__ = "Right (2)"
QgsDxfExport.HAlign.HAligned.__doc__ = "Aligned = (3) (if VAlign==0)"
QgsDxfExport.HAlign.HMiddle.__doc__ = "Middle = (4) (if VAlign==0)"
QgsDxfExport.HAlign.HFit.__doc__ = "Fit into point = (5) (if VAlign==0)"
QgsDxfExport.HAlign.Undefined.__doc__ = "Undefined"
QgsDxfExport.HAlign.__doc__ = 'Horizontal alignments.\n\n' + '* ``HLeft``: ' + QgsDxfExport.HAlign.HLeft.__doc__ + '\n' + '* ``HCenter``: ' + QgsDxfExport.HAlign.HCenter.__doc__ + '\n' + '* ``HRight``: ' + QgsDxfExport.HAlign.HRight.__doc__ + '\n' + '* ``HAligned``: ' + QgsDxfExport.HAlign.HAligned.__doc__ + '\n' + '* ``HMiddle``: ' + QgsDxfExport.HAlign.HMiddle.__doc__ + '\n' + '* ``HFit``: ' + QgsDxfExport.HAlign.HFit.__doc__ + '\n' + '* ``Undefined``: ' + QgsDxfExport.HAlign.Undefined.__doc__
# --
# The following has been generated automatically from src/core/editform/qgseditformconfig.h
QgsEditFormConfig.EditorLayout.baseClass = QgsEditFormConfig
QgsEditFormConfig.FeatureFormSuppress.baseClass = QgsEditFormConfig
QgsEditFormConfig.PythonInitCodeSource.baseClass = QgsEditFormConfig
# The following has been generated automatically from src/core/qgsfeatureiterator.h
# monkey patching scoped based enum
QgsAbstractFeatureIterator.RequestToSourceCrsResult.Success.__doc__ = "Request was successfully updated to the source CRS, or no changes were required"
QgsAbstractFeatureIterator.RequestToSourceCrsResult.DistanceWithinMustBeCheckedManually.__doc__ = "The distance within request cannot be losslessly updated to the source CRS, and callers will need to take appropriate steps to handle the distance within requirement manually during feature iteration"
QgsAbstractFeatureIterator.RequestToSourceCrsResult.__doc__ = 'Possible results from the :py:func:`~QgsAbstractFeatureIterator.updateRequestToSourceCrs` method.\n\n.. versionadded:: 3.22\n\n' + '* ``Success``: ' + QgsAbstractFeatureIterator.RequestToSourceCrsResult.Success.__doc__ + '\n' + '* ``DistanceWithinMustBeCheckedManually``: ' + QgsAbstractFeatureIterator.RequestToSourceCrsResult.DistanceWithinMustBeCheckedManually.__doc__
# --
# The following has been generated automatically from src/core/qgsfieldproxymodel.h
QgsFieldProxyModel.Filters.baseClass = QgsFieldProxyModel
Filters = QgsFieldProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/geocoding/qgsgeocoder.h
# monkey patching scoped based enum
QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ = "Can geocode string input values"
QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__ = "Can geocode QgsFeature input values"
QgsGeocoderInterface.Flag.__doc__ = 'Capability flags for the geocoder.\n\n' + '* ``GeocodesStrings``: ' + QgsGeocoderInterface.Flag.GeocodesStrings.__doc__ + '\n' + '* ``GeocodesFeatures``: ' + QgsGeocoderInterface.Flag.GeocodesFeatures.__doc__
# --
# The following has been generated automatically from src/core/geocms/geonode/qgsgeonoderequest.h
# monkey patching scoped based enum
QgsGeoNodeRequest.BackendServer.Unknown.__doc__ = "Unknown backend"
QgsGeoNodeRequest.BackendServer.QgisServer.__doc__ = "QGIS server used as backend"
QgsGeoNodeRequest.BackendServer.Geoserver.__doc__ = "Geoserver used as backend"
QgsGeoNodeRequest.BackendServer.__doc__ = 'GeoNode backend server type.\n\n' + '* ``Unknown``: ' + QgsGeoNodeRequest.BackendServer.Unknown.__doc__ + '\n' + '* ``QgisServer``: ' + QgsGeoNodeRequest.BackendServer.QgisServer.__doc__ + '\n' + '* ``Geoserver``: ' + QgsGeoNodeRequest.BackendServer.Geoserver.__doc__
# --
# The following has been generated automatically from src/core/labeling/qgslabellinesettings.h
# monkey patching scoped based enum
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolLeftRight.__doc__ = "Place direction symbols on left/right of label"
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolAbove.__doc__ = "Place direction symbols on above label"
QgsLabelLineSettings.DirectionSymbolPlacement.SymbolBelow.__doc__ = "Place direction symbols on below label"
QgsLabelLineSettings.DirectionSymbolPlacement.__doc__ = 'Placement options for direction symbols.\n\n' + '* ``SymbolLeftRight``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolLeftRight.__doc__ + '\n' + '* ``SymbolAbove``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolAbove.__doc__ + '\n' + '* ``SymbolBelow``: ' + QgsLabelLineSettings.DirectionSymbolPlacement.SymbolBelow.__doc__
# --
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorType.HintOnly.__doc__ = "Line anchor is a hint for preferred placement only, but other placements close to the hint are permitted"
QgsLabelLineSettings.AnchorType.Strict.__doc__ = "Line anchor is a strict placement, and other placements are not permitted"
QgsLabelLineSettings.AnchorType.__doc__ = 'Line anchor types\n\n' + '* ``HintOnly``: ' + QgsLabelLineSettings.AnchorType.HintOnly.__doc__ + '\n' + '* ``Strict``: ' + QgsLabelLineSettings.AnchorType.Strict.__doc__
# --
# monkey patching scoped based enum
QgsLabelLineSettings.AnchorClipping.UseVisiblePartsOfLine.__doc__ = "Only visible parts of lines are considered when calculating the line anchor for labels"
QgsLabelLineSettings.AnchorClipping.UseEntireLine.__doc__ = "Entire original feature line geometry is used when calculating the line anchor for labels"
QgsLabelLineSettings.AnchorClipping.__doc__ = 'Clipping behavior for line anchor calculation.\n\n.. versionadded:: 3.20\n\n' + '* ``UseVisiblePartsOfLine``: ' + QgsLabelLineSettings.AnchorClipping.UseVisiblePartsOfLine.__doc__ + '\n' + '* ``UseEntireLine``: ' + QgsLabelLineSettings.AnchorClipping.UseEntireLine.__doc__
# --
# The following has been generated automatically from src/core/layout/qgslayoutmanager.h
QgsLayoutManagerProxyModel.Filters.baseClass = QgsLayoutManagerProxyModel
Filters = QgsLayoutManagerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/locator/qgslocatorfilter.h
QgsLocatorFilter.Priority.baseClass = QgsLocatorFilter
QgsLocatorFilter.Flags.baseClass = QgsLocatorFilter
Flags = QgsLocatorFilter  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmapclippingregion.h
# monkey patching scoped based enum
QgsMapClippingRegion.FeatureClippingType.ClipToIntersection.__doc__ = "Clip the geometry of these features to the region prior to rendering (i.e. feature boundaries will follow the clip region)"
QgsMapClippingRegion.FeatureClippingType.ClipPainterOnly.__doc__ = "Applying clipping on the painter only (i.e. feature boundaries will be unchanged, but may be invisible where the feature falls outside the clipping region)"
QgsMapClippingRegion.FeatureClippingType.NoClipping.__doc__ = "Only render features which intersect the clipping region, but do not clip these features to the region"
QgsMapClippingRegion.FeatureClippingType.__doc__ = 'Feature clipping behavior, which controls how features from vector layers\nwill be clipped.\n\n' + '* ``ClipToIntersection``: ' + QgsMapClippingRegion.FeatureClippingType.ClipToIntersection.__doc__ + '\n' + '* ``ClipPainterOnly``: ' + QgsMapClippingRegion.FeatureClippingType.ClipPainterOnly.__doc__ + '\n' + '* ``NoClipping``: ' + QgsMapClippingRegion.FeatureClippingType.NoClipping.__doc__
# --
# The following has been generated automatically from src/core/qgsmaplayer.h
QgsMapLayer.LayerFlag.baseClass = QgsMapLayer
QgsMapLayer.LayerFlags.baseClass = QgsMapLayer
LayerFlags = QgsMapLayer  # dirty hack since SIP seems to introduce the flags in module
QgsMapLayer.StyleCategory.baseClass = QgsMapLayer
QgsMapLayer.StyleCategories.baseClass = QgsMapLayer
StyleCategories = QgsMapLayer  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmaplayermodel.h
QgsMapLayerModel.ItemDataRole.baseClass = QgsMapLayerModel
# The following has been generated automatically from src/core/qgsmaplayerproxymodel.h
QgsMapLayerProxyModel.Filters.baseClass = QgsMapLayerProxyModel
Filters = QgsMapLayerProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/qgsmaplayerserverproperties.h
QgsServerWmsDimensionProperties.PredefinedWmsDimensionName.baseClass = QgsServerWmsDimensionProperties
# The following has been generated automatically from src/core/qgsmapsettingsutils.h
# monkey patching scoped based enum
QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__ = "Ignore advanced effects which are supported in GeoPDF exports"
QgsMapSettingsUtils.EffectsCheckFlag.__doc__ = 'Flags for controlling the behavior of :py:func:`~QgsMapSettingsUtils.containsAdvancedEffects`\n\n.. versionadded:: 3.14\n\n' + '* ``IgnoreGeoPdfSupportedEffects``: ' + QgsMapSettingsUtils.EffectsCheckFlag.IgnoreGeoPdfSupportedEffects.__doc__
# --
# The following has been generated automatically from src/core/pointcloud/qgspointcloudattributemodel.h
QgsPointCloudAttributeProxyModel.Filters.baseClass = QgsPointCloudAttributeProxyModel
Filters = QgsPointCloudAttributeProxyModel  # dirty hack since SIP seems to introduce the flags in module
# The following has been generated automatically from src/core/processing/qgsprocessingutils.h
# monkey patching scoped based enum
QgsProcessingUtils.UnknownType = QgsProcessingUtils.LayerHint.UnknownType
QgsProcessingUtils.UnknownType.is_monkey_patched = True
QgsProcessingUtils.LayerHint.UnknownType.__doc__ = "Unknown layer type"
QgsProcessingUtils.Vector = QgsProcessingUtils.LayerHint.Vector
QgsProcessingUtils.Vector.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Vector.__doc__ = "Vector layer type"
QgsProcessingUtils.Raster = QgsProcessingUtils.LayerHint.Raster
QgsProcessingUtils.Raster.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Raster.__doc__ = "Raster layer type"
QgsProcessingUtils.Mesh = QgsProcessingUtils.LayerHint.Mesh
QgsProcessingUtils.Mesh.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Mesh.__doc__ = "Mesh layer type, since QGIS 3.6"
QgsProcessingUtils.PointCloud = QgsProcessingUtils.LayerHint.PointCloud
QgsProcessingUtils.PointCloud.is_monkey_patched = True
QgsProcessingUtils.LayerHint.PointCloud.__doc__ = "Point cloud layer type, since QGIS 3.22"
QgsProcessingUtils.Annotation = QgsProcessingUtils.LayerHint.Annotation
QgsProcessingUtils.Annotation.is_monkey_patched = True
QgsProcessingUtils.LayerHint.Annotation.__doc__ = "Annotation layer type, since QGIS 3.22"
QgsProcessingUtils.LayerHint.__doc__ = 'Layer type hints.\n\n.. versionadded:: 3.4\n\n' + '* ``UnknownType``: ' + QgsProcessingUtils.LayerHint.UnknownType.__doc__ + '\n' + '* ``Vector``: ' + QgsProcessingUtils.LayerHint.Vector.__doc__ + '\n' + '* ``Raster``: ' + QgsProcessingUtils.LayerHint.Raster.__doc__ + '\n' + '* ``Mesh``: ' + QgsProcessingUtils.LayerHint.Mesh.__doc__ + '\n' + '* ``PointCloud``: ' + QgsProcessingUtils.LayerHint.PointCloud.__doc__ + '\n' + '* ``Annotation``: ' + QgsProcessingUtils.LayerHint.Annotation.__doc__
# --
# The following has been generated automatically from src/core/project/qgsproject.h
# monkey patching scoped based enum
QgsProject.FlagDontResolveLayers = QgsProject.ReadFlag.FlagDontResolveLayers
QgsProject.FlagDontResolveLayers.is_monkey_patched = True
QgsProject.ReadFlag.FlagDontResolveLayers.__doc__ = "Don't resolve layer paths (i.e. don't load any layer content). Dramatically improves project read time if the actual data from the layers is not required."
QgsProject.FlagDontLoadLayouts = QgsProject.ReadFlag.FlagDontLoadLayouts
QgsProject.FlagDontLoadLayouts.is_monkey_patched = True
QgsProject.ReadFlag.FlagDontLoadLayouts.__doc__ = "Don't load print layouts. Improves project read time if layouts are not required, and allows projects to be safely read in background threads (since print layouts are not thread safe)."
QgsProject.FlagTrustLayerMetadata = QgsProject.ReadFlag.FlagTrustLayerMetadata
QgsProject.FlagTrustLayerMetadata.is_monkey_patched = True
QgsProject.ReadFlag.FlagTrustLayerMetadata.__doc__ = "Trust layer metadata. Improves project read time. Do not use it if layers' extent is not fixed during the project's use by QGIS and QGIS Server."
QgsProject.FlagDontStoreOriginalStyles = QgsProject.ReadFlag.FlagDontStoreOriginalStyles
QgsProject.FlagDontStoreOriginalStyles.is_monkey_patched = True
QgsProject.ReadFlag.FlagDontStoreOriginalStyles.__doc__ = "Skip the initial XML style storage for layers. Useful for minimising project load times in non-interactive contexts."
QgsProject.ReadFlag.__doc__ = 'Flags which control project read behavior.\n\n.. versionadded:: 3.10\n\n' + '* ``FlagDontResolveLayers``: ' + QgsProject.ReadFlag.FlagDontResolveLayers.__doc__ + '\n' + '* ``FlagDontLoadLayouts``: ' + QgsProject.ReadFlag.FlagDontLoadLayouts.__doc__ + '\n' + '* ``FlagTrustLayerMetadata``: ' + QgsProject.ReadFlag.FlagTrustLayerMetadata.__doc__ + '\n' + '* ``FlagDontStoreOriginalStyles``: ' + QgsProject.ReadFlag.FlagDontStoreOriginalStyles.__doc__
# --
# monkey patching scoped based enum
QgsProject.FileFormat.Qgz.__doc__ = "Archive file format, supports auxiliary data"
QgsProject.FileFormat.Qgs.__doc__ = "Project saved in a clear text, does not support auxiliary data"
QgsProject.FileFormat.__doc__ = 'Flags which control project read behavior.\n\n.. versionadded:: 3.12\n\n' + '* ``Qgz``: ' + QgsProject.FileFormat.Qgz.__doc__ + '\n' + '* ``Qgs``: ' + QgsProject.FileFormat.Qgs.__doc__
# --
QgsProject.FileFormat.baseClass = QgsProject
# monkey patching scoped based enum
QgsProject.AvoidIntersectionsMode.AllowIntersections.__doc__ = "Overlap with any feature allowed when digitizing new features"
QgsProject.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ = "Overlap with features from the active layer when digitizing new features not allowed"
QgsProject.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__ = "Overlap with features from a specified list of layers when digitizing new features not allowed"
QgsProject.AvoidIntersectionsMode.__doc__ = 'Flags which control how intersections of pre-existing feature are handled when digitizing new features.\n\n.. versionadded:: 3.14\n\n' + '* ``AllowIntersections``: ' + QgsProject.AvoidIntersectionsMode.AllowIntersections.__doc__ + '\n' + '* ``AvoidIntersectionsCurrentLayer``: ' + QgsProject.AvoidIntersectionsMode.AvoidIntersectionsCurrentLayer.__doc__ + '\n' + '* ``AvoidIntersectionsLayers``: ' + QgsProject.AvoidIntersectionsMode.AvoidIntersectionsLayers.__doc__
# --
QgsProject.AvoidIntersectionsMode.baseClass = QgsProject
# The following has been generated automatically from src/core/qgsproviderconnectionmodel.h
QgsProviderConnectionModel.Role.baseClass = QgsProviderConnectionModel
# The following has been generated automatically from src/core/providers/qgsprovidermetadata.h
QgsMeshDriverMetadata.MeshDriverCapability.baseClass = QgsMeshDriverMetadata
QgsMeshDriverMetadata.MeshDriverCapabilities.baseClass = QgsMeshDriverMetadata
MeshDriverCapabilities = QgsMeshDriverMetadata  # dirty hack since SIP seems to introduce the flags in module
# monkey patching scoped based enum
QgsProviderMetadata.FilterType.FilterVector.__doc__ = "Vector layers"
QgsProviderMetadata.FilterType.FilterRaster.__doc__ = "Raster layers"
QgsProviderMetadata.FilterType.FilterMesh.__doc__ = "Mesh layers"
QgsProviderMetadata.FilterType.FilterMeshDataset.__doc__ = "Mesh datasets"
QgsProviderMetadata.FilterType.FilterPointCloud.__doc__ = "Point clouds (since QGIS 3.18)"
QgsProviderMetadata.FilterType.__doc__ = 'Type of file filters\n\n.. versionadded:: 3.10\n\n' + '* ``FilterVector``: ' + QgsProviderMetadata.FilterType.FilterVector.__doc__ + '\n' + '* ``FilterRaster``: ' + QgsProviderMetadata.FilterType.FilterRaster.__doc__ + '\n' + '* ``FilterMesh``: ' + QgsProviderMetadata.FilterType.FilterMesh.__doc__ + '\n' + '* ``FilterMeshDataset``: ' + QgsProviderMetadata.FilterType.FilterMeshDataset.__doc__ + '\n' + '* ``FilterPointCloud``: ' + QgsProviderMetadata.FilterType.FilterPointCloud.__doc__
# --
# The following has been generated automatically from src/core/providers/qgsprovidersublayermodel.h
# monkey patching scoped based enum
QgsProviderSublayerModel.Role.ProviderKey.__doc__ = "Provider key"
QgsProviderSublayerModel.Role.LayerType.__doc__ = "Layer type"
QgsProviderSublayerModel.Role.Uri.__doc__ = "Layer URI"
QgsProviderSublayerModel.Role.Name.__doc__ = "Layer name"
QgsProviderSublayerModel.Role.Description.__doc__ = "Layer description"
QgsProviderSublayerModel.Role.Path.__doc__ = "Layer path"
QgsProviderSublayerModel.Role.FeatureCount.__doc__ = "Feature count (for vector sublayers)"
QgsProviderSublayerModel.Role.WkbType.__doc__ = "WKB geometry type (for vector sublayers)"
QgsProviderSublayerModel.Role.GeometryColumnName.__doc__ = "Geometry column name (for vector sublayers)"
QgsProviderSublayerModel.Role.LayerNumber.__doc__ = "Layer number"
QgsProviderSublayerModel.Role.IsNonLayerItem.__doc__ = "``True`` if item is a non-sublayer item (e.g. an embedded project)"
QgsProviderSublayerModel.Role.NonLayerItemType.__doc__ = "Item type (for non-sublayer items)"
QgsProviderSublayerModel.Role.Flags.__doc__ = "Sublayer flags"
QgsProviderSublayerModel.Role.__doc__ = 'Custom model roles\n\n' + '* ``ProviderKey``: ' + QgsProviderSublayerModel.Role.ProviderKey.__doc__ + '\n' + '* ``LayerType``: ' + QgsProviderSublayerModel.Role.LayerType.__doc__ + '\n' + '* ``Uri``: ' + QgsProviderSublayerModel.Role.Uri.__doc__ + '\n' + '* ``Name``: ' + QgsProviderSublayerModel.Role.Name.__doc__ + '\n' + '* ``Description``: ' + QgsProviderSublayerModel.Role.Description.__doc__ + '\n' + '* ``Path``: ' + QgsProviderSublayerModel.Role.Path.__doc__ + '\n' + '* ``FeatureCount``: ' + QgsProviderSublayerModel.Role.FeatureCount.__doc__ + '\n' + '* ``WkbType``: ' + QgsProviderSublayerModel.Role.WkbType.__doc__ + '\n' + '* ``GeometryColumnName``: ' + QgsProviderSublayerModel.Role.GeometryColumnName.__doc__ + '\n' + '* ``LayerNumber``: ' + QgsProviderSublayerModel.Role.LayerNumber.__doc__ + '\n' + '* ``IsNonLayerItem``: ' + QgsProviderSublayerModel.Role.IsNonLayerItem.__doc__ + '\n' + '* ``NonLayerItemType``: ' + QgsProviderSublayerModel.Role.NonLayerItemType.__doc__ + '\n' + '* ``Flags``: ' + QgsProviderSublayerModel.Role.Flags.__doc__
# --
# monkey patching scoped based enum
QgsProviderSublayerModel.Column.Name.__doc__ = "Layer name"
QgsProviderSublayerModel.Column.Description.__doc__ = "Layer description"
QgsProviderSublayerModel.Column.__doc__ = 'Model columns\n\n' + '* ``Name``: ' + QgsProviderSublayerModel.Column.Name.__doc__ + '\n' + '* ``Description``: ' + QgsProviderSublayerModel.Column.Description.__doc__
# --
# The following has been generated automatically from src/core/providers/qgsproviderutils.h
# monkey patching scoped based enum
QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownFeatureCount.__doc__ = "Indicates that an unknown feature count should not be considered as incomplete"
QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownGeometryType.__doc__ = "Indicates that an unknown geometry type should not be considered as incomplete"
QgsProviderUtils.SublayerCompletenessFlag.__doc__ = 'Flags which control how :py:func:`QgsProviderUtils.sublayerDetailsAreIncomplete()` tests for completeness.\n\n' + '* ``IgnoreUnknownFeatureCount``: ' + QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownFeatureCount.__doc__ + '\n' + '* ``IgnoreUnknownGeometryType``: ' + QgsProviderUtils.SublayerCompletenessFlag.IgnoreUnknownGeometryType.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterdataprovider.h
# monkey patching scoped based enum
QgsRasterDataProvider.ResamplingMethod.Nearest.__doc__ = "Nearest-neighbour resampling"
QgsRasterDataProvider.ResamplingMethod.Bilinear.__doc__ = "Bilinear (2x2 kernel) resampling"
QgsRasterDataProvider.ResamplingMethod.Cubic.__doc__ = "Cubic Convolution Approximation (4x4 kernel) resampling"
QgsRasterDataProvider.ResamplingMethod.CubicSpline.__doc__ = "Cubic B-Spline Approximation (4x4 kernel)"
QgsRasterDataProvider.ResamplingMethod.Lanczos.__doc__ = "Lanczos windowed sinc interpolation (6x6 kernel)"
QgsRasterDataProvider.ResamplingMethod.Average.__doc__ = "Average resampling"
QgsRasterDataProvider.ResamplingMethod.Mode.__doc__ = "Mode (selects the value which appears most often of all the sampled points)"
QgsRasterDataProvider.ResamplingMethod.Gauss.__doc__ = "Gauss blurring"
QgsRasterDataProvider.ResamplingMethod.__doc__ = 'Resampling method for provider-level resampling.\n\n.. versionadded:: 3.16\n\n' + '* ``Nearest``: ' + QgsRasterDataProvider.ResamplingMethod.Nearest.__doc__ + '\n' + '* ``Bilinear``: ' + QgsRasterDataProvider.ResamplingMethod.Bilinear.__doc__ + '\n' + '* ``Cubic``: ' + QgsRasterDataProvider.ResamplingMethod.Cubic.__doc__ + '\n' + '* ``CubicSpline``: ' + QgsRasterDataProvider.ResamplingMethod.CubicSpline.__doc__ + '\n' + '* ``Lanczos``: ' + QgsRasterDataProvider.ResamplingMethod.Lanczos.__doc__ + '\n' + '* ``Average``: ' + QgsRasterDataProvider.ResamplingMethod.Average.__doc__ + '\n' + '* ``Mode``: ' + QgsRasterDataProvider.ResamplingMethod.Mode.__doc__ + '\n' + '* ``Gauss``: ' + QgsRasterDataProvider.ResamplingMethod.Gauss.__doc__
# --
# The following has been generated automatically from src/core/raster/qgsrasterprojector.h
QgsRasterProjector.Precision.baseClass = QgsRasterProjector
# The following has been generated automatically from src/core/qgsrelation.h
QgsRelation.RelationType.baseClass = QgsRelation
QgsRelation.RelationStrength.baseClass = QgsRelation
# The following has been generated automatically from src/core/scalebar/qgsscalebarrenderer.h
# monkey patching scoped based enum
QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ = "Renderer utilizes the scalebar line symbol (see QgsScaleBarSettings::lineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ = "Renderer utilizes the scalebar fill symbol (see QgsScaleBarSettings::fillSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ = "Renderer utilizes the alternate scalebar fill symbol (see QgsScaleBarSettings::alternateFillSymbol() )"
QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ = "Renderer respects the QgsScaleBarSettings::units() setting"
QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ = "Renderer respects the QgsScaleBarSettings::mapUnitsPerScaleBarUnit() setting"
QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ = "Renderer uses the QgsScaleBarSettings::unitLabel() setting"
QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ = "Renderer uses the scalebar segments"
QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ = "Renderer uses the QgsScaleBarSettings::labelBarSpace() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings::labelVerticalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ = "Renderer uses the QgsScaleBarSettings::labelHorizontalPlacement() setting"
QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ = "Renderer uses the QgsScaleBarSettings::alignment() setting"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ = "Renderer uses the scalebar subdivisions (see QgsScaleBarSettings::numberOfSubdivisions() )"
QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ = "Renderer utilizes the scalebar division symbol (see QgsScaleBarSettings::divisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ = "Renderer utilizes the scalebar subdivision symbol (see QgsScaleBarSettings::subdivisionLineSymbol() )"
QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__ = "Renderer uses the scalebar subdivisions height (see QgsScaleBarSettings::subdivisionsHeight() )"
QgsScaleBarRenderer.Flag.__doc__ = 'Flags which control scalebar renderer behavior.\n\n.. versionadded:: 3.14\n\n' + '* ``FlagUsesLineSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesLineSymbol.__doc__ + '\n' + '* ``FlagUsesFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesFillSymbol.__doc__ + '\n' + '* ``FlagUsesAlternateFillSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlternateFillSymbol.__doc__ + '\n' + '* ``FlagRespectsUnits``: ' + QgsScaleBarRenderer.Flag.FlagRespectsUnits.__doc__ + '\n' + '* ``FlagRespectsMapUnitsPerScaleBarUnit``: ' + QgsScaleBarRenderer.Flag.FlagRespectsMapUnitsPerScaleBarUnit.__doc__ + '\n' + '* ``FlagUsesUnitLabel``: ' + QgsScaleBarRenderer.Flag.FlagUsesUnitLabel.__doc__ + '\n' + '* ``FlagUsesSegments``: ' + QgsScaleBarRenderer.Flag.FlagUsesSegments.__doc__ + '\n' + '* ``FlagUsesLabelBarSpace``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelBarSpace.__doc__ + '\n' + '* ``FlagUsesLabelVerticalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelVerticalPlacement.__doc__ + '\n' + '* ``FlagUsesLabelHorizontalPlacement``: ' + QgsScaleBarRenderer.Flag.FlagUsesLabelHorizontalPlacement.__doc__ + '\n' + '* ``FlagUsesAlignment``: ' + QgsScaleBarRenderer.Flag.FlagUsesAlignment.__doc__ + '\n' + '* ``FlagUsesSubdivisions``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisions.__doc__ + '\n' + '* ``FlagUsesDivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesDivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionSymbol``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionSymbol.__doc__ + '\n' + '* ``FlagUsesSubdivisionsHeight``: ' + QgsScaleBarRenderer.Flag.FlagUsesSubdivisionsHeight.__doc__
# --
# The following has been generated automatically from src/core/settings/qgssettingsentry.h
# monkey patching scoped based enum
QgsSettingsEntryBase.SettingsType.Variant.__doc__ = "Generic variant"
QgsSettingsEntryBase.SettingsType.String.__doc__ = "String"
QgsSettingsEntryBase.SettingsType.StringList.__doc__ = "List of strings"
QgsSettingsEntryBase.SettingsType.Bool.__doc__ = "Boolean"
QgsSettingsEntryBase.SettingsType.Integer.__doc__ = "Integer"
QgsSettingsEntryBase.SettingsType.Double.__doc__ = "Double precision numer"
QgsSettingsEntryBase.SettingsType.EnumFlag.__doc__ = "Enum or Flag"
QgsSettingsEntryBase.SettingsType.Color.__doc__ = "Color"
QgsSettingsEntryBase.SettingsType.__doc__ = 'Types of settings entries\n\n' + '* ``Variant``: ' + QgsSettingsEntryBase.SettingsType.Variant.__doc__ + '\n' + '* ``String``: ' + QgsSettingsEntryBase.SettingsType.String.__doc__ + '\n' + '* ``StringList``: ' + QgsSettingsEntryBase.SettingsType.StringList.__doc__ + '\n' + '* ``Bool``: ' + QgsSettingsEntryBase.SettingsType.Bool.__doc__ + '\n' + '* ``Integer``: ' + QgsSettingsEntryBase.SettingsType.Integer.__doc__ + '\n' + '* ``Double``: ' + QgsSettingsEntryBase.SettingsType.Double.__doc__ + '\n' + '* ``EnumFlag``: ' + QgsSettingsEntryBase.SettingsType.EnumFlag.__doc__ + '\n' + '* ``Color``: ' + QgsSettingsEntryBase.SettingsType.Color.__doc__
# --
# The following has been generated automatically from src/core/qgssnappingconfig.h
QgsSnappingConfig.SnappingMode.baseClass = QgsSnappingConfig
QgsSnappingConfig.SnappingTypes.baseClass = QgsSnappingConfig
QgsSnappingConfig.SnappingTypeFlag.baseClass = QgsSnappingConfig
SnappingTypeFlag = QgsSnappingConfig  # dirty hack since SIP seems to introduce the flags in module
QgsSnappingConfig.ScaleDependencyMode.baseClass = QgsSnappingConfig
# The following has been generated automatically from src/core/symbology/qgsstyle.h
# monkey patching scoped based enum
QgsStyle.TextFormatContext.Labeling.__doc__ = "Text format used in labeling"
QgsStyle.TextFormatContext.__doc__ = 'Text format context.\n\n.. versionadded:: 3.20\n\n' + '* ``Labeling``: ' + QgsStyle.TextFormatContext.Labeling.__doc__
# --
# The following has been generated automatically from src/core/symbology/qgsstyleentityvisitor.h
# monkey patching scoped based enum
QgsStyleEntityVisitorInterface.NodeType.Project.__doc__ = "QGIS Project node"
QgsStyleEntityVisitorInterface.NodeType.Layer.__doc__ = "Map layer"
QgsStyleEntityVisitorInterface.NodeType.SymbolRule.__doc__ = "Rule based symbology or label child rule"
QgsStyleEntityVisitorInterface.NodeType.Layouts.__doc__ = "Layout collection"
QgsStyleEntityVisitorInterface.NodeType.PrintLayout.__doc__ = "An individual print layout"
QgsStyleEntityVisitorInterface.NodeType.LayoutItem.__doc__ = "Individual item in a print layout"
QgsStyleEntityVisitorInterface.NodeType.Report.__doc__ = "A QGIS print report"
QgsStyleEntityVisitorInterface.NodeType.ReportHeader.__doc__ = "Report header section"
QgsStyleEntityVisitorInterface.NodeType.ReportFooter.__doc__ = "Report footer section"
QgsStyleEntityVisitorInterface.NodeType.ReportSection.__doc__ = "Report sub section"
QgsStyleEntityVisitorInterface.NodeType.Annotations.__doc__ = "Annotations collection"
QgsStyleEntityVisitorInterface.NodeType.Annotation.__doc__ = "An individual annotation"
QgsStyleEntityVisitorInterface.NodeType.__doc__ = 'Describes the types of nodes which may be visited by the visitor.\n\n' + '* ``Project``: ' + QgsStyleEntityVisitorInterface.NodeType.Project.__doc__ + '\n' + '* ``Layer``: ' + QgsStyleEntityVisitorInterface.NodeType.Layer.__doc__ + '\n' + '* ``SymbolRule``: ' + QgsStyleEntityVisitorInterface.NodeType.SymbolRule.__doc__ + '\n' + '* ``Layouts``: ' + QgsStyleEntityVisitorInterface.NodeType.Layouts.__doc__ + '\n' + '* ``PrintLayout``: ' + QgsStyleEntityVisitorInterface.NodeType.PrintLayout.__doc__ + '\n' + '* ``LayoutItem``: ' + QgsStyleEntityVisitorInterface.NodeType.LayoutItem.__doc__ + '\n' + '* ``Report``: ' + QgsStyleEntityVisitorInterface.NodeType.Report.__doc__ + '\n' + '* ``ReportHeader``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportHeader.__doc__ + '\n' + '* ``ReportFooter``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportFooter.__doc__ + '\n' + '* ``ReportSection``: ' + QgsStyleEntityVisitorInterface.NodeType.ReportSection.__doc__ + '\n' + '* ``Annotations``: ' + QgsStyleEntityVisitorInterface.NodeType.Annotations.__doc__ + '\n' + '* ``Annotation``: ' + QgsStyleEntityVisitorInterface.NodeType.Annotation.__doc__
# --
# The following has been generated automatically from src/core/qgstaskmanager.h
QgsTask.TaskStatus.baseClass = QgsTask
# The following has been generated automatically from src/core/textrenderer/qgstextcharacterformat.h
# monkey patching scoped based enum
QgsTextCharacterFormat.BooleanValue.NotSet.__doc__ = "Property is not set"
QgsTextCharacterFormat.BooleanValue.SetTrue.__doc__ = "Property is set and ``True``"
QgsTextCharacterFormat.BooleanValue.SetFalse.__doc__ = "Property is set and ``False``"
QgsTextCharacterFormat.BooleanValue.__doc__ = 'Status values for boolean format properties\n\n' + '* ``NotSet``: ' + QgsTextCharacterFormat.BooleanValue.NotSet.__doc__ + '\n' + '* ``SetTrue``: ' + QgsTextCharacterFormat.BooleanValue.SetTrue.__doc__ + '\n' + '* ``SetFalse``: ' + QgsTextCharacterFormat.BooleanValue.SetFalse.__doc__
# --
# The following has been generated automatically from src/core/qgstolerance.h
QgsTolerance.UnitType.baseClass = QgsTolerance
# The following has been generated automatically from src/core/qgsunittypes.h
QgsUnitTypes.SystemOfMeasurement.baseClass = QgsUnitTypes
QgsUnitTypes.DistanceUnit.baseClass = QgsUnitTypes
QgsUnitTypes.AreaUnit.baseClass = QgsUnitTypes
QgsUnitTypes.VolumeUnit.baseClass = QgsUnitTypes
QgsUnitTypes.AngleUnit.baseClass = QgsUnitTypes
QgsUnitTypes.TemporalUnit.baseClass = QgsUnitTypes
QgsUnitTypes.RenderUnit.baseClass = QgsUnitTypes
QgsUnitTypes.LayoutUnit.baseClass = QgsUnitTypes
# The following has been generated automatically from src/core/qgsvectorsimplifymethod.h
QgsVectorSimplifyMethod.SimplifyHint.baseClass = QgsVectorSimplifyMethod
QgsVectorSimplifyMethod.SimplifyHints.baseClass = QgsVectorSimplifyMethod
SimplifyHints = QgsVectorSimplifyMethod  # dirty hack since SIP seems to introduce the flags in module
QgsVectorSimplifyMethod.SimplifyAlgorithm.baseClass = QgsVectorSimplifyMethod
# The following has been generated automatically from src/core/geometry/qgswkbtypes.h
QgsWkbTypes.Type.baseClass = QgsWkbTypes
QgsWkbTypes.GeometryType.baseClass = QgsWkbTypes
