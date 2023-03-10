# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2023. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from obp_python.configuration import Configuration


class ProductCollectionJsonTreeV310(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'collection_code': 'str',
        'products': 'list[ProductJsonV310]'
    }

    attribute_map = {
        'collection_code': 'collection_code',
        'products': 'products'
    }

    def __init__(self, collection_code=None, products=None, _configuration=None):  # noqa: E501
        """ProductCollectionJsonTreeV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._collection_code = None
        self._products = None
        self.discriminator = None

        self.collection_code = collection_code
        self.products = products

    @property
    def collection_code(self):
        """Gets the collection_code of this ProductCollectionJsonTreeV310.  # noqa: E501


        :return: The collection_code of this ProductCollectionJsonTreeV310.  # noqa: E501
        :rtype: str
        """
        return self._collection_code

    @collection_code.setter
    def collection_code(self, collection_code):
        """Sets the collection_code of this ProductCollectionJsonTreeV310.


        :param collection_code: The collection_code of this ProductCollectionJsonTreeV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and collection_code is None:
            raise ValueError("Invalid value for `collection_code`, must not be `None`")  # noqa: E501

        self._collection_code = collection_code

    @property
    def products(self):
        """Gets the products of this ProductCollectionJsonTreeV310.  # noqa: E501


        :return: The products of this ProductCollectionJsonTreeV310.  # noqa: E501
        :rtype: list[ProductJsonV310]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ProductCollectionJsonTreeV310.


        :param products: The products of this ProductCollectionJsonTreeV310.  # noqa: E501
        :type: list[ProductJsonV310]
        """
        if self._configuration.client_side_validation and products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProductCollectionJsonTreeV310, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductCollectionJsonTreeV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductCollectionJsonTreeV310):
            return True

        return self.to_dict() != other.to_dict()
