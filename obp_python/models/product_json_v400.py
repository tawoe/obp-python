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


class ProductJsonV400(object):
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
        'description': 'str',
        'terms_and_conditions_url': 'str',
        'more_info_url': 'str',
        'attributes': 'list[ProductAttributeResponseWithoutBankIdJson]',
        'product_code': 'str',
        'bank_id': 'str',
        'meta': 'MetaJsonV140',
        'fees': 'list[ProductFeeJsonV400]',
        'parent_product_code': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'terms_and_conditions_url': 'terms_and_conditions_url',
        'more_info_url': 'more_info_url',
        'attributes': 'attributes',
        'product_code': 'product_code',
        'bank_id': 'bank_id',
        'meta': 'meta',
        'fees': 'fees',
        'parent_product_code': 'parent_product_code'
    }

    def __init__(self, name=None, description=None, terms_and_conditions_url=None, more_info_url=None, attributes=None, product_code=None, bank_id=None, meta=None, fees=None, parent_product_code=None, _configuration=None):  # noqa: E501
        """ProductJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._terms_and_conditions_url = None
        self._more_info_url = None
        self._attributes = None
        self._product_code = None
        self._bank_id = None
        self._meta = None
        self._fees = None
        self._parent_product_code = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.terms_and_conditions_url = terms_and_conditions_url
        self.more_info_url = more_info_url
        if attributes is not None:
            self.attributes = attributes
        self.product_code = product_code
        self.bank_id = bank_id
        self.meta = meta
        if fees is not None:
            self.fees = fees
        self.parent_product_code = parent_product_code

    @property
    def name(self):
        """Gets the name of this ProductJsonV400.  # noqa: E501


        :return: The name of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductJsonV400.


        :param name: The name of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProductJsonV400.  # noqa: E501


        :return: The description of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductJsonV400.


        :param description: The description of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def terms_and_conditions_url(self):
        """Gets the terms_and_conditions_url of this ProductJsonV400.  # noqa: E501


        :return: The terms_and_conditions_url of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._terms_and_conditions_url

    @terms_and_conditions_url.setter
    def terms_and_conditions_url(self, terms_and_conditions_url):
        """Sets the terms_and_conditions_url of this ProductJsonV400.


        :param terms_and_conditions_url: The terms_and_conditions_url of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and terms_and_conditions_url is None:
            raise ValueError("Invalid value for `terms_and_conditions_url`, must not be `None`")  # noqa: E501

        self._terms_and_conditions_url = terms_and_conditions_url

    @property
    def more_info_url(self):
        """Gets the more_info_url of this ProductJsonV400.  # noqa: E501


        :return: The more_info_url of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._more_info_url

    @more_info_url.setter
    def more_info_url(self, more_info_url):
        """Sets the more_info_url of this ProductJsonV400.


        :param more_info_url: The more_info_url of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and more_info_url is None:
            raise ValueError("Invalid value for `more_info_url`, must not be `None`")  # noqa: E501

        self._more_info_url = more_info_url

    @property
    def attributes(self):
        """Gets the attributes of this ProductJsonV400.  # noqa: E501


        :return: The attributes of this ProductJsonV400.  # noqa: E501
        :rtype: list[ProductAttributeResponseWithoutBankIdJson]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ProductJsonV400.


        :param attributes: The attributes of this ProductJsonV400.  # noqa: E501
        :type: list[ProductAttributeResponseWithoutBankIdJson]
        """

        self._attributes = attributes

    @property
    def product_code(self):
        """Gets the product_code of this ProductJsonV400.  # noqa: E501


        :return: The product_code of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this ProductJsonV400.


        :param product_code: The product_code of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def bank_id(self):
        """Gets the bank_id of this ProductJsonV400.  # noqa: E501


        :return: The bank_id of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this ProductJsonV400.


        :param bank_id: The bank_id of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def meta(self):
        """Gets the meta of this ProductJsonV400.  # noqa: E501


        :return: The meta of this ProductJsonV400.  # noqa: E501
        :rtype: MetaJsonV140
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ProductJsonV400.


        :param meta: The meta of this ProductJsonV400.  # noqa: E501
        :type: MetaJsonV140
        """
        if self._configuration.client_side_validation and meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def fees(self):
        """Gets the fees of this ProductJsonV400.  # noqa: E501


        :return: The fees of this ProductJsonV400.  # noqa: E501
        :rtype: list[ProductFeeJsonV400]
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this ProductJsonV400.


        :param fees: The fees of this ProductJsonV400.  # noqa: E501
        :type: list[ProductFeeJsonV400]
        """

        self._fees = fees

    @property
    def parent_product_code(self):
        """Gets the parent_product_code of this ProductJsonV400.  # noqa: E501


        :return: The parent_product_code of this ProductJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._parent_product_code

    @parent_product_code.setter
    def parent_product_code(self, parent_product_code):
        """Sets the parent_product_code of this ProductJsonV400.


        :param parent_product_code: The parent_product_code of this ProductJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and parent_product_code is None:
            raise ValueError("Invalid value for `parent_product_code`, must not be `None`")  # noqa: E501

        self._parent_product_code = parent_product_code

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
        if issubclass(ProductJsonV400, dict):
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
        if not isinstance(other, ProductJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductJsonV400):
            return True

        return self.to_dict() != other.to_dict()
