# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._application_insights_management_client_enums import *


class ManagedServiceIdentity(msrest.serialization.Model):
    """Managed service identity (system assigned and/or user assigned identities).

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar principal_id: The service principal ID of the system assigned identity. This property
     will only be provided for a system assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the system assigned identity. This property will only be
     provided for a system assigned identity.
    :vartype tenant_id: str
    :ivar type: Required. Type of managed service identity (where both SystemAssigned and
     UserAssigned types are allowed). Possible values include: "None", "SystemAssigned",
     "UserAssigned", "SystemAssigned,UserAssigned".
    :vartype type: str or
     ~azure.mgmt.applicationinsights.v2021_08_01.models.ManagedServiceIdentityType
    :ivar user_assigned_identities: The set of user assigned identities associated with the
     resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.
     The dictionary values can be empty objects ({}) in requests.
    :vartype user_assigned_identities: dict[str,
     ~azure.mgmt.applicationinsights.v2021_08_01.models.UserAssignedIdentity]
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserAssignedIdentity}'},
    }

    def __init__(
        self,
        *,
        type: Union[str, "ManagedServiceIdentityType"],
        user_assigned_identities: Optional[Dict[str, "UserAssignedIdentity"]] = None,
        **kwargs
    ):
        """
        :keyword type: Required. Type of managed service identity (where both SystemAssigned and
         UserAssigned types are allowed). Possible values include: "None", "SystemAssigned",
         "UserAssigned", "SystemAssigned,UserAssigned".
        :paramtype type: str or
         ~azure.mgmt.applicationinsights.v2021_08_01.models.ManagedServiceIdentityType
        :keyword user_assigned_identities: The set of user assigned identities associated with the
         resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.
         The dictionary values can be empty objects ({}) in requests.
        :paramtype user_assigned_identities: dict[str,
         ~azure.mgmt.applicationinsights.v2021_08_01.models.UserAssignedIdentity]
        """
        super(ManagedServiceIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type
        self.user_assigned_identities = user_assigned_identities


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
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
        """
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Possible values include:
     "User", "Application", "ManagedIdentity", "Key".
    :vartype created_by_type: str or
     ~azure.mgmt.applicationinsights.v2021_08_01.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :vartype last_modified_by_type: str or
     ~azure.mgmt.applicationinsights.v2021_08_01.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
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
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Possible values
         include: "User", "Application", "ManagedIdentity", "Key".
        :paramtype created_by_type: str or
         ~azure.mgmt.applicationinsights.v2021_08_01.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Possible
         values include: "User", "Application", "ManagedIdentity", "Key".
        :paramtype last_modified_by_type: str or
         ~azure.mgmt.applicationinsights.v2021_08_01.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: Required. The geo-location where the resource lives.
    :vartype location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: Required. The geo-location where the resource lives.
        :paramtype location: str
        """
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class UserAssignedIdentity(msrest.serialization.Model):
    """User assigned identity properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of the assigned identity.
    :vartype principal_id: str
    :ivar client_id: The client ID of the assigned identity.
    :vartype client_id: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'client_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(UserAssignedIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.client_id = None


class WorkbookResource(TrackedResource):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: Required. The geo-location where the resource lives.
    :vartype location: str
    :ivar identity: Identity used for BYOS.
    :vartype identity: ~azure.mgmt.applicationinsights.v2021_08_01.models.WorkbookResourceIdentity
    :ivar kind: The kind of workbook. Choices are user and shared. Possible values include: "user",
     "shared".
    :vartype kind: str or ~azure.mgmt.applicationinsights.v2021_08_01.models.Kind
    :ivar etag: Resource etag.
    :vartype etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'WorkbookResourceIdentity'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["WorkbookResourceIdentity"] = None,
        kind: Optional[Union[str, "Kind"]] = None,
        etag: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: Required. The geo-location where the resource lives.
        :paramtype location: str
        :keyword identity: Identity used for BYOS.
        :paramtype identity:
         ~azure.mgmt.applicationinsights.v2021_08_01.models.WorkbookResourceIdentity
        :keyword kind: The kind of workbook. Choices are user and shared. Possible values include:
         "user", "shared".
        :paramtype kind: str or ~azure.mgmt.applicationinsights.v2021_08_01.models.Kind
        :keyword etag: Resource etag.
        :paramtype etag: str
        """
        super(WorkbookResource, self).__init__(tags=tags, location=location, **kwargs)
        self.identity = identity
        self.kind = kind
        self.etag = etag


class Workbook(WorkbookResource):
    """An Application Insights workbook definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: Required. The geo-location where the resource lives.
    :vartype location: str
    :ivar identity: Identity used for BYOS.
    :vartype identity: ~azure.mgmt.applicationinsights.v2021_08_01.models.WorkbookResourceIdentity
    :ivar kind: The kind of workbook. Choices are user and shared. Possible values include: "user",
     "shared".
    :vartype kind: str or ~azure.mgmt.applicationinsights.v2021_08_01.models.Kind
    :ivar etag: Resource etag.
    :vartype etag: str
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.applicationinsights.v2021_08_01.models.SystemData
    :ivar display_name: The user-defined name (display name) of the workbook.
    :vartype display_name: str
    :ivar serialized_data: Configuration of this particular workbook. Configuration data is a
     string containing valid JSON.
    :vartype serialized_data: str
    :ivar version: Workbook schema version format, like 'Notebook/1.0', which should match the
     workbook in serializedData.
    :vartype version: str
    :ivar time_modified: Date and time in UTC of the last modification that was made to this
     workbook definition.
    :vartype time_modified: ~datetime.datetime
    :ivar category: Workbook category, as defined by the user at creation time.
    :vartype category: str
    :ivar tags_properties_tags: Being deprecated, please use the other tags field.
    :vartype tags_properties_tags: list[str]
    :ivar user_id: Unique user id of the specific user that owns this workbook.
    :vartype user_id: str
    :ivar source_id: ResourceId for a source resource.
    :vartype source_id: str
    :ivar storage_uri: The resourceId to the storage account when bring your own storage is used.
    :vartype storage_uri: str
    :ivar description: The description of the workbook.
    :vartype description: str
    :ivar revision: The unique revision id for this workbook definition.
    :vartype revision: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'time_modified': {'readonly': True},
        'user_id': {'readonly': True},
        'revision': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'WorkbookResourceIdentity'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'serialized_data': {'key': 'properties.serializedData', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'iso-8601'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'tags_properties_tags': {'key': 'properties.tags', 'type': '[str]'},
        'user_id': {'key': 'properties.userId', 'type': 'str'},
        'source_id': {'key': 'properties.sourceId', 'type': 'str'},
        'storage_uri': {'key': 'properties.storageUri', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'revision': {'key': 'properties.revision', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["WorkbookResourceIdentity"] = None,
        kind: Optional[Union[str, "Kind"]] = None,
        etag: Optional[str] = None,
        display_name: Optional[str] = None,
        serialized_data: Optional[str] = None,
        version: Optional[str] = None,
        category: Optional[str] = None,
        tags_properties_tags: Optional[List[str]] = None,
        source_id: Optional[str] = None,
        storage_uri: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: Required. The geo-location where the resource lives.
        :paramtype location: str
        :keyword identity: Identity used for BYOS.
        :paramtype identity:
         ~azure.mgmt.applicationinsights.v2021_08_01.models.WorkbookResourceIdentity
        :keyword kind: The kind of workbook. Choices are user and shared. Possible values include:
         "user", "shared".
        :paramtype kind: str or ~azure.mgmt.applicationinsights.v2021_08_01.models.Kind
        :keyword etag: Resource etag.
        :paramtype etag: str
        :keyword display_name: The user-defined name (display name) of the workbook.
        :paramtype display_name: str
        :keyword serialized_data: Configuration of this particular workbook. Configuration data is a
         string containing valid JSON.
        :paramtype serialized_data: str
        :keyword version: Workbook schema version format, like 'Notebook/1.0', which should match the
         workbook in serializedData.
        :paramtype version: str
        :keyword category: Workbook category, as defined by the user at creation time.
        :paramtype category: str
        :keyword tags_properties_tags: Being deprecated, please use the other tags field.
        :paramtype tags_properties_tags: list[str]
        :keyword source_id: ResourceId for a source resource.
        :paramtype source_id: str
        :keyword storage_uri: The resourceId to the storage account when bring your own storage is
         used.
        :paramtype storage_uri: str
        :keyword description: The description of the workbook.
        :paramtype description: str
        """
        super(Workbook, self).__init__(tags=tags, location=location, identity=identity, kind=kind, etag=etag, **kwargs)
        self.system_data = None
        self.display_name = display_name
        self.serialized_data = serialized_data
        self.version = version
        self.time_modified = None
        self.category = category
        self.tags_properties_tags = tags_properties_tags
        self.user_id = None
        self.source_id = source_id
        self.storage_uri = storage_uri
        self.description = description
        self.revision = None


class WorkbookError(msrest.serialization.Model):
    """Error response.

    :ivar error: The error details.
    :vartype error: ~azure.mgmt.applicationinsights.v2021_08_01.models.WorkbookErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'WorkbookErrorDefinition'},
    }

    def __init__(
        self,
        *,
        error: Optional["WorkbookErrorDefinition"] = None,
        **kwargs
    ):
        """
        :keyword error: The error details.
        :paramtype error: ~azure.mgmt.applicationinsights.v2021_08_01.models.WorkbookErrorDefinition
        """
        super(WorkbookError, self).__init__(**kwargs)
        self.error = error


class WorkbookErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar inner_error: Internal error details.
    :vartype inner_error: any
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(WorkbookErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.inner_error = None


class WorkbookInnerErrorTrace(msrest.serialization.Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar trace: detailed error trace.
    :vartype trace: list[str]
    """

    _validation = {
        'trace': {'readonly': True},
    }

    _attribute_map = {
        'trace': {'key': 'trace', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(WorkbookInnerErrorTrace, self).__init__(**kwargs)
        self.trace = None


class WorkbookResourceIdentity(ManagedServiceIdentity):
    """Identity used for BYOS.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar principal_id: The service principal ID of the system assigned identity. This property
     will only be provided for a system assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the system assigned identity. This property will only be
     provided for a system assigned identity.
    :vartype tenant_id: str
    :ivar type: Required. Type of managed service identity (where both SystemAssigned and
     UserAssigned types are allowed). Possible values include: "None", "SystemAssigned",
     "UserAssigned", "SystemAssigned,UserAssigned".
    :vartype type: str or
     ~azure.mgmt.applicationinsights.v2021_08_01.models.ManagedServiceIdentityType
    :ivar user_assigned_identities: The set of user assigned identities associated with the
     resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.
     The dictionary values can be empty objects ({}) in requests.
    :vartype user_assigned_identities: dict[str,
     ~azure.mgmt.applicationinsights.v2021_08_01.models.UserAssignedIdentity]
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserAssignedIdentity}'},
    }

    def __init__(
        self,
        *,
        type: Union[str, "ManagedServiceIdentityType"],
        user_assigned_identities: Optional[Dict[str, "UserAssignedIdentity"]] = None,
        **kwargs
    ):
        """
        :keyword type: Required. Type of managed service identity (where both SystemAssigned and
         UserAssigned types are allowed). Possible values include: "None", "SystemAssigned",
         "UserAssigned", "SystemAssigned,UserAssigned".
        :paramtype type: str or
         ~azure.mgmt.applicationinsights.v2021_08_01.models.ManagedServiceIdentityType
        :keyword user_assigned_identities: The set of user assigned identities associated with the
         resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}.
         The dictionary values can be empty objects ({}) in requests.
        :paramtype user_assigned_identities: dict[str,
         ~azure.mgmt.applicationinsights.v2021_08_01.models.UserAssignedIdentity]
        """
        super(WorkbookResourceIdentity, self).__init__(type=type, user_assigned_identities=user_assigned_identities, **kwargs)


class WorkbooksListResult(msrest.serialization.Model):
    """Workbook list result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: An array of workbooks.
    :vartype value: list[~azure.mgmt.applicationinsights.v2021_08_01.models.Workbook]
    :ivar next_link:
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Workbook]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword next_link:
        :paramtype next_link: str
        """
        super(WorkbooksListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = next_link


class WorkbookUpdateParameters(msrest.serialization.Model):
    """The parameters that can be provided when updating workbook properties properties.

    :ivar kind: The kind of workbook. Choices are user and shared. Possible values include: "user",
     "shared".
    :vartype kind: str or ~azure.mgmt.applicationinsights.v2021_08_01.models.SharedTypeKind
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar display_name: The user-defined name (display name) of the workbook.
    :vartype display_name: str
    :ivar serialized_data: Configuration of this particular workbook. Configuration data is a
     string containing valid JSON.
    :vartype serialized_data: str
    :ivar category: Workbook category, as defined by the user at creation time.
    :vartype category: str
    :ivar tags_properties_tags: A list of 0 or more tags that are associated with this workbook
     definition.
    :vartype tags_properties_tags: list[str]
    :ivar description: The description of the workbook.
    :vartype description: str
    :ivar revision: The unique revision id for this workbook definition.
    :vartype revision: str
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'serialized_data': {'key': 'properties.serializedData', 'type': 'str'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'tags_properties_tags': {'key': 'properties.tags', 'type': '[str]'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'revision': {'key': 'properties.revision', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        kind: Optional[Union[str, "SharedTypeKind"]] = None,
        tags: Optional[Dict[str, str]] = None,
        display_name: Optional[str] = None,
        serialized_data: Optional[str] = None,
        category: Optional[str] = None,
        tags_properties_tags: Optional[List[str]] = None,
        description: Optional[str] = None,
        revision: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword kind: The kind of workbook. Choices are user and shared. Possible values include:
         "user", "shared".
        :paramtype kind: str or ~azure.mgmt.applicationinsights.v2021_08_01.models.SharedTypeKind
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword display_name: The user-defined name (display name) of the workbook.
        :paramtype display_name: str
        :keyword serialized_data: Configuration of this particular workbook. Configuration data is a
         string containing valid JSON.
        :paramtype serialized_data: str
        :keyword category: Workbook category, as defined by the user at creation time.
        :paramtype category: str
        :keyword tags_properties_tags: A list of 0 or more tags that are associated with this workbook
         definition.
        :paramtype tags_properties_tags: list[str]
        :keyword description: The description of the workbook.
        :paramtype description: str
        :keyword revision: The unique revision id for this workbook definition.
        :paramtype revision: str
        """
        super(WorkbookUpdateParameters, self).__init__(**kwargs)
        self.kind = kind
        self.tags = tags
        self.display_name = display_name
        self.serialized_data = serialized_data
        self.category = category
        self.tags_properties_tags = tags_properties_tags
        self.description = description
        self.revision = revision
