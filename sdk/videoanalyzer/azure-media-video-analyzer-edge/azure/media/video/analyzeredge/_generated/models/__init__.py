# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AssetSink
    from ._models_py3 import CertificateSource
    from ._models_py3 import CognitiveServicesVisionExtension
    from ._models_py3 import Credentials
    from ._models_py3 import Endpoint
    from ._models_py3 import ExtensionProcessorBase
    from ._models_py3 import FileSink
    from ._models_py3 import GrpcExtension
    from ._models_py3 import GrpcExtensionDataTransfer
    from ._models_py3 import HttpExtension
    from ._models_py3 import HttpHeaderCredentials
    from ._models_py3 import Image
    from ._models_py3 import ImageFormat
    from ._models_py3 import ImageFormatBmp
    from ._models_py3 import ImageFormatJpeg
    from ._models_py3 import ImageFormatPng
    from ._models_py3 import ImageFormatRaw
    from ._models_py3 import ImageScale
    from ._models_py3 import IotHubMessageSink
    from ._models_py3 import IotHubMessageSource
    from ._models_py3 import ItemNonSetRequestBase
    from ._models_py3 import Line
    from ._models_py3 import LineCoordinates
    from ._models_py3 import LineCrossingProcessor
    from ._models_py3 import LivePipeline
    from ._models_py3 import LivePipelineActivateRequest
    from ._models_py3 import LivePipelineCollection
    from ._models_py3 import LivePipelineDeactivateRequest
    from ._models_py3 import LivePipelineDeleteRequest
    from ._models_py3 import LivePipelineGetRequest
    from ._models_py3 import LivePipelineListRequest
    from ._models_py3 import LivePipelineProperties
    from ._models_py3 import LivePipelineSetRequest
    from ._models_py3 import LivePipelineSetRequestBody
    from ._models_py3 import MethodRequest
    from ._models_py3 import MotionDetectionProcessor
    from ._models_py3 import NodeInput
    from ._models_py3 import ObjectTrackingProcessor
    from ._models_py3 import OutputSelector
    from ._models_py3 import ParameterDeclaration
    from ._models_py3 import ParameterDefinition
    from ._models_py3 import PemCertificateList
    from ._models_py3 import PipelineTopology
    from ._models_py3 import PipelineTopologyCollection
    from ._models_py3 import PipelineTopologyDeleteRequest
    from ._models_py3 import PipelineTopologyGetRequest
    from ._models_py3 import PipelineTopologyListRequest
    from ._models_py3 import PipelineTopologyProperties
    from ._models_py3 import PipelineTopologySetRequest
    from ._models_py3 import PipelineTopologySetRequestBody
    from ._models_py3 import Point
    from ._models_py3 import Processor
    from ._models_py3 import RtspSource
    from ._models_py3 import SamplingOptions
    from ._models_py3 import SignalGateProcessor
    from ._models_py3 import Sink
    from ._models_py3 import Source
    from ._models_py3 import SymmetricKeyCredentials
    from ._models_py3 import SystemData
    from ._models_py3 import TlsEndpoint
    from ._models_py3 import TlsValidationOptions
    from ._models_py3 import UnsecuredEndpoint
    from ._models_py3 import UsernamePasswordCredentials
except (SyntaxError, ImportError):
    from ._models import AssetSink  # type: ignore
    from ._models import CertificateSource  # type: ignore
    from ._models import CognitiveServicesVisionExtension  # type: ignore
    from ._models import Credentials  # type: ignore
    from ._models import Endpoint  # type: ignore
    from ._models import ExtensionProcessorBase  # type: ignore
    from ._models import FileSink  # type: ignore
    from ._models import GrpcExtension  # type: ignore
    from ._models import GrpcExtensionDataTransfer  # type: ignore
    from ._models import HttpExtension  # type: ignore
    from ._models import HttpHeaderCredentials  # type: ignore
    from ._models import Image  # type: ignore
    from ._models import ImageFormat  # type: ignore
    from ._models import ImageFormatBmp  # type: ignore
    from ._models import ImageFormatJpeg  # type: ignore
    from ._models import ImageFormatPng  # type: ignore
    from ._models import ImageFormatRaw  # type: ignore
    from ._models import ImageScale  # type: ignore
    from ._models import IotHubMessageSink  # type: ignore
    from ._models import IotHubMessageSource  # type: ignore
    from ._models import ItemNonSetRequestBase  # type: ignore
    from ._models import Line  # type: ignore
    from ._models import LineCoordinates  # type: ignore
    from ._models import LineCrossingProcessor  # type: ignore
    from ._models import LivePipeline  # type: ignore
    from ._models import LivePipelineActivateRequest  # type: ignore
    from ._models import LivePipelineCollection  # type: ignore
    from ._models import LivePipelineDeactivateRequest  # type: ignore
    from ._models import LivePipelineDeleteRequest  # type: ignore
    from ._models import LivePipelineGetRequest  # type: ignore
    from ._models import LivePipelineListRequest  # type: ignore
    from ._models import LivePipelineProperties  # type: ignore
    from ._models import LivePipelineSetRequest  # type: ignore
    from ._models import LivePipelineSetRequestBody  # type: ignore
    from ._models import MethodRequest  # type: ignore
    from ._models import MotionDetectionProcessor  # type: ignore
    from ._models import NodeInput  # type: ignore
    from ._models import ObjectTrackingProcessor  # type: ignore
    from ._models import OutputSelector  # type: ignore
    from ._models import ParameterDeclaration  # type: ignore
    from ._models import ParameterDefinition  # type: ignore
    from ._models import PemCertificateList  # type: ignore
    from ._models import PipelineTopology  # type: ignore
    from ._models import PipelineTopologyCollection  # type: ignore
    from ._models import PipelineTopologyDeleteRequest  # type: ignore
    from ._models import PipelineTopologyGetRequest  # type: ignore
    from ._models import PipelineTopologyListRequest  # type: ignore
    from ._models import PipelineTopologyProperties  # type: ignore
    from ._models import PipelineTopologySetRequest  # type: ignore
    from ._models import PipelineTopologySetRequestBody  # type: ignore
    from ._models import Point  # type: ignore
    from ._models import Processor  # type: ignore
    from ._models import RtspSource  # type: ignore
    from ._models import SamplingOptions  # type: ignore
    from ._models import SignalGateProcessor  # type: ignore
    from ._models import Sink  # type: ignore
    from ._models import Source  # type: ignore
    from ._models import SymmetricKeyCredentials  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TlsEndpoint  # type: ignore
    from ._models import TlsValidationOptions  # type: ignore
    from ._models import UnsecuredEndpoint  # type: ignore
    from ._models import UsernamePasswordCredentials  # type: ignore

from ._direct_methodsfor_azure_video_analyzeron_io_tedge_enums import (
    GrpcExtensionDataTransferMode,
    ImageFormatRawPixelFormat,
    ImageScaleMode,
    LivePipelineState,
    MotionDetectionSensitivity,
    ObjectTrackingAccuracy,
    OutputSelectorOperator,
    OutputSelectorProperty,
    ParameterType,
    RtspTransport,
)

__all__ = [
    'AssetSink',
    'CertificateSource',
    'CognitiveServicesVisionExtension',
    'Credentials',
    'Endpoint',
    'ExtensionProcessorBase',
    'FileSink',
    'GrpcExtension',
    'GrpcExtensionDataTransfer',
    'HttpExtension',
    'HttpHeaderCredentials',
    'Image',
    'ImageFormat',
    'ImageFormatBmp',
    'ImageFormatJpeg',
    'ImageFormatPng',
    'ImageFormatRaw',
    'ImageScale',
    'IotHubMessageSink',
    'IotHubMessageSource',
    'ItemNonSetRequestBase',
    'Line',
    'LineCoordinates',
    'LineCrossingProcessor',
    'LivePipeline',
    'LivePipelineActivateRequest',
    'LivePipelineCollection',
    'LivePipelineDeactivateRequest',
    'LivePipelineDeleteRequest',
    'LivePipelineGetRequest',
    'LivePipelineListRequest',
    'LivePipelineProperties',
    'LivePipelineSetRequest',
    'LivePipelineSetRequestBody',
    'MethodRequest',
    'MotionDetectionProcessor',
    'NodeInput',
    'ObjectTrackingProcessor',
    'OutputSelector',
    'ParameterDeclaration',
    'ParameterDefinition',
    'PemCertificateList',
    'PipelineTopology',
    'PipelineTopologyCollection',
    'PipelineTopologyDeleteRequest',
    'PipelineTopologyGetRequest',
    'PipelineTopologyListRequest',
    'PipelineTopologyProperties',
    'PipelineTopologySetRequest',
    'PipelineTopologySetRequestBody',
    'Point',
    'Processor',
    'RtspSource',
    'SamplingOptions',
    'SignalGateProcessor',
    'Sink',
    'Source',
    'SymmetricKeyCredentials',
    'SystemData',
    'TlsEndpoint',
    'TlsValidationOptions',
    'UnsecuredEndpoint',
    'UsernamePasswordCredentials',
    'GrpcExtensionDataTransferMode',
    'ImageFormatRawPixelFormat',
    'ImageScaleMode',
    'LivePipelineState',
    'MotionDetectionSensitivity',
    'ObjectTrackingAccuracy',
    'OutputSelectorOperator',
    'OutputSelectorProperty',
    'ParameterType',
    'RtspTransport',
]
