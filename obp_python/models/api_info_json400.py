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


class APIInfoJson400(object):
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
        'local_identity_provider': 'str',
        'resource_docs_requires_role': 'bool',
        'hostname': 'str',
        'version_status': 'str',
        'version': 'str',
        'hosted_at': 'HostedAt400',
        'connector': 'str',
        'energy_source': 'EnergySource400',
        'hosted_by': 'HostedBy400',
        'git_commit': 'str'
    }

    attribute_map = {
        'local_identity_provider': 'local_identity_provider',
        'resource_docs_requires_role': 'resource_docs_requires_role',
        'hostname': 'hostname',
        'version_status': 'version_status',
        'version': 'version',
        'hosted_at': 'hosted_at',
        'connector': 'connector',
        'energy_source': 'energy_source',
        'hosted_by': 'hosted_by',
        'git_commit': 'git_commit'
    }

    def __init__(self, local_identity_provider=None, resource_docs_requires_role=None, hostname=None, version_status=None, version=None, hosted_at=None, connector=None, energy_source=None, hosted_by=None, git_commit=None, _configuration=None):  # noqa: E501
        """APIInfoJson400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._local_identity_provider = None
        self._resource_docs_requires_role = None
        self._hostname = None
        self._version_status = None
        self._version = None
        self._hosted_at = None
        self._connector = None
        self._energy_source = None
        self._hosted_by = None
        self._git_commit = None
        self.discriminator = None

        self.local_identity_provider = local_identity_provider
        self.resource_docs_requires_role = resource_docs_requires_role
        self.hostname = hostname
        self.version_status = version_status
        self.version = version
        self.hosted_at = hosted_at
        self.connector = connector
        self.energy_source = energy_source
        self.hosted_by = hosted_by
        self.git_commit = git_commit

    @property
    def local_identity_provider(self):
        """Gets the local_identity_provider of this APIInfoJson400.  # noqa: E501


        :return: The local_identity_provider of this APIInfoJson400.  # noqa: E501
        :rtype: str
        """
        return self._local_identity_provider

    @local_identity_provider.setter
    def local_identity_provider(self, local_identity_provider):
        """Sets the local_identity_provider of this APIInfoJson400.


        :param local_identity_provider: The local_identity_provider of this APIInfoJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and local_identity_provider is None:
            raise ValueError("Invalid value for `local_identity_provider`, must not be `None`")  # noqa: E501

        self._local_identity_provider = local_identity_provider

    @property
    def resource_docs_requires_role(self):
        """Gets the resource_docs_requires_role of this APIInfoJson400.  # noqa: E501


        :return: The resource_docs_requires_role of this APIInfoJson400.  # noqa: E501
        :rtype: bool
        """
        return self._resource_docs_requires_role

    @resource_docs_requires_role.setter
    def resource_docs_requires_role(self, resource_docs_requires_role):
        """Sets the resource_docs_requires_role of this APIInfoJson400.


        :param resource_docs_requires_role: The resource_docs_requires_role of this APIInfoJson400.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and resource_docs_requires_role is None:
            raise ValueError("Invalid value for `resource_docs_requires_role`, must not be `None`")  # noqa: E501

        self._resource_docs_requires_role = resource_docs_requires_role

    @property
    def hostname(self):
        """Gets the hostname of this APIInfoJson400.  # noqa: E501


        :return: The hostname of this APIInfoJson400.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this APIInfoJson400.


        :param hostname: The hostname of this APIInfoJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def version_status(self):
        """Gets the version_status of this APIInfoJson400.  # noqa: E501


        :return: The version_status of this APIInfoJson400.  # noqa: E501
        :rtype: str
        """
        return self._version_status

    @version_status.setter
    def version_status(self, version_status):
        """Sets the version_status of this APIInfoJson400.


        :param version_status: The version_status of this APIInfoJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version_status is None:
            raise ValueError("Invalid value for `version_status`, must not be `None`")  # noqa: E501

        self._version_status = version_status

    @property
    def version(self):
        """Gets the version of this APIInfoJson400.  # noqa: E501


        :return: The version of this APIInfoJson400.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this APIInfoJson400.


        :param version: The version of this APIInfoJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def hosted_at(self):
        """Gets the hosted_at of this APIInfoJson400.  # noqa: E501


        :return: The hosted_at of this APIInfoJson400.  # noqa: E501
        :rtype: HostedAt400
        """
        return self._hosted_at

    @hosted_at.setter
    def hosted_at(self, hosted_at):
        """Sets the hosted_at of this APIInfoJson400.


        :param hosted_at: The hosted_at of this APIInfoJson400.  # noqa: E501
        :type: HostedAt400
        """
        if self._configuration.client_side_validation and hosted_at is None:
            raise ValueError("Invalid value for `hosted_at`, must not be `None`")  # noqa: E501

        self._hosted_at = hosted_at

    @property
    def connector(self):
        """Gets the connector of this APIInfoJson400.  # noqa: E501


        :return: The connector of this APIInfoJson400.  # noqa: E501
        :rtype: str
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this APIInfoJson400.


        :param connector: The connector of this APIInfoJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connector is None:
            raise ValueError("Invalid value for `connector`, must not be `None`")  # noqa: E501

        self._connector = connector

    @property
    def energy_source(self):
        """Gets the energy_source of this APIInfoJson400.  # noqa: E501


        :return: The energy_source of this APIInfoJson400.  # noqa: E501
        :rtype: EnergySource400
        """
        return self._energy_source

    @energy_source.setter
    def energy_source(self, energy_source):
        """Sets the energy_source of this APIInfoJson400.


        :param energy_source: The energy_source of this APIInfoJson400.  # noqa: E501
        :type: EnergySource400
        """
        if self._configuration.client_side_validation and energy_source is None:
            raise ValueError("Invalid value for `energy_source`, must not be `None`")  # noqa: E501

        self._energy_source = energy_source

    @property
    def hosted_by(self):
        """Gets the hosted_by of this APIInfoJson400.  # noqa: E501


        :return: The hosted_by of this APIInfoJson400.  # noqa: E501
        :rtype: HostedBy400
        """
        return self._hosted_by

    @hosted_by.setter
    def hosted_by(self, hosted_by):
        """Sets the hosted_by of this APIInfoJson400.


        :param hosted_by: The hosted_by of this APIInfoJson400.  # noqa: E501
        :type: HostedBy400
        """
        if self._configuration.client_side_validation and hosted_by is None:
            raise ValueError("Invalid value for `hosted_by`, must not be `None`")  # noqa: E501

        self._hosted_by = hosted_by

    @property
    def git_commit(self):
        """Gets the git_commit of this APIInfoJson400.  # noqa: E501


        :return: The git_commit of this APIInfoJson400.  # noqa: E501
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this APIInfoJson400.


        :param git_commit: The git_commit of this APIInfoJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and git_commit is None:
            raise ValueError("Invalid value for `git_commit`, must not be `None`")  # noqa: E501

        self._git_commit = git_commit

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
        if issubclass(APIInfoJson400, dict):
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
        if not isinstance(other, APIInfoJson400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIInfoJson400):
            return True

        return self.to_dict() != other.to_dict()
