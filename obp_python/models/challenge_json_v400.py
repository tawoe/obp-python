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


class ChallengeJsonV400(object):
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
        'allowed_attempts': 'int',
        'user_id': 'str',
        'id': 'str',
        'link': 'str',
        'challenge_type': 'str'
    }

    attribute_map = {
        'allowed_attempts': 'allowed_attempts',
        'user_id': 'user_id',
        'id': 'id',
        'link': 'link',
        'challenge_type': 'challenge_type'
    }

    def __init__(self, allowed_attempts=None, user_id=None, id=None, link=None, challenge_type=None, _configuration=None):  # noqa: E501
        """ChallengeJsonV400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allowed_attempts = None
        self._user_id = None
        self._id = None
        self._link = None
        self._challenge_type = None
        self.discriminator = None

        self.allowed_attempts = allowed_attempts
        self.user_id = user_id
        self.id = id
        self.link = link
        self.challenge_type = challenge_type

    @property
    def allowed_attempts(self):
        """Gets the allowed_attempts of this ChallengeJsonV400.  # noqa: E501


        :return: The allowed_attempts of this ChallengeJsonV400.  # noqa: E501
        :rtype: int
        """
        return self._allowed_attempts

    @allowed_attempts.setter
    def allowed_attempts(self, allowed_attempts):
        """Sets the allowed_attempts of this ChallengeJsonV400.


        :param allowed_attempts: The allowed_attempts of this ChallengeJsonV400.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and allowed_attempts is None:
            raise ValueError("Invalid value for `allowed_attempts`, must not be `None`")  # noqa: E501

        self._allowed_attempts = allowed_attempts

    @property
    def user_id(self):
        """Gets the user_id of this ChallengeJsonV400.  # noqa: E501


        :return: The user_id of this ChallengeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChallengeJsonV400.


        :param user_id: The user_id of this ChallengeJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def id(self):
        """Gets the id of this ChallengeJsonV400.  # noqa: E501


        :return: The id of this ChallengeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChallengeJsonV400.


        :param id: The id of this ChallengeJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def link(self):
        """Gets the link of this ChallengeJsonV400.  # noqa: E501


        :return: The link of this ChallengeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ChallengeJsonV400.


        :param link: The link of this ChallengeJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def challenge_type(self):
        """Gets the challenge_type of this ChallengeJsonV400.  # noqa: E501


        :return: The challenge_type of this ChallengeJsonV400.  # noqa: E501
        :rtype: str
        """
        return self._challenge_type

    @challenge_type.setter
    def challenge_type(self, challenge_type):
        """Sets the challenge_type of this ChallengeJsonV400.


        :param challenge_type: The challenge_type of this ChallengeJsonV400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and challenge_type is None:
            raise ValueError("Invalid value for `challenge_type`, must not be `None`")  # noqa: E501

        self._challenge_type = challenge_type

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
        if issubclass(ChallengeJsonV400, dict):
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
        if not isinstance(other, ChallengeJsonV400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengeJsonV400):
            return True

        return self.to_dict() != other.to_dict()