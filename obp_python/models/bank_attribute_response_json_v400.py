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


class BankAttributeResponseJsonV400(object):
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
        'name': 'str',
        'is_active': 'bool',
        'bank_attribute_id': 'str',
        'bank_id': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_active': 'is_active',
        'bank_attribute_id': 'bank_attribute_id',
        'bank_id': 'bank_id',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, name=None, is_active=None, bank_attribute_id=None, bank_id=None, type=None, value=None, _configuration=None):  # noqa: E501
        """BankAttributeResponseJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._is_active = None
        self._bank_attribute_id = None
        self._bank_id = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.name = name
        if is_active is not None:
            self.is_active = is_active
        self.bank_attribute_id = bank_attribute_id
        self.bank_id = bank_id
        self.type = type
        self.value = value

    @property
    def name(self):
        """Gets the name of this BankAttributeResponseJsonV400.  # noqa: E501


        :return: The name of this BankAttributeResponseJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankAttributeResponseJsonV400.


        :param name: The name of this BankAttributeResponseJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_active(self):
        """Gets the is_active of this BankAttributeResponseJsonV400.  # noqa: E501


        :return: The is_active of this BankAttributeResponseJsonV400.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this BankAttributeResponseJsonV400.


        :param is_active: The is_active of this BankAttributeResponseJsonV400.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def bank_attribute_id(self):
        """Gets the bank_attribute_id of this BankAttributeResponseJsonV400.  # noqa: E501


        :return: The bank_attribute_id of this BankAttributeResponseJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._bank_attribute_id

    @bank_attribute_id.setter
    def bank_attribute_id(self, bank_attribute_id):
        """Sets the bank_attribute_id of this BankAttributeResponseJsonV400.


        :param bank_attribute_id: The bank_attribute_id of this BankAttributeResponseJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_attribute_id is None:
            raise ValueError("Invalid value for `bank_attribute_id`, must not be `None`")  # noqa: E501

        self._bank_attribute_id = bank_attribute_id

    @property
    def bank_id(self):
        """Gets the bank_id of this BankAttributeResponseJsonV400.  # noqa: E501


        :return: The bank_id of this BankAttributeResponseJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this BankAttributeResponseJsonV400.


        :param bank_id: The bank_id of this BankAttributeResponseJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def type(self):
        """Gets the type of this BankAttributeResponseJsonV400.  # noqa: E501


        :return: The type of this BankAttributeResponseJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankAttributeResponseJsonV400.


        :param type: The type of this BankAttributeResponseJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this BankAttributeResponseJsonV400.  # noqa: E501


        :return: The value of this BankAttributeResponseJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BankAttributeResponseJsonV400.


        :param value: The value of this BankAttributeResponseJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(BankAttributeResponseJsonV400, dict):
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
        if not isinstance(other, BankAttributeResponseJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankAttributeResponseJsonV400):
            return True

        return self.to_dict() != other.to_dict()
