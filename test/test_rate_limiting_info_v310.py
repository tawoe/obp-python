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
from obp_python.models.rate_limiting_info_v310 import RateLimitingInfoV310


class TestRateLimitingInfoV310(unittest.TestCase):
    """ RateLimitingInfoV310 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRateLimitingInfoV310(self):
        """
        Test RateLimitingInfoV310
        """
        model = obp_python.models.rate_limiting_info_v310.RateLimitingInfoV310()


if __name__ == '__main__':
    unittest.main()
