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


class TransactionRequestBodyJsonV200(object):
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
        'to': 'TransactionRequestAccountJsonV140',
        'value': 'AmountOfMoneyJsonV121',
        'description': 'str'
    }

    attribute_map = {
        'to': 'to',
        'value': 'value',
        'description': 'description'
    }

    def __init__(self, to=None, value=None, description=None, _configuration=None):  # noqa: E501
        """TransactionRequestBodyJsonV200 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._to = None
        self._value = None
        self._description = None
        self.discriminator = None

        self.to = to
        self.value = value
        self.description = description

    @property
    def to(self):
        """Gets the to of this TransactionRequestBodyJsonV200.  # noqa: E501


        :return: The to of this TransactionRequestBodyJsonV200.  # noqa: E501
        :rtype: TransactionRequestAccountJsonV140
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this TransactionRequestBodyJsonV200.


        :param to: The to of this TransactionRequestBodyJsonV200.  # noqa: E501
        :type: TransactionRequestAccountJsonV140
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def value(self):
        """Gets the value of this TransactionRequestBodyJsonV200.  # noqa: E501


        :return: The value of this TransactionRequestBodyJsonV200.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransactionRequestBodyJsonV200.


        :param value: The value of this TransactionRequestBodyJsonV200.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def description(self):
        """Gets the description of this TransactionRequestBodyJsonV200.  # noqa: E501


        :return: The description of this TransactionRequestBodyJsonV200.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionRequestBodyJsonV200.


        :param description: The description of this TransactionRequestBodyJsonV200.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

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
        if issubclass(TransactionRequestBodyJsonV200, dict):
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
        if not isinstance(other, TransactionRequestBodyJsonV200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionRequestBodyJsonV200):
            return True

        return self.to_dict() != other.to_dict()
