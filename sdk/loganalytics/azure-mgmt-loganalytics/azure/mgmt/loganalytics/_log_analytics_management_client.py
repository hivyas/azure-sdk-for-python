# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import LogAnalyticsManagementClientConfiguration
from .operations import DataExportsOperations
from .operations import DataSourcesOperations
from .operations import IntelligencePacksOperations
from .operations import LinkedServicesOperations
from .operations import LinkedStorageAccountsOperations
from .operations import ManagementGroupsOperations
from .operations import Operations
from .operations import OperationStatusesOperations
from .operations import SharedKeysOperations
from .operations import UsagesOperations
from .operations import WorkspacesOperations
from .operations import DeletedWorkspacesOperations
from .operations import ClustersOperations
from .operations import StorageInsightConfigsOperations
from .operations import SavedSearchesOperations
from .operations import AvailableServiceTiersOperations
from .operations import GatewaysOperations
from .operations import SchemaOperations
from .operations import WorkspacePurgeOperations
from .operations import TablesOperations
from . import models


class LogAnalyticsManagementClient(object):
    """Operational Insights Client.

    :ivar data_exports: DataExportsOperations operations
    :vartype data_exports: azure.mgmt.loganalytics.operations.DataExportsOperations
    :ivar data_sources: DataSourcesOperations operations
    :vartype data_sources: azure.mgmt.loganalytics.operations.DataSourcesOperations
    :ivar intelligence_packs: IntelligencePacksOperations operations
    :vartype intelligence_packs: azure.mgmt.loganalytics.operations.IntelligencePacksOperations
    :ivar linked_services: LinkedServicesOperations operations
    :vartype linked_services: azure.mgmt.loganalytics.operations.LinkedServicesOperations
    :ivar linked_storage_accounts: LinkedStorageAccountsOperations operations
    :vartype linked_storage_accounts: azure.mgmt.loganalytics.operations.LinkedStorageAccountsOperations
    :ivar management_groups: ManagementGroupsOperations operations
    :vartype management_groups: azure.mgmt.loganalytics.operations.ManagementGroupsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.loganalytics.operations.Operations
    :ivar operation_statuses: OperationStatusesOperations operations
    :vartype operation_statuses: azure.mgmt.loganalytics.operations.OperationStatusesOperations
    :ivar shared_keys: SharedKeysOperations operations
    :vartype shared_keys: azure.mgmt.loganalytics.operations.SharedKeysOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.loganalytics.operations.UsagesOperations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.loganalytics.operations.WorkspacesOperations
    :ivar deleted_workspaces: DeletedWorkspacesOperations operations
    :vartype deleted_workspaces: azure.mgmt.loganalytics.operations.DeletedWorkspacesOperations
    :ivar clusters: ClustersOperations operations
    :vartype clusters: azure.mgmt.loganalytics.operations.ClustersOperations
    :ivar storage_insight_configs: StorageInsightConfigsOperations operations
    :vartype storage_insight_configs: azure.mgmt.loganalytics.operations.StorageInsightConfigsOperations
    :ivar saved_searches: SavedSearchesOperations operations
    :vartype saved_searches: azure.mgmt.loganalytics.operations.SavedSearchesOperations
    :ivar available_service_tiers: AvailableServiceTiersOperations operations
    :vartype available_service_tiers: azure.mgmt.loganalytics.operations.AvailableServiceTiersOperations
    :ivar gateways: GatewaysOperations operations
    :vartype gateways: azure.mgmt.loganalytics.operations.GatewaysOperations
    :ivar schema: SchemaOperations operations
    :vartype schema: azure.mgmt.loganalytics.operations.SchemaOperations
    :ivar workspace_purge: WorkspacePurgeOperations operations
    :vartype workspace_purge: azure.mgmt.loganalytics.operations.WorkspacePurgeOperations
    :ivar tables: TablesOperations operations
    :vartype tables: azure.mgmt.loganalytics.operations.TablesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = LogAnalyticsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.data_exports = DataExportsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_sources = DataSourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.intelligence_packs = IntelligencePacksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_services = LinkedServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.linked_storage_accounts = LinkedStorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_groups = ManagementGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_statuses = OperationStatusesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.shared_keys = SharedKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deleted_workspaces = DeletedWorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.clusters = ClustersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_insight_configs = StorageInsightConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.saved_searches = SavedSearchesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_service_tiers = AvailableServiceTiersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gateways = GatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.schema = SchemaOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_purge = WorkspacePurgeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tables = TablesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> LogAnalyticsManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
