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


class TransactionAttributesResponseJson(object):
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
        'transaction_attributes': 'list[TransactionAttributeResponseJson]'
    }

    attribute_map = {
        'transaction_attributes': 'transaction_attributes'
    }

    def __init__(self, transaction_attributes=None, _configuration=None):  # noqa: E501
        """TransactionAttributesResponseJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_attributes = None
        self.discriminator = None

        self.transaction_attributes = transaction_attributes

    @property
    def transaction_attributes(self):
        """Gets the transaction_attributes of this TransactionAttributesResponseJson.  # noqa: E501


        :return: The transaction_attributes of this TransactionAttributesResponseJson.  # noqa: E501
        :rtype: list[TransactionAttributeResponseJson]
        """
        return self._transaction_attributes

    @transaction_attributes.setter
    def transaction_attributes(self, transaction_attributes):
        """Sets the transaction_attributes of this TransactionAttributesResponseJson.


        :param transaction_attributes: The transaction_attributes of this TransactionAttributesResponseJson.  # noqa: E501
        :type: list[TransactionAttributeResponseJson]
        """
        if self._configuration.client_side_validation and transaction_attributes is None:
            raise ValueError("Invalid value for `transaction_attributes`, must not be `None`")  # noqa: E501

        self._transaction_attributes = transaction_attributes

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
        if issubclass(TransactionAttributesResponseJson, dict):
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
        if not isinstance(other, TransactionAttributesResponseJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionAttributesResponseJson):
            return True

        return self.to_dict() != other.to_dict()