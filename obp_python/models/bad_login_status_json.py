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


class BadLoginStatusJson(object):
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
        'username': 'str',
        'bad_attempts_since_last_success_or_reset': 'int',
        'last_failure_date': 'date'
    }

    attribute_map = {
        'username': 'username',
        'bad_attempts_since_last_success_or_reset': 'bad_attempts_since_last_success_or_reset',
        'last_failure_date': 'last_failure_date'
    }

    def __init__(self, username=None, bad_attempts_since_last_success_or_reset=None, last_failure_date=None, _configuration=None):  # noqa: E501
        """BadLoginStatusJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._username = None
        self._bad_attempts_since_last_success_or_reset = None
        self._last_failure_date = None
        self.discriminator = None

        self.username = username
        self.bad_attempts_since_last_success_or_reset = bad_attempts_since_last_success_or_reset
        self.last_failure_date = last_failure_date

    @property
    def username(self):
        """Gets the username of this BadLoginStatusJson.  # noqa: E501


        :return: The username of this BadLoginStatusJson.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this BadLoginStatusJson.


        :param username: The username of this BadLoginStatusJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def bad_attempts_since_last_success_or_reset(self):
        """Gets the bad_attempts_since_last_success_or_reset of this BadLoginStatusJson.  # noqa: E501


        :return: The bad_attempts_since_last_success_or_reset of this BadLoginStatusJson.  # noqa: E501
        :rtype: int
        """
        return self._bad_attempts_since_last_success_or_reset

    @bad_attempts_since_last_success_or_reset.setter
    def bad_attempts_since_last_success_or_reset(self, bad_attempts_since_last_success_or_reset):
        """Sets the bad_attempts_since_last_success_or_reset of this BadLoginStatusJson.


        :param bad_attempts_since_last_success_or_reset: The bad_attempts_since_last_success_or_reset of this BadLoginStatusJson.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and bad_attempts_since_last_success_or_reset is None:
            raise ValueError("Invalid value for `bad_attempts_since_last_success_or_reset`, must not be `None`")  # noqa: E501

        self._bad_attempts_since_last_success_or_reset = bad_attempts_since_last_success_or_reset

    @property
    def last_failure_date(self):
        """Gets the last_failure_date of this BadLoginStatusJson.  # noqa: E501


        :return: The last_failure_date of this BadLoginStatusJson.  # noqa: E501
        :rtype: date
        """
        return self._last_failure_date

    @last_failure_date.setter
    def last_failure_date(self, last_failure_date):
        """Sets the last_failure_date of this BadLoginStatusJson.


        :param last_failure_date: The last_failure_date of this BadLoginStatusJson.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and last_failure_date is None:
            raise ValueError("Invalid value for `last_failure_date`, must not be `None`")  # noqa: E501

        self._last_failure_date = last_failure_date

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
        if issubclass(BadLoginStatusJson, dict):
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
        if not isinstance(other, BadLoginStatusJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BadLoginStatusJson):
            return True

        return self.to_dict() != other.to_dict()