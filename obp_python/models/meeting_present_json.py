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


class MeetingPresentJson(object):
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
        'staff_user_id': 'str',
        'customer_user_id': 'str'
    }

    attribute_map = {
        'staff_user_id': 'staff_user_id',
        'customer_user_id': 'customer_user_id'
    }

    def __init__(self, staff_user_id=None, customer_user_id=None, _configuration=None):  # noqa: E501
        """MeetingPresentJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._staff_user_id = None
        self._customer_user_id = None
        self.discriminator = None

        self.staff_user_id = staff_user_id
        self.customer_user_id = customer_user_id

    @property
    def staff_user_id(self):
        """Gets the staff_user_id of this MeetingPresentJson.  # noqa: E501


        :return: The staff_user_id of this MeetingPresentJson.  # noqa: E501
        :rtype: str
        """
        return self._staff_user_id

    @staff_user_id.setter
    def staff_user_id(self, staff_user_id):
        """Sets the staff_user_id of this MeetingPresentJson.


        :param staff_user_id: The staff_user_id of this MeetingPresentJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and staff_user_id is None:
            raise ValueError("Invalid value for `staff_user_id`, must not be `None`")  # noqa: E501

        self._staff_user_id = staff_user_id

    @property
    def customer_user_id(self):
        """Gets the customer_user_id of this MeetingPresentJson.  # noqa: E501


        :return: The customer_user_id of this MeetingPresentJson.  # noqa: E501
        :rtype: str
        """
        return self._customer_user_id

    @customer_user_id.setter
    def customer_user_id(self, customer_user_id):
        """Sets the customer_user_id of this MeetingPresentJson.


        :param customer_user_id: The customer_user_id of this MeetingPresentJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_user_id is None:
            raise ValueError("Invalid value for `customer_user_id`, must not be `None`")  # noqa: E501

        self._customer_user_id = customer_user_id

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
        if issubclass(MeetingPresentJson, dict):
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
        if not isinstance(other, MeetingPresentJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeetingPresentJson):
            return True

        return self.to_dict() != other.to_dict()
