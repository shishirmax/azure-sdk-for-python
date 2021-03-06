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


class WorkloadItem(Model):
    """Base class for backup item. Workload-specific backup items are derived from
    this class.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureVmWorkloadItem

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup managemenent to backup an
     item.
    :type backup_management_type: str
    :param workload_type: Type of workload for the backup management
    :type workload_type: str
    :param friendly_name: Friendly name of the backup item.
    :type friendly_name: str
    :param protection_state: State of the back up item. Possible values
     include: 'Invalid', 'NotProtected', 'Protecting', 'Protected',
     'ProtectionFailed'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionStatus
    :param workload_item_type: Required. Constant filled by server.
    :type workload_item_type: str
    """

    _validation = {
        'workload_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'workload_item_type': {'key': 'workloadItemType', 'type': 'str'},
    }

    _subtype_map = {
        'workload_item_type': {'AzureVmWorkloadItem': 'AzureVmWorkloadItem'}
    }

    def __init__(self, *, backup_management_type: str=None, workload_type: str=None, friendly_name: str=None, protection_state=None, **kwargs) -> None:
        super(WorkloadItem, self).__init__(**kwargs)
        self.backup_management_type = backup_management_type
        self.workload_type = workload_type
        self.friendly_name = friendly_name
        self.protection_state = protection_state
        self.workload_item_type = None
