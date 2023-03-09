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


class CardJsonV400(object):
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
        'expiry_year': 'str',
        'cvv': 'str',
        'expiry_month': 'str',
        'brand': 'str',
        'card_number': 'str',
        'name_on_card': 'str',
        'card_type': 'str'
    }

    attribute_map = {
        'expiry_year': 'expiry_year',
        'cvv': 'cvv',
        'expiry_month': 'expiry_month',
        'brand': 'brand',
        'card_number': 'card_number',
        'name_on_card': 'name_on_card',
        'card_type': 'card_type'
    }

    def __init__(self, expiry_year=None, cvv=None, expiry_month=None, brand=None, card_number=None, name_on_card=None, card_type=None, _configuration=None):  # noqa: E501
        """CardJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expiry_year = None
        self._cvv = None
        self._expiry_month = None
        self._brand = None
        self._card_number = None
        self._name_on_card = None
        self._card_type = None
        self.discriminator = None

        self.expiry_year = expiry_year
        self.cvv = cvv
        self.expiry_month = expiry_month
        self.brand = brand
        self.card_number = card_number
        self.name_on_card = name_on_card
        self.card_type = card_type

    @property
    def expiry_year(self):
        """Gets the expiry_year of this CardJsonV400.  # noqa: E501


        :return: The expiry_year of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._expiry_year

    @expiry_year.setter
    def expiry_year(self, expiry_year):
        """Sets the expiry_year of this CardJsonV400.


        :param expiry_year: The expiry_year of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and expiry_year is None:
            raise ValueError("Invalid value for `expiry_year`, must not be `None`")  # noqa: E501

        self._expiry_year = expiry_year

    @property
    def cvv(self):
        """Gets the cvv of this CardJsonV400.  # noqa: E501


        :return: The cvv of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this CardJsonV400.


        :param cvv: The cvv of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cvv is None:
            raise ValueError("Invalid value for `cvv`, must not be `None`")  # noqa: E501

        self._cvv = cvv

    @property
    def expiry_month(self):
        """Gets the expiry_month of this CardJsonV400.  # noqa: E501


        :return: The expiry_month of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._expiry_month

    @expiry_month.setter
    def expiry_month(self, expiry_month):
        """Sets the expiry_month of this CardJsonV400.


        :param expiry_month: The expiry_month of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and expiry_month is None:
            raise ValueError("Invalid value for `expiry_month`, must not be `None`")  # noqa: E501

        self._expiry_month = expiry_month

    @property
    def brand(self):
        """Gets the brand of this CardJsonV400.  # noqa: E501


        :return: The brand of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CardJsonV400.


        :param brand: The brand of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def card_number(self):
        """Gets the card_number of this CardJsonV400.  # noqa: E501


        :return: The card_number of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this CardJsonV400.


        :param card_number: The card_number of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and card_number is None:
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

    @property
    def name_on_card(self):
        """Gets the name_on_card of this CardJsonV400.  # noqa: E501


        :return: The name_on_card of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._name_on_card

    @name_on_card.setter
    def name_on_card(self, name_on_card):
        """Sets the name_on_card of this CardJsonV400.


        :param name_on_card: The name_on_card of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_on_card is None:
            raise ValueError("Invalid value for `name_on_card`, must not be `None`")  # noqa: E501

        self._name_on_card = name_on_card

    @property
    def card_type(self):
        """Gets the card_type of this CardJsonV400.  # noqa: E501


        :return: The card_type of this CardJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """Sets the card_type of this CardJsonV400.


        :param card_type: The card_type of this CardJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and card_type is None:
            raise ValueError("Invalid value for `card_type`, must not be `None`")  # noqa: E501

        self._card_type = card_type

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
        if issubclass(CardJsonV400, dict):
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
        if not isinstance(other, CardJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardJsonV400):
            return True

        return self.to_dict() != other.to_dict()
