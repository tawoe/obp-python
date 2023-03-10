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


class SandboxProductImport(object):
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
        'more_info_url': 'str',
        'super_family': 'str',
        'code': 'str',
        'bank_id': 'str',
        'meta': 'SandboxMetaImport',
        'category': 'str',
        'family': 'str'
    }

    attribute_map = {
        'name': 'name',
        'more_info_url': 'more_info_url',
        'super_family': 'super_family',
        'code': 'code',
        'bank_id': 'bank_id',
        'meta': 'meta',
        'category': 'category',
        'family': 'family'
    }

    def __init__(self, name=None, more_info_url=None, super_family=None, code=None, bank_id=None, meta=None, category=None, family=None, _configuration=None):  # noqa: E501
        """SandboxProductImport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._more_info_url = None
        self._super_family = None
        self._code = None
        self._bank_id = None
        self._meta = None
        self._category = None
        self._family = None
        self.discriminator = None

        self.name = name
        self.more_info_url = more_info_url
        self.super_family = super_family
        self.code = code
        self.bank_id = bank_id
        self.meta = meta
        self.category = category
        self.family = family

    @property
    def name(self):
        """Gets the name of this SandboxProductImport.  # noqa: E501


        :return: The name of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SandboxProductImport.


        :param name: The name of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def more_info_url(self):
        """Gets the more_info_url of this SandboxProductImport.  # noqa: E501


        :return: The more_info_url of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._more_info_url

    @more_info_url.setter
    def more_info_url(self, more_info_url):
        """Sets the more_info_url of this SandboxProductImport.


        :param more_info_url: The more_info_url of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and more_info_url is None:
            raise ValueError("Invalid value for `more_info_url`, must not be `None`")  # noqa: E501

        self._more_info_url = more_info_url

    @property
    def super_family(self):
        """Gets the super_family of this SandboxProductImport.  # noqa: E501


        :return: The super_family of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._super_family

    @super_family.setter
    def super_family(self, super_family):
        """Sets the super_family of this SandboxProductImport.


        :param super_family: The super_family of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and super_family is None:
            raise ValueError("Invalid value for `super_family`, must not be `None`")  # noqa: E501

        self._super_family = super_family

    @property
    def code(self):
        """Gets the code of this SandboxProductImport.  # noqa: E501


        :return: The code of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SandboxProductImport.


        :param code: The code of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def bank_id(self):
        """Gets the bank_id of this SandboxProductImport.  # noqa: E501


        :return: The bank_id of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this SandboxProductImport.


        :param bank_id: The bank_id of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def meta(self):
        """Gets the meta of this SandboxProductImport.  # noqa: E501


        :return: The meta of this SandboxProductImport.  # noqa: E501
        :rtype: SandboxMetaImport
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this SandboxProductImport.


        :param meta: The meta of this SandboxProductImport.  # noqa: E501
        :type: SandboxMetaImport
        """
        if self._configuration.client_side_validation and meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def category(self):
        """Gets the category of this SandboxProductImport.  # noqa: E501


        :return: The category of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SandboxProductImport.


        :param category: The category of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def family(self):
        """Gets the family of this SandboxProductImport.  # noqa: E501


        :return: The family of this SandboxProductImport.  # noqa: E501
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this SandboxProductImport.


        :param family: The family of this SandboxProductImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and family is None:
            raise ValueError("Invalid value for `family`, must not be `None`")  # noqa: E501

        self._family = family

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
        if issubclass(SandboxProductImport, dict):
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
        if not isinstance(other, SandboxProductImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxProductImport):
            return True

        return self.to_dict() != other.to_dict()
