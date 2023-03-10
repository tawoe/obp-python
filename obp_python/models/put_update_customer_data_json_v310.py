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


class PutUpdateCustomerDataJsonV310(object):
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
        'highest_education_attained': 'str',
        'employment_status': 'str',
        'face_image': 'CustomerFaceImageJson',
        'dependants': 'int',
        'relationship_status': 'str'
    }

    attribute_map = {
        'highest_education_attained': 'highest_education_attained',
        'employment_status': 'employment_status',
        'face_image': 'face_image',
        'dependants': 'dependants',
        'relationship_status': 'relationship_status'
    }

    def __init__(self, highest_education_attained=None, employment_status=None, face_image=None, dependants=None, relationship_status=None, _configuration=None):  # noqa: E501
        """PutUpdateCustomerDataJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._highest_education_attained = None
        self._employment_status = None
        self._face_image = None
        self._dependants = None
        self._relationship_status = None
        self.discriminator = None

        self.highest_education_attained = highest_education_attained
        self.employment_status = employment_status
        self.face_image = face_image
        self.dependants = dependants
        self.relationship_status = relationship_status

    @property
    def highest_education_attained(self):
        """Gets the highest_education_attained of this PutUpdateCustomerDataJsonV310.  # noqa: E501


        :return: The highest_education_attained of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._highest_education_attained

    @highest_education_attained.setter
    def highest_education_attained(self, highest_education_attained):
        """Sets the highest_education_attained of this PutUpdateCustomerDataJsonV310.


        :param highest_education_attained: The highest_education_attained of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and highest_education_attained is None:
            raise ValueError("Invalid value for `highest_education_attained`, must not be `None`")  # noqa: E501

        self._highest_education_attained = highest_education_attained

    @property
    def employment_status(self):
        """Gets the employment_status of this PutUpdateCustomerDataJsonV310.  # noqa: E501


        :return: The employment_status of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._employment_status

    @employment_status.setter
    def employment_status(self, employment_status):
        """Sets the employment_status of this PutUpdateCustomerDataJsonV310.


        :param employment_status: The employment_status of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and employment_status is None:
            raise ValueError("Invalid value for `employment_status`, must not be `None`")  # noqa: E501

        self._employment_status = employment_status

    @property
    def face_image(self):
        """Gets the face_image of this PutUpdateCustomerDataJsonV310.  # noqa: E501


        :return: The face_image of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :rtype: CustomerFaceImageJson
        """
        return self._face_image

    @face_image.setter
    def face_image(self, face_image):
        """Sets the face_image of this PutUpdateCustomerDataJsonV310.


        :param face_image: The face_image of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :type: CustomerFaceImageJson
        """
        if self._configuration.client_side_validation and face_image is None:
            raise ValueError("Invalid value for `face_image`, must not be `None`")  # noqa: E501

        self._face_image = face_image

    @property
    def dependants(self):
        """Gets the dependants of this PutUpdateCustomerDataJsonV310.  # noqa: E501


        :return: The dependants of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :rtype: int
        """
        return self._dependants

    @dependants.setter
    def dependants(self, dependants):
        """Sets the dependants of this PutUpdateCustomerDataJsonV310.


        :param dependants: The dependants of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and dependants is None:
            raise ValueError("Invalid value for `dependants`, must not be `None`")  # noqa: E501

        self._dependants = dependants

    @property
    def relationship_status(self):
        """Gets the relationship_status of this PutUpdateCustomerDataJsonV310.  # noqa: E501


        :return: The relationship_status of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._relationship_status

    @relationship_status.setter
    def relationship_status(self, relationship_status):
        """Sets the relationship_status of this PutUpdateCustomerDataJsonV310.


        :param relationship_status: The relationship_status of this PutUpdateCustomerDataJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relationship_status is None:
            raise ValueError("Invalid value for `relationship_status`, must not be `None`")  # noqa: E501

        self._relationship_status = relationship_status

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
        if issubclass(PutUpdateCustomerDataJsonV310, dict):
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
        if not isinstance(other, PutUpdateCustomerDataJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutUpdateCustomerDataJsonV310):
            return True

        return self.to_dict() != other.to_dict()
