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
from obp_python.apis.transaction_api import TransactionApi


class TestTransactionApi(unittest.TestCase):
    """ TransactionApi unit test stubs """

    def setUp(self):
        self.api = obp_python.apis.transaction_api.TransactionApi()

    def tearDown(self):
        pass

    def test_o_b_pv1_2_1_add_comment_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_add_comment_for_view_on_transaction

        Add a Transaction Comment
        """
        pass

    def test_o_b_pv1_2_1_add_image_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_add_image_for_view_on_transaction

        Add a Transaction Image
        """
        pass

    def test_o_b_pv1_2_1_add_tag_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_add_tag_for_view_on_transaction

        Add a Transaction Tag
        """
        pass

    def test_o_b_pv1_2_1_add_transaction_narrative(self):
        """
        Test case for o_b_pv1_2_1_add_transaction_narrative

        Add a Transaction Narrative
        """
        pass

    def test_o_b_pv1_2_1_add_where_tag_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_add_where_tag_for_view_on_transaction

        Add a Transaction where Tag
        """
        pass

    def test_o_b_pv1_2_1_delete_comment_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_delete_comment_for_view_on_transaction

        Delete a Transaction Comment
        """
        pass

    def test_o_b_pv1_2_1_delete_image_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_delete_image_for_view_on_transaction

        Delete a Transaction Image
        """
        pass

    def test_o_b_pv1_2_1_delete_tag_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_delete_tag_for_view_on_transaction

        Delete a Transaction Tag
        """
        pass

    def test_o_b_pv1_2_1_delete_transaction_narrative(self):
        """
        Test case for o_b_pv1_2_1_delete_transaction_narrative

        Delete a Transaction Narrative
        """
        pass

    def test_o_b_pv1_2_1_delete_where_tag_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_delete_where_tag_for_view_on_transaction

        Delete a Transaction Tag
        """
        pass

    def test_o_b_pv1_2_1_get_comments_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_get_comments_for_view_on_transaction

        Get Transaction Comments
        """
        pass

    def test_o_b_pv1_2_1_get_images_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_get_images_for_view_on_transaction

        Get Transaction Images
        """
        pass

    def test_o_b_pv1_2_1_get_other_account_for_transaction(self):
        """
        Test case for o_b_pv1_2_1_get_other_account_for_transaction

        Get Other Account of Transaction
        """
        pass

    def test_o_b_pv1_2_1_get_tags_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_get_tags_for_view_on_transaction

        Get Transaction Tags
        """
        pass

    def test_o_b_pv1_2_1_get_transaction_narrative(self):
        """
        Test case for o_b_pv1_2_1_get_transaction_narrative

        Get a Transaction Narrative
        """
        pass

    def test_o_b_pv1_2_1_get_where_tag_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_get_where_tag_for_view_on_transaction

        Get a Transaction where Tag
        """
        pass

    def test_o_b_pv1_2_1_update_transaction_narrative(self):
        """
        Test case for o_b_pv1_2_1_update_transaction_narrative

        Update a Transaction Narrative
        """
        pass

    def test_o_b_pv1_2_1_update_where_tag_for_view_on_transaction(self):
        """
        Test case for o_b_pv1_2_1_update_where_tag_for_view_on_transaction

        Update a Transaction where Tag
        """
        pass

    def test_o_b_pv3_0_0_get_core_transactions_for_bank_account(self):
        """
        Test case for o_b_pv3_0_0_get_core_transactions_for_bank_account

        Get Transactions for Account (Core)
        """
        pass

    def test_o_b_pv3_0_0_get_firehose_transactions_for_bank_account(self):
        """
        Test case for o_b_pv3_0_0_get_firehose_transactions_for_bank_account

        Get Firehose Transactions for Account
        """
        pass

    def test_o_b_pv3_0_0_get_transactions_for_bank_account(self):
        """
        Test case for o_b_pv3_0_0_get_transactions_for_bank_account

        Get Transactions for Account (Full)
        """
        pass

    def test_o_b_pv3_1_0_get_transaction_by_id_for_bank_account(self):
        """
        Test case for o_b_pv3_1_0_get_transaction_by_id_for_bank_account

        Get Transaction by Id
        """
        pass

    def test_o_b_pv4_0_0_create_or_update_transaction_attribute_definition(self):
        """
        Test case for o_b_pv4_0_0_create_or_update_transaction_attribute_definition

        Create or Update Transaction Attribute Definition
        """
        pass

    def test_o_b_pv4_0_0_create_transaction_attribute(self):
        """
        Test case for o_b_pv4_0_0_create_transaction_attribute

        Create Transaction Attribute
        """
        pass

    def test_o_b_pv4_0_0_delete_transaction_attribute_definition(self):
        """
        Test case for o_b_pv4_0_0_delete_transaction_attribute_definition

        Delete Transaction Attribute Definition
        """
        pass

    def test_o_b_pv4_0_0_delete_transaction_cascade(self):
        """
        Test case for o_b_pv4_0_0_delete_transaction_cascade

        Delete Transaction Cascade
        """
        pass

    def test_o_b_pv4_0_0_get_balancing_transaction(self):
        """
        Test case for o_b_pv4_0_0_get_balancing_transaction

        Get Balancing Transaction
        """
        pass

    def test_o_b_pv4_0_0_get_double_entry_transaction(self):
        """
        Test case for o_b_pv4_0_0_get_double_entry_transaction

        Get Double Entry Transaction
        """
        pass

    def test_o_b_pv4_0_0_get_transaction_attribute_by_id(self):
        """
        Test case for o_b_pv4_0_0_get_transaction_attribute_by_id

        Get Transaction Attribute By Id
        """
        pass

    def test_o_b_pv4_0_0_get_transaction_attribute_definition(self):
        """
        Test case for o_b_pv4_0_0_get_transaction_attribute_definition

        Get Transaction Attribute Definition
        """
        pass

    def test_o_b_pv4_0_0_get_transaction_attributes(self):
        """
        Test case for o_b_pv4_0_0_get_transaction_attributes

        Get Transaction Attributes
        """
        pass

    def test_o_b_pv4_0_0_update_transaction_attribute(self):
        """
        Test case for o_b_pv4_0_0_update_transaction_attribute

        Update Transaction Attribute
        """
        pass


if __name__ == '__main__':
    unittest.main()