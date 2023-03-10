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


class PostApiCollectionJson400(object):
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
        'api_collection_name': 'str',
        'is_sharable': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'api_collection_name': 'api_collection_name',
        'is_sharable': 'is_sharable',
        'description': 'description'
    }

    def __init__(self, api_collection_name=None, is_sharable=None, description=None, _configuration=None):  # noqa: E501
        """PostApiCollectionJson400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_collection_name = None
        self._is_sharable = None
        self._description = None
        self.discriminator = None

        self.api_collection_name = api_collection_name
        self.is_sharable = is_sharable
        if description is not None:
            self.description = description

    @property
    def api_collection_name(self):
        """Gets the api_collection_name of this PostApiCollectionJson400.  # noqa: E501


        :return: The api_collection_name of this PostApiCollectionJson400.  # noqa: E501
        :rtype: str
        """
        return self._api_collection_name

    @api_collection_name.setter
    def api_collection_name(self, api_collection_name):
        """Sets the api_collection_name of this PostApiCollectionJson400.


        :param api_collection_name: The api_collection_name of this PostApiCollectionJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and api_collection_name is None:
            raise ValueError("Invalid value for `api_collection_name`, must not be `None`")  # noqa: E501

        self._api_collection_name = api_collection_name

    @property
    def is_sharable(self):
        """Gets the is_sharable of this PostApiCollectionJson400.  # noqa: E501


        :return: The is_sharable of this PostApiCollectionJson400.  # noqa: E501
        :rtype: bool
        """
        return self._is_sharable

    @is_sharable.setter
    def is_sharable(self, is_sharable):
        """Sets the is_sharable of this PostApiCollectionJson400.


        :param is_sharable: The is_sharable of this PostApiCollectionJson400.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_sharable is None:
            raise ValueError("Invalid value for `is_sharable`, must not be `None`")  # noqa: E501

        self._is_sharable = is_sharable

    @property
    def description(self):
        """Gets the description of this PostApiCollectionJson400.  # noqa: E501


        :return: The description of this PostApiCollectionJson400.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostApiCollectionJson400.


        :param description: The description of this PostApiCollectionJson400.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(PostApiCollectionJson400, dict):
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
        if not isinstance(other, PostApiCollectionJson400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostApiCollectionJson400):
            return True

        return self.to_dict() != other.to_dict()
