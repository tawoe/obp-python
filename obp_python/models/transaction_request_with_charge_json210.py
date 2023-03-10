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


class TransactionRequestWithChargeJSON210(object):
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
        'challenge': 'ChallengeJsonV140',
        'start_date': 'date',
        'id': 'str',
        'end_date': 'date',
        'status': 'str',
        '_from': 'TransactionRequestAccountJsonV140',
        'details': 'TransactionRequestBodyAllTypes',
        'charge': 'TransactionRequestChargeJsonV200',
        'type': 'str',
        'transaction_ids': 'list[str]'
    }

    attribute_map = {
        'challenge': 'challenge',
        'start_date': 'start_date',
        'id': 'id',
        'end_date': 'end_date',
        'status': 'status',
        '_from': 'from',
        'details': 'details',
        'charge': 'charge',
        'type': 'type',
        'transaction_ids': 'transaction_ids'
    }

    def __init__(self, challenge=None, start_date=None, id=None, end_date=None, status=None, _from=None, details=None, charge=None, type=None, transaction_ids=None, _configuration=None):  # noqa: E501
        """TransactionRequestWithChargeJSON210 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._challenge = None
        self._start_date = None
        self._id = None
        self._end_date = None
        self._status = None
        self.__from = None
        self._details = None
        self._charge = None
        self._type = None
        self._transaction_ids = None
        self.discriminator = None

        self.challenge = challenge
        self.start_date = start_date
        self.id = id
        self.end_date = end_date
        self.status = status
        self._from = _from
        self.details = details
        self.charge = charge
        self.type = type
        self.transaction_ids = transaction_ids

    @property
    def challenge(self):
        """Gets the challenge of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The challenge of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: ChallengeJsonV140
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this TransactionRequestWithChargeJSON210.


        :param challenge: The challenge of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: ChallengeJsonV140
        """
        if self._configuration.client_side_validation and challenge is None:
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def start_date(self):
        """Gets the start_date of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The start_date of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TransactionRequestWithChargeJSON210.


        :param start_date: The start_date of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def id(self):
        """Gets the id of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The id of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionRequestWithChargeJSON210.


        :param id: The id of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def end_date(self):
        """Gets the end_date of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The end_date of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TransactionRequestWithChargeJSON210.


        :param end_date: The end_date of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def status(self):
        """Gets the status of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The status of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionRequestWithChargeJSON210.


        :param status: The status of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def _from(self):
        """Gets the _from of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The _from of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: TransactionRequestAccountJsonV140
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this TransactionRequestWithChargeJSON210.


        :param _from: The _from of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: TransactionRequestAccountJsonV140
        """
        if self._configuration.client_side_validation and _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def details(self):
        """Gets the details of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The details of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: TransactionRequestBodyAllTypes
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this TransactionRequestWithChargeJSON210.


        :param details: The details of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: TransactionRequestBodyAllTypes
        """
        if self._configuration.client_side_validation and details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def charge(self):
        """Gets the charge of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The charge of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: TransactionRequestChargeJsonV200
        """
        return self._charge

    @charge.setter
    def charge(self, charge):
        """Sets the charge of this TransactionRequestWithChargeJSON210.


        :param charge: The charge of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: TransactionRequestChargeJsonV200
        """
        if self._configuration.client_side_validation and charge is None:
            raise ValueError("Invalid value for `charge`, must not be `None`")  # noqa: E501

        self._charge = charge

    @property
    def type(self):
        """Gets the type of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The type of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionRequestWithChargeJSON210.


        :param type: The type of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def transaction_ids(self):
        """Gets the transaction_ids of this TransactionRequestWithChargeJSON210.  # noqa: E501


        :return: The transaction_ids of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :rtype: list[str]
        """
        return self._transaction_ids

    @transaction_ids.setter
    def transaction_ids(self, transaction_ids):
        """Sets the transaction_ids of this TransactionRequestWithChargeJSON210.


        :param transaction_ids: The transaction_ids of this TransactionRequestWithChargeJSON210.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and transaction_ids is None:
            raise ValueError("Invalid value for `transaction_ids`, must not be `None`")  # noqa: E501

        self._transaction_ids = transaction_ids

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
        if issubclass(TransactionRequestWithChargeJSON210, dict):
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
        if not isinstance(other, TransactionRequestWithChargeJSON210):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionRequestWithChargeJSON210):
            return True

        return self.to_dict() != other.to_dict()
