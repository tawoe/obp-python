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


class HistoricalTransactionAccountJsonV310(object):
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
        'bank_id': 'str',
        'account_id': 'str',
        'counterparty_id': 'str'
    }

    attribute_map = {
        'bank_id': 'bank_id',
        'account_id': 'account_id',
        'counterparty_id': 'counterparty_id'
    }

    def __init__(self, bank_id=None, account_id=None, counterparty_id=None, _configuration=None):  # noqa: E501
        """HistoricalTransactionAccountJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bank_id = None
        self._account_id = None
        self._counterparty_id = None
        self.discriminator = None

        if bank_id is not None:
            self.bank_id = bank_id
        if account_id is not None:
            self.account_id = account_id
        if counterparty_id is not None:
            self.counterparty_id = counterparty_id

    @property
    def bank_id(self):
        """Gets the bank_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501


        :return: The bank_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this HistoricalTransactionAccountJsonV310.


        :param bank_id: The bank_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501
        :type: str
        """

        self._bank_id = bank_id

    @property
    def account_id(self):
        """Gets the account_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501


        :return: The account_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this HistoricalTransactionAccountJsonV310.


        :param account_id: The account_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def counterparty_id(self):
        """Gets the counterparty_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501


        :return: The counterparty_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._counterparty_id

    @counterparty_id.setter
    def counterparty_id(self, counterparty_id):
        """Sets the counterparty_id of this HistoricalTransactionAccountJsonV310.


        :param counterparty_id: The counterparty_id of this HistoricalTransactionAccountJsonV310.  # noqa: E501
        :type: str
        """

        self._counterparty_id = counterparty_id

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
        if issubclass(HistoricalTransactionAccountJsonV310, dict):
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
        if not isinstance(other, HistoricalTransactionAccountJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HistoricalTransactionAccountJsonV310):
            return True

        return self.to_dict() != other.to_dict()
