# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2022. Licensed under the AGPL and commercial licences.

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import obp_python
from obp_python.rest import ApiException
from obp_python.apis.psd_api import PSDApi


class TestPSDApi(unittest.TestCase):
    """ PSDApi unit test stubs """

    def setUp(self):
        self.api = obp_python.apis.psd_api.PSDApi()

    def tearDown(self):
        pass

    def test_o_b_pv1_4_0_get_transaction_request_types(self):
        """
        Test case for o_b_pv1_4_0_get_transaction_request_types

        Get Transaction Request Types for Account
        """
        pass

    def test_o_b_pv2_0_0_get_transaction_types(self):
        """
        Test case for o_b_pv2_0_0_get_transaction_types

        Get Transaction Types at Bank
        """
        pass

    def test_o_b_pv2_1_0_create_transaction_request_sandbox_tan(self):
        """
        Test case for o_b_pv2_1_0_create_transaction_request_sandbox_tan

        Create Transaction Request (SANDBOX_TAN)
        """
        pass

    def test_o_b_pv3_0_0_core_private_accounts_all_banks(self):
        """
        Test case for o_b_pv3_0_0_core_private_accounts_all_banks

        Get Accounts at all Banks (private)
        """
        pass

    def test_o_b_pv3_0_0_get_accounts_held(self):
        """
        Test case for o_b_pv3_0_0_get_accounts_held

        Get Accounts Held
        """
        pass

    def test_o_b_pv3_0_0_get_core_transactions_for_bank_account(self):
        """
        Test case for o_b_pv3_0_0_get_core_transactions_for_bank_account

        Get Transactions for Account (Core)
        """
        pass

    def test_o_b_pv3_0_0_get_private_account_idsby_bank_id(self):
        """
        Test case for o_b_pv3_0_0_get_private_account_idsby_bank_id

        Get Accounts at Bank (IDs only)
        """
        pass

    def test_o_b_pv3_0_0_private_accounts_at_one_bank(self):
        """
        Test case for o_b_pv3_0_0_private_accounts_at_one_bank

        Get Accounts at Bank (Minimal)
        """
        pass

    def test_o_b_pv3_1_0_answer_consent_challenge(self):
        """
        Test case for o_b_pv3_1_0_answer_consent_challenge

        Answer Consent Challenge
        """
        pass

    def test_o_b_pv3_1_0_check_funds_available(self):
        """
        Test case for o_b_pv3_1_0_check_funds_available

        Check Available Funds
        """
        pass

    def test_o_b_pv3_1_0_create_consent_email(self):
        """
        Test case for o_b_pv3_1_0_create_consent_email

        Create Consent (EMAIL)
        """
        pass

    def test_o_b_pv3_1_0_create_consent_sms(self):
        """
        Test case for o_b_pv3_1_0_create_consent_sms

        Create Consent (SMS)
        """
        pass

    def test_o_b_pv3_1_0_get_server_jwk(self):
        """
        Test case for o_b_pv3_1_0_get_server_jwk

        Get JSON Web Key (JWK)
        """
        pass

    def test_o_b_pv3_1_0_revoke_consent(self):
        """
        Test case for o_b_pv3_1_0_revoke_consent

        Revoke Consent
        """
        pass

    def test_o_b_pv4_0_0_answer_transaction_request_challenge(self):
        """
        Test case for o_b_pv4_0_0_answer_transaction_request_challenge

        Answer Transaction Request Challenge
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_account(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_account

        Create Transaction Request (ACCOUNT)
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_account_otp(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_account_otp

        Create Transaction Request (ACCOUNT_OTP)
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_card(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_card

        Create Transaction Request (CARD)
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_counterparty(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_counterparty

        Create Transaction Request (COUNTERPARTY)
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_refund(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_refund

        Create Transaction Request (REFUND)
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_sepa(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_sepa

        Create Transaction Request (SEPA)
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_request_simple(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_request_simple

        Create Transaction Request (SIMPLE)
        """
        pass

    def test_o_b_pv4_0_0_get_bank_account_balances(self):
        """
        Test case for o_b_pv4_0_0_get_bank_account_balances

        Get Account Balances
        """
        pass

    def test_o_b_pv4_0_0_get_bank_accounts_balances(self):
        """
        Test case for o_b_pv4_0_0_get_bank_accounts_balances

        Get Accounts Balances
        """
        pass

    def test_o_b_pv4_0_0_get_banks(self):
        """
        Test case for o_b_pv4_0_0_get_banks

        Get Banks
        """
        pass

    def test_o_b_pv4_0_0_get_consent_infos(self):
        """
        Test case for o_b_pv4_0_0_get_consent_infos

        Get Consents Info
        """
        pass

    def test_o_b_pv4_0_0_get_consents(self):
        """
        Test case for o_b_pv4_0_0_get_consents

        Get Consents
        """
        pass

    def test_o_b_pv4_0_0_get_core_account_by_id(self):
        """
        Test case for o_b_pv4_0_0_get_core_account_by_id

        Get Account by Id (Core)
        """
        pass

    def test_o_b_pv4_0_0_get_counterparties_for_any_account(self):
        """
        Test case for o_b_pv4_0_0_get_counterparties_for_any_account

        Get Counterparties for any account (Explicit)
        """
        pass

    def test_o_b_pv4_0_0_get_explict_counterparties_for_account(self):
        """
        Test case for o_b_pv4_0_0_get_explict_counterparties_for_account

        Get Counterparties (Explicit)
        """
        pass

    def test_o_b_pv4_0_0_get_explict_counterparty_by_id(self):
        """
        Test case for o_b_pv4_0_0_get_explict_counterparty_by_id

        Get Counterparty by Id (Explicit)
        """
        pass

    def test_o_b_pv4_0_0_get_settlement_accounts(self):
        """
        Test case for o_b_pv4_0_0_get_settlement_accounts

        Get Settlement accounts at Bank
        """
        pass

    def test_o_b_pv4_0_0_get_transaction_request(self):
        """
        Test case for o_b_pv4_0_0_get_transaction_request

        Get Transaction Request.
        """
        pass

    def test_o_b_pv5_0_0_create_consent_by_consent_request_id_email(self):
        """
        Test case for o_b_pv5_0_0_create_consent_by_consent_request_id_email

        Create Consent By Request Id(EMAIL)
        """
        pass

    def test_o_b_pv5_0_0_create_consent_by_consent_request_id_sms(self):
        """
        Test case for o_b_pv5_0_0_create_consent_by_consent_request_id_sms

        Create Consent By Request Id (SMS)
        """
        pass

    def test_o_b_pv5_0_0_create_consent_request(self):
        """
        Test case for o_b_pv5_0_0_create_consent_request

        Create Consent Request
        """
        pass

    def test_o_b_pv5_0_0_get_bank(self):
        """
        Test case for o_b_pv5_0_0_get_bank

        Get Bank
        """
        pass

    def test_o_b_pv5_0_0_get_consent_by_consent_request_id(self):
        """
        Test case for o_b_pv5_0_0_get_consent_by_consent_request_id

        Get Consent By Consent Request Id
        """
        pass

    def test_o_b_pv5_0_0_get_consent_request(self):
        """
        Test case for o_b_pv5_0_0_get_consent_request

        Get Consent Request
        """
        pass


if __name__ == '__main__':
    unittest.main()
