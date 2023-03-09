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


class CustomerAccountLinkJson(object):
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
        'customer_id': 'str',
        'customer_account_link_id': 'str',
        'bank_id': 'str',
        'account_id': 'str',
        'relationship_type': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'customer_account_link_id': 'customer_account_link_id',
        'bank_id': 'bank_id',
        'account_id': 'account_id',
        'relationship_type': 'relationship_type'
    }

    def __init__(self, customer_id=None, customer_account_link_id=None, bank_id=None, account_id=None, relationship_type=None, _configuration=None):  # noqa: E501
        """CustomerAccountLinkJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer_id = None
        self._customer_account_link_id = None
        self._bank_id = None
        self._account_id = None
        self._relationship_type = None
        self.discriminator = None

        self.customer_id = customer_id
        self.customer_account_link_id = customer_account_link_id
        self.bank_id = bank_id
        self.account_id = account_id
        self.relationship_type = relationship_type

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerAccountLinkJson.  # noqa: E501


        :return: The customer_id of this CustomerAccountLinkJson.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerAccountLinkJson.


        :param customer_id: The customer_id of this CustomerAccountLinkJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def customer_account_link_id(self):
        """Gets the customer_account_link_id of this CustomerAccountLinkJson.  # noqa: E501


        :return: The customer_account_link_id of this CustomerAccountLinkJson.  # noqa: E501
        :rtype: str
        """
        return self._customer_account_link_id

    @customer_account_link_id.setter
    def customer_account_link_id(self, customer_account_link_id):
        """Sets the customer_account_link_id of this CustomerAccountLinkJson.


        :param customer_account_link_id: The customer_account_link_id of this CustomerAccountLinkJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_account_link_id is None:
            raise ValueError("Invalid value for `customer_account_link_id`, must not be `None`")  # noqa: E501

        self._customer_account_link_id = customer_account_link_id

    @property
    def bank_id(self):
        """Gets the bank_id of this CustomerAccountLinkJson.  # noqa: E501


        :return: The bank_id of this CustomerAccountLinkJson.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this CustomerAccountLinkJson.


        :param bank_id: The bank_id of this CustomerAccountLinkJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def account_id(self):
        """Gets the account_id of this CustomerAccountLinkJson.  # noqa: E501


        :return: The account_id of this CustomerAccountLinkJson.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CustomerAccountLinkJson.


        :param account_id: The account_id of this CustomerAccountLinkJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def relationship_type(self):
        """Gets the relationship_type of this CustomerAccountLinkJson.  # noqa: E501


        :return: The relationship_type of this CustomerAccountLinkJson.  # noqa: E501
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        """Sets the relationship_type of this CustomerAccountLinkJson.


        :param relationship_type: The relationship_type of this CustomerAccountLinkJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relationship_type is None:
            raise ValueError("Invalid value for `relationship_type`, must not be `None`")  # noqa: E501

        self._relationship_type = relationship_type

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
        if issubclass(CustomerAccountLinkJson, dict):
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
        if not isinstance(other, CustomerAccountLinkJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerAccountLinkJson):
            return True

        return self.to_dict() != other.to_dict()
