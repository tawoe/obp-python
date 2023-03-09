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


class ConsentInfosJsonV400(object):
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
        'consents': 'list[ConsentInfoJsonV400]'
    }

    attribute_map = {
        'consents': 'consents'
    }

    def __init__(self, consents=None, _configuration=None):  # noqa: E501
        """ConsentInfosJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consents = None
        self.discriminator = None

        self.consents = consents

    @property
    def consents(self):
        """Gets the consents of this ConsentInfosJsonV400.  # noqa: E501


        :return: The consents of this ConsentInfosJsonV400.  # noqa: E501
        :rtype: list[ConsentInfoJsonV400]
        """
        return self._consents

    @consents.setter
    def consents(self, consents):
        """Sets the consents of this ConsentInfosJsonV400.


        :param consents: The consents of this ConsentInfosJsonV400.  # noqa: E501
        :type: list[ConsentInfoJsonV400]
        """
        if self._configuration.client_side_validation and consents is None:
            raise ValueError("Invalid value for `consents`, must not be `None`")  # noqa: E501

        self._consents = consents

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
        if issubclass(ConsentInfosJsonV400, dict):
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
        if not isinstance(other, ConsentInfosJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsentInfosJsonV400):
            return True

        return self.to_dict() != other.to_dict()
