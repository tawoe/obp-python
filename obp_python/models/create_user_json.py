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


class CreateUserJson(object):
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
        'first_name': 'str',
        'email': 'str',
        'username': 'str',
        'last_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'email': 'email',
        'username': 'username',
        'last_name': 'last_name',
        'password': 'password'
    }

    def __init__(self, first_name=None, email=None, username=None, last_name=None, password=None, _configuration=None):  # noqa: E501
        """CreateUserJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._email = None
        self._username = None
        self._last_name = None
        self._password = None
        self.discriminator = None

        self.first_name = first_name
        self.email = email
        self.username = username
        self.last_name = last_name
        self.password = password

    @property
    def first_name(self):
        """Gets the first_name of this CreateUserJson.  # noqa: E501


        :return: The first_name of this CreateUserJson.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreateUserJson.


        :param first_name: The first_name of this CreateUserJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def email(self):
        """Gets the email of this CreateUserJson.  # noqa: E501


        :return: The email of this CreateUserJson.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserJson.


        :param email: The email of this CreateUserJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def username(self):
        """Gets the username of this CreateUserJson.  # noqa: E501


        :return: The username of this CreateUserJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateUserJson.


        :param username: The username of this CreateUserJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def last_name(self):
        """Gets the last_name of this CreateUserJson.  # noqa: E501


        :return: The last_name of this CreateUserJson.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreateUserJson.


        :param last_name: The last_name of this CreateUserJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def password(self):
        """Gets the password of this CreateUserJson.  # noqa: E501


        :return: The password of this CreateUserJson.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateUserJson.


        :param password: The password of this CreateUserJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

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
        if issubclass(CreateUserJson, dict):
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
        if not isinstance(other, CreateUserJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUserJson):
            return True

        return self.to_dict() != other.to_dict()
