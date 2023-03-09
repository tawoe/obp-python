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


class PostCustomerAddressJsonV310(object):
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
        'city': 'str',
        'line_2': 'str',
        'state': 'str',
        'tags': 'list[str]',
        'postcode': 'str',
        'county': 'str',
        'country_code': 'str',
        'status': 'str',
        'line_3': 'str',
        'line_1': 'str'
    }

    attribute_map = {
        'city': 'city',
        'line_2': 'line_2',
        'state': 'state',
        'tags': 'tags',
        'postcode': 'postcode',
        'county': 'county',
        'country_code': 'country_code',
        'status': 'status',
        'line_3': 'line_3',
        'line_1': 'line_1'
    }

    def __init__(self, city=None, line_2=None, state=None, tags=None, postcode=None, county=None, country_code=None, status=None, line_3=None, line_1=None, _configuration=None):  # noqa: E501
        """PostCustomerAddressJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._city = None
        self._line_2 = None
        self._state = None
        self._tags = None
        self._postcode = None
        self._county = None
        self._country_code = None
        self._status = None
        self._line_3 = None
        self._line_1 = None
        self.discriminator = None

        self.city = city
        self.line_2 = line_2
        self.state = state
        self.tags = tags
        self.postcode = postcode
        self.county = county
        self.country_code = country_code
        self.status = status
        self.line_3 = line_3
        self.line_1 = line_1

    @property
    def city(self):
        """Gets the city of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The city of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PostCustomerAddressJsonV310.


        :param city: The city of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def line_2(self):
        """Gets the line_2 of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The line_2 of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._line_2

    @line_2.setter
    def line_2(self, line_2):
        """Sets the line_2 of this PostCustomerAddressJsonV310.


        :param line_2: The line_2 of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and line_2 is None:
            raise ValueError("Invalid value for `line_2`, must not be `None`")  # noqa: E501

        self._line_2 = line_2

    @property
    def state(self):
        """Gets the state of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The state of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PostCustomerAddressJsonV310.


        :param state: The state of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def tags(self):
        """Gets the tags of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The tags of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PostCustomerAddressJsonV310.


        :param tags: The tags of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def postcode(self):
        """Gets the postcode of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The postcode of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this PostCustomerAddressJsonV310.


        :param postcode: The postcode of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and postcode is None:
            raise ValueError("Invalid value for `postcode`, must not be `None`")  # noqa: E501

        self._postcode = postcode

    @property
    def county(self):
        """Gets the county of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The county of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """Sets the county of this PostCustomerAddressJsonV310.


        :param county: The county of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and county is None:
            raise ValueError("Invalid value for `county`, must not be `None`")  # noqa: E501

        self._county = county

    @property
    def country_code(self):
        """Gets the country_code of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The country_code of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PostCustomerAddressJsonV310.


        :param country_code: The country_code of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def status(self):
        """Gets the status of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The status of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostCustomerAddressJsonV310.


        :param status: The status of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def line_3(self):
        """Gets the line_3 of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The line_3 of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._line_3

    @line_3.setter
    def line_3(self, line_3):
        """Sets the line_3 of this PostCustomerAddressJsonV310.


        :param line_3: The line_3 of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and line_3 is None:
            raise ValueError("Invalid value for `line_3`, must not be `None`")  # noqa: E501

        self._line_3 = line_3

    @property
    def line_1(self):
        """Gets the line_1 of this PostCustomerAddressJsonV310.  # noqa: E501


        :return: The line_1 of this PostCustomerAddressJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._line_1

    @line_1.setter
    def line_1(self, line_1):
        """Sets the line_1 of this PostCustomerAddressJsonV310.


        :param line_1: The line_1 of this PostCustomerAddressJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and line_1 is None:
            raise ValueError("Invalid value for `line_1`, must not be `None`")  # noqa: E501

        self._line_1 = line_1

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
        if issubclass(PostCustomerAddressJsonV310, dict):
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
        if not isinstance(other, PostCustomerAddressJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostCustomerAddressJsonV310):
            return True

        return self.to_dict() != other.to_dict()