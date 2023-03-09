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


class TopApisJson(object):
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
        'top_apis': 'list[TopApiJson]'
    }

    attribute_map = {
        'top_apis': 'top_apis'
    }

    def __init__(self, top_apis=None, _configuration=None):  # noqa: E501
        """TopApisJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._top_apis = None
        self.discriminator = None

        self.top_apis = top_apis

    @property
    def top_apis(self):
        """Gets the top_apis of this TopApisJson.  # noqa: E501


        :return: The top_apis of this TopApisJson.  # noqa: E501
        :rtype: list[TopApiJson]
        """
        return self._top_apis

    @top_apis.setter
    def top_apis(self, top_apis):
        """Sets the top_apis of this TopApisJson.


        :param top_apis: The top_apis of this TopApisJson.  # noqa: E501
        :type: list[TopApiJson]
        """
        if self._configuration.client_side_validation and top_apis is None:
            raise ValueError("Invalid value for `top_apis`, must not be `None`")  # noqa: E501

        self._top_apis = top_apis

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
        if issubclass(TopApisJson, dict):
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
        if not isinstance(other, TopApisJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TopApisJson):
            return True

        return self.to_dict() != other.to_dict()
