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


class DynamicEntityDefinition(object):
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
        'required': 'list[str]',
        'properties': 'DynamicEntityFullBarFields'
    }

    attribute_map = {
        'description': 'description',
        'required': 'required',
        'properties': 'properties'
    }

    def __init__(self, description=None, required=None, properties=None, _configuration=None):  # noqa: E501
        """DynamicEntityDefinition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._required = None
        self._properties = None
        self.discriminator = None

        self.description = description
        self.required = required
        self.properties = properties

    @property
    def description(self):
        """Gets the description of this DynamicEntityDefinition.  # noqa: E501


        :return: The description of this DynamicEntityDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicEntityDefinition.


        :param description: The description of this DynamicEntityDefinition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def required(self):
        """Gets the required of this DynamicEntityDefinition.  # noqa: E501


        :return: The required of this DynamicEntityDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DynamicEntityDefinition.


        :param required: The required of this DynamicEntityDefinition.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def properties(self):
        """Gets the properties of this DynamicEntityDefinition.  # noqa: E501


        :return: The properties of this DynamicEntityDefinition.  # noqa: E501
        :rtype: DynamicEntityFullBarFields
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DynamicEntityDefinition.


        :param properties: The properties of this DynamicEntityDefinition.  # noqa: E501
        :type: DynamicEntityFullBarFields
        """
        if self._configuration.client_side_validation and properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if issubclass(DynamicEntityDefinition, dict):
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
        if not isinstance(other, DynamicEntityDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicEntityDefinition):
            return True

        return self.to_dict() != other.to_dict()
