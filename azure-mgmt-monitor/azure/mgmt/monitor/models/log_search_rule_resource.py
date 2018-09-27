# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class LogSearchRuleResource(Resource):
    """The Log Search Rule resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param description: The description of the Log Search rule.
    :type description: str
    :param enabled: The flag which indicates whether the Log Search rule is
     enabled. Value should be true or false. Possible values include: 'true',
     'false'
    :type enabled: str or ~azure.mgmt.monitor.models.Enabled
    :ivar last_updated_time: Last time the rule was updated in IS08601 format.
    :vartype last_updated_time: datetime
    :ivar provisioning_state: Provisioning state of the scheduledquery rule.
     Possible values include: 'Succeeded', 'Deploying', 'Canceled', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.monitor.models.ProvisioningState
    :param source: Required. Data Source against which rule will Query Data
    :type source: ~azure.mgmt.monitor.models.Source
    :param schedule: Schedule (Frequnecy, Time Window) for rule. Required for
     action type - AlertingAction
    :type schedule: ~azure.mgmt.monitor.models.Schedule
    :param action: Required. Action needs to be taken on rule execution.
    :type action: ~azure.mgmt.monitor.models.Action
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'last_updated_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'source': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'str'},
        'last_updated_time': {'key': 'properties.lastUpdatedTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'source': {'key': 'properties.source', 'type': 'Source'},
        'schedule': {'key': 'properties.schedule', 'type': 'Schedule'},
        'action': {'key': 'properties.action', 'type': 'Action'},
    }

    def __init__(self, **kwargs):
        super(LogSearchRuleResource, self).__init__(**kwargs)
        self.description = kwargs.get('description', None)
        self.enabled = kwargs.get('enabled', None)
        self.last_updated_time = None
        self.provisioning_state = None
        self.source = kwargs.get('source', None)
        self.schedule = kwargs.get('schedule', None)
        self.action = kwargs.get('action', None)
