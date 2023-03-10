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


class PostKycMediaJSON(object):
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
        'url': 'str',
        'customer_number': 'str',
        '_date': 'date',
        'relates_to_kyc_document_id': 'str',
        'relates_to_kyc_check_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'url': 'url',
        'customer_number': 'customer_number',
        '_date': 'date',
        'relates_to_kyc_document_id': 'relates_to_kyc_document_id',
        'relates_to_kyc_check_id': 'relates_to_kyc_check_id',
        'type': 'type'
    }

    def __init__(self, url=None, customer_number=None, _date=None, relates_to_kyc_document_id=None, relates_to_kyc_check_id=None, type=None, _configuration=None):  # noqa: E501
        """PostKycMediaJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._url = None
        self._customer_number = None
        self.__date = None
        self._relates_to_kyc_document_id = None
        self._relates_to_kyc_check_id = None
        self._type = None
        self.discriminator = None

        self.url = url
        self.customer_number = customer_number
        self._date = _date
        self.relates_to_kyc_document_id = relates_to_kyc_document_id
        self.relates_to_kyc_check_id = relates_to_kyc_check_id
        self.type = type

    @property
    def url(self):
        """Gets the url of this PostKycMediaJSON.  # noqa: E501


        :return: The url of this PostKycMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PostKycMediaJSON.


        :param url: The url of this PostKycMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def customer_number(self):
        """Gets the customer_number of this PostKycMediaJSON.  # noqa: E501


        :return: The customer_number of this PostKycMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this PostKycMediaJSON.


        :param customer_number: The customer_number of this PostKycMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def _date(self):
        """Gets the _date of this PostKycMediaJSON.  # noqa: E501


        :return: The _date of this PostKycMediaJSON.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PostKycMediaJSON.


        :param _date: The _date of this PostKycMediaJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def relates_to_kyc_document_id(self):
        """Gets the relates_to_kyc_document_id of this PostKycMediaJSON.  # noqa: E501


        :return: The relates_to_kyc_document_id of this PostKycMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._relates_to_kyc_document_id

    @relates_to_kyc_document_id.setter
    def relates_to_kyc_document_id(self, relates_to_kyc_document_id):
        """Sets the relates_to_kyc_document_id of this PostKycMediaJSON.


        :param relates_to_kyc_document_id: The relates_to_kyc_document_id of this PostKycMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relates_to_kyc_document_id is None:
            raise ValueError("Invalid value for `relates_to_kyc_document_id`, must not be `None`")  # noqa: E501

        self._relates_to_kyc_document_id = relates_to_kyc_document_id

    @property
    def relates_to_kyc_check_id(self):
        """Gets the relates_to_kyc_check_id of this PostKycMediaJSON.  # noqa: E501


        :return: The relates_to_kyc_check_id of this PostKycMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._relates_to_kyc_check_id

    @relates_to_kyc_check_id.setter
    def relates_to_kyc_check_id(self, relates_to_kyc_check_id):
        """Sets the relates_to_kyc_check_id of this PostKycMediaJSON.


        :param relates_to_kyc_check_id: The relates_to_kyc_check_id of this PostKycMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relates_to_kyc_check_id is None:
            raise ValueError("Invalid value for `relates_to_kyc_check_id`, must not be `None`")  # noqa: E501

        self._relates_to_kyc_check_id = relates_to_kyc_check_id

    @property
    def type(self):
        """Gets the type of this PostKycMediaJSON.  # noqa: E501


        :return: The type of this PostKycMediaJSON.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostKycMediaJSON.


        :param type: The type of this PostKycMediaJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(PostKycMediaJSON, dict):
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
        if not isinstance(other, PostKycMediaJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostKycMediaJSON):
            return True

        return self.to_dict() != other.to_dict()
