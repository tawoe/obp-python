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


class WebUiPropsApi(object):
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

    def o_b_pv3_1_0_create_web_ui_props(self, body, **kwargs):
        """
        Create WebUiProps
        <p>Create a WebUiProps.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>name is required String value</li><li>value is required String value</li></ul><p>The line break and double quotations should do escape, example:</p><pre><code>{&quot;name&quot;: &quot;webui_some&quot;, &quot;value&quot;: &quot;this valuehave &quot;line break&quot; and double quotations.&quot;}</code></pre><p>should do escape like this:</p><pre><code>{&quot;name&quot;: &quot;webui_some&quot;, &quot;value&quot;: &quot;this value\\nhave \\&quot;line break\\&quot; and double quotations.&quot;}</code></pre><p>Insert image examples:</p><pre><code>// set width=100 and height=50{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;100&quot; height=&quot;50&quot; /&gt;&quot;}// only set height=50{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;&quot; height=&quot;50&quot; /&gt;&quot;}// only width=20%{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;20%&quot; height=&quot;&quot; /&gt;&quot;}</code></pre>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_create_web_ui_props(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WebUiPropsCommons body: WebUiPropsCommons object that needs to be added. (required)
        :return: WebUiPropsCommons
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_create_web_ui_props_with_http_info(body, **kwargs)
        else:
            (data) = self.o_b_pv3_1_0_create_web_ui_props_with_http_info(body, **kwargs)
            return data

    def o_b_pv3_1_0_create_web_ui_props_with_http_info(self, body, **kwargs):
        """
        Create WebUiProps
        <p>Create a WebUiProps.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>name is required String value</li><li>value is required String value</li></ul><p>The line break and double quotations should do escape, example:</p><pre><code>{&quot;name&quot;: &quot;webui_some&quot;, &quot;value&quot;: &quot;this valuehave &quot;line break&quot; and double quotations.&quot;}</code></pre><p>should do escape like this:</p><pre><code>{&quot;name&quot;: &quot;webui_some&quot;, &quot;value&quot;: &quot;this value\\nhave \\&quot;line break\\&quot; and double quotations.&quot;}</code></pre><p>Insert image examples:</p><pre><code>// set width=100 and height=50{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;100&quot; height=&quot;50&quot; /&gt;&quot;}// only set height=50{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;&quot; height=&quot;50&quot; /&gt;&quot;}// only width=20%{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;20%&quot; height=&quot;&quot; /&gt;&quot;}</code></pre>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_create_web_ui_props_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param WebUiPropsCommons body: WebUiPropsCommons object that needs to be added. (required)
        :return: WebUiPropsCommons
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
                    " to method o_b_pv3_1_0_create_web_ui_props" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `o_b_pv3_1_0_create_web_ui_props`")

        resource_path = '/obp/v5.0.0/management/webui_props'.replace('{format}', 'json')
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
                                            response_type='WebUiPropsCommons',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def o_b_pv3_1_0_delete_web_ui_props(self, web_ui_props_id, **kwargs):
        """
        Delete WebUiProps
        <p>Delete a WebUiProps specified by WEB_UI_PROPS_ID.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_delete_web_ui_props(web_ui_props_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_ui_props_id: the web ui props id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_delete_web_ui_props_with_http_info(web_ui_props_id, **kwargs)
        else:
            (data) = self.o_b_pv3_1_0_delete_web_ui_props_with_http_info(web_ui_props_id, **kwargs)
            return data

    def o_b_pv3_1_0_delete_web_ui_props_with_http_info(self, web_ui_props_id, **kwargs):
        """
        Delete WebUiProps
        <p>Delete a WebUiProps specified by WEB_UI_PROPS_ID.</p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_delete_web_ui_props_with_http_info(web_ui_props_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str web_ui_props_id: the web ui props id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['web_ui_props_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_b_pv3_1_0_delete_web_ui_props" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'web_ui_props_id' is set
        if ('web_ui_props_id' not in params) or (params['web_ui_props_id'] is None):
            raise ValueError("Missing the required parameter `web_ui_props_id` when calling `o_b_pv3_1_0_delete_web_ui_props`")

        resource_path = '/obp/v5.0.0/management/webui_props/{WEB_UI_PROPS_ID}'.replace('{format}', 'json')
        path_params = {}
        if 'web_ui_props_id' in params:
            path_params['WEB_UI_PROPS_ID'] = params['web_ui_props_id']

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

    def o_b_pv3_1_0_get_web_ui_props(self, **kwargs):
        """
        Get WebUiProps
        <p>Get the all WebUiProps key values, those props key with &quot;webui_&quot; can be stored in DB, this endpoint get all from DB.</p><p>url query parameter:<br />active: It must be a boolean string. and If active = true, it will show<br />combination of explicit (inserted) + implicit (default)  method_routings.</p><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/webui_props\">https://test.openbankproject.com/obp/v3.1.0/management/webui_props</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/webui_props?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/webui_props?active=true</a></p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_get_web_ui_props(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.o_b_pv3_1_0_get_web_ui_props_with_http_info(**kwargs)
        else:
            (data) = self.o_b_pv3_1_0_get_web_ui_props_with_http_info(**kwargs)
            return data

    def o_b_pv3_1_0_get_web_ui_props_with_http_info(self, **kwargs):
        """
        Get WebUiProps
        <p>Get the all WebUiProps key values, those props key with &quot;webui_&quot; can be stored in DB, this endpoint get all from DB.</p><p>url query parameter:<br />active: It must be a boolean string. and If active = true, it will show<br />combination of explicit (inserted) + implicit (default)  method_routings.</p><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/webui_props\">https://test.openbankproject.com/obp/v3.1.0/management/webui_props</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/webui_props?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/webui_props?active=true</a></p><p>Authentication is Mandatory</p>

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.o_b_pv3_1_0_get_web_ui_props_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse20010
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
                    " to method o_b_pv3_1_0_get_web_ui_props" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/obp/v5.0.0/management/webui_props'.replace('{format}', 'json')
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
                                            response_type='InlineResponse20010',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))