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


class PutUpdateCustomerIdentityJsonV310(object):
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
        'legal_name': 'str',
        'date_of_birth': 'date',
        'title': 'str',
        'name_suffix': 'str'
    }

    attribute_map = {
        'legal_name': 'legal_name',
        'date_of_birth': 'date_of_birth',
        'title': 'title',
        'name_suffix': 'name_suffix'
    }

    def __init__(self, legal_name=None, date_of_birth=None, title=None, name_suffix=None, _configuration=None):  # noqa: E501
        """PutUpdateCustomerIdentityJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._legal_name = None
        self._date_of_birth = None
        self._title = None
        self._name_suffix = None
        self.discriminator = None

        self.legal_name = legal_name
        self.date_of_birth = date_of_birth
        self.title = title
        self.name_suffix = name_suffix

    @property
    def legal_name(self):
        """Gets the legal_name of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501


        :return: The legal_name of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this PutUpdateCustomerIdentityJsonV310.


        :param legal_name: The legal_name of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and legal_name is None:
            raise ValueError("Invalid value for `legal_name`, must not be `None`")  # noqa: E501

        self._legal_name = legal_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501


        :return: The date_of_birth of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PutUpdateCustomerIdentityJsonV310.


        :param date_of_birth: The date_of_birth of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def title(self):
        """Gets the title of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501


        :return: The title of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PutUpdateCustomerIdentityJsonV310.


        :param title: The title of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def name_suffix(self):
        """Gets the name_suffix of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501


        :return: The name_suffix of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._name_suffix

    @name_suffix.setter
    def name_suffix(self, name_suffix):
        """Sets the name_suffix of this PutUpdateCustomerIdentityJsonV310.


        :param name_suffix: The name_suffix of this PutUpdateCustomerIdentityJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_suffix is None:
            raise ValueError("Invalid value for `name_suffix`, must not be `None`")  # noqa: E501

        self._name_suffix = name_suffix

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
        if issubclass(PutUpdateCustomerIdentityJsonV310, dict):
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
        if not isinstance(other, PutUpdateCustomerIdentityJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutUpdateCustomerIdentityJsonV310):
            return True

        return self.to_dict() != other.to_dict()
