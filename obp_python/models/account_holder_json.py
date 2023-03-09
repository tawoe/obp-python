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


class AccountHolderJSON(object):
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
        'is_alias': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_alias': 'is_alias'
    }

    def __init__(self, name=None, is_alias=None, _configuration=None):  # noqa: E501
        """AccountHolderJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._is_alias = None
        self.discriminator = None

        self.name = name
        self.is_alias = is_alias

    @property
    def name(self):
        """Gets the name of this AccountHolderJSON.  # noqa: E501


        :return: The name of this AccountHolderJSON.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountHolderJSON.


        :param name: The name of this AccountHolderJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_alias(self):
        """Gets the is_alias of this AccountHolderJSON.  # noqa: E501


        :return: The is_alias of this AccountHolderJSON.  # noqa: E501
        :rtype: bool
        """
        return self._is_alias

    @is_alias.setter
    def is_alias(self, is_alias):
        """Sets the is_alias of this AccountHolderJSON.


        :param is_alias: The is_alias of this AccountHolderJSON.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_alias is None:
            raise ValueError("Invalid value for `is_alias`, must not be `None`")  # noqa: E501

        self._is_alias = is_alias

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
        if issubclass(AccountHolderJSON, dict):
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
        if not isinstance(other, AccountHolderJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountHolderJSON):
            return True

        return self.to_dict() != other.to_dict()
