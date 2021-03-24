# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import SearchClientConfiguration
from .operations import DataSourcesOperations
from .operations import IndexersOperations
from .operations import SkillsetsOperations
from .operations import SynonymMapsOperations
from .operations import IndexesOperations
from .operations import SearchClientOperationsMixin
from . import models


class SearchClient(SearchClientOperationsMixin):
    """Client that can be used to manage and query indexes and documents, as well as manage other resources, on a search service.

    :ivar data_sources: DataSourcesOperations operations
    :vartype data_sources: azure.search.documents.indexes.v2020_06.operations.DataSourcesOperations
    :ivar indexers: IndexersOperations operations
    :vartype indexers: azure.search.documents.indexes.v2020_06.operations.IndexersOperations
    :ivar skillsets: SkillsetsOperations operations
    :vartype skillsets: azure.search.documents.indexes.v2020_06.operations.SkillsetsOperations
    :ivar synonym_maps: SynonymMapsOperations operations
    :vartype synonym_maps: azure.search.documents.indexes.v2020_06.operations.SynonymMapsOperations
    :ivar indexes: IndexesOperations operations
    :vartype indexes: azure.search.documents.indexes.v2020_06.operations.IndexesOperations
    :param endpoint: The endpoint URL of the search service.
    :type endpoint: str
    """

    def __init__(
        self,
        endpoint,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = '{endpoint}'
        self._config = SearchClientConfiguration(endpoint, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.data_sources = DataSourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.indexers = IndexersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skillsets = SkillsetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.synonym_maps = SynonymMapsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.indexes = IndexesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> SearchClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
