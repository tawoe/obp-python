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


class XxxId(object):
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
        'type': 'str',
        'min_length': 'int',
        'max_length': 'int',
        'examples': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'min_length': 'minLength',
        'max_length': 'maxLength',
        'examples': 'examples'
    }

    def __init__(self, type=None, min_length=None, max_length=None, examples=None, _configuration=None):  # noqa: E501
        """XxxId - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._min_length = None
        self._max_length = None
        self._examples = None
        self.discriminator = None

        self.type = type
        self.min_length = min_length
        self.max_length = max_length
        self.examples = examples

    @property
    def type(self):
        """Gets the type of this XxxId.  # noqa: E501


        :return: The type of this XxxId.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XxxId.


        :param type: The type of this XxxId.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def min_length(self):
        """Gets the min_length of this XxxId.  # noqa: E501


        :return: The min_length of this XxxId.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this XxxId.


        :param min_length: The min_length of this XxxId.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and min_length is None:
            raise ValueError("Invalid value for `min_length`, must not be `None`")  # noqa: E501

        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this XxxId.  # noqa: E501


        :return: The max_length of this XxxId.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this XxxId.


        :param max_length: The max_length of this XxxId.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and max_length is None:
            raise ValueError("Invalid value for `max_length`, must not be `None`")  # noqa: E501

        self._max_length = max_length

    @property
    def examples(self):
        """Gets the examples of this XxxId.  # noqa: E501


        :return: The examples of this XxxId.  # noqa: E501
        :rtype: list[str]
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """Sets the examples of this XxxId.


        :param examples: The examples of this XxxId.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and examples is None:
            raise ValueError("Invalid value for `examples`, must not be `None`")  # noqa: E501

        self._examples = examples

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
        if issubclass(XxxId, dict):
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
        if not isinstance(other, XxxId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XxxId):
            return True

        return self.to_dict() != other.to_dict()
