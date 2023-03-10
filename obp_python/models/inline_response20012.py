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


class InlineResponse20012(object):
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
        'dynamic_endpoints': 'list[InlineResponse2011]'
    }

    attribute_map = {
        'dynamic_endpoints': 'dynamic_endpoints'
    }

    def __init__(self, dynamic_endpoints=None, _configuration=None):  # noqa: E501
        """InlineResponse20012 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dynamic_endpoints = None
        self.discriminator = None

        self.dynamic_endpoints = dynamic_endpoints

    @property
    def dynamic_endpoints(self):
        """Gets the dynamic_endpoints of this InlineResponse20012.  # noqa: E501


        :return: The dynamic_endpoints of this InlineResponse20012.  # noqa: E501
        :rtype: list[InlineResponse2011]
        """
        return self._dynamic_endpoints

    @dynamic_endpoints.setter
    def dynamic_endpoints(self, dynamic_endpoints):
        """Sets the dynamic_endpoints of this InlineResponse20012.


        :param dynamic_endpoints: The dynamic_endpoints of this InlineResponse20012.  # noqa: E501
        :type: list[InlineResponse2011]
        """
        if self._configuration.client_side_validation and dynamic_endpoints is None:
            raise ValueError("Invalid value for `dynamic_endpoints`, must not be `None`")  # noqa: E501

        self._dynamic_endpoints = dynamic_endpoints

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
        if issubclass(InlineResponse20012, dict):
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
        if not isinstance(other, InlineResponse20012):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse20012):
            return True

        return self.to_dict() != other.to_dict()
