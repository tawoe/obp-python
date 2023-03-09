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


class CorrelatedEntities(object):
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
        'correlated_entities': 'list[CustomerAndUsersWithAttributesResponseJson]'
    }

    attribute_map = {
        'correlated_entities': 'correlated_entities'
    }

    def __init__(self, correlated_entities=None, _configuration=None):  # noqa: E501
        """CorrelatedEntities - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._correlated_entities = None
        self.discriminator = None

        self.correlated_entities = correlated_entities

    @property
    def correlated_entities(self):
        """Gets the correlated_entities of this CorrelatedEntities.  # noqa: E501


        :return: The correlated_entities of this CorrelatedEntities.  # noqa: E501
        :rtype: list[CustomerAndUsersWithAttributesResponseJson]
        """
        return self._correlated_entities

    @correlated_entities.setter
    def correlated_entities(self, correlated_entities):
        """Sets the correlated_entities of this CorrelatedEntities.


        :param correlated_entities: The correlated_entities of this CorrelatedEntities.  # noqa: E501
        :type: list[CustomerAndUsersWithAttributesResponseJson]
        """
        if self._configuration.client_side_validation and correlated_entities is None:
            raise ValueError("Invalid value for `correlated_entities`, must not be `None`")  # noqa: E501

        self._correlated_entities = correlated_entities

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
        if issubclass(CorrelatedEntities, dict):
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
        if not isinstance(other, CorrelatedEntities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CorrelatedEntities):
            return True

        return self.to_dict() != other.to_dict()
