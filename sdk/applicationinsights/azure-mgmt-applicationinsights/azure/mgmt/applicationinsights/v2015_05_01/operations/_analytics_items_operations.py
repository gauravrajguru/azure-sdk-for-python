# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    scope_path: Union[str, "_models.ItemScopePath"],
    *,
    scope: Optional[Union[str, "_models.ItemScope"]] = None,
    type: Optional[Union[str, "_models.ItemTypeParameter"]] = "none",
    include_content: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2015-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "scopePath": _SERIALIZER.url("scope_path", scope_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if scope is not None:
        query_parameters['scope'] = _SERIALIZER.query("scope", scope, 'str')
    if type is not None:
        query_parameters['type'] = _SERIALIZER.query("type", type, 'str')
    if include_content is not None:
        query_parameters['includeContent'] = _SERIALIZER.query("include_content", include_content, 'bool')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    scope_path: Union[str, "_models.ItemScopePath"],
    *,
    id: Optional[str] = None,
    name: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2015-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "scopePath": _SERIALIZER.url("scope_path", scope_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if id is not None:
        query_parameters['id'] = _SERIALIZER.query("id", id, 'str')
    if name is not None:
        query_parameters['name'] = _SERIALIZER.query("name", name, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_put_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    scope_path: Union[str, "_models.ItemScopePath"],
    *,
    json: JSONType = None,
    content: Any = None,
    override_item: Optional[bool] = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2015-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "scopePath": _SERIALIZER.url("scope_path", scope_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if override_item is not None:
        query_parameters['overrideItem'] = _SERIALIZER.query("override_item", override_item, 'bool')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_delete_request(
    subscription_id: str,
    resource_group_name: str,
    resource_name: str,
    scope_path: Union[str, "_models.ItemScopePath"],
    *,
    id: Optional[str] = None,
    name: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2015-05-01"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, 'str'),
        "scopePath": _SERIALIZER.url("scope_path", scope_path, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if id is not None:
        query_parameters['id'] = _SERIALIZER.query("id", id, 'str')
    if name is not None:
        query_parameters['name'] = _SERIALIZER.query("name", name, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        **kwargs
    )

class AnalyticsItemsOperations(object):
    """AnalyticsItemsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.applicationinsights.v2015_05_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        resource_name: str,
        scope_path: Union[str, "_models.ItemScopePath"],
        scope: Optional[Union[str, "_models.ItemScope"]] = None,
        type: Optional[Union[str, "_models.ItemTypeParameter"]] = "none",
        include_content: Optional[bool] = None,
        **kwargs: Any
    ) -> List["_models.ApplicationInsightsComponentAnalyticsItem"]:
        """Gets a list of Analytics Items defined within an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by a specific user or is
         shared between all users with access to the Application Insights component.
        :type scope_path: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.ItemScopePath
        :param scope: Enum indicating if this item definition is owned by a specific user or is shared
         between all users with access to the Application Insights component.
        :type scope: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.ItemScope
        :param type: Enum indicating the type of the Analytics item.
        :type type: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.ItemTypeParameter
        :param include_content: Flag indicating whether or not to return the content of each applicable
         item. If false, only return the item information.
        :type include_content: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ApplicationInsightsComponentAnalyticsItem, or the result of cls(response)
        :rtype:
         list[~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentAnalyticsItem]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.ApplicationInsightsComponentAnalyticsItem"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_list_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            scope_path=scope_path,
            scope=scope,
            type=type,
            include_content=include_content,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[ApplicationInsightsComponentAnalyticsItem]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        resource_name: str,
        scope_path: Union[str, "_models.ItemScopePath"],
        id: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentAnalyticsItem":
        """Gets a specific Analytics Items defined within an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by a specific user or is
         shared between all users with access to the Application Insights component.
        :type scope_path: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.ItemScopePath
        :param id: The Id of a specific item defined in the Application Insights component.
        :type id: str
        :param name: The name of a specific item defined in the Application Insights component.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentAnalyticsItem, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentAnalyticsItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentAnalyticsItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            scope_path=scope_path,
            id=id,
            name=name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentAnalyticsItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item'}  # type: ignore


    @distributed_trace
    def put(
        self,
        resource_group_name: str,
        resource_name: str,
        scope_path: Union[str, "_models.ItemScopePath"],
        item_properties: "_models.ApplicationInsightsComponentAnalyticsItem",
        override_item: Optional[bool] = None,
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentAnalyticsItem":
        """Adds or Updates a specific Analytics Item within an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by a specific user or is
         shared between all users with access to the Application Insights component.
        :type scope_path: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.ItemScopePath
        :param item_properties: Properties that need to be specified to create a new item and add it to
         an Application Insights component.
        :type item_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentAnalyticsItem
        :param override_item: Flag indicating whether or not to force save an item. This allows
         overriding an item if it already exists.
        :type override_item: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentAnalyticsItem, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentAnalyticsItem
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentAnalyticsItem"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(item_properties, 'ApplicationInsightsComponentAnalyticsItem')

        request = build_put_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            scope_path=scope_path,
            content_type=content_type,
            json=_json,
            override_item=override_item,
            template_url=self.put.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentAnalyticsItem', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        resource_name: str,
        scope_path: Union[str, "_models.ItemScopePath"],
        id: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Deletes a specific Analytics Items defined within an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param scope_path: Enum indicating if this item definition is owned by a specific user or is
         shared between all users with access to the Application Insights component.
        :type scope_path: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.ItemScopePath
        :param id: The Id of a specific item defined in the Application Insights component.
        :type id: str
        :param name: The name of a specific item defined in the Application Insights component.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            scope_path=scope_path,
            id=id,
            name=name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item'}  # type: ignore

