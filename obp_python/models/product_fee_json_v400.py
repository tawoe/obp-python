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


class ProductFeeJsonV400(object):
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
        'is_active': 'bool',
        'more_info': 'str',
        'product_fee_id': 'str',
        'value': 'ProductFeeValueJsonV400'
    }

    attribute_map = {
        'name': 'name',
        'is_active': 'is_active',
        'more_info': 'more_info',
        'product_fee_id': 'product_fee_id',
        'value': 'value'
    }

    def __init__(self, name=None, is_active=None, more_info=None, product_fee_id=None, value=None, _configuration=None):  # noqa: E501
        """ProductFeeJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._is_active = None
        self._more_info = None
        self._product_fee_id = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.is_active = is_active
        self.more_info = more_info
        if product_fee_id is not None:
            self.product_fee_id = product_fee_id
        self.value = value

    @property
    def name(self):
        """Gets the name of this ProductFeeJsonV400.  # noqa: E501


        :return: The name of this ProductFeeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductFeeJsonV400.


        :param name: The name of this ProductFeeJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_active(self):
        """Gets the is_active of this ProductFeeJsonV400.  # noqa: E501


        :return: The is_active of this ProductFeeJsonV400.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ProductFeeJsonV400.


        :param is_active: The is_active of this ProductFeeJsonV400.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def more_info(self):
        """Gets the more_info of this ProductFeeJsonV400.  # noqa: E501


        :return: The more_info of this ProductFeeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._more_info

    @more_info.setter
    def more_info(self, more_info):
        """Sets the more_info of this ProductFeeJsonV400.


        :param more_info: The more_info of this ProductFeeJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and more_info is None:
            raise ValueError("Invalid value for `more_info`, must not be `None`")  # noqa: E501

        self._more_info = more_info

    @property
    def product_fee_id(self):
        """Gets the product_fee_id of this ProductFeeJsonV400.  # noqa: E501


        :return: The product_fee_id of this ProductFeeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._product_fee_id

    @product_fee_id.setter
    def product_fee_id(self, product_fee_id):
        """Sets the product_fee_id of this ProductFeeJsonV400.


        :param product_fee_id: The product_fee_id of this ProductFeeJsonV400.  # noqa: E501
        :type: str
        """

        self._product_fee_id = product_fee_id

    @property
    def value(self):
        """Gets the value of this ProductFeeJsonV400.  # noqa: E501


        :return: The value of this ProductFeeJsonV400.  # noqa: E501
        :rtype: ProductFeeValueJsonV400
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProductFeeJsonV400.


        :param value: The value of this ProductFeeJsonV400.  # noqa: E501
        :type: ProductFeeValueJsonV400
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
        if issubclass(ProductFeeJsonV400, dict):
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
        if not isinstance(other, ProductFeeJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductFeeJsonV400):
            return True

        return self.to_dict() != other.to_dict()
