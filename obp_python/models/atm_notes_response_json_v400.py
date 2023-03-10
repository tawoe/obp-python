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


class AtmNotesResponseJsonV400(object):
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
        'atm_id': 'str',
        'notes': 'list[str]'
    }

    attribute_map = {
        'atm_id': 'atm_id',
        'notes': 'notes'
    }

    def __init__(self, atm_id=None, notes=None, _configuration=None):  # noqa: E501
        """AtmNotesResponseJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._atm_id = None
        self._notes = None
        self.discriminator = None

        self.atm_id = atm_id
        self.notes = notes

    @property
    def atm_id(self):
        """Gets the atm_id of this AtmNotesResponseJsonV400.  # noqa: E501


        :return: The atm_id of this AtmNotesResponseJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._atm_id

    @atm_id.setter
    def atm_id(self, atm_id):
        """Sets the atm_id of this AtmNotesResponseJsonV400.


        :param atm_id: The atm_id of this AtmNotesResponseJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and atm_id is None:
            raise ValueError("Invalid value for `atm_id`, must not be `None`")  # noqa: E501

        self._atm_id = atm_id

    @property
    def notes(self):
        """Gets the notes of this AtmNotesResponseJsonV400.  # noqa: E501


        :return: The notes of this AtmNotesResponseJsonV400.  # noqa: E501
        :rtype: list[str]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AtmNotesResponseJsonV400.


        :param notes: The notes of this AtmNotesResponseJsonV400.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and notes is None:
            raise ValueError("Invalid value for `notes`, must not be `None`")  # noqa: E501

        self._notes = notes

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
        if issubclass(AtmNotesResponseJsonV400, dict):
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
        if not isinstance(other, AtmNotesResponseJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AtmNotesResponseJsonV400):
            return True

        return self.to_dict() != other.to_dict()
