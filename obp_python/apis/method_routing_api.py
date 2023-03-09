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


class MethodRoutingApi(object):
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

    def o_b_pv3_1_0_create_method_routing(self, body, **kwargs):
        """
        Create MethodRouting
        <p>Create a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explanation of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some parameters for this method</li></ul><p>note and CAVEAT!:</p><ul><li>bank_id_pattern has to be empty for methods that do not take bank_id as a function parameter, otherwise might get empty result</li><li>methods that aggregate bank objects (e.g. getBankAccountsForUser) have to take any  existing method routings for these objects into consideration</li><li>so if you create e.g. a bank specific method routing for getting an account, make sure that it is also served by endpoints getting ALL accounts for ALL banks</li><li>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</li></ul><p>If the connector name starts with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_create_method_routing(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MethodRoutingCommons body: MethodRoutingCommons object that needs to be added. (required)
        :return: MethodRoutingCommons
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_create_method_routing_with_http_info(body, **kwargs)
        else:
            (data) = self.o_b_pv3_1_0_create_method_routing_with_http_info(body, **kwargs)
            return data

    def o_b_pv3_1_0_create_method_routing_with_http_info(self, body, **kwargs):
        """
        Create MethodRouting
        <p>Create a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explanation of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some parameters for this method</li></ul><p>note and CAVEAT!:</p><ul><li>bank_id_pattern has to be empty for methods that do not take bank_id as a function parameter, otherwise might get empty result</li><li>methods that aggregate bank objects (e.g. getBankAccountsForUser) have to take any  existing method routings for these objects into consideration</li><li>so if you create e.g. a bank specific method routing for getting an account, make sure that it is also served by endpoints getting ALL accounts for ALL banks</li><li>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</li></ul><p>If the connector name starts with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_create_method_routing_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MethodRoutingCommons body: MethodRoutingCommons object that needs to be added. (required)
        :return: MethodRoutingCommons
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_1_0_create_method_routing" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `o_b_pv3_1_0_create_method_routing`")

        resource_path = '/obp/v5.0.0/management/method_routings'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='MethodRoutingCommons',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def o_b_pv3_1_0_delete_method_routing(self, method_routing_id, **kwargs):
        """
        Delete MethodRouting
        <p>Delete a MethodRouting specified by METHOD_ROUTING_ID.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_delete_method_routing(method_routing_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str method_routing_id: the method routing id  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_delete_method_routing_with_http_info(method_routing_id, **kwargs)
        else:
            (data) = self.o_b_pv3_1_0_delete_method_routing_with_http_info(method_routing_id, **kwargs)
            return data

    def o_b_pv3_1_0_delete_method_routing_with_http_info(self, method_routing_id, **kwargs):
        """
        Delete MethodRouting
        <p>Delete a MethodRouting specified by METHOD_ROUTING_ID.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_delete_method_routing_with_http_info(method_routing_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str method_routing_id: the method routing id  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['method_routing_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_1_0_delete_method_routing" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'method_routing_id' is set
        if ('method_routing_id' not in params) or (params['method_routing_id'] is None):
            raise ValueError("Missing the required parameter `method_routing_id` when calling `o_b_pv3_1_0_delete_method_routing`")

        resource_path = '/obp/v5.0.0/management/method_routings/{METHOD_ROUTING_ID}'.replace('{format}', 'json')
        path_params = {}
        if 'method_routing_id' in params:
            path_params['METHOD_ROUTING_ID'] = params['method_routing_id']

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

    def o_b_pv3_1_0_get_method_routings(self, **kwargs):
        """
        Get MethodRoutings
        <p>Get the all MethodRoutings.</p><p>Query url parameters:</p><ul><li>method_name: filter with method_name</li><li>active: if active = true, it will show all the webui_ props. Even if they are set yet, we will return all the default webui_ props</li></ul><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank</a></p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_get_method_routings(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_get_method_routings_with_http_info(**kwargs)
        else:
            (data) = self.o_b_pv3_1_0_get_method_routings_with_http_info(**kwargs)
            return data

    def o_b_pv3_1_0_get_method_routings_with_http_info(self, **kwargs):
        """
        Get MethodRoutings
        <p>Get the all MethodRoutings.</p><p>Query url parameters:</p><ul><li>method_name: filter with method_name</li><li>active: if active = true, it will show all the webui_ props. Even if they are set yet, we will return all the default webui_ props</li></ul><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank</a></p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_get_method_routings_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_1_0_get_method_routings" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/obp/v5.0.0/management/method_routings'.replace('{format}', 'json')
        path_params = {}

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
                                            response_type='InlineResponse2009',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def o_b_pv3_1_0_update_method_routing(self, body, method_routing_id, **kwargs):
        """
        Update MethodRouting
        <p>Update a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some paremeters for this method<br />note:</li><li><p>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</p></li></ul><p>If connector name start with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, to convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_update_method_routing(body, method_routing_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MethodRoutingCommons body: MethodRoutingCommons object that needs to be added. (required)
        :param str method_routing_id: the method routing id  (required)
        :return: MethodRoutingCommons
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_update_method_routing_with_http_info(body, method_routing_id, **kwargs)
        else:
            (data) = self.o_b_pv3_1_0_update_method_routing_with_http_info(body, method_routing_id, **kwargs)
            return data

    def o_b_pv3_1_0_update_method_routing_with_http_info(self, body, method_routing_id, **kwargs):
        """
        Update MethodRouting
        <p>Update a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some paremeters for this method<br />note:</li><li><p>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</p></li></ul><p>If connector name start with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, to convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_update_method_routing_with_http_info(body, method_routing_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param MethodRoutingCommons body: MethodRoutingCommons object that needs to be added. (required)
        :param str method_routing_id: the method routing id  (required)
        :return: MethodRoutingCommons
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'method_routing_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_1_0_update_method_routing" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `o_b_pv3_1_0_update_method_routing`")
        # verify the required parameter 'method_routing_id' is set
        if ('method_routing_id' not in params) or (params['method_routing_id'] is None):
            raise ValueError("Missing the required parameter `method_routing_id` when calling `o_b_pv3_1_0_update_method_routing`")

        resource_path = '/obp/v5.0.0/management/method_routings/{METHOD_ROUTING_ID}'.replace('{format}', 'json')
        path_params = {}
        if 'method_routing_id' in params:
            path_params['METHOD_ROUTING_ID'] = params['method_routing_id']

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

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MethodRoutingCommons',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
