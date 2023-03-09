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


class SandboxBankImport(object):
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
        'website': 'str',
        'full_name': 'str',
        'logo': 'str',
        'id': 'str',
        'short_name': 'str'
    }

    attribute_map = {
        'website': 'website',
        'full_name': 'full_name',
        'logo': 'logo',
        'id': 'id',
        'short_name': 'short_name'
    }

    def __init__(self, website=None, full_name=None, logo=None, id=None, short_name=None, _configuration=None):  # noqa: E501
        """SandboxBankImport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._website = None
        self._full_name = None
        self._logo = None
        self._id = None
        self._short_name = None
        self.discriminator = None

        self.website = website
        self.full_name = full_name
        self.logo = logo
        self.id = id
        self.short_name = short_name

    @property
    def website(self):
        """Gets the website of this SandboxBankImport.  # noqa: E501


        :return: The website of this SandboxBankImport.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this SandboxBankImport.


        :param website: The website of this SandboxBankImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and website is None:
            raise ValueError("Invalid value for `website`, must not be `None`")  # noqa: E501

        self._website = website

    @property
    def full_name(self):
        """Gets the full_name of this SandboxBankImport.  # noqa: E501


        :return: The full_name of this SandboxBankImport.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this SandboxBankImport.


        :param full_name: The full_name of this SandboxBankImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def logo(self):
        """Gets the logo of this SandboxBankImport.  # noqa: E501


        :return: The logo of this SandboxBankImport.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this SandboxBankImport.


        :param logo: The logo of this SandboxBankImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and logo is None:
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

    @property
    def id(self):
        """Gets the id of this SandboxBankImport.  # noqa: E501


        :return: The id of this SandboxBankImport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SandboxBankImport.


        :param id: The id of this SandboxBankImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def short_name(self):
        """Gets the short_name of this SandboxBankImport.  # noqa: E501


        :return: The short_name of this SandboxBankImport.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this SandboxBankImport.


        :param short_name: The short_name of this SandboxBankImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and short_name is None:
            raise ValueError("Invalid value for `short_name`, must not be `None`")  # noqa: E501

        self._short_name = short_name

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
        if issubclass(SandboxBankImport, dict):
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
        if not isinstance(other, SandboxBankImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxBankImport):
            return True

        return self.to_dict() != other.to_dict()