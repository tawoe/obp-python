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


class TransactionRequestTypesJsonV140(object):
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
        'transaction_request_types': 'list[TransactionRequestTypeJsonV140]'
    }

    attribute_map = {
        'transaction_request_types': 'transaction_request_types'
    }

    def __init__(self, transaction_request_types=None, _configuration=None):  # noqa: E501
        """TransactionRequestTypesJsonV140 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_request_types = None
        self.discriminator = None

        self.transaction_request_types = transaction_request_types

    @property
    def transaction_request_types(self):
        """Gets the transaction_request_types of this TransactionRequestTypesJsonV140.  # noqa: E501


        :return: The transaction_request_types of this TransactionRequestTypesJsonV140.  # noqa: E501
        :rtype: list[TransactionRequestTypeJsonV140]
        """
        return self._transaction_request_types

    @transaction_request_types.setter
    def transaction_request_types(self, transaction_request_types):
        """Sets the transaction_request_types of this TransactionRequestTypesJsonV140.


        :param transaction_request_types: The transaction_request_types of this TransactionRequestTypesJsonV140.  # noqa: E501
        :type: list[TransactionRequestTypeJsonV140]
        """
        if self._configuration.client_side_validation and transaction_request_types is None:
            raise ValueError("Invalid value for `transaction_request_types`, must not be `None`")  # noqa: E501

        self._transaction_request_types = transaction_request_types

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
        if issubclass(TransactionRequestTypesJsonV140, dict):
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
        if not isinstance(other, TransactionRequestTypesJsonV140):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionRequestTypesJsonV140):
            return True

        return self.to_dict() != other.to_dict()
