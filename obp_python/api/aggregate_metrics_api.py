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


class AggregateMetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def o_bpv3_0_0_get_aggregate_metrics(self, **kwargs):  # noqa: E501
        """Get Aggregate Metrics  # noqa: E501

        <p>Returns aggregate metrics on api usage eg. total count, response time (in ms), etc.</p><p>Should be able to filter on the following fields</p><p>eg: /management/aggregate-metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;consumer_id=5<br />&amp;user_id=66214b8e-259e-44ad-8868-3eb47be70646&amp;implemented_by_partial_function=getTransactionsForBankAccount<br />&amp;implemented_in_version=v3.0.0&amp;url=/obp/v3.0.0/banks/gh.29.uk/accounts/8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0/owner/transactions<br />&amp;verb=GET&amp;anon=false&amp;app_name=MapperPostman<br />&amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>1 from_date (defaults to the day before the current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to the current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 consumer_id  (if null ignore)</p><p>4 user_id (if null ignore)</p><p>5 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>6 url (if null ignore), note: can not contain '&amp;'.</p><p>7 app_name (if null ignore)</p><p>8 implemented_by_partial_function (if null ignore),</p><p>9 implemented_in_version (if null ignore)</p><p>10 verb (if null ignore)</p><p>11 correlation_id (if null ignore)</p><p>12 duration (if null ignore) non digit chars will be silently omitted</p><p>13 exclude_app_names (if null ignore).eg: &amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>14 exclude_url_patterns (if null ignore).you can design you own SQL NOT LIKE pattern. eg: &amp;exclude_url_patterns=%management/metrics%,%management/aggregate-metrics%</p><p>15 exclude_implemented_by_partial_functions (if null ignore).eg: &amp;exclude_implemented_by_partial_functions=getMetrics,getConnectorMetrics,getAggregateMetrics</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_0_0_get_aggregate_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AggregateMetricJSON
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv3_0_0_get_aggregate_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv3_0_0_get_aggregate_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def o_bpv3_0_0_get_aggregate_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """Get Aggregate Metrics  # noqa: E501

        <p>Returns aggregate metrics on api usage eg. total count, response time (in ms), etc.</p><p>Should be able to filter on the following fields</p><p>eg: /management/aggregate-metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;consumer_id=5<br />&amp;user_id=66214b8e-259e-44ad-8868-3eb47be70646&amp;implemented_by_partial_function=getTransactionsForBankAccount<br />&amp;implemented_in_version=v3.0.0&amp;url=/obp/v3.0.0/banks/gh.29.uk/accounts/8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0/owner/transactions<br />&amp;verb=GET&amp;anon=false&amp;app_name=MapperPostman<br />&amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>1 from_date (defaults to the day before the current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to the current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 consumer_id  (if null ignore)</p><p>4 user_id (if null ignore)</p><p>5 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>6 url (if null ignore), note: can not contain '&amp;'.</p><p>7 app_name (if null ignore)</p><p>8 implemented_by_partial_function (if null ignore),</p><p>9 implemented_in_version (if null ignore)</p><p>10 verb (if null ignore)</p><p>11 correlation_id (if null ignore)</p><p>12 duration (if null ignore) non digit chars will be silently omitted</p><p>13 exclude_app_names (if null ignore).eg: &amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>14 exclude_url_patterns (if null ignore).you can design you own SQL NOT LIKE pattern. eg: &amp;exclude_url_patterns=%management/metrics%,%management/aggregate-metrics%</p><p>15 exclude_implemented_by_partial_functions (if null ignore).eg: &amp;exclude_implemented_by_partial_functions=getMetrics,getConnectorMetrics,getAggregateMetrics</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_0_0_get_aggregate_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AggregateMetricJSON
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv3_0_0_get_aggregate_metrics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/aggregate-metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AggregateMetricJSON',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
