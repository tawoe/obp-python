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


class CustomerWithAttributesJsonV300(object):
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
        'highest_education_attained': 'str',
        'dob_of_dependants': 'list[str]',
        'bank_id': 'str',
        'date_of_birth': 'str',
        'credit_rating': 'CustomerCreditRatingJSON',
        'last_ok_date': 'date',
        'employment_status': 'str',
        'legal_name': 'str',
        'credit_limit': 'AmountOfMoneyJsonV121',
        'title': 'str',
        'face_image': 'CustomerFaceImageJson',
        'dependants': 'int',
        'relationship_status': 'str',
        'kyc_status': 'bool'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'name_suffix': 'name_suffix',
        'email': 'email',
        'branch_id': 'branch_id',
        'mobile_phone_number': 'mobile_phone_number',
        'customer_number': 'customer_number',
        'customer_attributes': 'customer_attributes',
        'highest_education_attained': 'highest_education_attained',
        'dob_of_dependants': 'dob_of_dependants',
        'bank_id': 'bank_id',
        'date_of_birth': 'date_of_birth',
        'credit_rating': 'credit_rating',
        'last_ok_date': 'last_ok_date',
        'employment_status': 'employment_status',
        'legal_name': 'legal_name',
        'credit_limit': 'credit_limit',
        'title': 'title',
        'face_image': 'face_image',
        'dependants': 'dependants',
        'relationship_status': 'relationship_status',
        'kyc_status': 'kyc_status'
    }

    def __init__(self, customer_id=None, name_suffix=None, email=None, branch_id=None, mobile_phone_number=None, customer_number=None, customer_attributes=None, highest_education_attained=None, dob_of_dependants=None, bank_id=None, date_of_birth=None, credit_rating=None, last_ok_date=None, employment_status=None, legal_name=None, credit_limit=None, title=None, face_image=None, dependants=None, relationship_status=None, kyc_status=None, _configuration=None):  # noqa: E501
        """CustomerWithAttributesJsonV300 - a model defined in Swagger"""  # noqa: E501
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
        self._highest_education_attained = None
        self._dob_of_dependants = None
        self._bank_id = None
        self._date_of_birth = None
        self._credit_rating = None
        self._last_ok_date = None
        self._employment_status = None
        self._legal_name = None
        self._credit_limit = None
        self._title = None
        self._face_image = None
        self._dependants = None
        self._relationship_status = None
        self._kyc_status = None
        self.discriminator = None

        self.customer_id = customer_id
        self.name_suffix = name_suffix
        self.email = email
        self.branch_id = branch_id
        self.mobile_phone_number = mobile_phone_number
        self.customer_number = customer_number
        self.customer_attributes = customer_attributes
        self.highest_education_attained = highest_education_attained
        self.dob_of_dependants = dob_of_dependants
        self.bank_id = bank_id
        self.date_of_birth = date_of_birth
        if credit_rating is not None:
            self.credit_rating = credit_rating
        self.last_ok_date = last_ok_date
        self.employment_status = employment_status
        self.legal_name = legal_name
        if credit_limit is not None:
            self.credit_limit = credit_limit
        self.title = title
        self.face_image = face_image
        self.dependants = dependants
        self.relationship_status = relationship_status
        self.kyc_status = kyc_status

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The customer_id of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerWithAttributesJsonV300.


        :param customer_id: The customer_id of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def name_suffix(self):
        """Gets the name_suffix of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The name_suffix of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._name_suffix

    @name_suffix.setter
    def name_suffix(self, name_suffix):
        """Sets the name_suffix of this CustomerWithAttributesJsonV300.


        :param name_suffix: The name_suffix of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name_suffix is None:
            raise ValueError("Invalid value for `name_suffix`, must not be `None`")  # noqa: E501

        self._name_suffix = name_suffix

    @property
    def email(self):
        """Gets the email of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The email of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CustomerWithAttributesJsonV300.


        :param email: The email of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def branch_id(self):
        """Gets the branch_id of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The branch_id of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this CustomerWithAttributesJsonV300.


        :param branch_id: The branch_id of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and branch_id is None:
            raise ValueError("Invalid value for `branch_id`, must not be `None`")  # noqa: E501

        self._branch_id = branch_id

    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The mobile_phone_number of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this CustomerWithAttributesJsonV300.


        :param mobile_phone_number: The mobile_phone_number of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mobile_phone_number is None:
            raise ValueError("Invalid value for `mobile_phone_number`, must not be `None`")  # noqa: E501

        self._mobile_phone_number = mobile_phone_number

    @property
    def customer_number(self):
        """Gets the customer_number of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The customer_number of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this CustomerWithAttributesJsonV300.


        :param customer_number: The customer_number of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_number is None:
            raise ValueError("Invalid value for `customer_number`, must not be `None`")  # noqa: E501

        self._customer_number = customer_number

    @property
    def customer_attributes(self):
        """Gets the customer_attributes of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The customer_attributes of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: list[CustomerAttributeResponseJsonV300]
        """
        return self._customer_attributes

    @customer_attributes.setter
    def customer_attributes(self, customer_attributes):
        """Sets the customer_attributes of this CustomerWithAttributesJsonV300.


        :param customer_attributes: The customer_attributes of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: list[CustomerAttributeResponseJsonV300]
        """
        if self._configuration.client_side_validation and customer_attributes is None:
            raise ValueError("Invalid value for `customer_attributes`, must not be `None`")  # noqa: E501

        self._customer_attributes = customer_attributes

    @property
    def highest_education_attained(self):
        """Gets the highest_education_attained of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The highest_education_attained of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._highest_education_attained

    @highest_education_attained.setter
    def highest_education_attained(self, highest_education_attained):
        """Sets the highest_education_attained of this CustomerWithAttributesJsonV300.


        :param highest_education_attained: The highest_education_attained of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and highest_education_attained is None:
            raise ValueError("Invalid value for `highest_education_attained`, must not be `None`")  # noqa: E501

        self._highest_education_attained = highest_education_attained

    @property
    def dob_of_dependants(self):
        """Gets the dob_of_dependants of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The dob_of_dependants of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: list[str]
        """
        return self._dob_of_dependants

    @dob_of_dependants.setter
    def dob_of_dependants(self, dob_of_dependants):
        """Sets the dob_of_dependants of this CustomerWithAttributesJsonV300.


        :param dob_of_dependants: The dob_of_dependants of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and dob_of_dependants is None:
            raise ValueError("Invalid value for `dob_of_dependants`, must not be `None`")  # noqa: E501

        self._dob_of_dependants = dob_of_dependants

    @property
    def bank_id(self):
        """Gets the bank_id of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The bank_id of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this CustomerWithAttributesJsonV300.


        :param bank_id: The bank_id of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The date_of_birth of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CustomerWithAttributesJsonV300.


        :param date_of_birth: The date_of_birth of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def credit_rating(self):
        """Gets the credit_rating of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The credit_rating of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: CustomerCreditRatingJSON
        """
        return self._credit_rating

    @credit_rating.setter
    def credit_rating(self, credit_rating):
        """Sets the credit_rating of this CustomerWithAttributesJsonV300.


        :param credit_rating: The credit_rating of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: CustomerCreditRatingJSON
        """

        self._credit_rating = credit_rating

    @property
    def last_ok_date(self):
        """Gets the last_ok_date of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The last_ok_date of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: date
        """
        return self._last_ok_date

    @last_ok_date.setter
    def last_ok_date(self, last_ok_date):
        """Sets the last_ok_date of this CustomerWithAttributesJsonV300.


        :param last_ok_date: The last_ok_date of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and last_ok_date is None:
            raise ValueError("Invalid value for `last_ok_date`, must not be `None`")  # noqa: E501

        self._last_ok_date = last_ok_date

    @property
    def employment_status(self):
        """Gets the employment_status of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The employment_status of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._employment_status

    @employment_status.setter
    def employment_status(self, employment_status):
        """Sets the employment_status of this CustomerWithAttributesJsonV300.


        :param employment_status: The employment_status of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and employment_status is None:
            raise ValueError("Invalid value for `employment_status`, must not be `None`")  # noqa: E501

        self._employment_status = employment_status

    @property
    def legal_name(self):
        """Gets the legal_name of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The legal_name of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this CustomerWithAttributesJsonV300.


        :param legal_name: The legal_name of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and legal_name is None:
            raise ValueError("Invalid value for `legal_name`, must not be `None`")  # noqa: E501

        self._legal_name = legal_name

    @property
    def credit_limit(self):
        """Gets the credit_limit of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The credit_limit of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this CustomerWithAttributesJsonV300.


        :param credit_limit: The credit_limit of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """

        self._credit_limit = credit_limit

    @property
    def title(self):
        """Gets the title of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The title of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CustomerWithAttributesJsonV300.


        :param title: The title of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def face_image(self):
        """Gets the face_image of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The face_image of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: CustomerFaceImageJson
        """
        return self._face_image

    @face_image.setter
    def face_image(self, face_image):
        """Sets the face_image of this CustomerWithAttributesJsonV300.


        :param face_image: The face_image of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: CustomerFaceImageJson
        """
        if self._configuration.client_side_validation and face_image is None:
            raise ValueError("Invalid value for `face_image`, must not be `None`")  # noqa: E501

        self._face_image = face_image

    @property
    def dependants(self):
        """Gets the dependants of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The dependants of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: int
        """
        return self._dependants

    @dependants.setter
    def dependants(self, dependants):
        """Sets the dependants of this CustomerWithAttributesJsonV300.


        :param dependants: The dependants of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and dependants is None:
            raise ValueError("Invalid value for `dependants`, must not be `None`")  # noqa: E501

        self._dependants = dependants

    @property
    def relationship_status(self):
        """Gets the relationship_status of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The relationship_status of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: str
        """
        return self._relationship_status

    @relationship_status.setter
    def relationship_status(self, relationship_status):
        """Sets the relationship_status of this CustomerWithAttributesJsonV300.


        :param relationship_status: The relationship_status of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relationship_status is None:
            raise ValueError("Invalid value for `relationship_status`, must not be `None`")  # noqa: E501

        self._relationship_status = relationship_status

    @property
    def kyc_status(self):
        """Gets the kyc_status of this CustomerWithAttributesJsonV300.  # noqa: E501


        :return: The kyc_status of this CustomerWithAttributesJsonV300.  # noqa: E501
        :rtype: bool
        """
        return self._kyc_status

    @kyc_status.setter
    def kyc_status(self, kyc_status):
        """Sets the kyc_status of this CustomerWithAttributesJsonV300.


        :param kyc_status: The kyc_status of this CustomerWithAttributesJsonV300.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and kyc_status is None:
            raise ValueError("Invalid value for `kyc_status`, must not be `None`")  # noqa: E501

        self._kyc_status = kyc_status

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
        if issubclass(CustomerWithAttributesJsonV300, dict):
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
        if not isinstance(other, CustomerWithAttributesJsonV300):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerWithAttributesJsonV300):
            return True

        return self.to_dict() != other.to_dict()
