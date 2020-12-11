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

from ._configuration import SynapseManagementClientConfiguration
from .operations import BigDataPoolsOperations
from .operations import Operations
from .operations import IpFirewallRulesOperations
from .operations import SqlPoolsOperations
from .operations import SqlPoolMetadataSyncConfigsOperations
from .operations import SqlPoolOperationResultsOperations
from .operations import SqlPoolGeoBackupPoliciesOperations
from .operations import SqlPoolDataWarehouseUserActivitiesOperations
from .operations import SqlPoolRestorePointsOperations
from .operations import SqlPoolReplicationLinksOperations
from .operations import SqlPoolTransparentDataEncryptionsOperations
from .operations import SqlPoolBlobAuditingPoliciesOperations
from .operations import SqlPoolOperationsOperations
from .operations import SqlPoolUsagesOperations
from .operations import SqlPoolSensitivityLabelsOperations
from .operations import SqlPoolSchemasOperations
from .operations import SqlPoolTablesOperations
from .operations import SqlPoolTableColumnsOperations
from .operations import SqlPoolConnectionPoliciesOperations
from .operations import SqlPoolVulnerabilityAssessmentsOperations
from .operations import SqlPoolVulnerabilityAssessmentScansOperations
from .operations import SqlPoolSecurityAlertPoliciesOperations
from .operations import SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
from .operations import ExtendedSqlPoolBlobAuditingPoliciesOperations
from .operations import DataMaskingPoliciesOperations
from .operations import DataMaskingRulesOperations
from .operations import SqlPoolColumnsOperations
from .operations import SqlPoolWorkloadGroupOperations
from .operations import SqlPoolWorkloadClassifierOperations
from .operations import WorkspacesOperations
from .operations import WorkspaceAadAdminsOperations
from .operations import WorkspaceSqlAadAdminsOperations
from .operations import WorkspaceManagedIdentitySqlControlSettingsOperations
from .operations import RestorableDroppedSqlPoolsOperations
from .operations import IntegrationRuntimesOperations
from .operations import IntegrationRuntimeNodeIpAddressOperations
from .operations import IntegrationRuntimeObjectMetadataOperations
from .operations import IntegrationRuntimeNodesOperations
from .operations import IntegrationRuntimeCredentialsOperations
from .operations import IntegrationRuntimeConnectionInfosOperations
from .operations import IntegrationRuntimeAuthKeysOperations
from .operations import IntegrationRuntimeMonitoringDataOperations
from .operations import IntegrationRuntimeStatusOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkHubsOperations
from .operations import PrivateEndpointConnectionsPrivateLinkHubOperations
from .operations import WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
from .operations import WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
from .operations import WorkspaceManagedSqlServerSecurityAlertPolicyOperations
from .operations import WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
from .operations import WorkspaceManagedSqlServerUsagesOperations
from .operations import WorkspaceManagedSqlServerRecoverableSqlpoolsOperations
from .operations import KeysOperations
from . import models


class SynapseManagementClient(object):
    """Azure Synapse Analytics Management Client.

    :ivar big_data_pools: BigDataPoolsOperations operations
    :vartype big_data_pools: azure.mgmt.synapse.operations.BigDataPoolsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.synapse.operations.Operations
    :ivar ip_firewall_rules: IpFirewallRulesOperations operations
    :vartype ip_firewall_rules: azure.mgmt.synapse.operations.IpFirewallRulesOperations
    :ivar sql_pools: SqlPoolsOperations operations
    :vartype sql_pools: azure.mgmt.synapse.operations.SqlPoolsOperations
    :ivar sql_pool_metadata_sync_configs: SqlPoolMetadataSyncConfigsOperations operations
    :vartype sql_pool_metadata_sync_configs: azure.mgmt.synapse.operations.SqlPoolMetadataSyncConfigsOperations
    :ivar sql_pool_operation_results: SqlPoolOperationResultsOperations operations
    :vartype sql_pool_operation_results: azure.mgmt.synapse.operations.SqlPoolOperationResultsOperations
    :ivar sql_pool_geo_backup_policies: SqlPoolGeoBackupPoliciesOperations operations
    :vartype sql_pool_geo_backup_policies: azure.mgmt.synapse.operations.SqlPoolGeoBackupPoliciesOperations
    :ivar sql_pool_data_warehouse_user_activities: SqlPoolDataWarehouseUserActivitiesOperations operations
    :vartype sql_pool_data_warehouse_user_activities: azure.mgmt.synapse.operations.SqlPoolDataWarehouseUserActivitiesOperations
    :ivar sql_pool_restore_points: SqlPoolRestorePointsOperations operations
    :vartype sql_pool_restore_points: azure.mgmt.synapse.operations.SqlPoolRestorePointsOperations
    :ivar sql_pool_replication_links: SqlPoolReplicationLinksOperations operations
    :vartype sql_pool_replication_links: azure.mgmt.synapse.operations.SqlPoolReplicationLinksOperations
    :ivar sql_pool_transparent_data_encryptions: SqlPoolTransparentDataEncryptionsOperations operations
    :vartype sql_pool_transparent_data_encryptions: azure.mgmt.synapse.operations.SqlPoolTransparentDataEncryptionsOperations
    :ivar sql_pool_blob_auditing_policies: SqlPoolBlobAuditingPoliciesOperations operations
    :vartype sql_pool_blob_auditing_policies: azure.mgmt.synapse.operations.SqlPoolBlobAuditingPoliciesOperations
    :ivar sql_pool_operations: SqlPoolOperationsOperations operations
    :vartype sql_pool_operations: azure.mgmt.synapse.operations.SqlPoolOperationsOperations
    :ivar sql_pool_usages: SqlPoolUsagesOperations operations
    :vartype sql_pool_usages: azure.mgmt.synapse.operations.SqlPoolUsagesOperations
    :ivar sql_pool_sensitivity_labels: SqlPoolSensitivityLabelsOperations operations
    :vartype sql_pool_sensitivity_labels: azure.mgmt.synapse.operations.SqlPoolSensitivityLabelsOperations
    :ivar sql_pool_schemas: SqlPoolSchemasOperations operations
    :vartype sql_pool_schemas: azure.mgmt.synapse.operations.SqlPoolSchemasOperations
    :ivar sql_pool_tables: SqlPoolTablesOperations operations
    :vartype sql_pool_tables: azure.mgmt.synapse.operations.SqlPoolTablesOperations
    :ivar sql_pool_table_columns: SqlPoolTableColumnsOperations operations
    :vartype sql_pool_table_columns: azure.mgmt.synapse.operations.SqlPoolTableColumnsOperations
    :ivar sql_pool_connection_policies: SqlPoolConnectionPoliciesOperations operations
    :vartype sql_pool_connection_policies: azure.mgmt.synapse.operations.SqlPoolConnectionPoliciesOperations
    :ivar sql_pool_vulnerability_assessments: SqlPoolVulnerabilityAssessmentsOperations operations
    :vartype sql_pool_vulnerability_assessments: azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentsOperations
    :ivar sql_pool_vulnerability_assessment_scans: SqlPoolVulnerabilityAssessmentScansOperations operations
    :vartype sql_pool_vulnerability_assessment_scans: azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentScansOperations
    :ivar sql_pool_security_alert_policies: SqlPoolSecurityAlertPoliciesOperations operations
    :vartype sql_pool_security_alert_policies: azure.mgmt.synapse.operations.SqlPoolSecurityAlertPoliciesOperations
    :ivar sql_pool_vulnerability_assessment_rule_baselines: SqlPoolVulnerabilityAssessmentRuleBaselinesOperations operations
    :vartype sql_pool_vulnerability_assessment_rule_baselines: azure.mgmt.synapse.operations.SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
    :ivar extended_sql_pool_blob_auditing_policies: ExtendedSqlPoolBlobAuditingPoliciesOperations operations
    :vartype extended_sql_pool_blob_auditing_policies: azure.mgmt.synapse.operations.ExtendedSqlPoolBlobAuditingPoliciesOperations
    :ivar data_masking_policies: DataMaskingPoliciesOperations operations
    :vartype data_masking_policies: azure.mgmt.synapse.operations.DataMaskingPoliciesOperations
    :ivar data_masking_rules: DataMaskingRulesOperations operations
    :vartype data_masking_rules: azure.mgmt.synapse.operations.DataMaskingRulesOperations
    :ivar sql_pool_columns: SqlPoolColumnsOperations operations
    :vartype sql_pool_columns: azure.mgmt.synapse.operations.SqlPoolColumnsOperations
    :ivar sql_pool_workload_group: SqlPoolWorkloadGroupOperations operations
    :vartype sql_pool_workload_group: azure.mgmt.synapse.operations.SqlPoolWorkloadGroupOperations
    :ivar sql_pool_workload_classifier: SqlPoolWorkloadClassifierOperations operations
    :vartype sql_pool_workload_classifier: azure.mgmt.synapse.operations.SqlPoolWorkloadClassifierOperations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.synapse.operations.WorkspacesOperations
    :ivar workspace_aad_admins: WorkspaceAadAdminsOperations operations
    :vartype workspace_aad_admins: azure.mgmt.synapse.operations.WorkspaceAadAdminsOperations
    :ivar workspace_sql_aad_admins: WorkspaceSqlAadAdminsOperations operations
    :vartype workspace_sql_aad_admins: azure.mgmt.synapse.operations.WorkspaceSqlAadAdminsOperations
    :ivar workspace_managed_identity_sql_control_settings: WorkspaceManagedIdentitySqlControlSettingsOperations operations
    :vartype workspace_managed_identity_sql_control_settings: azure.mgmt.synapse.operations.WorkspaceManagedIdentitySqlControlSettingsOperations
    :ivar restorable_dropped_sql_pools: RestorableDroppedSqlPoolsOperations operations
    :vartype restorable_dropped_sql_pools: azure.mgmt.synapse.operations.RestorableDroppedSqlPoolsOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.mgmt.synapse.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_node_ip_address: IntegrationRuntimeNodeIpAddressOperations operations
    :vartype integration_runtime_node_ip_address: azure.mgmt.synapse.operations.IntegrationRuntimeNodeIpAddressOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations operations
    :vartype integration_runtime_object_metadata: azure.mgmt.synapse.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodesOperations operations
    :vartype integration_runtime_nodes: azure.mgmt.synapse.operations.IntegrationRuntimeNodesOperations
    :ivar integration_runtime_credentials: IntegrationRuntimeCredentialsOperations operations
    :vartype integration_runtime_credentials: azure.mgmt.synapse.operations.IntegrationRuntimeCredentialsOperations
    :ivar integration_runtime_connection_infos: IntegrationRuntimeConnectionInfosOperations operations
    :vartype integration_runtime_connection_infos: azure.mgmt.synapse.operations.IntegrationRuntimeConnectionInfosOperations
    :ivar integration_runtime_auth_keys: IntegrationRuntimeAuthKeysOperations operations
    :vartype integration_runtime_auth_keys: azure.mgmt.synapse.operations.IntegrationRuntimeAuthKeysOperations
    :ivar integration_runtime_monitoring_data: IntegrationRuntimeMonitoringDataOperations operations
    :vartype integration_runtime_monitoring_data: azure.mgmt.synapse.operations.IntegrationRuntimeMonitoringDataOperations
    :ivar integration_runtime_status: IntegrationRuntimeStatusOperations operations
    :vartype integration_runtime_status: azure.mgmt.synapse.operations.IntegrationRuntimeStatusOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.synapse.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.synapse.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_hubs: PrivateLinkHubsOperations operations
    :vartype private_link_hubs: azure.mgmt.synapse.operations.PrivateLinkHubsOperations
    :ivar private_endpoint_connections_private_link_hub: PrivateEndpointConnectionsPrivateLinkHubOperations operations
    :vartype private_endpoint_connections_private_link_hub: azure.mgmt.synapse.operations.PrivateEndpointConnectionsPrivateLinkHubOperations
    :ivar workspace_managed_sql_server_blob_auditing_policies: WorkspaceManagedSqlServerBlobAuditingPoliciesOperations operations
    :vartype workspace_managed_sql_server_blob_auditing_policies: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_extended_blob_auditing_policies: WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations operations
    :vartype workspace_managed_sql_server_extended_blob_auditing_policies: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_security_alert_policy: WorkspaceManagedSqlServerSecurityAlertPolicyOperations operations
    :vartype workspace_managed_sql_server_security_alert_policy: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerSecurityAlertPolicyOperations
    :ivar workspace_managed_sql_server_vulnerability_assessments: WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations operations
    :vartype workspace_managed_sql_server_vulnerability_assessments: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
    :ivar workspace_managed_sql_server_usages: WorkspaceManagedSqlServerUsagesOperations operations
    :vartype workspace_managed_sql_server_usages: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerUsagesOperations
    :ivar workspace_managed_sql_server_recoverable_sqlpools: WorkspaceManagedSqlServerRecoverableSqlpoolsOperations operations
    :vartype workspace_managed_sql_server_recoverable_sqlpools: azure.mgmt.synapse.operations.WorkspaceManagedSqlServerRecoverableSqlpoolsOperations
    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.synapse.operations.KeysOperations
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
        self._config = SynapseManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.big_data_pools = BigDataPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.ip_firewall_rules = IpFirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pools = SqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_metadata_sync_configs = SqlPoolMetadataSyncConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_operation_results = SqlPoolOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_geo_backup_policies = SqlPoolGeoBackupPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_data_warehouse_user_activities = SqlPoolDataWarehouseUserActivitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_restore_points = SqlPoolRestorePointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_replication_links = SqlPoolReplicationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_transparent_data_encryptions = SqlPoolTransparentDataEncryptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_blob_auditing_policies = SqlPoolBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_operations = SqlPoolOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_usages = SqlPoolUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_sensitivity_labels = SqlPoolSensitivityLabelsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_schemas = SqlPoolSchemasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_tables = SqlPoolTablesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_table_columns = SqlPoolTableColumnsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_connection_policies = SqlPoolConnectionPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessments = SqlPoolVulnerabilityAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessment_scans = SqlPoolVulnerabilityAssessmentScansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_security_alert_policies = SqlPoolSecurityAlertPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessment_rule_baselines = SqlPoolVulnerabilityAssessmentRuleBaselinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.extended_sql_pool_blob_auditing_policies = ExtendedSqlPoolBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_masking_policies = DataMaskingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_masking_rules = DataMaskingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_columns = SqlPoolColumnsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_workload_group = SqlPoolWorkloadGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_workload_classifier = SqlPoolWorkloadClassifierOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_aad_admins = WorkspaceAadAdminsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_sql_aad_admins = WorkspaceSqlAadAdminsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_identity_sql_control_settings = WorkspaceManagedIdentitySqlControlSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_dropped_sql_pools = RestorableDroppedSqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_node_ip_address = IntegrationRuntimeNodeIpAddressOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_credentials = IntegrationRuntimeCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_connection_infos = IntegrationRuntimeConnectionInfosOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_auth_keys = IntegrationRuntimeAuthKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_monitoring_data = IntegrationRuntimeMonitoringDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_status = IntegrationRuntimeStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_hubs = PrivateLinkHubsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections_private_link_hub = PrivateEndpointConnectionsPrivateLinkHubOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_blob_auditing_policies = WorkspaceManagedSqlServerBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_extended_blob_auditing_policies = WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_security_alert_policy = WorkspaceManagedSqlServerSecurityAlertPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_vulnerability_assessments = WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_usages = WorkspaceManagedSqlServerUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_recoverable_sqlpools = WorkspaceManagedSqlServerRecoverableSqlpoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.keys = KeysOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> SynapseManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
