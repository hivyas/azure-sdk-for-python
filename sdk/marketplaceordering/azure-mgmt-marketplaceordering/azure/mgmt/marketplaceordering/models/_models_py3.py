# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._marketplace_ordering_agreements_enums import *


class Resource(msrest.serialization.Model):
    """ARM resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class AgreementTerms(Resource):
    """Terms properties for provided Publisher/Offer/Plan tuple.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar system_data: The system meta data relating to this resource.
    :vartype system_data: ~azure.mgmt.marketplaceordering.models.SystemData
    :param publisher: Publisher identifier string of image being deployed.
    :type publisher: str
    :param product: Offer identifier string of image being deployed.
    :type product: str
    :param plan: Plan identifier string of image being deployed.
    :type plan: str
    :param license_text_link: Link to HTML with Microsoft and Publisher terms.
    :type license_text_link: str
    :param privacy_policy_link: Link to the privacy policy of the publisher.
    :type privacy_policy_link: str
    :param marketplace_terms_link: Link to HTML with Azure Marketplace terms.
    :type marketplace_terms_link: str
    :param retrieve_datetime: Date and time in UTC of when the terms were accepted. This is empty
     if Accepted is false.
    :type retrieve_datetime: str
    :param signature: Terms signature.
    :type signature: str
    :param accepted: If any version of the terms have been accepted, otherwise false.
    :type accepted: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'publisher': {'key': 'properties.publisher', 'type': 'str'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'plan': {'key': 'properties.plan', 'type': 'str'},
        'license_text_link': {'key': 'properties.licenseTextLink', 'type': 'str'},
        'privacy_policy_link': {'key': 'properties.privacyPolicyLink', 'type': 'str'},
        'marketplace_terms_link': {'key': 'properties.marketplaceTermsLink', 'type': 'str'},
        'retrieve_datetime': {'key': 'properties.retrieveDatetime', 'type': 'str'},
        'signature': {'key': 'properties.signature', 'type': 'str'},
        'accepted': {'key': 'properties.accepted', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        publisher: Optional[str] = None,
        product: Optional[str] = None,
        plan: Optional[str] = None,
        license_text_link: Optional[str] = None,
        privacy_policy_link: Optional[str] = None,
        marketplace_terms_link: Optional[str] = None,
        retrieve_datetime: Optional[str] = None,
        signature: Optional[str] = None,
        accepted: Optional[bool] = None,
        **kwargs
    ):
        super(AgreementTerms, self).__init__(**kwargs)
        self.system_data = None
        self.publisher = publisher
        self.product = product
        self.plan = plan
        self.license_text_link = license_text_link
        self.privacy_policy_link = privacy_policy_link
        self.marketplace_terms_link = marketplace_terms_link
        self.retrieve_datetime = retrieve_datetime
        self.signature = signature
        self.accepted = accepted


class ErrorResponse(msrest.serialization.Model):
    """Error response indicates Microsoft.MarketplaceOrdering service is not able to process the incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~azure.mgmt.marketplaceordering.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponseError"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseError(msrest.serialization.Model):
    """The details of the error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = None
        self.message = None


class Operation(msrest.serialization.Model):
    """Microsoft.MarketplaceOrdering REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.marketplaceordering.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.MarketplaceOrdering.
    :type provider: str
    :param resource: Resource on which the operation is performed: Agreement, virtualmachine, etc.
    :type resource: str
    :param operation: Operation type: Get Agreement, Sign Agreement, Cancel Agreement etc.
    :type operation: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list MarketplaceOrdering operations. It contains a list of operations and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of Microsoft.MarketplaceOrdering operations supported by the
     Microsoft.MarketplaceOrdering resource provider.
    :type value: list[~azure.mgmt.marketplaceordering.models.Operation]
    :ivar next_link: URL to get the next set of operation list results if there are any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~azure.mgmt.marketplaceordering.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or ~azure.mgmt.marketplaceordering.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
