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
from obp_python.apis.experimental_api import ExperimentalApi


class TestExperimentalApi(unittest.TestCase):
    """ ExperimentalApi unit test stubs """

    def setUp(self):
        self.api = obp_python.apis.experimental_api.ExperimentalApi()

    def tearDown(self):
        pass

    def test_o_b_pv3_1_0_create_meeting(self):
        """
        Test case for o_b_pv3_1_0_create_meeting

        Create Meeting (video conference/call)
        """
        pass

    def test_o_b_pv3_1_0_get_meeting(self):
        """
        Test case for o_b_pv3_1_0_get_meeting

        Get Meeting
        """
        pass

    def test_o_b_pv3_1_0_get_meetings(self):
        """
        Test case for o_b_pv3_1_0_get_meetings

        Get Meetings
        """
        pass


if __name__ == '__main__':
    unittest.main()
