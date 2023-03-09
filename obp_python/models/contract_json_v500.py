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


class ContractJsonV500(object):
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
        'form_of_payment': 'str',
        'maturity_date': 'str',
        'renewal_date': 'str',
        'interest_rate': 'str',
        'instrument_status_code': 'str',
        'product_description': 'str',
        'issuance_amount': 'str',
        'term': 'str',
        'is_substituted': 'str',
        'opening_date': 'str',
        'payment_method': 'str',
        'product_code': 'str',
        'branch_code': 'str',
        'contract_code': 'str',
        'instrument_status_definition': 'str',
        'cancellation_date': 'str',
        'interest_amount': 'str'
    }

    attribute_map = {
        'form_of_payment': 'form_of_payment',
        'maturity_date': 'maturity_date',
        'renewal_date': 'renewal_date',
        'interest_rate': 'interest_rate',
        'instrument_status_code': 'instrument_status_code',
        'product_description': 'product_description',
        'issuance_amount': 'issuance_amount',
        'term': 'term',
        'is_substituted': 'is_substituted',
        'opening_date': 'opening_date',
        'payment_method': 'payment_method',
        'product_code': 'product_code',
        'branch_code': 'branch_code',
        'contract_code': 'contract_code',
        'instrument_status_definition': 'instrument_status_definition',
        'cancellation_date': 'cancellation_date',
        'interest_amount': 'interest_amount'
    }

    def __init__(self, form_of_payment=None, maturity_date=None, renewal_date=None, interest_rate=None, instrument_status_code=None, product_description=None, issuance_amount=None, term=None, is_substituted=None, opening_date=None, payment_method=None, product_code=None, branch_code=None, contract_code=None, instrument_status_definition=None, cancellation_date=None, interest_amount=None, _configuration=None):  # noqa: E501
        """ContractJsonV500 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._form_of_payment = None
        self._maturity_date = None
        self._renewal_date = None
        self._interest_rate = None
        self._instrument_status_code = None
        self._product_description = None
        self._issuance_amount = None
        self._term = None
        self._is_substituted = None
        self._opening_date = None
        self._payment_method = None
        self._product_code = None
        self._branch_code = None
        self._contract_code = None
        self._instrument_status_definition = None
        self._cancellation_date = None
        self._interest_amount = None
        self.discriminator = None

        if form_of_payment is not None:
            self.form_of_payment = form_of_payment
        if maturity_date is not None:
            self.maturity_date = maturity_date
        if renewal_date is not None:
            self.renewal_date = renewal_date
        if interest_rate is not None:
            self.interest_rate = interest_rate
        if instrument_status_code is not None:
            self.instrument_status_code = instrument_status_code
        if product_description is not None:
            self.product_description = product_description
        if issuance_amount is not None:
            self.issuance_amount = issuance_amount
        if term is not None:
            self.term = term
        if is_substituted is not None:
            self.is_substituted = is_substituted
        if opening_date is not None:
            self.opening_date = opening_date
        if payment_method is not None:
            self.payment_method = payment_method
        self.product_code = product_code
        if branch_code is not None:
            self.branch_code = branch_code
        self.contract_code = contract_code
        if instrument_status_definition is not None:
            self.instrument_status_definition = instrument_status_definition
        if cancellation_date is not None:
            self.cancellation_date = cancellation_date
        if interest_amount is not None:
            self.interest_amount = interest_amount

    @property
    def form_of_payment(self):
        """Gets the form_of_payment of this ContractJsonV500.  # noqa: E501


        :return: The form_of_payment of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._form_of_payment

    @form_of_payment.setter
    def form_of_payment(self, form_of_payment):
        """Sets the form_of_payment of this ContractJsonV500.


        :param form_of_payment: The form_of_payment of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._form_of_payment = form_of_payment

    @property
    def maturity_date(self):
        """Gets the maturity_date of this ContractJsonV500.  # noqa: E501


        :return: The maturity_date of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this ContractJsonV500.


        :param maturity_date: The maturity_date of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._maturity_date = maturity_date

    @property
    def renewal_date(self):
        """Gets the renewal_date of this ContractJsonV500.  # noqa: E501


        :return: The renewal_date of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._renewal_date

    @renewal_date.setter
    def renewal_date(self, renewal_date):
        """Sets the renewal_date of this ContractJsonV500.


        :param renewal_date: The renewal_date of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._renewal_date = renewal_date

    @property
    def interest_rate(self):
        """Gets the interest_rate of this ContractJsonV500.  # noqa: E501


        :return: The interest_rate of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this ContractJsonV500.


        :param interest_rate: The interest_rate of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._interest_rate = interest_rate

    @property
    def instrument_status_code(self):
        """Gets the instrument_status_code of this ContractJsonV500.  # noqa: E501


        :return: The instrument_status_code of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._instrument_status_code

    @instrument_status_code.setter
    def instrument_status_code(self, instrument_status_code):
        """Sets the instrument_status_code of this ContractJsonV500.


        :param instrument_status_code: The instrument_status_code of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._instrument_status_code = instrument_status_code

    @property
    def product_description(self):
        """Gets the product_description of this ContractJsonV500.  # noqa: E501


        :return: The product_description of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this ContractJsonV500.


        :param product_description: The product_description of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def issuance_amount(self):
        """Gets the issuance_amount of this ContractJsonV500.  # noqa: E501


        :return: The issuance_amount of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._issuance_amount

    @issuance_amount.setter
    def issuance_amount(self, issuance_amount):
        """Sets the issuance_amount of this ContractJsonV500.


        :param issuance_amount: The issuance_amount of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._issuance_amount = issuance_amount

    @property
    def term(self):
        """Gets the term of this ContractJsonV500.  # noqa: E501


        :return: The term of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this ContractJsonV500.


        :param term: The term of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._term = term

    @property
    def is_substituted(self):
        """Gets the is_substituted of this ContractJsonV500.  # noqa: E501


        :return: The is_substituted of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._is_substituted

    @is_substituted.setter
    def is_substituted(self, is_substituted):
        """Sets the is_substituted of this ContractJsonV500.


        :param is_substituted: The is_substituted of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._is_substituted = is_substituted

    @property
    def opening_date(self):
        """Gets the opening_date of this ContractJsonV500.  # noqa: E501


        :return: The opening_date of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date):
        """Sets the opening_date of this ContractJsonV500.


        :param opening_date: The opening_date of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._opening_date = opening_date

    @property
    def payment_method(self):
        """Gets the payment_method of this ContractJsonV500.  # noqa: E501


        :return: The payment_method of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this ContractJsonV500.


        :param payment_method: The payment_method of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def product_code(self):
        """Gets the product_code of this ContractJsonV500.  # noqa: E501


        :return: The product_code of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this ContractJsonV500.


        :param product_code: The product_code of this ContractJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def branch_code(self):
        """Gets the branch_code of this ContractJsonV500.  # noqa: E501


        :return: The branch_code of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this ContractJsonV500.


        :param branch_code: The branch_code of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._branch_code = branch_code

    @property
    def contract_code(self):
        """Gets the contract_code of this ContractJsonV500.  # noqa: E501


        :return: The contract_code of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._contract_code

    @contract_code.setter
    def contract_code(self, contract_code):
        """Sets the contract_code of this ContractJsonV500.


        :param contract_code: The contract_code of this ContractJsonV500.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contract_code is None:
            raise ValueError("Invalid value for `contract_code`, must not be `None`")  # noqa: E501

        self._contract_code = contract_code

    @property
    def instrument_status_definition(self):
        """Gets the instrument_status_definition of this ContractJsonV500.  # noqa: E501


        :return: The instrument_status_definition of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._instrument_status_definition

    @instrument_status_definition.setter
    def instrument_status_definition(self, instrument_status_definition):
        """Sets the instrument_status_definition of this ContractJsonV500.


        :param instrument_status_definition: The instrument_status_definition of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._instrument_status_definition = instrument_status_definition

    @property
    def cancellation_date(self):
        """Gets the cancellation_date of this ContractJsonV500.  # noqa: E501


        :return: The cancellation_date of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._cancellation_date

    @cancellation_date.setter
    def cancellation_date(self, cancellation_date):
        """Sets the cancellation_date of this ContractJsonV500.


        :param cancellation_date: The cancellation_date of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._cancellation_date = cancellation_date

    @property
    def interest_amount(self):
        """Gets the interest_amount of this ContractJsonV500.  # noqa: E501


        :return: The interest_amount of this ContractJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._interest_amount

    @interest_amount.setter
    def interest_amount(self, interest_amount):
        """Sets the interest_amount of this ContractJsonV500.


        :param interest_amount: The interest_amount of this ContractJsonV500.  # noqa: E501
        :type: str
        """

        self._interest_amount = interest_amount

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
        if issubclass(ContractJsonV500, dict):
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
        if not isinstance(other, ContractJsonV500):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContractJsonV500):
            return True

        return self.to_dict() != other.to_dict()