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


class PinResetJSON(object):
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
        'requested_date': 'date',
        'reason_requested': 'str'
    }

    attribute_map = {
        'requested_date': 'requested_date',
        'reason_requested': 'reason_requested'
    }

    def __init__(self, requested_date=None, reason_requested=None, _configuration=None):  # noqa: E501
        """PinResetJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._requested_date = None
        self._reason_requested = None
        self.discriminator = None

        self.requested_date = requested_date
        self.reason_requested = reason_requested

    @property
    def requested_date(self):
        """Gets the requested_date of this PinResetJSON.  # noqa: E501


        :return: The requested_date of this PinResetJSON.  # noqa: E501
        :rtype: date
        """
        return self._requested_date

    @requested_date.setter
    def requested_date(self, requested_date):
        """Sets the requested_date of this PinResetJSON.


        :param requested_date: The requested_date of this PinResetJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and requested_date is None:
            raise ValueError("Invalid value for `requested_date`, must not be `None`")  # noqa: E501

        self._requested_date = requested_date

    @property
    def reason_requested(self):
        """Gets the reason_requested of this PinResetJSON.  # noqa: E501


        :return: The reason_requested of this PinResetJSON.  # noqa: E501
        :rtype: str
        """
        return self._reason_requested

    @reason_requested.setter
    def reason_requested(self, reason_requested):
        """Sets the reason_requested of this PinResetJSON.


        :param reason_requested: The reason_requested of this PinResetJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reason_requested is None:
            raise ValueError("Invalid value for `reason_requested`, must not be `None`")  # noqa: E501

        self._reason_requested = reason_requested

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
        if issubclass(PinResetJSON, dict):
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
        if not isinstance(other, PinResetJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PinResetJSON):
            return True

        return self.to_dict() != other.to_dict()
