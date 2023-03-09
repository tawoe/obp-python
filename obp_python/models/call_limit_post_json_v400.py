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


class CallLimitPostJsonV400(object):
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
        'per_month_call_limit': 'str',
        'per_week_call_limit': 'str',
        'api_version': 'str',
        'per_hour_call_limit': 'str',
        'bank_id': 'str',
        'per_second_call_limit': 'str',
        'from_date': 'date',
        'api_name': 'str',
        'per_minute_call_limit': 'str',
        'per_day_call_limit': 'str',
        'to_date': 'date'
    }

    attribute_map = {
        'per_month_call_limit': 'per_month_call_limit',
        'per_week_call_limit': 'per_week_call_limit',
        'api_version': 'api_version',
        'per_hour_call_limit': 'per_hour_call_limit',
        'bank_id': 'bank_id',
        'per_second_call_limit': 'per_second_call_limit',
        'from_date': 'from_date',
        'api_name': 'api_name',
        'per_minute_call_limit': 'per_minute_call_limit',
        'per_day_call_limit': 'per_day_call_limit',
        'to_date': 'to_date'
    }

    def __init__(self, per_month_call_limit=None, per_week_call_limit=None, api_version=None, per_hour_call_limit=None, bank_id=None, per_second_call_limit=None, from_date=None, api_name=None, per_minute_call_limit=None, per_day_call_limit=None, to_date=None, _configuration=None):  # noqa: E501
        """CallLimitPostJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._per_month_call_limit = None
        self._per_week_call_limit = None
        self._api_version = None
        self._per_hour_call_limit = None
        self._bank_id = None
        self._per_second_call_limit = None
        self._from_date = None
        self._api_name = None
        self._per_minute_call_limit = None
        self._per_day_call_limit = None
        self._to_date = None
        self.discriminator = None

        self.per_month_call_limit = per_month_call_limit
        self.per_week_call_limit = per_week_call_limit
        if api_version is not None:
            self.api_version = api_version
        self.per_hour_call_limit = per_hour_call_limit
        if bank_id is not None:
            self.bank_id = bank_id
        self.per_second_call_limit = per_second_call_limit
        self.from_date = from_date
        if api_name is not None:
            self.api_name = api_name
        self.per_minute_call_limit = per_minute_call_limit
        self.per_day_call_limit = per_day_call_limit
        self.to_date = to_date

    @property
    def per_month_call_limit(self):
        """Gets the per_month_call_limit of this CallLimitPostJsonV400.  # noqa: E501


        :return: The per_month_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._per_month_call_limit

    @per_month_call_limit.setter
    def per_month_call_limit(self, per_month_call_limit):
        """Sets the per_month_call_limit of this CallLimitPostJsonV400.


        :param per_month_call_limit: The per_month_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_month_call_limit is None:
            raise ValueError("Invalid value for `per_month_call_limit`, must not be `None`")  # noqa: E501

        self._per_month_call_limit = per_month_call_limit

    @property
    def per_week_call_limit(self):
        """Gets the per_week_call_limit of this CallLimitPostJsonV400.  # noqa: E501


        :return: The per_week_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._per_week_call_limit

    @per_week_call_limit.setter
    def per_week_call_limit(self, per_week_call_limit):
        """Sets the per_week_call_limit of this CallLimitPostJsonV400.


        :param per_week_call_limit: The per_week_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_week_call_limit is None:
            raise ValueError("Invalid value for `per_week_call_limit`, must not be `None`")  # noqa: E501

        self._per_week_call_limit = per_week_call_limit

    @property
    def api_version(self):
        """Gets the api_version of this CallLimitPostJsonV400.  # noqa: E501


        :return: The api_version of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this CallLimitPostJsonV400.


        :param api_version: The api_version of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def per_hour_call_limit(self):
        """Gets the per_hour_call_limit of this CallLimitPostJsonV400.  # noqa: E501


        :return: The per_hour_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._per_hour_call_limit

    @per_hour_call_limit.setter
    def per_hour_call_limit(self, per_hour_call_limit):
        """Sets the per_hour_call_limit of this CallLimitPostJsonV400.


        :param per_hour_call_limit: The per_hour_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_hour_call_limit is None:
            raise ValueError("Invalid value for `per_hour_call_limit`, must not be `None`")  # noqa: E501

        self._per_hour_call_limit = per_hour_call_limit

    @property
    def bank_id(self):
        """Gets the bank_id of this CallLimitPostJsonV400.  # noqa: E501


        :return: The bank_id of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this CallLimitPostJsonV400.


        :param bank_id: The bank_id of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """

        self._bank_id = bank_id

    @property
    def per_second_call_limit(self):
        """Gets the per_second_call_limit of this CallLimitPostJsonV400.  # noqa: E501


        :return: The per_second_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._per_second_call_limit

    @per_second_call_limit.setter
    def per_second_call_limit(self, per_second_call_limit):
        """Sets the per_second_call_limit of this CallLimitPostJsonV400.


        :param per_second_call_limit: The per_second_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_second_call_limit is None:
            raise ValueError("Invalid value for `per_second_call_limit`, must not be `None`")  # noqa: E501

        self._per_second_call_limit = per_second_call_limit

    @property
    def from_date(self):
        """Gets the from_date of this CallLimitPostJsonV400.  # noqa: E501


        :return: The from_date of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this CallLimitPostJsonV400.


        :param from_date: The from_date of this CallLimitPostJsonV400.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and from_date is None:
            raise ValueError("Invalid value for `from_date`, must not be `None`")  # noqa: E501

        self._from_date = from_date

    @property
    def api_name(self):
        """Gets the api_name of this CallLimitPostJsonV400.  # noqa: E501


        :return: The api_name of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this CallLimitPostJsonV400.


        :param api_name: The api_name of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """

        self._api_name = api_name

    @property
    def per_minute_call_limit(self):
        """Gets the per_minute_call_limit of this CallLimitPostJsonV400.  # noqa: E501


        :return: The per_minute_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._per_minute_call_limit

    @per_minute_call_limit.setter
    def per_minute_call_limit(self, per_minute_call_limit):
        """Sets the per_minute_call_limit of this CallLimitPostJsonV400.


        :param per_minute_call_limit: The per_minute_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_minute_call_limit is None:
            raise ValueError("Invalid value for `per_minute_call_limit`, must not be `None`")  # noqa: E501

        self._per_minute_call_limit = per_minute_call_limit

    @property
    def per_day_call_limit(self):
        """Gets the per_day_call_limit of this CallLimitPostJsonV400.  # noqa: E501


        :return: The per_day_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._per_day_call_limit

    @per_day_call_limit.setter
    def per_day_call_limit(self, per_day_call_limit):
        """Sets the per_day_call_limit of this CallLimitPostJsonV400.


        :param per_day_call_limit: The per_day_call_limit of this CallLimitPostJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_day_call_limit is None:
            raise ValueError("Invalid value for `per_day_call_limit`, must not be `None`")  # noqa: E501

        self._per_day_call_limit = per_day_call_limit

    @property
    def to_date(self):
        """Gets the to_date of this CallLimitPostJsonV400.  # noqa: E501


        :return: The to_date of this CallLimitPostJsonV400.  # noqa: E501
        :rtype: date
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this CallLimitPostJsonV400.


        :param to_date: The to_date of this CallLimitPostJsonV400.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and to_date is None:
            raise ValueError("Invalid value for `to_date`, must not be `None`")  # noqa: E501

        self._to_date = to_date

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
        if issubclass(CallLimitPostJsonV400, dict):
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
        if not isinstance(other, CallLimitPostJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallLimitPostJsonV400):
            return True

        return self.to_dict() != other.to_dict()
