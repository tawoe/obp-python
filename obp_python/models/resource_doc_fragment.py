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


class ResourceDocFragment(object):
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
        'request_verb': 'str',
        'request_url': 'str',
        'example_request_body': 'JsonDynamicResourceDocExampleRequestBody',
        'success_response_body': 'JsonDynamicResourceDocSuccessResponseBody'
    }

    attribute_map = {
        'request_verb': 'request_verb',
        'request_url': 'request_url',
        'example_request_body': 'example_request_body',
        'success_response_body': 'success_response_body'
    }

    def __init__(self, request_verb=None, request_url=None, example_request_body=None, success_response_body=None, _configuration=None):  # noqa: E501
        """ResourceDocFragment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._request_verb = None
        self._request_url = None
        self._example_request_body = None
        self._success_response_body = None
        self.discriminator = None

        self.request_verb = request_verb
        self.request_url = request_url
        if example_request_body is not None:
            self.example_request_body = example_request_body
        if success_response_body is not None:
            self.success_response_body = success_response_body

    @property
    def request_verb(self):
        """Gets the request_verb of this ResourceDocFragment.  # noqa: E501


        :return: The request_verb of this ResourceDocFragment.  # noqa: E501
        :rtype: str
        """
        return self._request_verb

    @request_verb.setter
    def request_verb(self, request_verb):
        """Sets the request_verb of this ResourceDocFragment.


        :param request_verb: The request_verb of this ResourceDocFragment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and request_verb is None:
            raise ValueError("Invalid value for `request_verb`, must not be `None`")  # noqa: E501

        self._request_verb = request_verb

    @property
    def request_url(self):
        """Gets the request_url of this ResourceDocFragment.  # noqa: E501


        :return: The request_url of this ResourceDocFragment.  # noqa: E501
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this ResourceDocFragment.


        :param request_url: The request_url of this ResourceDocFragment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and request_url is None:
            raise ValueError("Invalid value for `request_url`, must not be `None`")  # noqa: E501

        self._request_url = request_url

    @property
    def example_request_body(self):
        """Gets the example_request_body of this ResourceDocFragment.  # noqa: E501


        :return: The example_request_body of this ResourceDocFragment.  # noqa: E501
        :rtype: JsonDynamicResourceDocExampleRequestBody
        """
        return self._example_request_body

    @example_request_body.setter
    def example_request_body(self, example_request_body):
        """Sets the example_request_body of this ResourceDocFragment.


        :param example_request_body: The example_request_body of this ResourceDocFragment.  # noqa: E501
        :type: JsonDynamicResourceDocExampleRequestBody
        """

        self._example_request_body = example_request_body

    @property
    def success_response_body(self):
        """Gets the success_response_body of this ResourceDocFragment.  # noqa: E501


        :return: The success_response_body of this ResourceDocFragment.  # noqa: E501
        :rtype: JsonDynamicResourceDocSuccessResponseBody
        """
        return self._success_response_body

    @success_response_body.setter
    def success_response_body(self, success_response_body):
        """Sets the success_response_body of this ResourceDocFragment.


        :param success_response_body: The success_response_body of this ResourceDocFragment.  # noqa: E501
        :type: JsonDynamicResourceDocSuccessResponseBody
        """

        self._success_response_body = success_response_body

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
        if issubclass(ResourceDocFragment, dict):
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
        if not isinstance(other, ResourceDocFragment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceDocFragment):
            return True

        return self.to_dict() != other.to_dict()