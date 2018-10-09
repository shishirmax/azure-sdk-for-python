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


class JobError(Model):
    """Details of JobOutput errors.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Error code describing the error. Possible values include:
     'ServiceError', 'ServiceTransientError', 'DownloadNotAccessible',
     'DownloadTransientError', 'UploadNotAccessible', 'UploadTransientError',
     'ConfigurationUnsupported', 'ContentMalformed', 'ContentUnsupported'
    :vartype code: str or ~azure.eventgrid.models.JobErrorCode
    :ivar message: A human-readable language-dependent representation of the
     error.
    :vartype message: str
    :ivar category: Helps with categorization of errors. Possible values
     include: 'Service', 'Download', 'Upload', 'Configuration', 'Content'
    :vartype category: str or ~azure.eventgrid.models.JobErrorCategory
    :ivar retry: Indicates that it may be possible to retry the Job. If retry
     is unsuccessful, please contact Azure support via Azure Portal. Possible
     values include: 'DoNotRetry', 'MayRetry'
    :vartype retry: str or ~azure.eventgrid.models.JobRetry
    :ivar details: An array of details about specific errors that led to this
     reported error.
    :vartype details: list[~azure.eventgrid.models.JobErrorDetail]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'category': {'readonly': True},
        'retry': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'JobErrorCode'},
        'message': {'key': 'message', 'type': 'str'},
        'category': {'key': 'category', 'type': 'JobErrorCategory'},
        'retry': {'key': 'retry', 'type': 'JobRetry'},
        'details': {'key': 'details', 'type': '[JobErrorDetail]'},
    }

    def __init__(self, **kwargs) -> None:
        super(JobError, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.category = None
        self.retry = None
        self.details = None
