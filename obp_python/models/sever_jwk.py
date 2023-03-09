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


class SeverJWK(object):
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
        'e': 'str',
        'n': 'str',
        'kty': 'str',
        'use': 'str',
        'kid': 'str'
    }

    attribute_map = {
        'e': 'e',
        'n': 'n',
        'kty': 'kty',
        'use': 'use',
        'kid': 'kid'
    }

    def __init__(self, e=None, n=None, kty=None, use=None, kid=None, _configuration=None):  # noqa: E501
        """SeverJWK - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._e = None
        self._n = None
        self._kty = None
        self._use = None
        self._kid = None
        self.discriminator = None

        self.e = e
        self.n = n
        self.kty = kty
        self.use = use
        self.kid = kid

    @property
    def e(self):
        """Gets the e of this SeverJWK.  # noqa: E501


        :return: The e of this SeverJWK.  # noqa: E501
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """Sets the e of this SeverJWK.


        :param e: The e of this SeverJWK.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and e is None:
            raise ValueError("Invalid value for `e`, must not be `None`")  # noqa: E501

        self._e = e

    @property
    def n(self):
        """Gets the n of this SeverJWK.  # noqa: E501


        :return: The n of this SeverJWK.  # noqa: E501
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this SeverJWK.


        :param n: The n of this SeverJWK.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and n is None:
            raise ValueError("Invalid value for `n`, must not be `None`")  # noqa: E501

        self._n = n

    @property
    def kty(self):
        """Gets the kty of this SeverJWK.  # noqa: E501


        :return: The kty of this SeverJWK.  # noqa: E501
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """Sets the kty of this SeverJWK.


        :param kty: The kty of this SeverJWK.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and kty is None:
            raise ValueError("Invalid value for `kty`, must not be `None`")  # noqa: E501

        self._kty = kty

    @property
    def use(self):
        """Gets the use of this SeverJWK.  # noqa: E501


        :return: The use of this SeverJWK.  # noqa: E501
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """Sets the use of this SeverJWK.


        :param use: The use of this SeverJWK.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and use is None:
            raise ValueError("Invalid value for `use`, must not be `None`")  # noqa: E501

        self._use = use

    @property
    def kid(self):
        """Gets the kid of this SeverJWK.  # noqa: E501


        :return: The kid of this SeverJWK.  # noqa: E501
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """Sets the kid of this SeverJWK.


        :param kid: The kid of this SeverJWK.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and kid is None:
            raise ValueError("Invalid value for `kid`, must not be `None`")  # noqa: E501

        self._kid = kid

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
        if issubclass(SeverJWK, dict):
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
        if not isinstance(other, SeverJWK):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SeverJWK):
            return True

        return self.to_dict() != other.to_dict()
