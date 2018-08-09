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


class ImagePurchasePlan(Model):
    """Describes the gallery image purchase plan. This is used by marketplace
    images.

    :param name: The plan ID.
    :type name: str
    :param publisher: The publisher ID.
    :type publisher: str
    :param product: The product ID.
    :type product: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, publisher: str=None, product: str=None, **kwargs) -> None:
        super(ImagePurchasePlan, self).__init__(**kwargs)
        self.name = name
        self.publisher = publisher
        self.product = product