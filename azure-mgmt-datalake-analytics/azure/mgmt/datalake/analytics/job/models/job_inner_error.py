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


class JobInnerError(Model):
    """
    The Data Lake Analytics job error details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar diagnostic_code: Gets the diagnostic error code.
    :vartype diagnostic_code: int
    :ivar severity: Gets the severity level of the failure. Possible values
     include: 'Warning', 'Error'
    :vartype severity: str
    :ivar details: Gets the details of the error message.
    :vartype details: str
    :ivar component: Gets the component that failed.
    :vartype component: str
    :ivar error_id: Gets the specific identifier for the type of error
     encountered in the job.
    :vartype error_id: str
    :ivar help_link: Gets the link to MSDN or Azure help for this type of
     error, if any.
    :vartype help_link: str
    :ivar internal_diagnostics: Gets the internal diagnostic stack trace if
     the user requesting the job error details has sufficient permissions it
     will be retrieved, otherwise it will be empty.
    :vartype internal_diagnostics: str
    :ivar message: Gets the user friendly error message for the failure.
    :vartype message: str
    :ivar resolution: Gets the recommended resolution for the failure, if any.
    :vartype resolution: str
    :ivar source: Gets the ultimate source of the failure (usually either
     SYSTEM or USER).
    :vartype source: str
    :ivar description: Gets the error message description
    :vartype description: str
    """ 

    _validation = {
        'diagnostic_code': {'readonly': True},
        'severity': {'readonly': True},
        'details': {'readonly': True},
        'component': {'readonly': True},
        'error_id': {'readonly': True},
        'help_link': {'readonly': True},
        'internal_diagnostics': {'readonly': True},
        'message': {'readonly': True},
        'resolution': {'readonly': True},
        'source': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'diagnostic_code': {'key': 'diagnosticCode', 'type': 'int'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'details': {'key': 'details', 'type': 'str'},
        'component': {'key': 'component', 'type': 'str'},
        'error_id': {'key': 'errorId', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'internal_diagnostics': {'key': 'internalDiagnostics', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self):
        self.diagnostic_code = None
        self.severity = None
        self.details = None
        self.component = None
        self.error_id = None
        self.help_link = None
        self.internal_diagnostics = None
        self.message = None
        self.resolution = None
        self.source = None
        self.description = None
