# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2023. Licensed under the AGPL and commercial licences.

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class InlineResponse2007Endpointmappings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, operation_id=None, request_mapping=None, response_mapping=None, endpoint_mapping_id=None):
        """
        InlineResponse2007Endpointmappings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operation_id': 'str',
            'request_mapping': 'object',
            'response_mapping': 'InlineResponse2007ResponseMapping',
            'endpoint_mapping_id': 'str'
        }

        self.attribute_map = {
            'operation_id': 'operation_id',
            'request_mapping': 'request_mapping',
            'response_mapping': 'response_mapping',
            'endpoint_mapping_id': 'endpoint_mapping_id'
        }

        self._operation_id = operation_id
        self._request_mapping = request_mapping
        self._response_mapping = response_mapping
        self._endpoint_mapping_id = endpoint_mapping_id

    @property
    def operation_id(self):
        """
        Gets the operation_id of this InlineResponse2007Endpointmappings.


        :return: The operation_id of this InlineResponse2007Endpointmappings.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """
        Sets the operation_id of this InlineResponse2007Endpointmappings.


        :param operation_id: The operation_id of this InlineResponse2007Endpointmappings.
        :type: str
        """

        self._operation_id = operation_id

    @property
    def request_mapping(self):
        """
        Gets the request_mapping of this InlineResponse2007Endpointmappings.


        :return: The request_mapping of this InlineResponse2007Endpointmappings.
        :rtype: object
        """
        return self._request_mapping

    @request_mapping.setter
    def request_mapping(self, request_mapping):
        """
        Sets the request_mapping of this InlineResponse2007Endpointmappings.


        :param request_mapping: The request_mapping of this InlineResponse2007Endpointmappings.
        :type: object
        """

        self._request_mapping = request_mapping

    @property
    def response_mapping(self):
        """
        Gets the response_mapping of this InlineResponse2007Endpointmappings.


        :return: The response_mapping of this InlineResponse2007Endpointmappings.
        :rtype: InlineResponse2007ResponseMapping
        """
        return self._response_mapping

    @response_mapping.setter
    def response_mapping(self, response_mapping):
        """
        Sets the response_mapping of this InlineResponse2007Endpointmappings.


        :param response_mapping: The response_mapping of this InlineResponse2007Endpointmappings.
        :type: InlineResponse2007ResponseMapping
        """

        self._response_mapping = response_mapping

    @property
    def endpoint_mapping_id(self):
        """
        Gets the endpoint_mapping_id of this InlineResponse2007Endpointmappings.


        :return: The endpoint_mapping_id of this InlineResponse2007Endpointmappings.
        :rtype: str
        """
        return self._endpoint_mapping_id

    @endpoint_mapping_id.setter
    def endpoint_mapping_id(self, endpoint_mapping_id):
        """
        Sets the endpoint_mapping_id of this InlineResponse2007Endpointmappings.


        :param endpoint_mapping_id: The endpoint_mapping_id of this InlineResponse2007Endpointmappings.
        :type: str
        """

        self._endpoint_mapping_id = endpoint_mapping_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other