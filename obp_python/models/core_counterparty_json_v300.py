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


class CoreCounterpartyJsonV300(object):
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
        'holder': 'AccountHolderJSON',
        'bank_routing': 'BankRoutingJsonV121',
        'account_routings': 'list[AccountRoutingJsonV121]'
    }

    attribute_map = {
        'id': 'id',
        'holder': 'holder',
        'bank_routing': 'bank_routing',
        'account_routings': 'account_routings'
    }

    def __init__(self, id=None, holder=None, bank_routing=None, account_routings=None, _configuration=None):  # noqa: E501
        """CoreCounterpartyJsonV300 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._holder = None
        self._bank_routing = None
        self._account_routings = None
        self.discriminator = None

        self.id = id
        self.holder = holder
        self.bank_routing = bank_routing
        self.account_routings = account_routings

    @property
    def id(self):
        """Gets the id of this CoreCounterpartyJsonV300.  # noqa: E501


        :return: The id of this CoreCounterpartyJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CoreCounterpartyJsonV300.


        :param id: The id of this CoreCounterpartyJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def holder(self):
        """Gets the holder of this CoreCounterpartyJsonV300.  # noqa: E501


        :return: The holder of this CoreCounterpartyJsonV300.  # noqa: E501
        :rtype: AccountHolderJSON
        """
        return self._holder

    @holder.setter
    def holder(self, holder):
        """Sets the holder of this CoreCounterpartyJsonV300.


        :param holder: The holder of this CoreCounterpartyJsonV300.  # noqa: E501
        :type: AccountHolderJSON
        """
        if self._configuration.client_side_validation and holder is None:
            raise ValueError("Invalid value for `holder`, must not be `None`")  # noqa: E501

        self._holder = holder

    @property
    def bank_routing(self):
        """Gets the bank_routing of this CoreCounterpartyJsonV300.  # noqa: E501


        :return: The bank_routing of this CoreCounterpartyJsonV300.  # noqa: E501
        :rtype: BankRoutingJsonV121
        """
        return self._bank_routing

    @bank_routing.setter
    def bank_routing(self, bank_routing):
        """Sets the bank_routing of this CoreCounterpartyJsonV300.


        :param bank_routing: The bank_routing of this CoreCounterpartyJsonV300.  # noqa: E501
        :type: BankRoutingJsonV121
        """
        if self._configuration.client_side_validation and bank_routing is None:
            raise ValueError("Invalid value for `bank_routing`, must not be `None`")  # noqa: E501

        self._bank_routing = bank_routing

    @property
    def account_routings(self):
        """Gets the account_routings of this CoreCounterpartyJsonV300.  # noqa: E501


        :return: The account_routings of this CoreCounterpartyJsonV300.  # noqa: E501
        :rtype: list[AccountRoutingJsonV121]
        """
        return self._account_routings

    @account_routings.setter
    def account_routings(self, account_routings):
        """Sets the account_routings of this CoreCounterpartyJsonV300.


        :param account_routings: The account_routings of this CoreCounterpartyJsonV300.  # noqa: E501
        :type: list[AccountRoutingJsonV121]
        """
        if self._configuration.client_side_validation and account_routings is None:
            raise ValueError("Invalid value for `account_routings`, must not be `None`")  # noqa: E501

        self._account_routings = account_routings

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
        if issubclass(CoreCounterpartyJsonV300, dict):
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
        if not isinstance(other, CoreCounterpartyJsonV300):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CoreCounterpartyJsonV300):
            return True

        return self.to_dict() != other.to_dict()
