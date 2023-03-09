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


class PostViewJsonV400(object):
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
        'view_id': 'str',
        'is_system': 'bool'
    }

    attribute_map = {
        'view_id': 'view_id',
        'is_system': 'is_system'
    }

    def __init__(self, view_id=None, is_system=None, _configuration=None):  # noqa: E501
        """PostViewJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._view_id = None
        self._is_system = None
        self.discriminator = None

        self.view_id = view_id
        self.is_system = is_system

    @property
    def view_id(self):
        """Gets the view_id of this PostViewJsonV400.  # noqa: E501


        :return: The view_id of this PostViewJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this PostViewJsonV400.


        :param view_id: The view_id of this PostViewJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and view_id is None:
            raise ValueError("Invalid value for `view_id`, must not be `None`")  # noqa: E501

        self._view_id = view_id

    @property
    def is_system(self):
        """Gets the is_system of this PostViewJsonV400.  # noqa: E501


        :return: The is_system of this PostViewJsonV400.  # noqa: E501
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """Sets the is_system of this PostViewJsonV400.


        :param is_system: The is_system of this PostViewJsonV400.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_system is None:
            raise ValueError("Invalid value for `is_system`, must not be `None`")  # noqa: E501

        self._is_system = is_system

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
        if issubclass(PostViewJsonV400, dict):
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
        if not isinstance(other, PostViewJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostViewJsonV400):
            return True

        return self.to_dict() != other.to_dict()
