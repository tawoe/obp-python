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


class JsonDynamicResourceDocExampleRequestBody(object):
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
        'age': 'int',
        'hobby': 'list[str]',
        'optional_fields_': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'age': 'age',
        'hobby': 'hobby',
        'optional_fields_': '_optional_fields_'
    }

    def __init__(self, name=None, age=None, hobby=None, optional_fields_=None, _configuration=None):  # noqa: E501
        """JsonDynamicResourceDocExampleRequestBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._age = None
        self._hobby = None
        self._optional_fields_ = None
        self.discriminator = None

        self.name = name
        self.age = age
        self.hobby = hobby
        self.optional_fields_ = optional_fields_

    @property
    def name(self):
        """Gets the name of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501


        :return: The name of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonDynamicResourceDocExampleRequestBody.


        :param name: The name of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def age(self):
        """Gets the age of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501


        :return: The age of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this JsonDynamicResourceDocExampleRequestBody.


        :param age: The age of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and age is None:
            raise ValueError("Invalid value for `age`, must not be `None`")  # noqa: E501

        self._age = age

    @property
    def hobby(self):
        """Gets the hobby of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501


        :return: The hobby of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._hobby

    @hobby.setter
    def hobby(self, hobby):
        """Sets the hobby of this JsonDynamicResourceDocExampleRequestBody.


        :param hobby: The hobby of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and hobby is None:
            raise ValueError("Invalid value for `hobby`, must not be `None`")  # noqa: E501

        self._hobby = hobby

    @property
    def optional_fields_(self):
        """Gets the optional_fields_ of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501


        :return: The optional_fields_ of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._optional_fields_

    @optional_fields_.setter
    def optional_fields_(self, optional_fields_):
        """Sets the optional_fields_ of this JsonDynamicResourceDocExampleRequestBody.


        :param optional_fields_: The optional_fields_ of this JsonDynamicResourceDocExampleRequestBody.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and optional_fields_ is None:
            raise ValueError("Invalid value for `optional_fields_`, must not be `None`")  # noqa: E501

        self._optional_fields_ = optional_fields_

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
        if issubclass(JsonDynamicResourceDocExampleRequestBody, dict):
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
        if not isinstance(other, JsonDynamicResourceDocExampleRequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonDynamicResourceDocExampleRequestBody):
            return True

        return self.to_dict() != other.to_dict()
