# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CacheExpirationActionParameters
    from ._models_py3 import CacheKeyQueryStringActionParameters
    from ._models_py3 import CdnCertificateSourceParameters
    from ._models_py3 import CdnEndpoint
    from ._models_py3 import CdnManagedHttpsParameters
    from ._models_py3 import CdnWebApplicationFirewallPolicy
    from ._models_py3 import CdnWebApplicationFirewallPolicyList
    from ._models_py3 import CdnWebApplicationFirewallPolicyPatchParameters
    from ._models_py3 import CheckNameAvailabilityInput
    from ._models_py3 import CheckNameAvailabilityOutput
    from ._models_py3 import CidrIpAddress
    from ._models_py3 import CookiesMatchConditionParameters
    from ._models_py3 import CustomDomain
    from ._models_py3 import CustomDomainHttpsParameters
    from ._models_py3 import CustomDomainListResult
    from ._models_py3 import CustomDomainParameters
    from ._models_py3 import CustomRule
    from ._models_py3 import CustomRuleList
    from ._models_py3 import DeepCreatedOrigin
    from ._models_py3 import DeepCreatedOriginGroup
    from ._models_py3 import DeliveryRule
    from ._models_py3 import DeliveryRuleAction
    from ._models_py3 import DeliveryRuleCacheExpirationAction
    from ._models_py3 import DeliveryRuleCacheKeyQueryStringAction
    from ._models_py3 import DeliveryRuleCondition
    from ._models_py3 import DeliveryRuleCookiesCondition
    from ._models_py3 import DeliveryRuleHttpVersionCondition
    from ._models_py3 import DeliveryRuleIsDeviceCondition
    from ._models_py3 import DeliveryRulePostArgsCondition
    from ._models_py3 import DeliveryRuleQueryStringCondition
    from ._models_py3 import DeliveryRuleRemoteAddressCondition
    from ._models_py3 import DeliveryRuleRequestBodyCondition
    from ._models_py3 import DeliveryRuleRequestHeaderAction
    from ._models_py3 import DeliveryRuleRequestHeaderCondition
    from ._models_py3 import DeliveryRuleRequestMethodCondition
    from ._models_py3 import DeliveryRuleRequestSchemeCondition
    from ._models_py3 import DeliveryRuleRequestUriCondition
    from ._models_py3 import DeliveryRuleResponseHeaderAction
    from ._models_py3 import DeliveryRuleUrlFileExtensionCondition
    from ._models_py3 import DeliveryRuleUrlFileNameCondition
    from ._models_py3 import DeliveryRuleUrlPathCondition
    from ._models_py3 import EdgeNode
    from ._models_py3 import EdgenodeResult
    from ._models_py3 import Endpoint
    from ._models_py3 import EndpointListResult
    from ._models_py3 import EndpointProperties
    from ._models_py3 import EndpointPropertiesUpdateParameters
    from ._models_py3 import EndpointPropertiesUpdateParametersDeliveryPolicy
    from ._models_py3 import EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink
    from ._models_py3 import EndpointUpdateParameters
    from ._models_py3 import ErrorResponse
    from ._models_py3 import GeoFilter
    from ._models_py3 import HeaderActionParameters
    from ._models_py3 import HealthProbeParameters
    from ._models_py3 import HttpErrorRangeParameters
    from ._models_py3 import HttpVersionMatchConditionParameters
    from ._models_py3 import IpAddressGroup
    from ._models_py3 import IsDeviceMatchConditionParameters
    from ._models_py3 import KeyVaultCertificateSourceParameters
    from ._models_py3 import KeyVaultSigningKeyParameters
    from ._models_py3 import LoadParameters
    from ._models_py3 import ManagedRuleDefinition
    from ._models_py3 import ManagedRuleGroupDefinition
    from ._models_py3 import ManagedRuleGroupOverride
    from ._models_py3 import ManagedRuleOverride
    from ._models_py3 import ManagedRuleSet
    from ._models_py3 import ManagedRuleSetDefinition
    from ._models_py3 import ManagedRuleSetDefinitionList
    from ._models_py3 import ManagedRuleSetList
    from ._models_py3 import MatchCondition
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationsListResult
    from ._models_py3 import Origin
    from ._models_py3 import OriginGroup
    from ._models_py3 import OriginGroupListResult
    from ._models_py3 import OriginGroupProperties
    from ._models_py3 import OriginGroupUpdateParameters
    from ._models_py3 import OriginGroupUpdatePropertiesParameters
    from ._models_py3 import OriginListResult
    from ._models_py3 import OriginProperties
    from ._models_py3 import OriginUpdateParameters
    from ._models_py3 import OriginUpdatePropertiesParameters
    from ._models_py3 import PolicySettings
    from ._models_py3 import PostArgsMatchConditionParameters
    from ._models_py3 import Profile
    from ._models_py3 import ProfileListResult
    from ._models_py3 import ProfileUpdateParameters
    from ._models_py3 import ProxyResource
    from ._models_py3 import PurgeParameters
    from ._models_py3 import QueryStringMatchConditionParameters
    from ._models_py3 import RateLimitRule
    from ._models_py3 import RateLimitRuleList
    from ._models_py3 import RemoteAddressMatchConditionParameters
    from ._models_py3 import RequestBodyMatchConditionParameters
    from ._models_py3 import RequestHeaderMatchConditionParameters
    from ._models_py3 import RequestMethodMatchConditionParameters
    from ._models_py3 import RequestSchemeMatchConditionParameters
    from ._models_py3 import RequestUriMatchConditionParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceReference
    from ._models_py3 import ResourceUsage
    from ._models_py3 import ResourceUsageListResult
    from ._models_py3 import ResponseBasedOriginErrorDetectionParameters
    from ._models_py3 import Sku
    from ._models_py3 import SsoUri
    from ._models_py3 import SupportedOptimizationTypesListResult
    from ._models_py3 import TrackedResource
    from ._models_py3 import UrlFileExtensionMatchConditionParameters
    from ._models_py3 import UrlFileNameMatchConditionParameters
    from ._models_py3 import UrlPathMatchConditionParameters
    from ._models_py3 import UrlRedirectAction
    from ._models_py3 import UrlRedirectActionParameters
    from ._models_py3 import UrlRewriteAction
    from ._models_py3 import UrlRewriteActionParameters
    from ._models_py3 import UrlSigningAction
    from ._models_py3 import UrlSigningActionParameters
    from ._models_py3 import UrlSigningKey
    from ._models_py3 import UrlSigningParamIdentifier
    from ._models_py3 import UserManagedHttpsParameters
    from ._models_py3 import ValidateCustomDomainInput
    from ._models_py3 import ValidateCustomDomainOutput
    from ._models_py3 import ValidateProbeInput
    from ._models_py3 import ValidateProbeOutput
except (SyntaxError, ImportError):
    from ._models import CacheExpirationActionParameters  # type: ignore
    from ._models import CacheKeyQueryStringActionParameters  # type: ignore
    from ._models import CdnCertificateSourceParameters  # type: ignore
    from ._models import CdnEndpoint  # type: ignore
    from ._models import CdnManagedHttpsParameters  # type: ignore
    from ._models import CdnWebApplicationFirewallPolicy  # type: ignore
    from ._models import CdnWebApplicationFirewallPolicyList  # type: ignore
    from ._models import CdnWebApplicationFirewallPolicyPatchParameters  # type: ignore
    from ._models import CheckNameAvailabilityInput  # type: ignore
    from ._models import CheckNameAvailabilityOutput  # type: ignore
    from ._models import CidrIpAddress  # type: ignore
    from ._models import CookiesMatchConditionParameters  # type: ignore
    from ._models import CustomDomain  # type: ignore
    from ._models import CustomDomainHttpsParameters  # type: ignore
    from ._models import CustomDomainListResult  # type: ignore
    from ._models import CustomDomainParameters  # type: ignore
    from ._models import CustomRule  # type: ignore
    from ._models import CustomRuleList  # type: ignore
    from ._models import DeepCreatedOrigin  # type: ignore
    from ._models import DeepCreatedOriginGroup  # type: ignore
    from ._models import DeliveryRule  # type: ignore
    from ._models import DeliveryRuleAction  # type: ignore
    from ._models import DeliveryRuleCacheExpirationAction  # type: ignore
    from ._models import DeliveryRuleCacheKeyQueryStringAction  # type: ignore
    from ._models import DeliveryRuleCondition  # type: ignore
    from ._models import DeliveryRuleCookiesCondition  # type: ignore
    from ._models import DeliveryRuleHttpVersionCondition  # type: ignore
    from ._models import DeliveryRuleIsDeviceCondition  # type: ignore
    from ._models import DeliveryRulePostArgsCondition  # type: ignore
    from ._models import DeliveryRuleQueryStringCondition  # type: ignore
    from ._models import DeliveryRuleRemoteAddressCondition  # type: ignore
    from ._models import DeliveryRuleRequestBodyCondition  # type: ignore
    from ._models import DeliveryRuleRequestHeaderAction  # type: ignore
    from ._models import DeliveryRuleRequestHeaderCondition  # type: ignore
    from ._models import DeliveryRuleRequestMethodCondition  # type: ignore
    from ._models import DeliveryRuleRequestSchemeCondition  # type: ignore
    from ._models import DeliveryRuleRequestUriCondition  # type: ignore
    from ._models import DeliveryRuleResponseHeaderAction  # type: ignore
    from ._models import DeliveryRuleUrlFileExtensionCondition  # type: ignore
    from ._models import DeliveryRuleUrlFileNameCondition  # type: ignore
    from ._models import DeliveryRuleUrlPathCondition  # type: ignore
    from ._models import EdgeNode  # type: ignore
    from ._models import EdgenodeResult  # type: ignore
    from ._models import Endpoint  # type: ignore
    from ._models import EndpointListResult  # type: ignore
    from ._models import EndpointProperties  # type: ignore
    from ._models import EndpointPropertiesUpdateParameters  # type: ignore
    from ._models import EndpointPropertiesUpdateParametersDeliveryPolicy  # type: ignore
    from ._models import EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink  # type: ignore
    from ._models import EndpointUpdateParameters  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import GeoFilter  # type: ignore
    from ._models import HeaderActionParameters  # type: ignore
    from ._models import HealthProbeParameters  # type: ignore
    from ._models import HttpErrorRangeParameters  # type: ignore
    from ._models import HttpVersionMatchConditionParameters  # type: ignore
    from ._models import IpAddressGroup  # type: ignore
    from ._models import IsDeviceMatchConditionParameters  # type: ignore
    from ._models import KeyVaultCertificateSourceParameters  # type: ignore
    from ._models import KeyVaultSigningKeyParameters  # type: ignore
    from ._models import LoadParameters  # type: ignore
    from ._models import ManagedRuleDefinition  # type: ignore
    from ._models import ManagedRuleGroupDefinition  # type: ignore
    from ._models import ManagedRuleGroupOverride  # type: ignore
    from ._models import ManagedRuleOverride  # type: ignore
    from ._models import ManagedRuleSet  # type: ignore
    from ._models import ManagedRuleSetDefinition  # type: ignore
    from ._models import ManagedRuleSetDefinitionList  # type: ignore
    from ._models import ManagedRuleSetList  # type: ignore
    from ._models import MatchCondition  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationsListResult  # type: ignore
    from ._models import Origin  # type: ignore
    from ._models import OriginGroup  # type: ignore
    from ._models import OriginGroupListResult  # type: ignore
    from ._models import OriginGroupProperties  # type: ignore
    from ._models import OriginGroupUpdateParameters  # type: ignore
    from ._models import OriginGroupUpdatePropertiesParameters  # type: ignore
    from ._models import OriginListResult  # type: ignore
    from ._models import OriginProperties  # type: ignore
    from ._models import OriginUpdateParameters  # type: ignore
    from ._models import OriginUpdatePropertiesParameters  # type: ignore
    from ._models import PolicySettings  # type: ignore
    from ._models import PostArgsMatchConditionParameters  # type: ignore
    from ._models import Profile  # type: ignore
    from ._models import ProfileListResult  # type: ignore
    from ._models import ProfileUpdateParameters  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import PurgeParameters  # type: ignore
    from ._models import QueryStringMatchConditionParameters  # type: ignore
    from ._models import RateLimitRule  # type: ignore
    from ._models import RateLimitRuleList  # type: ignore
    from ._models import RemoteAddressMatchConditionParameters  # type: ignore
    from ._models import RequestBodyMatchConditionParameters  # type: ignore
    from ._models import RequestHeaderMatchConditionParameters  # type: ignore
    from ._models import RequestMethodMatchConditionParameters  # type: ignore
    from ._models import RequestSchemeMatchConditionParameters  # type: ignore
    from ._models import RequestUriMatchConditionParameters  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceReference  # type: ignore
    from ._models import ResourceUsage  # type: ignore
    from ._models import ResourceUsageListResult  # type: ignore
    from ._models import ResponseBasedOriginErrorDetectionParameters  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import SsoUri  # type: ignore
    from ._models import SupportedOptimizationTypesListResult  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import UrlFileExtensionMatchConditionParameters  # type: ignore
    from ._models import UrlFileNameMatchConditionParameters  # type: ignore
    from ._models import UrlPathMatchConditionParameters  # type: ignore
    from ._models import UrlRedirectAction  # type: ignore
    from ._models import UrlRedirectActionParameters  # type: ignore
    from ._models import UrlRewriteAction  # type: ignore
    from ._models import UrlRewriteActionParameters  # type: ignore
    from ._models import UrlSigningAction  # type: ignore
    from ._models import UrlSigningActionParameters  # type: ignore
    from ._models import UrlSigningKey  # type: ignore
    from ._models import UrlSigningParamIdentifier  # type: ignore
    from ._models import UserManagedHttpsParameters  # type: ignore
    from ._models import ValidateCustomDomainInput  # type: ignore
    from ._models import ValidateCustomDomainOutput  # type: ignore
    from ._models import ValidateProbeInput  # type: ignore
    from ._models import ValidateProbeOutput  # type: ignore

from ._cdn_management_client_enums import (
    ActionType,
    Algorithm,
    CacheBehavior,
    CacheType,
    CertificateSource,
    CertificateType,
    CookiesOperator,
    CustomDomainResourceState,
    CustomHttpsProvisioningState,
    CustomHttpsProvisioningSubstate,
    CustomRuleEnabledState,
    DeleteRule,
    DeliveryRuleActionName,
    DestinationProtocol,
    EndpointResourceState,
    Enum16,
    GeoFilterActions,
    HeaderAction,
    HealthProbeRequestType,
    HttpVersionOperator,
    IsDeviceMatchConditionParametersMatchValuesItem,
    IsDeviceOperator,
    ManagedRuleEnabledState,
    MatchVariable,
    MinimumTlsVersion,
    Operator,
    OptimizationType,
    OriginGroupResourceState,
    OriginResourceState,
    ParamIndicator,
    PolicyEnabledState,
    PolicyMode,
    PolicyResourceState,
    PostArgsOperator,
    PrivateEndpointStatus,
    ProbeProtocol,
    ProfileResourceState,
    ProtocolType,
    ProvisioningState,
    QueryStringBehavior,
    QueryStringCachingBehavior,
    QueryStringOperator,
    RedirectType,
    RemoteAddressOperator,
    RequestBodyOperator,
    RequestHeaderOperator,
    RequestMethodMatchConditionParametersMatchValuesItem,
    RequestMethodOperator,
    RequestSchemeMatchConditionParametersMatchValuesItem,
    RequestUriOperator,
    ResponseBasedDetectedErrorTypes,
    SkuName,
    Transform,
    TransformType,
    UpdateRule,
    UrlFileExtensionOperator,
    UrlFileNameOperator,
    UrlPathOperator,
)

__all__ = [
    'CacheExpirationActionParameters',
    'CacheKeyQueryStringActionParameters',
    'CdnCertificateSourceParameters',
    'CdnEndpoint',
    'CdnManagedHttpsParameters',
    'CdnWebApplicationFirewallPolicy',
    'CdnWebApplicationFirewallPolicyList',
    'CdnWebApplicationFirewallPolicyPatchParameters',
    'CheckNameAvailabilityInput',
    'CheckNameAvailabilityOutput',
    'CidrIpAddress',
    'CookiesMatchConditionParameters',
    'CustomDomain',
    'CustomDomainHttpsParameters',
    'CustomDomainListResult',
    'CustomDomainParameters',
    'CustomRule',
    'CustomRuleList',
    'DeepCreatedOrigin',
    'DeepCreatedOriginGroup',
    'DeliveryRule',
    'DeliveryRuleAction',
    'DeliveryRuleCacheExpirationAction',
    'DeliveryRuleCacheKeyQueryStringAction',
    'DeliveryRuleCondition',
    'DeliveryRuleCookiesCondition',
    'DeliveryRuleHttpVersionCondition',
    'DeliveryRuleIsDeviceCondition',
    'DeliveryRulePostArgsCondition',
    'DeliveryRuleQueryStringCondition',
    'DeliveryRuleRemoteAddressCondition',
    'DeliveryRuleRequestBodyCondition',
    'DeliveryRuleRequestHeaderAction',
    'DeliveryRuleRequestHeaderCondition',
    'DeliveryRuleRequestMethodCondition',
    'DeliveryRuleRequestSchemeCondition',
    'DeliveryRuleRequestUriCondition',
    'DeliveryRuleResponseHeaderAction',
    'DeliveryRuleUrlFileExtensionCondition',
    'DeliveryRuleUrlFileNameCondition',
    'DeliveryRuleUrlPathCondition',
    'EdgeNode',
    'EdgenodeResult',
    'Endpoint',
    'EndpointListResult',
    'EndpointProperties',
    'EndpointPropertiesUpdateParameters',
    'EndpointPropertiesUpdateParametersDeliveryPolicy',
    'EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink',
    'EndpointUpdateParameters',
    'ErrorResponse',
    'GeoFilter',
    'HeaderActionParameters',
    'HealthProbeParameters',
    'HttpErrorRangeParameters',
    'HttpVersionMatchConditionParameters',
    'IpAddressGroup',
    'IsDeviceMatchConditionParameters',
    'KeyVaultCertificateSourceParameters',
    'KeyVaultSigningKeyParameters',
    'LoadParameters',
    'ManagedRuleDefinition',
    'ManagedRuleGroupDefinition',
    'ManagedRuleGroupOverride',
    'ManagedRuleOverride',
    'ManagedRuleSet',
    'ManagedRuleSetDefinition',
    'ManagedRuleSetDefinitionList',
    'ManagedRuleSetList',
    'MatchCondition',
    'Operation',
    'OperationDisplay',
    'OperationsListResult',
    'Origin',
    'OriginGroup',
    'OriginGroupListResult',
    'OriginGroupProperties',
    'OriginGroupUpdateParameters',
    'OriginGroupUpdatePropertiesParameters',
    'OriginListResult',
    'OriginProperties',
    'OriginUpdateParameters',
    'OriginUpdatePropertiesParameters',
    'PolicySettings',
    'PostArgsMatchConditionParameters',
    'Profile',
    'ProfileListResult',
    'ProfileUpdateParameters',
    'ProxyResource',
    'PurgeParameters',
    'QueryStringMatchConditionParameters',
    'RateLimitRule',
    'RateLimitRuleList',
    'RemoteAddressMatchConditionParameters',
    'RequestBodyMatchConditionParameters',
    'RequestHeaderMatchConditionParameters',
    'RequestMethodMatchConditionParameters',
    'RequestSchemeMatchConditionParameters',
    'RequestUriMatchConditionParameters',
    'Resource',
    'ResourceReference',
    'ResourceUsage',
    'ResourceUsageListResult',
    'ResponseBasedOriginErrorDetectionParameters',
    'Sku',
    'SsoUri',
    'SupportedOptimizationTypesListResult',
    'TrackedResource',
    'UrlFileExtensionMatchConditionParameters',
    'UrlFileNameMatchConditionParameters',
    'UrlPathMatchConditionParameters',
    'UrlRedirectAction',
    'UrlRedirectActionParameters',
    'UrlRewriteAction',
    'UrlRewriteActionParameters',
    'UrlSigningAction',
    'UrlSigningActionParameters',
    'UrlSigningKey',
    'UrlSigningParamIdentifier',
    'UserManagedHttpsParameters',
    'ValidateCustomDomainInput',
    'ValidateCustomDomainOutput',
    'ValidateProbeInput',
    'ValidateProbeOutput',
    'ActionType',
    'Algorithm',
    'CacheBehavior',
    'CacheType',
    'CertificateSource',
    'CertificateType',
    'CookiesOperator',
    'CustomDomainResourceState',
    'CustomHttpsProvisioningState',
    'CustomHttpsProvisioningSubstate',
    'CustomRuleEnabledState',
    'DeleteRule',
    'DeliveryRuleActionName',
    'DestinationProtocol',
    'EndpointResourceState',
    'Enum16',
    'GeoFilterActions',
    'HeaderAction',
    'HealthProbeRequestType',
    'HttpVersionOperator',
    'IsDeviceMatchConditionParametersMatchValuesItem',
    'IsDeviceOperator',
    'ManagedRuleEnabledState',
    'MatchVariable',
    'MinimumTlsVersion',
    'Operator',
    'OptimizationType',
    'OriginGroupResourceState',
    'OriginResourceState',
    'ParamIndicator',
    'PolicyEnabledState',
    'PolicyMode',
    'PolicyResourceState',
    'PostArgsOperator',
    'PrivateEndpointStatus',
    'ProbeProtocol',
    'ProfileResourceState',
    'ProtocolType',
    'ProvisioningState',
    'QueryStringBehavior',
    'QueryStringCachingBehavior',
    'QueryStringOperator',
    'RedirectType',
    'RemoteAddressOperator',
    'RequestBodyOperator',
    'RequestHeaderOperator',
    'RequestMethodMatchConditionParametersMatchValuesItem',
    'RequestMethodOperator',
    'RequestSchemeMatchConditionParametersMatchValuesItem',
    'RequestUriOperator',
    'ResponseBasedDetectedErrorTypes',
    'SkuName',
    'Transform',
    'TransformType',
    'UpdateRule',
    'UrlFileExtensionOperator',
    'UrlFileNameOperator',
    'UrlPathOperator',
]
