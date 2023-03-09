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


class AccountApplicationJson(object):
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
        'product_code': 'str',
        'user_id': 'str',
        'customer_id': 'str'
    }

    attribute_map = {
        'product_code': 'product_code',
        'user_id': 'user_id',
        'customer_id': 'customer_id'
    }

    def __init__(self, product_code=None, user_id=None, customer_id=None, _configuration=None):  # noqa: E501
        """AccountApplicationJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_code = None
        self._user_id = None
        self._customer_id = None
        self.discriminator = None

        self.product_code = product_code
        if user_id is not None:
            self.user_id = user_id
        if customer_id is not None:
            self.customer_id = customer_id

    @property
    def product_code(self):
        """Gets the product_code of this AccountApplicationJson.  # noqa: E501


        :return: The product_code of this AccountApplicationJson.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this AccountApplicationJson.


        :param product_code: The product_code of this AccountApplicationJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def user_id(self):
        """Gets the user_id of this AccountApplicationJson.  # noqa: E501


        :return: The user_id of this AccountApplicationJson.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccountApplicationJson.


        :param user_id: The user_id of this AccountApplicationJson.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def customer_id(self):
        """Gets the customer_id of this AccountApplicationJson.  # noqa: E501


        :return: The customer_id of this AccountApplicationJson.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AccountApplicationJson.


        :param customer_id: The customer_id of this AccountApplicationJson.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

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
        if issubclass(AccountApplicationJson, dict):
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
        if not isinstance(other, AccountApplicationJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountApplicationJson):
            return True

        return self.to_dict() != other.to_dict()
