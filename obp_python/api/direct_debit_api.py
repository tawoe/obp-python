# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2023. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from obp_python.api_client import ApiClient


class DirectDebitApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def o_bpv4_0_0_create_direct_debit(self, body, view_id, account_id, bank_id, **kwargs):  # noqa: E501
        """Create Direct Debit  # noqa: E501

        <p>Create direct debit for an account.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_direct_debit(body, view_id, account_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectDebitJsonV400 body: PostDirectDebitJsonV400 object that needs to be added. (required)
        :param str view_id: The view id (required)
        :param str account_id: The account id (required)
        :param str bank_id: The bank id (required)
        :return: DirectDebitJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv4_0_0_create_direct_debit_with_http_info(body, view_id, account_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv4_0_0_create_direct_debit_with_http_info(body, view_id, account_id, bank_id, **kwargs)  # noqa: E501
            return data

    def o_bpv4_0_0_create_direct_debit_with_http_info(self, body, view_id, account_id, bank_id, **kwargs):  # noqa: E501
        """Create Direct Debit  # noqa: E501

        <p>Create direct debit for an account.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_direct_debit_with_http_info(body, view_id, account_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectDebitJsonV400 body: PostDirectDebitJsonV400 object that needs to be added. (required)
        :param str view_id: The view id (required)
        :param str account_id: The account id (required)
        :param str bank_id: The bank id (required)
        :return: DirectDebitJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'view_id', 'account_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv4_0_0_create_direct_debit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `o_bpv4_0_0_create_direct_debit`")  # noqa: E501
        # verify the required parameter 'view_id' is set
        if self.api_client.client_side_validation and ('view_id' not in params or
                                                       params['view_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `view_id` when calling `o_bpv4_0_0_create_direct_debit`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `o_bpv4_0_0_create_direct_debit`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `o_bpv4_0_0_create_direct_debit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'view_id' in params:
            path_params['VIEW_ID'] = params['view_id']  # noqa: E501
        if 'account_id' in params:
            path_params['ACCOUNT_ID'] = params['account_id']  # noqa: E501
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/direct-debit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectDebitJsonV400',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_bpv4_0_0_create_direct_debit_management(self, body, account_id, bank_id, **kwargs):  # noqa: E501
        """Create Direct Debit (management)  # noqa: E501

        <p>Create direct debit for an account.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_direct_debit_management(body, account_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectDebitJsonV400 body: PostDirectDebitJsonV400 object that needs to be added. (required)
        :param str account_id: The account id (required)
        :param str bank_id: The bank id (required)
        :return: DirectDebitJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv4_0_0_create_direct_debit_management_with_http_info(body, account_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv4_0_0_create_direct_debit_management_with_http_info(body, account_id, bank_id, **kwargs)  # noqa: E501
            return data

    def o_bpv4_0_0_create_direct_debit_management_with_http_info(self, body, account_id, bank_id, **kwargs):  # noqa: E501
        """Create Direct Debit (management)  # noqa: E501

        <p>Create direct debit for an account.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_direct_debit_management_with_http_info(body, account_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostDirectDebitJsonV400 body: PostDirectDebitJsonV400 object that needs to be added. (required)
        :param str account_id: The account id (required)
        :param str bank_id: The bank id (required)
        :return: DirectDebitJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'account_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv4_0_0_create_direct_debit_management" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `o_bpv4_0_0_create_direct_debit_management`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `o_bpv4_0_0_create_direct_debit_management`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `o_bpv4_0_0_create_direct_debit_management`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['ACCOUNT_ID'] = params['account_id']  # noqa: E501
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/direct-debit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectDebitJsonV400',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
