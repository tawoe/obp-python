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


class CustomerOverviewFlatJsonV500(object):
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
        'customer_id': 'str',
        'name_suffix': 'str',
        'email': 'str',
        'branch_id': 'str',
        'mobile_phone_number': 'str',
        'customer_number': 'str',
        'customer_attributes': 'list[CustomerAttributeResponseJsonV300]',
        'bank_id': 'str',
        'date_of_birth': 'date',
        'legal_name': 'str',
        'title': 'str',
        'accounts': 'list[AccountResponseJson500]'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'name_suffix': 'name_suffix',
        'email': 'email',
        'branch_id': 'branch_id',
        'mobile_phone_number': 'mobile_phone_number',
        'customer_number': 'customer_number',
        'customer_attributes': 'customer_attributes',
        'bank_id': 'bank_id',
        'date_of_birth': 'date_of_birth',
        'legal_name': 'legal_name',
        'title': 'title',
        'accounts': 'accounts'
    }

    def __init__(self, customer_id=None, name_suffix=None, email=None, branch_id=None, mobile_phone_number=None, customer_number=None, customer_attributes=None, bank_id=None, date_of_birth=None, legal_name=None, title=None, accounts=None, _configuration=None):  # noqa: E501
        """CustomerOverviewFlatJsonV500 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._customer_id = None
        self._name_suffix = None
        self._email = None
        self._branch_id = None
        self._mobile_phone_number = None
        self._customer_number = None
        self._customer_attributes = None
        self._bank_id = None
        self._date_of_birth = None
        self._legal_name = None
        self._title = None
        self._accounts = None
        self.discriminator = None

        self.customer_id = customer_id
        self.name_suffix = name_suffix
        self.email = email
        self.branch_id = branch_id
        self.mobile_phone_number = mobile_phone_number
        self.customer_number = customer_number
        self.customer_attributes = customer_attributes
        self.bank_id = bank_id
        self.date_of_birth = date_of_birth
        self.legal_name = legal_name
        self.title = title
        self.accounts = accounts

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The customer_id of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerOverviewFlatJsonV500.


        :param customer_id: The customer_id of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def name_suffix(self):
        """Gets the name_suffix of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The name_suffix of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._name_suffix

    @name_suffix.setter
    def name_suffix(self, name_suffix):
        """Sets the name_suffix of this CustomerOverviewFlatJsonV500.


        :param name_suffix: The name_suffix of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_suffix is None:
            raise ValueError("Invalid value for `name_suffix`, must not be `None`")  # noqa: E501

        self._name_suffix = name_suffix

    @property
    def email(self):
        """Gets the email of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The email of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerOverviewFlatJsonV500.


        :param email: The email of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def branch_id(self):
        """Gets the branch_id of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The branch_id of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this CustomerOverviewFlatJsonV500.


        :param branch_id: The branch_id of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and branch_id is None:
            raise ValueError("Invalid value for `branch_id`, must not be `None`")  # noqa: E501

        self._branch_id = branch_id

    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The mobile_phone_number of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this CustomerOverviewFlatJsonV500.


        :param mobile_phone_number: The mobile_phone_number of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mobile_phone_number is None:
            raise ValueError("Invalid value for `mobile_phone_number`, must not be `None`")  # noqa: E501

        self._mobile_phone_number = mobile_phone_number

    @property
    def customer_number(self):
        """Gets the customer_number of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The customer_number of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this CustomerOverviewFlatJsonV500.


        :param customer_number: The customer_number of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def customer_attributes(self):
        """Gets the customer_attributes of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The customer_attributes of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: list[CustomerAttributeResponseJsonV300]
        """
        return self._customer_attributes

    @customer_attributes.setter
    def customer_attributes(self, customer_attributes):
        """Sets the customer_attributes of this CustomerOverviewFlatJsonV500.


        :param customer_attributes: The customer_attributes of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: list[CustomerAttributeResponseJsonV300]
        """
        if self._configuration.client_side_validation and customer_attributes is None:
            raise ValueError("Invalid value for `customer_attributes`, must not be `None`")  # noqa: E501

        self._customer_attributes = customer_attributes

    @property
    def bank_id(self):
        """Gets the bank_id of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The bank_id of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this CustomerOverviewFlatJsonV500.


        :param bank_id: The bank_id of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The date_of_birth of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CustomerOverviewFlatJsonV500.


        :param date_of_birth: The date_of_birth of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def legal_name(self):
        """Gets the legal_name of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The legal_name of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this CustomerOverviewFlatJsonV500.


        :param legal_name: The legal_name of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and legal_name is None:
            raise ValueError("Invalid value for `legal_name`, must not be `None`")  # noqa: E501

        self._legal_name = legal_name

    @property
    def title(self):
        """Gets the title of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The title of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CustomerOverviewFlatJsonV500.


        :param title: The title of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def accounts(self):
        """Gets the accounts of this CustomerOverviewFlatJsonV500.  # noqa: E501


        :return: The accounts of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :rtype: list[AccountResponseJson500]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this CustomerOverviewFlatJsonV500.


        :param accounts: The accounts of this CustomerOverviewFlatJsonV500.  # noqa: E501
        :type: list[AccountResponseJson500]
        """
        if self._configuration.client_side_validation and accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

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
        if issubclass(CustomerOverviewFlatJsonV500, dict):
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
        if not isinstance(other, CustomerOverviewFlatJsonV500):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerOverviewFlatJsonV500):
            return True

        return self.to_dict() != other.to_dict()
