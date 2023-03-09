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


class InboundStatusMessage(object):
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
        'duration': 'str',
        'source': 'str',
        'text': 'str',
        'error_code': 'str',
        'status': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'source': 'source',
        'text': 'text',
        'error_code': 'errorCode',
        'status': 'status'
    }

    def __init__(self, duration=None, source=None, text=None, error_code=None, status=None, _configuration=None):  # noqa: E501
        """InboundStatusMessage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._duration = None
        self._source = None
        self._text = None
        self._error_code = None
        self._status = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        self.source = source
        self.text = text
        self.error_code = error_code
        self.status = status

    @property
    def duration(self):
        """Gets the duration of this InboundStatusMessage.  # noqa: E501


        :return: The duration of this InboundStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InboundStatusMessage.


        :param duration: The duration of this InboundStatusMessage.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def source(self):
        """Gets the source of this InboundStatusMessage.  # noqa: E501


        :return: The source of this InboundStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InboundStatusMessage.


        :param source: The source of this InboundStatusMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def text(self):
        """Gets the text of this InboundStatusMessage.  # noqa: E501


        :return: The text of this InboundStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InboundStatusMessage.


        :param text: The text of this InboundStatusMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def error_code(self):
        """Gets the error_code of this InboundStatusMessage.  # noqa: E501


        :return: The error_code of this InboundStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InboundStatusMessage.


        :param error_code: The error_code of this InboundStatusMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def status(self):
        """Gets the status of this InboundStatusMessage.  # noqa: E501


        :return: The status of this InboundStatusMessage.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InboundStatusMessage.


        :param status: The status of this InboundStatusMessage.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if issubclass(InboundStatusMessage, dict):
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
        if not isinstance(other, InboundStatusMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboundStatusMessage):
            return True

        return self.to_dict() != other.to_dict()
