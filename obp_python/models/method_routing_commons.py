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


class MethodRoutingCommons(object):
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
        'is_bank_id_exact_match': 'bool',
        'method_name': 'str',
        'connector_name': 'str',
        'method_routing_id': 'str',
        'bank_id_pattern': 'str',
        'parameters': 'list[MethodRoutingParam]'
    }

    attribute_map = {
        'is_bank_id_exact_match': 'is_bank_id_exact_match',
        'method_name': 'method_name',
        'connector_name': 'connector_name',
        'method_routing_id': 'method_routing_id',
        'bank_id_pattern': 'bank_id_pattern',
        'parameters': 'parameters'
    }

    def __init__(self, is_bank_id_exact_match=None, method_name=None, connector_name=None, method_routing_id=None, bank_id_pattern=None, parameters=None, _configuration=None):  # noqa: E501
        """MethodRoutingCommons - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_bank_id_exact_match = None
        self._method_name = None
        self._connector_name = None
        self._method_routing_id = None
        self._bank_id_pattern = None
        self._parameters = None
        self.discriminator = None

        self.is_bank_id_exact_match = is_bank_id_exact_match
        self.method_name = method_name
        self.connector_name = connector_name
        if method_routing_id is not None:
            self.method_routing_id = method_routing_id
        if bank_id_pattern is not None:
            self.bank_id_pattern = bank_id_pattern
        self.parameters = parameters

    @property
    def is_bank_id_exact_match(self):
        """Gets the is_bank_id_exact_match of this MethodRoutingCommons.  # noqa: E501


        :return: The is_bank_id_exact_match of this MethodRoutingCommons.  # noqa: E501
        :rtype: bool
        """
        return self._is_bank_id_exact_match

    @is_bank_id_exact_match.setter
    def is_bank_id_exact_match(self, is_bank_id_exact_match):
        """Sets the is_bank_id_exact_match of this MethodRoutingCommons.


        :param is_bank_id_exact_match: The is_bank_id_exact_match of this MethodRoutingCommons.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_bank_id_exact_match is None:
            raise ValueError("Invalid value for `is_bank_id_exact_match`, must not be `None`")  # noqa: E501

        self._is_bank_id_exact_match = is_bank_id_exact_match

    @property
    def method_name(self):
        """Gets the method_name of this MethodRoutingCommons.  # noqa: E501


        :return: The method_name of this MethodRoutingCommons.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this MethodRoutingCommons.


        :param method_name: The method_name of this MethodRoutingCommons.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and method_name is None:
            raise ValueError("Invalid value for `method_name`, must not be `None`")  # noqa: E501

        self._method_name = method_name

    @property
    def connector_name(self):
        """Gets the connector_name of this MethodRoutingCommons.  # noqa: E501


        :return: The connector_name of this MethodRoutingCommons.  # noqa: E501
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this MethodRoutingCommons.


        :param connector_name: The connector_name of this MethodRoutingCommons.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connector_name is None:
            raise ValueError("Invalid value for `connector_name`, must not be `None`")  # noqa: E501

        self._connector_name = connector_name

    @property
    def method_routing_id(self):
        """Gets the method_routing_id of this MethodRoutingCommons.  # noqa: E501


        :return: The method_routing_id of this MethodRoutingCommons.  # noqa: E501
        :rtype: str
        """
        return self._method_routing_id

    @method_routing_id.setter
    def method_routing_id(self, method_routing_id):
        """Sets the method_routing_id of this MethodRoutingCommons.


        :param method_routing_id: The method_routing_id of this MethodRoutingCommons.  # noqa: E501
        :type: str
        """

        self._method_routing_id = method_routing_id

    @property
    def bank_id_pattern(self):
        """Gets the bank_id_pattern of this MethodRoutingCommons.  # noqa: E501


        :return: The bank_id_pattern of this MethodRoutingCommons.  # noqa: E501
        :rtype: str
        """
        return self._bank_id_pattern

    @bank_id_pattern.setter
    def bank_id_pattern(self, bank_id_pattern):
        """Sets the bank_id_pattern of this MethodRoutingCommons.


        :param bank_id_pattern: The bank_id_pattern of this MethodRoutingCommons.  # noqa: E501
        :type: str
        """

        self._bank_id_pattern = bank_id_pattern

    @property
    def parameters(self):
        """Gets the parameters of this MethodRoutingCommons.  # noqa: E501


        :return: The parameters of this MethodRoutingCommons.  # noqa: E501
        :rtype: list[MethodRoutingParam]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MethodRoutingCommons.


        :param parameters: The parameters of this MethodRoutingCommons.  # noqa: E501
        :type: list[MethodRoutingParam]
        """
        if self._configuration.client_side_validation and parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

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
        if issubclass(MethodRoutingCommons, dict):
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
        if not isinstance(other, MethodRoutingCommons):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MethodRoutingCommons):
            return True

        return self.to_dict() != other.to_dict()
