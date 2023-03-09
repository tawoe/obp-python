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


class AccountV310Json(object):
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
        'account_routings': 'list[AccountRoutingJsonV121]',
        'account_type': 'str',
        'bank_id': 'str',
        'account_id': 'str',
        'branch_routings': 'list[BranchRoutingJsonV141]'
    }

    attribute_map = {
        'account_routings': 'account_routings',
        'account_type': 'account_type',
        'bank_id': 'bank_id',
        'account_id': 'account_id',
        'branch_routings': 'branch_routings'
    }

    def __init__(self, account_routings=None, account_type=None, bank_id=None, account_id=None, branch_routings=None, _configuration=None):  # noqa: E501
        """AccountV310Json - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_routings = None
        self._account_type = None
        self._bank_id = None
        self._account_id = None
        self._branch_routings = None
        self.discriminator = None

        self.account_routings = account_routings
        self.account_type = account_type
        self.bank_id = bank_id
        self.account_id = account_id
        self.branch_routings = branch_routings

    @property
    def account_routings(self):
        """Gets the account_routings of this AccountV310Json.  # noqa: E501


        :return: The account_routings of this AccountV310Json.  # noqa: E501
        :rtype: list[AccountRoutingJsonV121]
        """
        return self._account_routings

    @account_routings.setter
    def account_routings(self, account_routings):
        """Sets the account_routings of this AccountV310Json.


        :param account_routings: The account_routings of this AccountV310Json.  # noqa: E501
        :type: list[AccountRoutingJsonV121]
        """
        if self._configuration.client_side_validation and account_routings is None:
            raise ValueError("Invalid value for `account_routings`, must not be `None`")  # noqa: E501

        self._account_routings = account_routings

    @property
    def account_type(self):
        """Gets the account_type of this AccountV310Json.  # noqa: E501


        :return: The account_type of this AccountV310Json.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountV310Json.


        :param account_type: The account_type of this AccountV310Json.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def bank_id(self):
        """Gets the bank_id of this AccountV310Json.  # noqa: E501


        :return: The bank_id of this AccountV310Json.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this AccountV310Json.


        :param bank_id: The bank_id of this AccountV310Json.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def account_id(self):
        """Gets the account_id of this AccountV310Json.  # noqa: E501


        :return: The account_id of this AccountV310Json.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountV310Json.


        :param account_id: The account_id of this AccountV310Json.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def branch_routings(self):
        """Gets the branch_routings of this AccountV310Json.  # noqa: E501


        :return: The branch_routings of this AccountV310Json.  # noqa: E501
        :rtype: list[BranchRoutingJsonV141]
        """
        return self._branch_routings

    @branch_routings.setter
    def branch_routings(self, branch_routings):
        """Sets the branch_routings of this AccountV310Json.


        :param branch_routings: The branch_routings of this AccountV310Json.  # noqa: E501
        :type: list[BranchRoutingJsonV141]
        """
        if self._configuration.client_side_validation and branch_routings is None:
            raise ValueError("Invalid value for `branch_routings`, must not be `None`")  # noqa: E501

        self._branch_routings = branch_routings

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
        if issubclass(AccountV310Json, dict):
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
        if not isinstance(other, AccountV310Json):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountV310Json):
            return True

        return self.to_dict() != other.to_dict()
