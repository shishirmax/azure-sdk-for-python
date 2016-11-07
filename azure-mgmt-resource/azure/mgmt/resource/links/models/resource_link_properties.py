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

from msrest.serialization import Model


class ResourceLinkProperties(Model):
    """The resource link properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar source_id: The fully qualified source resource Id.
    :vartype source_id: str
    :param target_id: The fully qualified target resource Id. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite.
    :type target_id: str
    :param notes: The resource link notes.
    :type notes: str
    """ 

    _validation = {
        'source_id': {'readonly': True},
        'target_id': {'required': True},
    }

    _attribute_map = {
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'target_id': {'key': 'targetId', 'type': 'str'},
        'notes': {'key': 'notes', 'type': 'str'},
    }

    def __init__(self, target_id, notes=None):
        self.source_id = None
        self.target_id = target_id
        self.notes = notes