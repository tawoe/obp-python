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


class SandboxCrmEventImport(object):
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
        'channel': 'str',
        'bank_id': 'str',
        'id': 'str',
        'customer': 'SandboxCustomerImport',
        'category': 'str',
        'detail': 'str',
        'actual_date': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'bank_id': 'bank_id',
        'id': 'id',
        'customer': 'customer',
        'category': 'category',
        'detail': 'detail',
        'actual_date': 'actual_date'
    }

    def __init__(self, channel=None, bank_id=None, id=None, customer=None, category=None, detail=None, actual_date=None, _configuration=None):  # noqa: E501
        """SandboxCrmEventImport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._channel = None
        self._bank_id = None
        self._id = None
        self._customer = None
        self._category = None
        self._detail = None
        self._actual_date = None
        self.discriminator = None

        self.channel = channel
        self.bank_id = bank_id
        self.id = id
        self.customer = customer
        self.category = category
        self.detail = detail
        self.actual_date = actual_date

    @property
    def channel(self):
        """Gets the channel of this SandboxCrmEventImport.  # noqa: E501


        :return: The channel of this SandboxCrmEventImport.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this SandboxCrmEventImport.


        :param channel: The channel of this SandboxCrmEventImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def bank_id(self):
        """Gets the bank_id of this SandboxCrmEventImport.  # noqa: E501


        :return: The bank_id of this SandboxCrmEventImport.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this SandboxCrmEventImport.


        :param bank_id: The bank_id of this SandboxCrmEventImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def id(self):
        """Gets the id of this SandboxCrmEventImport.  # noqa: E501


        :return: The id of this SandboxCrmEventImport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SandboxCrmEventImport.


        :param id: The id of this SandboxCrmEventImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def customer(self):
        """Gets the customer of this SandboxCrmEventImport.  # noqa: E501


        :return: The customer of this SandboxCrmEventImport.  # noqa: E501
        :rtype: SandboxCustomerImport
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SandboxCrmEventImport.


        :param customer: The customer of this SandboxCrmEventImport.  # noqa: E501
        :type: SandboxCustomerImport
        """
        if self._configuration.client_side_validation and customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def category(self):
        """Gets the category of this SandboxCrmEventImport.  # noqa: E501


        :return: The category of this SandboxCrmEventImport.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SandboxCrmEventImport.


        :param category: The category of this SandboxCrmEventImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def detail(self):
        """Gets the detail of this SandboxCrmEventImport.  # noqa: E501


        :return: The detail of this SandboxCrmEventImport.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SandboxCrmEventImport.


        :param detail: The detail of this SandboxCrmEventImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def actual_date(self):
        """Gets the actual_date of this SandboxCrmEventImport.  # noqa: E501


        :return: The actual_date of this SandboxCrmEventImport.  # noqa: E501
        :rtype: str
        """
        return self._actual_date

    @actual_date.setter
    def actual_date(self, actual_date):
        """Sets the actual_date of this SandboxCrmEventImport.


        :param actual_date: The actual_date of this SandboxCrmEventImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and actual_date is None:
            raise ValueError("Invalid value for `actual_date`, must not be `None`")  # noqa: E501

        self._actual_date = actual_date

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
        if issubclass(SandboxCrmEventImport, dict):
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
        if not isinstance(other, SandboxCrmEventImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxCrmEventImport):
            return True

        return self.to_dict() != other.to_dict()
