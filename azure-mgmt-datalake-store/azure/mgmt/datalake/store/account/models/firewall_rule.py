# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FirewallRule(Model):
    """
    Data Lake Store firewall rule information

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Gets or sets the firewall rule's name.
    :type name: str
    :ivar type: Gets the namespace and type of the firewall Rule.
    :vartype type: str
    :param id: Gets or sets the firewall rule's subscription ID.
    :type id: str
    :param location: Gets or sets the firewall rule's regional location.
    :type location: str
    :param properties: Gets or sets the properties of the firewall rule.
    :type properties: :class:`FirewallRuleProperties
     <azure.mgmt.datalake.store.account.models.FirewallRuleProperties>`
    """ 

    _validation = {
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'FirewallRuleProperties'},
    }

    def __init__(self, name=None, id=None, location=None, properties=None):
        self.name = name
        self.type = None
        self.id = id
        self.location = location
        self.properties = properties
