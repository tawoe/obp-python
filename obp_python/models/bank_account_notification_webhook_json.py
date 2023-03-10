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


class BankAccountNotificationWebhookJson(object):
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
        'created_by_user_id': 'str',
        'url': 'str',
        'trigger_name': 'str',
        'http_protocol': 'str',
        'http_method': 'str',
        'bank_id': 'str',
        'webhook_id': 'str'
    }

    attribute_map = {
        'created_by_user_id': 'created_by_user_id',
        'url': 'url',
        'trigger_name': 'trigger_name',
        'http_protocol': 'http_protocol',
        'http_method': 'http_method',
        'bank_id': 'bank_id',
        'webhook_id': 'webhook_id'
    }

    def __init__(self, created_by_user_id=None, url=None, trigger_name=None, http_protocol=None, http_method=None, bank_id=None, webhook_id=None, _configuration=None):  # noqa: E501
        """BankAccountNotificationWebhookJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_by_user_id = None
        self._url = None
        self._trigger_name = None
        self._http_protocol = None
        self._http_method = None
        self._bank_id = None
        self._webhook_id = None
        self.discriminator = None

        self.created_by_user_id = created_by_user_id
        self.url = url
        self.trigger_name = trigger_name
        self.http_protocol = http_protocol
        self.http_method = http_method
        self.bank_id = bank_id
        self.webhook_id = webhook_id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The created_by_user_id of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this BankAccountNotificationWebhookJson.


        :param created_by_user_id: The created_by_user_id of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and created_by_user_id is None:
            raise ValueError("Invalid value for `created_by_user_id`, must not be `None`")  # noqa: E501

        self._created_by_user_id = created_by_user_id

    @property
    def url(self):
        """Gets the url of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The url of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BankAccountNotificationWebhookJson.


        :param url: The url of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def trigger_name(self):
        """Gets the trigger_name of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The trigger_name of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        """Sets the trigger_name of this BankAccountNotificationWebhookJson.


        :param trigger_name: The trigger_name of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and trigger_name is None:
            raise ValueError("Invalid value for `trigger_name`, must not be `None`")  # noqa: E501

        self._trigger_name = trigger_name

    @property
    def http_protocol(self):
        """Gets the http_protocol of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The http_protocol of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._http_protocol

    @http_protocol.setter
    def http_protocol(self, http_protocol):
        """Sets the http_protocol of this BankAccountNotificationWebhookJson.


        :param http_protocol: The http_protocol of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and http_protocol is None:
            raise ValueError("Invalid value for `http_protocol`, must not be `None`")  # noqa: E501

        self._http_protocol = http_protocol

    @property
    def http_method(self):
        """Gets the http_method of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The http_method of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this BankAccountNotificationWebhookJson.


        :param http_method: The http_method of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and http_method is None:
            raise ValueError("Invalid value for `http_method`, must not be `None`")  # noqa: E501

        self._http_method = http_method

    @property
    def bank_id(self):
        """Gets the bank_id of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The bank_id of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this BankAccountNotificationWebhookJson.


        :param bank_id: The bank_id of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this BankAccountNotificationWebhookJson.  # noqa: E501


        :return: The webhook_id of this BankAccountNotificationWebhookJson.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this BankAccountNotificationWebhookJson.


        :param webhook_id: The webhook_id of this BankAccountNotificationWebhookJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and webhook_id is None:
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

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
        if issubclass(BankAccountNotificationWebhookJson, dict):
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
        if not isinstance(other, BankAccountNotificationWebhookJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BankAccountNotificationWebhookJson):
            return True

        return self.to_dict() != other.to_dict()
