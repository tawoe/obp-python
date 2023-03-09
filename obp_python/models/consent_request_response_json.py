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


class ConsentRequestResponseJson(object):
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
        'consent_request_id': 'str',
        'payload': 'ConsentRequestResponseJsonPayload',
        'consumer_id': 'str'
    }

    attribute_map = {
        'consent_request_id': 'consent_request_id',
        'payload': 'payload',
        'consumer_id': 'consumer_id'
    }

    def __init__(self, consent_request_id=None, payload=None, consumer_id=None, _configuration=None):  # noqa: E501
        """ConsentRequestResponseJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._consent_request_id = None
        self._payload = None
        self._consumer_id = None
        self.discriminator = None

        self.consent_request_id = consent_request_id
        self.payload = payload
        self.consumer_id = consumer_id

    @property
    def consent_request_id(self):
        """Gets the consent_request_id of this ConsentRequestResponseJson.  # noqa: E501


        :return: The consent_request_id of this ConsentRequestResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._consent_request_id

    @consent_request_id.setter
    def consent_request_id(self, consent_request_id):
        """Sets the consent_request_id of this ConsentRequestResponseJson.


        :param consent_request_id: The consent_request_id of this ConsentRequestResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and consent_request_id is None:
            raise ValueError("Invalid value for `consent_request_id`, must not be `None`")  # noqa: E501

        self._consent_request_id = consent_request_id

    @property
    def payload(self):
        """Gets the payload of this ConsentRequestResponseJson.  # noqa: E501


        :return: The payload of this ConsentRequestResponseJson.  # noqa: E501
        :rtype: ConsentRequestResponseJsonPayload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ConsentRequestResponseJson.


        :param payload: The payload of this ConsentRequestResponseJson.  # noqa: E501
        :type: ConsentRequestResponseJsonPayload
        """
        if self._configuration.client_side_validation and payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def consumer_id(self):
        """Gets the consumer_id of this ConsentRequestResponseJson.  # noqa: E501


        :return: The consumer_id of this ConsentRequestResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        """Sets the consumer_id of this ConsentRequestResponseJson.


        :param consumer_id: The consumer_id of this ConsentRequestResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and consumer_id is None:
            raise ValueError("Invalid value for `consumer_id`, must not be `None`")  # noqa: E501

        self._consumer_id = consumer_id

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
        if issubclass(ConsentRequestResponseJson, dict):
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
        if not isinstance(other, ConsentRequestResponseJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsentRequestResponseJson):
            return True

        return self.to_dict() != other.to_dict()
