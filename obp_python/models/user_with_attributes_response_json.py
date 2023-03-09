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


class UserWithAttributesResponseJson(object):
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
        'provider': 'str',
        'email': 'str',
        'username': 'str',
        'provider_id': 'str',
        'user_id': 'str',
        'user_attributes': 'list[UserAttributeResponseJsonV400]'
    }

    attribute_map = {
        'provider': 'provider',
        'email': 'email',
        'username': 'username',
        'provider_id': 'provider_id',
        'user_id': 'user_id',
        'user_attributes': 'user_attributes'
    }

    def __init__(self, provider=None, email=None, username=None, provider_id=None, user_id=None, user_attributes=None, _configuration=None):  # noqa: E501
        """UserWithAttributesResponseJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._provider = None
        self._email = None
        self._username = None
        self._provider_id = None
        self._user_id = None
        self._user_attributes = None
        self.discriminator = None

        self.provider = provider
        self.email = email
        self.username = username
        self.provider_id = provider_id
        self.user_id = user_id
        self.user_attributes = user_attributes

    @property
    def provider(self):
        """Gets the provider of this UserWithAttributesResponseJson.  # noqa: E501


        :return: The provider of this UserWithAttributesResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this UserWithAttributesResponseJson.


        :param provider: The provider of this UserWithAttributesResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def email(self):
        """Gets the email of this UserWithAttributesResponseJson.  # noqa: E501


        :return: The email of this UserWithAttributesResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserWithAttributesResponseJson.


        :param email: The email of this UserWithAttributesResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def username(self):
        """Gets the username of this UserWithAttributesResponseJson.  # noqa: E501


        :return: The username of this UserWithAttributesResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserWithAttributesResponseJson.


        :param username: The username of this UserWithAttributesResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def provider_id(self):
        """Gets the provider_id of this UserWithAttributesResponseJson.  # noqa: E501


        :return: The provider_id of this UserWithAttributesResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this UserWithAttributesResponseJson.


        :param provider_id: The provider_id of this UserWithAttributesResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def user_id(self):
        """Gets the user_id of this UserWithAttributesResponseJson.  # noqa: E501


        :return: The user_id of this UserWithAttributesResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserWithAttributesResponseJson.


        :param user_id: The user_id of this UserWithAttributesResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def user_attributes(self):
        """Gets the user_attributes of this UserWithAttributesResponseJson.  # noqa: E501


        :return: The user_attributes of this UserWithAttributesResponseJson.  # noqa: E501
        :rtype: list[UserAttributeResponseJsonV400]
        """
        return self._user_attributes

    @user_attributes.setter
    def user_attributes(self, user_attributes):
        """Sets the user_attributes of this UserWithAttributesResponseJson.


        :param user_attributes: The user_attributes of this UserWithAttributesResponseJson.  # noqa: E501
        :type: list[UserAttributeResponseJsonV400]
        """
        if self._configuration.client_side_validation and user_attributes is None:
            raise ValueError("Invalid value for `user_attributes`, must not be `None`")  # noqa: E501

        self._user_attributes = user_attributes

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
        if issubclass(UserWithAttributesResponseJson, dict):
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
        if not isinstance(other, UserWithAttributesResponseJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserWithAttributesResponseJson):
            return True

        return self.to_dict() != other.to_dict()
