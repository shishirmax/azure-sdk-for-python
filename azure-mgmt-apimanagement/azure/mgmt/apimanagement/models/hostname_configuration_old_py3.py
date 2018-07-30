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


class HostnameConfigurationOld(Model):
    """Custom hostname configuration.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Hostname type. Possible values include: 'Proxy',
     'Portal', 'Management', 'Scm'
    :type type: str or ~azure.mgmt.apimanagement.models.HostnameType
    :param hostname: Required. Hostname to configure.
    :type hostname: str
    :param certificate: Required. Certificate information.
    :type certificate: ~azure.mgmt.apimanagement.models.CertificateInformation
    """

    _validation = {
        'type': {'required': True},
        'hostname': {'required': True},
        'certificate': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'HostnameType'},
        'hostname': {'key': 'hostname', 'type': 'str'},
        'certificate': {'key': 'certificate', 'type': 'CertificateInformation'},
    }

    def __init__(self, *, type, hostname: str, certificate, **kwargs) -> None:
        super(HostnameConfigurationOld, self).__init__(**kwargs)
        self.type = type
        self.hostname = hostname
        self.certificate = certificate