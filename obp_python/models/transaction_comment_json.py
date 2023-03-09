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


class TransactionCommentJSON(object):
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
        'id': 'str',
        'value': 'str',
        '_date': 'date',
        'user': 'UserJSONV121'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value',
        '_date': 'date',
        'user': 'user'
    }

    def __init__(self, id=None, value=None, _date=None, user=None, _configuration=None):  # noqa: E501
        """TransactionCommentJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._value = None
        self.__date = None
        self._user = None
        self.discriminator = None

        self.id = id
        self.value = value
        self._date = _date
        self.user = user

    @property
    def id(self):
        """Gets the id of this TransactionCommentJSON.  # noqa: E501


        :return: The id of this TransactionCommentJSON.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionCommentJSON.


        :param id: The id of this TransactionCommentJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def value(self):
        """Gets the value of this TransactionCommentJSON.  # noqa: E501


        :return: The value of this TransactionCommentJSON.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransactionCommentJSON.


        :param value: The value of this TransactionCommentJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def _date(self):
        """Gets the _date of this TransactionCommentJSON.  # noqa: E501


        :return: The _date of this TransactionCommentJSON.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TransactionCommentJSON.


        :param _date: The _date of this TransactionCommentJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def user(self):
        """Gets the user of this TransactionCommentJSON.  # noqa: E501


        :return: The user of this TransactionCommentJSON.  # noqa: E501
        :rtype: UserJSONV121
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TransactionCommentJSON.


        :param user: The user of this TransactionCommentJSON.  # noqa: E501
        :type: UserJSONV121
        """
        if self._configuration.client_side_validation and user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(TransactionCommentJSON, dict):
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
        if not isinstance(other, TransactionCommentJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionCommentJSON):
            return True

        return self.to_dict() != other.to_dict()
