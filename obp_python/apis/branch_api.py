# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2023. Licensed under the AGPL and commercial licences.

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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BranchApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def o_b_pv3_0_0_create_branch(self, body, bank_id, **kwargs):
        """
        Create Branch
        <p>Create Branch for the Bank.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_0_0_create_branch(body, bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BranchJsonV300 body: BranchJsonV300 object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_0_0_create_branch_with_http_info(body, bank_id, **kwargs)
        else:
            (data) = self.o_b_pv3_0_0_create_branch_with_http_info(body, bank_id, **kwargs)
            return data

    def o_b_pv3_0_0_create_branch_with_http_info(self, body, bank_id, **kwargs):
        """
        Create Branch
        <p>Create Branch for the Bank.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_0_0_create_branch_with_http_info(body, bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BranchJsonV300 body: BranchJsonV300 object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bank_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_0_0_create_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `o_b_pv3_0_0_create_branch`")
        # verify the required parameter 'bank_id' is set
        if ('bank_id' not in params) or (params['bank_id'] is None):
            raise ValueError("Missing the required parameter `bank_id` when calling `o_b_pv3_0_0_create_branch`")

        resource_path = '/obp/v5.0.0/banks/{BANK_ID}/branches'.replace('{format}', 'json')
        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BranchJsonV300',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def o_b_pv3_0_0_get_branch(self, branch_id, bank_id, **kwargs):
        """
        Get Branch
        <p>Returns information about a single Branch specified by BANK_ID and BRANCH_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under.</li></ul><p>Authentication is Optional</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_0_0_get_branch(branch_id, bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_0_0_get_branch_with_http_info(branch_id, bank_id, **kwargs)
        else:
            (data) = self.o_b_pv3_0_0_get_branch_with_http_info(branch_id, bank_id, **kwargs)
            return data

    def o_b_pv3_0_0_get_branch_with_http_info(self, branch_id, bank_id, **kwargs):
        """
        Get Branch
        <p>Returns information about a single Branch specified by BANK_ID and BRANCH_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under.</li></ul><p>Authentication is Optional</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_0_0_get_branch_with_http_info(branch_id, bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: BranchJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['branch_id', 'bank_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_0_0_get_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'branch_id' is set
        if ('branch_id' not in params) or (params['branch_id'] is None):
            raise ValueError("Missing the required parameter `branch_id` when calling `o_b_pv3_0_0_get_branch`")
        # verify the required parameter 'bank_id' is set
        if ('bank_id' not in params) or (params['bank_id'] is None):
            raise ValueError("Missing the required parameter `bank_id` when calling `o_b_pv3_0_0_get_branch`")

        resource_path = '/obp/v5.0.0/banks/{BANK_ID}/branches/{BRANCH_ID}'.replace('{format}', 'json')
        path_params = {}
        if 'branch_id' in params:
            path_params['BRANCH_ID'] = params['branch_id']
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BranchJsonV300',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def o_b_pv3_0_0_get_branches(self, bank_id, **kwargs):
        """
        Get Branches for a Bank
        <p>Returns information about branches for a single bank specified by BANK_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under</li><li>Structured opening hours</li><li>Accessible flag</li><li>Branch Type</li><li>More Info</li></ul><p>Pagination:</p><p>By default, 50 records are returned.</p><p>You can use the url query parameters <em>limit</em> and <em>offset</em> for pagination<br />You can also use the follow url query parameters:</p><ul><li><p>city - string, find Branches those in this city, optional</p></li><li><p>withinMetersOf - number, find Branches within given meters distance, optional</p></li><li>nearLatitude - number, a position of latitude value, cooperate with withMetersOf do query filter, optional</li><li>nearLongitude - number, a position of longitude value, cooperate with withMetersOf do query filter, optional</li></ul><p>note: withinMetersOf, nearLatitude and nearLongitude either all empty or all have value.</p><p>Authentication is Optional</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_0_0_get_branches(bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bank_id: The bank id (required)
        :return: BranchesJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_0_0_get_branches_with_http_info(bank_id, **kwargs)
        else:
            (data) = self.o_b_pv3_0_0_get_branches_with_http_info(bank_id, **kwargs)
            return data

    def o_b_pv3_0_0_get_branches_with_http_info(self, bank_id, **kwargs):
        """
        Get Branches for a Bank
        <p>Returns information about branches for a single bank specified by BANK_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under</li><li>Structured opening hours</li><li>Accessible flag</li><li>Branch Type</li><li>More Info</li></ul><p>Pagination:</p><p>By default, 50 records are returned.</p><p>You can use the url query parameters <em>limit</em> and <em>offset</em> for pagination<br />You can also use the follow url query parameters:</p><ul><li><p>city - string, find Branches those in this city, optional</p></li><li><p>withinMetersOf - number, find Branches within given meters distance, optional</p></li><li>nearLatitude - number, a position of latitude value, cooperate with withMetersOf do query filter, optional</li><li>nearLongitude - number, a position of longitude value, cooperate with withMetersOf do query filter, optional</li></ul><p>note: withinMetersOf, nearLatitude and nearLongitude either all empty or all have value.</p><p>Authentication is Optional</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_0_0_get_branches_with_http_info(bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str bank_id: The bank id (required)
        :return: BranchesJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bank_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_0_0_get_branches" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bank_id' is set
        if ('bank_id' not in params) or (params['bank_id'] is None):
            raise ValueError("Missing the required parameter `bank_id` when calling `o_b_pv3_0_0_get_branches`")

        resource_path = '/obp/v5.0.0/banks/{BANK_ID}/branches'.replace('{format}', 'json')
        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BranchesJsonV300',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def o_b_pv3_1_0_delete_branch(self, branch_id, bank_id, **kwargs):
        """
        Delete Branch
        <p>Delete Branch from given Bank.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_delete_branch(branch_id, bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_delete_branch_with_http_info(branch_id, bank_id, **kwargs)
        else:
            (data) = self.o_b_pv3_1_0_delete_branch_with_http_info(branch_id, bank_id, **kwargs)
            return data

    def o_b_pv3_1_0_delete_branch_with_http_info(self, branch_id, bank_id, **kwargs):
        """
        Delete Branch
        <p>Delete Branch from given Bank.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_delete_branch_with_http_info(branch_id, bank_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str branch_id: The branch id (required)
        :param str bank_id: The bank id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['branch_id', 'bank_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_1_0_delete_branch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'branch_id' is set
        if ('branch_id' not in params) or (params['branch_id'] is None):
            raise ValueError("Missing the required parameter `branch_id` when calling `o_b_pv3_1_0_delete_branch`")
        # verify the required parameter 'bank_id' is set
        if ('bank_id' not in params) or (params['bank_id'] is None):
            raise ValueError("Missing the required parameter `bank_id` when calling `o_b_pv3_1_0_delete_branch`")

        resource_path = '/obp/v5.0.0/banks/{BANK_ID}/branches/{BRANCH_ID}'.replace('{format}', 'json')
        path_params = {}
        if 'branch_id' in params:
            path_params['BRANCH_ID'] = params['branch_id']
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
