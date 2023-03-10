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


class PostHistoricalTransactionResponseJson(object):
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
        'description': 'str',
        'to': 'HistoricalTransactionAccountJsonV310',
        'transaction_id': 'str',
        'transaction_request_type': 'str',
        'completed': 'date',
        'charge_policy': 'str',
        '_from': 'HistoricalTransactionAccountJsonV310',
        'value': 'AmountOfMoneyJsonV121',
        'posted': 'date'
    }

    attribute_map = {
        'description': 'description',
        'to': 'to',
        'transaction_id': 'transaction_id',
        'transaction_request_type': 'transaction_request_type',
        'completed': 'completed',
        'charge_policy': 'charge_policy',
        '_from': 'from',
        'value': 'value',
        'posted': 'posted'
    }

    def __init__(self, description=None, to=None, transaction_id=None, transaction_request_type=None, completed=None, charge_policy=None, _from=None, value=None, posted=None, _configuration=None):  # noqa: E501
        """PostHistoricalTransactionResponseJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._to = None
        self._transaction_id = None
        self._transaction_request_type = None
        self._completed = None
        self._charge_policy = None
        self.__from = None
        self._value = None
        self._posted = None
        self.discriminator = None

        self.description = description
        self.to = to
        self.transaction_id = transaction_id
        self.transaction_request_type = transaction_request_type
        self.completed = completed
        self.charge_policy = charge_policy
        self._from = _from
        self.value = value
        self.posted = posted

    @property
    def description(self):
        """Gets the description of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The description of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostHistoricalTransactionResponseJson.


        :param description: The description of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def to(self):
        """Gets the to of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The to of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: HistoricalTransactionAccountJsonV310
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PostHistoricalTransactionResponseJson.


        :param to: The to of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: HistoricalTransactionAccountJsonV310
        """
        if self._configuration.client_side_validation and to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The transaction_id of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PostHistoricalTransactionResponseJson.


        :param transaction_id: The transaction_id of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def transaction_request_type(self):
        """Gets the transaction_request_type of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The transaction_request_type of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._transaction_request_type

    @transaction_request_type.setter
    def transaction_request_type(self, transaction_request_type):
        """Sets the transaction_request_type of this PostHistoricalTransactionResponseJson.


        :param transaction_request_type: The transaction_request_type of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_request_type is None:
            raise ValueError("Invalid value for `transaction_request_type`, must not be `None`")  # noqa: E501

        self._transaction_request_type = transaction_request_type

    @property
    def completed(self):
        """Gets the completed of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The completed of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: date
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this PostHistoricalTransactionResponseJson.


        :param completed: The completed of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and completed is None:
            raise ValueError("Invalid value for `completed`, must not be `None`")  # noqa: E501

        self._completed = completed

    @property
    def charge_policy(self):
        """Gets the charge_policy of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The charge_policy of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._charge_policy

    @charge_policy.setter
    def charge_policy(self, charge_policy):
        """Sets the charge_policy of this PostHistoricalTransactionResponseJson.


        :param charge_policy: The charge_policy of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and charge_policy is None:
            raise ValueError("Invalid value for `charge_policy`, must not be `None`")  # noqa: E501

        self._charge_policy = charge_policy

    @property
    def _from(self):
        """Gets the _from of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The _from of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: HistoricalTransactionAccountJsonV310
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this PostHistoricalTransactionResponseJson.


        :param _from: The _from of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: HistoricalTransactionAccountJsonV310
        """
        if self._configuration.client_side_validation and _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def value(self):
        """Gets the value of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The value of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PostHistoricalTransactionResponseJson.


        :param value: The value of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def posted(self):
        """Gets the posted of this PostHistoricalTransactionResponseJson.  # noqa: E501


        :return: The posted of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :rtype: date
        """
        return self._posted

    @posted.setter
    def posted(self, posted):
        """Sets the posted of this PostHistoricalTransactionResponseJson.


        :param posted: The posted of this PostHistoricalTransactionResponseJson.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and posted is None:
            raise ValueError("Invalid value for `posted`, must not be `None`")  # noqa: E501

        self._posted = posted

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
        if issubclass(PostHistoricalTransactionResponseJson, dict):
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
        if not isinstance(other, PostHistoricalTransactionResponseJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostHistoricalTransactionResponseJson):
            return True

        return self.to_dict() != other.to_dict()
