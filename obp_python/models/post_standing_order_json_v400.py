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


class PostStandingOrderJsonV400(object):
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
        'date_starts': 'date',
        'customer_id': 'str',
        'date_signed': 'date',
        'user_id': 'str',
        'amount': 'AmountOfMoneyJsonV121',
        'date_expires': 'date',
        'counterparty_id': 'str',
        'when': 'When'
    }

    attribute_map = {
        'date_starts': 'date_starts',
        'customer_id': 'customer_id',
        'date_signed': 'date_signed',
        'user_id': 'user_id',
        'amount': 'amount',
        'date_expires': 'date_expires',
        'counterparty_id': 'counterparty_id',
        'when': 'when'
    }

    def __init__(self, date_starts=None, customer_id=None, date_signed=None, user_id=None, amount=None, date_expires=None, counterparty_id=None, when=None, _configuration=None):  # noqa: E501
        """PostStandingOrderJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._date_starts = None
        self._customer_id = None
        self._date_signed = None
        self._user_id = None
        self._amount = None
        self._date_expires = None
        self._counterparty_id = None
        self._when = None
        self.discriminator = None

        self.date_starts = date_starts
        self.customer_id = customer_id
        if date_signed is not None:
            self.date_signed = date_signed
        self.user_id = user_id
        self.amount = amount
        if date_expires is not None:
            self.date_expires = date_expires
        self.counterparty_id = counterparty_id
        self.when = when

    @property
    def date_starts(self):
        """Gets the date_starts of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The date_starts of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: date
        """
        return self._date_starts

    @date_starts.setter
    def date_starts(self, date_starts):
        """Sets the date_starts of this PostStandingOrderJsonV400.


        :param date_starts: The date_starts of this PostStandingOrderJsonV400.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_starts is None:
            raise ValueError("Invalid value for `date_starts`, must not be `None`")  # noqa: E501

        self._date_starts = date_starts

    @property
    def customer_id(self):
        """Gets the customer_id of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The customer_id of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this PostStandingOrderJsonV400.


        :param customer_id: The customer_id of this PostStandingOrderJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def date_signed(self):
        """Gets the date_signed of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The date_signed of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: date
        """
        return self._date_signed

    @date_signed.setter
    def date_signed(self, date_signed):
        """Sets the date_signed of this PostStandingOrderJsonV400.


        :param date_signed: The date_signed of this PostStandingOrderJsonV400.  # noqa: E501
        :type: date
        """

        self._date_signed = date_signed

    @property
    def user_id(self):
        """Gets the user_id of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The user_id of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PostStandingOrderJsonV400.


        :param user_id: The user_id of this PostStandingOrderJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def amount(self):
        """Gets the amount of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The amount of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PostStandingOrderJsonV400.


        :param amount: The amount of this PostStandingOrderJsonV400.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def date_expires(self):
        """Gets the date_expires of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The date_expires of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: date
        """
        return self._date_expires

    @date_expires.setter
    def date_expires(self, date_expires):
        """Sets the date_expires of this PostStandingOrderJsonV400.


        :param date_expires: The date_expires of this PostStandingOrderJsonV400.  # noqa: E501
        :type: date
        """

        self._date_expires = date_expires

    @property
    def counterparty_id(self):
        """Gets the counterparty_id of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The counterparty_id of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._counterparty_id

    @counterparty_id.setter
    def counterparty_id(self, counterparty_id):
        """Sets the counterparty_id of this PostStandingOrderJsonV400.


        :param counterparty_id: The counterparty_id of this PostStandingOrderJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and counterparty_id is None:
            raise ValueError("Invalid value for `counterparty_id`, must not be `None`")  # noqa: E501

        self._counterparty_id = counterparty_id

    @property
    def when(self):
        """Gets the when of this PostStandingOrderJsonV400.  # noqa: E501


        :return: The when of this PostStandingOrderJsonV400.  # noqa: E501
        :rtype: When
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this PostStandingOrderJsonV400.


        :param when: The when of this PostStandingOrderJsonV400.  # noqa: E501
        :type: When
        """
        if self._configuration.client_side_validation and when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

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
        if issubclass(PostStandingOrderJsonV400, dict):
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
        if not isinstance(other, PostStandingOrderJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostStandingOrderJsonV400):
            return True

        return self.to_dict() != other.to_dict()
