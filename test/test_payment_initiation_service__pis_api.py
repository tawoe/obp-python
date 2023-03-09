# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2023. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import obp_python
from obp_python.api.payment_initiation_service__pis_api import PaymentInitiationServicePISApi  # noqa: E501
from obp_python.rest import ApiException


class TestPaymentInitiationServicePISApi(unittest.TestCase):
    """PaymentInitiationServicePISApi unit test stubs"""

    def setUp(self):
        self.api = obp_python.api.payment_initiation_service__pis_api.PaymentInitiationServicePISApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_o_bpv1_4_0_get_transaction_request_types(self):
        """Test case for o_bpv1_4_0_get_transaction_request_types

        Get Transaction Request Types for Account  # noqa: E501
        """
        pass

    def test_o_bpv2_1_0_create_transaction_request_sandbox_tan(self):
        """Test case for o_bpv2_1_0_create_transaction_request_sandbox_tan

        Create Transaction Request (SANDBOX_TAN)  # noqa: E501
        """
        pass

    def test_o_bpv3_1_0_get_transaction_requests(self):
        """Test case for o_bpv3_1_0_get_transaction_requests

        Get Transaction Requests.  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_answer_transaction_request_challenge(self):
        """Test case for o_bpv4_0_0_answer_transaction_request_challenge

        Answer Transaction Request Challenge  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_account(self):
        """Test case for o_bpv4_0_0_create_transaction_request_account

        Create Transaction Request (ACCOUNT)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_account_otp(self):
        """Test case for o_bpv4_0_0_create_transaction_request_account_otp

        Create Transaction Request (ACCOUNT_OTP)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_card(self):
        """Test case for o_bpv4_0_0_create_transaction_request_card

        Create Transaction Request (CARD)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_counterparty(self):
        """Test case for o_bpv4_0_0_create_transaction_request_counterparty

        Create Transaction Request (COUNTERPARTY)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_free_form(self):
        """Test case for o_bpv4_0_0_create_transaction_request_free_form

        Create Transaction Request (FREE_FORM)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_refund(self):
        """Test case for o_bpv4_0_0_create_transaction_request_refund

        Create Transaction Request (REFUND)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_sepa(self):
        """Test case for o_bpv4_0_0_create_transaction_request_sepa

        Create Transaction Request (SEPA)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_create_transaction_request_simple(self):
        """Test case for o_bpv4_0_0_create_transaction_request_simple

        Create Transaction Request (SIMPLE)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_get_counterparties_for_any_account(self):
        """Test case for o_bpv4_0_0_get_counterparties_for_any_account

        Get Counterparties for any account (Explicit)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_get_explict_counterparties_for_account(self):
        """Test case for o_bpv4_0_0_get_explict_counterparties_for_account

        Get Counterparties (Explicit)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_get_explict_counterparty_by_id(self):
        """Test case for o_bpv4_0_0_get_explict_counterparty_by_id

        Get Counterparty by Id (Explicit)  # noqa: E501
        """
        pass

    def test_o_bpv4_0_0_get_transaction_request(self):
        """Test case for o_bpv4_0_0_get_transaction_request

        Get Transaction Request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
