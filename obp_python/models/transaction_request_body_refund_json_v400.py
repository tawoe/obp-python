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


class TransactionRequestBodyRefundJsonV400(object):
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
        'description': 'str',
        'refund': 'RefundJson',
        'to': 'TransactionRequestRefundTo',
        '_from': 'TransactionRequestRefundFrom',
        'value': 'AmountOfMoneyJsonV121'
    }

    attribute_map = {
        'description': 'description',
        'refund': 'refund',
        'to': 'to',
        '_from': 'from',
        'value': 'value'
    }

    def __init__(self, description=None, refund=None, to=None, _from=None, value=None, _configuration=None):  # noqa: E501
        """TransactionRequestBodyRefundJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._refund = None
        self._to = None
        self.__from = None
        self._value = None
        self.discriminator = None

        self.description = description
        self.refund = refund
        if to is not None:
            self.to = to
        if _from is not None:
            self._from = _from
        self.value = value

    @property
    def description(self):
        """Gets the description of this TransactionRequestBodyRefundJsonV400.  # noqa: E501


        :return: The description of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransactionRequestBodyRefundJsonV400.


        :param description: The description of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def refund(self):
        """Gets the refund of this TransactionRequestBodyRefundJsonV400.  # noqa: E501


        :return: The refund of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :rtype: RefundJson
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this TransactionRequestBodyRefundJsonV400.


        :param refund: The refund of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :type: RefundJson
        """
        if self._configuration.client_side_validation and refund is None:
            raise ValueError("Invalid value for `refund`, must not be `None`")  # noqa: E501

        self._refund = refund

    @property
    def to(self):
        """Gets the to of this TransactionRequestBodyRefundJsonV400.  # noqa: E501


        :return: The to of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :rtype: TransactionRequestRefundTo
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this TransactionRequestBodyRefundJsonV400.


        :param to: The to of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :type: TransactionRequestRefundTo
        """

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this TransactionRequestBodyRefundJsonV400.  # noqa: E501


        :return: The _from of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :rtype: TransactionRequestRefundFrom
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TransactionRequestBodyRefundJsonV400.


        :param _from: The _from of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :type: TransactionRequestRefundFrom
        """

        self.__from = _from

    @property
    def value(self):
        """Gets the value of this TransactionRequestBodyRefundJsonV400.  # noqa: E501


        :return: The value of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransactionRequestBodyRefundJsonV400.


        :param value: The value of this TransactionRequestBodyRefundJsonV400.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(TransactionRequestBodyRefundJsonV400, dict):
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
        if not isinstance(other, TransactionRequestBodyRefundJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionRequestBodyRefundJsonV400):
            return True

        return self.to_dict() != other.to_dict()
