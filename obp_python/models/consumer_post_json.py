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


class ConsumerPostJSON(object):
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
        'app_type': 'str',
        'description': 'str',
        'enabled': 'bool',
        'redirect_url': 'str',
        'developer_email': 'str',
        'client_certificate': 'str',
        'app_name': 'str',
        'created': 'date'
    }

    attribute_map = {
        'created_by_user_id': 'created_by_user_id',
        'app_type': 'app_type',
        'description': 'description',
        'enabled': 'enabled',
        'redirect_url': 'redirect_url',
        'developer_email': 'developer_email',
        'client_certificate': 'clientCertificate',
        'app_name': 'app_name',
        'created': 'created'
    }

    def __init__(self, created_by_user_id=None, app_type=None, description=None, enabled=None, redirect_url=None, developer_email=None, client_certificate=None, app_name=None, created=None, _configuration=None):  # noqa: E501
        """ConsumerPostJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_by_user_id = None
        self._app_type = None
        self._description = None
        self._enabled = None
        self._redirect_url = None
        self._developer_email = None
        self._client_certificate = None
        self._app_name = None
        self._created = None
        self.discriminator = None

        self.created_by_user_id = created_by_user_id
        self.app_type = app_type
        self.description = description
        self.enabled = enabled
        self.redirect_url = redirect_url
        self.developer_email = developer_email
        self.client_certificate = client_certificate
        self.app_name = app_name
        self.created = created

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this ConsumerPostJSON.  # noqa: E501


        :return: The created_by_user_id of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this ConsumerPostJSON.


        :param created_by_user_id: The created_by_user_id of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and created_by_user_id is None:
            raise ValueError("Invalid value for `created_by_user_id`, must not be `None`")  # noqa: E501

        self._created_by_user_id = created_by_user_id

    @property
    def app_type(self):
        """Gets the app_type of this ConsumerPostJSON.  # noqa: E501


        :return: The app_type of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ConsumerPostJSON.


        :param app_type: The app_type of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and app_type is None:
            raise ValueError("Invalid value for `app_type`, must not be `None`")  # noqa: E501

        self._app_type = app_type

    @property
    def description(self):
        """Gets the description of this ConsumerPostJSON.  # noqa: E501


        :return: The description of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConsumerPostJSON.


        :param description: The description of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ConsumerPostJSON.  # noqa: E501


        :return: The enabled of this ConsumerPostJSON.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConsumerPostJSON.


        :param enabled: The enabled of this ConsumerPostJSON.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def redirect_url(self):
        """Gets the redirect_url of this ConsumerPostJSON.  # noqa: E501


        :return: The redirect_url of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this ConsumerPostJSON.


        :param redirect_url: The redirect_url of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and redirect_url is None:
            raise ValueError("Invalid value for `redirect_url`, must not be `None`")  # noqa: E501

        self._redirect_url = redirect_url

    @property
    def developer_email(self):
        """Gets the developer_email of this ConsumerPostJSON.  # noqa: E501


        :return: The developer_email of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._developer_email

    @developer_email.setter
    def developer_email(self, developer_email):
        """Sets the developer_email of this ConsumerPostJSON.


        :param developer_email: The developer_email of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and developer_email is None:
            raise ValueError("Invalid value for `developer_email`, must not be `None`")  # noqa: E501

        self._developer_email = developer_email

    @property
    def client_certificate(self):
        """Gets the client_certificate of this ConsumerPostJSON.  # noqa: E501


        :return: The client_certificate of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._client_certificate

    @client_certificate.setter
    def client_certificate(self, client_certificate):
        """Sets the client_certificate of this ConsumerPostJSON.


        :param client_certificate: The client_certificate of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and client_certificate is None:
            raise ValueError("Invalid value for `client_certificate`, must not be `None`")  # noqa: E501

        self._client_certificate = client_certificate

    @property
    def app_name(self):
        """Gets the app_name of this ConsumerPostJSON.  # noqa: E501


        :return: The app_name of this ConsumerPostJSON.  # noqa: E501
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ConsumerPostJSON.


        :param app_name: The app_name of this ConsumerPostJSON.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

    @property
    def created(self):
        """Gets the created of this ConsumerPostJSON.  # noqa: E501


        :return: The created of this ConsumerPostJSON.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConsumerPostJSON.


        :param created: The created of this ConsumerPostJSON.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

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
        if issubclass(ConsumerPostJSON, dict):
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
        if not isinstance(other, ConsumerPostJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConsumerPostJSON):
            return True

        return self.to_dict() != other.to_dict()
