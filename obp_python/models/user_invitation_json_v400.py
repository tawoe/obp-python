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


class UserInvitationJsonV400(object):
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
        'country': 'str',
        'purpose': 'str',
        'company': 'str',
        'last_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'first_name': 'first_name',
        'email': 'email',
        'country': 'country',
        'purpose': 'purpose',
        'company': 'company',
        'last_name': 'last_name',
        'status': 'status'
    }

    def __init__(self, first_name=None, email=None, country=None, purpose=None, company=None, last_name=None, status=None, _configuration=None):  # noqa: E501
        """UserInvitationJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_name = None
        self._email = None
        self._country = None
        self._purpose = None
        self._company = None
        self._last_name = None
        self._status = None
        self.discriminator = None

        self.first_name = first_name
        self.email = email
        self.country = country
        self.purpose = purpose
        self.company = company
        self.last_name = last_name
        self.status = status

    @property
    def first_name(self):
        """Gets the first_name of this UserInvitationJsonV400.  # noqa: E501


        :return: The first_name of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserInvitationJsonV400.


        :param first_name: The first_name of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def email(self):
        """Gets the email of this UserInvitationJsonV400.  # noqa: E501


        :return: The email of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInvitationJsonV400.


        :param email: The email of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def country(self):
        """Gets the country of this UserInvitationJsonV400.  # noqa: E501


        :return: The country of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UserInvitationJsonV400.


        :param country: The country of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def purpose(self):
        """Gets the purpose of this UserInvitationJsonV400.  # noqa: E501


        :return: The purpose of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this UserInvitationJsonV400.


        :param purpose: The purpose of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and purpose is None:
            raise ValueError("Invalid value for `purpose`, must not be `None`")  # noqa: E501

        self._purpose = purpose

    @property
    def company(self):
        """Gets the company of this UserInvitationJsonV400.  # noqa: E501


        :return: The company of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UserInvitationJsonV400.


        :param company: The company of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def last_name(self):
        """Gets the last_name of this UserInvitationJsonV400.  # noqa: E501


        :return: The last_name of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserInvitationJsonV400.


        :param last_name: The last_name of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def status(self):
        """Gets the status of this UserInvitationJsonV400.  # noqa: E501


        :return: The status of this UserInvitationJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserInvitationJsonV400.


        :param status: The status of this UserInvitationJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(UserInvitationJsonV400, dict):
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
        if not isinstance(other, UserInvitationJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserInvitationJsonV400):
            return True

        return self.to_dict() != other.to_dict()
