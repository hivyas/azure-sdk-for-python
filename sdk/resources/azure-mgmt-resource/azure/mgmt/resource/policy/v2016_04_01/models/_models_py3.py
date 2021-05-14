# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

import msrest.serialization

from ._policy_client_enums import *


class PolicyAssignment(msrest.serialization.Model):
    """The policy assignment.

    :param id: The ID of the policy assignment.
    :type id: str
    :param type: The type of the policy assignment.
    :type type: str
    :param name: The name of the policy assignment.
    :type name: str
    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition.
    :type policy_definition_id: str
    :param scope: The scope for the policy assignment.
    :type scope: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        type: Optional[str] = None,
        name: Optional[str] = None,
        display_name: Optional[str] = None,
        policy_definition_id: Optional[str] = None,
        scope: Optional[str] = None,
        **kwargs
    ):
        super(PolicyAssignment, self).__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope


class PolicyAssignmentListResult(msrest.serialization.Model):
    """List of policy assignments.

    :param value: An array of policy assignments.
    :type value: list[~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyAssignment]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicyAssignment"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PolicyAssignmentListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PolicyDefinition(msrest.serialization.Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of the policy definition.
    :vartype id: str
    :param name: The name of the policy definition. If you do not specify a value for name, the
     value is inferred from the name value in the request URI.
    :type name: str
    :param policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn,
     and Custom. Possible values include: "NotSpecified", "BuiltIn", "Custom".
    :type policy_type: str or ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyType
    :param display_name: The display name of the policy definition.
    :type display_name: str
    :param description: The policy definition description.
    :type description: str
    :param policy_rule: The policy rule.
    :type policy_rule: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        policy_type: Optional[Union[str, "PolicyType"]] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        policy_rule: Optional[str] = None,
        **kwargs
    ):
        super(PolicyDefinition, self).__init__(**kwargs)
        self.id = None
        self.name = name
        self.policy_type = policy_type
        self.display_name = display_name
        self.description = description
        self.policy_rule = policy_rule


class PolicyDefinitionListResult(msrest.serialization.Model):
    """List of policy definitions.

    :param value: An array of policy definitions.
    :type value: list[~azure.mgmt.resource.policy.v2016_04_01.models.PolicyDefinition]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PolicyDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PolicyDefinition"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PolicyDefinitionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
