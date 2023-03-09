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


class ChallengeAnswerJson400(object):
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
        'id': 'str',
        'answer': 'str',
        'reason_code': 'str',
        'additional_information': 'str'
    }

    attribute_map = {
        'id': 'id',
        'answer': 'answer',
        'reason_code': 'reason_code',
        'additional_information': 'additional_information'
    }

    def __init__(self, id=None, answer=None, reason_code=None, additional_information=None, _configuration=None):  # noqa: E501
        """ChallengeAnswerJson400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._answer = None
        self._reason_code = None
        self._additional_information = None
        self.discriminator = None

        self.id = id
        self.answer = answer
        if reason_code is not None:
            self.reason_code = reason_code
        if additional_information is not None:
            self.additional_information = additional_information

    @property
    def id(self):
        """Gets the id of this ChallengeAnswerJson400.  # noqa: E501


        :return: The id of this ChallengeAnswerJson400.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChallengeAnswerJson400.


        :param id: The id of this ChallengeAnswerJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def answer(self):
        """Gets the answer of this ChallengeAnswerJson400.  # noqa: E501


        :return: The answer of this ChallengeAnswerJson400.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this ChallengeAnswerJson400.


        :param answer: The answer of this ChallengeAnswerJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and answer is None:
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer

    @property
    def reason_code(self):
        """Gets the reason_code of this ChallengeAnswerJson400.  # noqa: E501


        :return: The reason_code of this ChallengeAnswerJson400.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this ChallengeAnswerJson400.


        :param reason_code: The reason_code of this ChallengeAnswerJson400.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def additional_information(self):
        """Gets the additional_information of this ChallengeAnswerJson400.  # noqa: E501


        :return: The additional_information of this ChallengeAnswerJson400.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this ChallengeAnswerJson400.


        :param additional_information: The additional_information of this ChallengeAnswerJson400.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

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
        if issubclass(ChallengeAnswerJson400, dict):
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
        if not isinstance(other, ChallengeAnswerJson400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengeAnswerJson400):
            return True

        return self.to_dict() != other.to_dict()
