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

from .media_job_output_state_change_event_data_py3 import MediaJobOutputStateChangeEventData


class MediaJobOutputFinishedEventData(MediaJobOutputStateChangeEventData):
    """Job output finished event data.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar previous_state: The previous state of the Job. Possible values
     include: 'Canceled', 'Canceling', 'Error', 'Finished', 'Processing',
     'Queued', 'Scheduled'
    :vartype previous_state: str or ~azure.eventgrid.models.JobState
    :param output: Gets the output.
    :type output: ~azure.eventgrid.models.MediaJobOutput
    :param job_correlation_data: Gets the Job correlation data.
    :type job_correlation_data: dict[str, str]
    """

    _validation = {
        'previous_state': {'readonly': True},
    }

    _attribute_map = {
        'previous_state': {'key': 'previousState', 'type': 'JobState'},
        'output': {'key': 'output', 'type': 'MediaJobOutput'},
        'job_correlation_data': {'key': 'jobCorrelationData', 'type': '{str}'},
    }

    def __init__(self, *, output=None, job_correlation_data=None, **kwargs) -> None:
        super(MediaJobOutputFinishedEventData, self).__init__(output=output, job_correlation_data=job_correlation_data, **kwargs)
