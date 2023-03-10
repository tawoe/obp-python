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


class WebhookApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def o_bpv3_1_0_create_account_webhook(self, body, bank_id, **kwargs):  # noqa: E501
        """Create an Account Webhook  # noqa: E501

        <p>Create an Account Webhook</p><p>Webhooks are used to call external URLs when certain events happen.</p><p>Account Webhooks focus on events around accounts.</p><p>For instance, a webhook could be used to notify an external service if a balance changes on an account.</p><p>This functionality is work in progress! Please note that only implemented trigger is: OnBalanceChange</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_1_0_create_account_webhook(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountWebhookPostJson body: AccountWebhookPostJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: AccountWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv3_1_0_create_account_webhook_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv3_1_0_create_account_webhook_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def o_bpv3_1_0_create_account_webhook_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Create an Account Webhook  # noqa: E501

        <p>Create an Account Webhook</p><p>Webhooks are used to call external URLs when certain events happen.</p><p>Account Webhooks focus on events around accounts.</p><p>For instance, a webhook could be used to notify an external service if a balance changes on an account.</p><p>This functionality is work in progress! Please note that only implemented trigger is: OnBalanceChange</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_1_0_create_account_webhook_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountWebhookPostJson body: AccountWebhookPostJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: AccountWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv3_1_0_create_account_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `o_bpv3_1_0_create_account_webhook`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `o_bpv3_1_0_create_account_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/obp/v5.0.0/banks/{BANK_ID}/account-web-hooks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountWebhookJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_bpv3_1_0_enable_disable_account_webhook(self, body, bank_id, **kwargs):  # noqa: E501
        """Enable/Disable an Account Webhook  # noqa: E501

        <p>Enable/Disable an Account Webhook</p><p>Webhooks are used to call external URLs when certain events happen.</p><p>Account Webhooks focus on events around accounts.</p><p>For instance, a webhook could be used to notify an external service if a balance changes on an account.</p><p>This functionality is work in progress! Please note that only implemented trigger is: OnBalanceChange</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_1_0_enable_disable_account_webhook(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountWebhookPutJson body: AccountWebhookPutJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: AccountWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv3_1_0_enable_disable_account_webhook_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv3_1_0_enable_disable_account_webhook_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def o_bpv3_1_0_enable_disable_account_webhook_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Enable/Disable an Account Webhook  # noqa: E501

        <p>Enable/Disable an Account Webhook</p><p>Webhooks are used to call external URLs when certain events happen.</p><p>Account Webhooks focus on events around accounts.</p><p>For instance, a webhook could be used to notify an external service if a balance changes on an account.</p><p>This functionality is work in progress! Please note that only implemented trigger is: OnBalanceChange</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_1_0_enable_disable_account_webhook_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountWebhookPutJson body: AccountWebhookPutJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: AccountWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv3_1_0_enable_disable_account_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `o_bpv3_1_0_enable_disable_account_webhook`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `o_bpv3_1_0_enable_disable_account_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/obp/v5.0.0/banks/{BANK_ID}/account-web-hooks', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountWebhookJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_bpv3_1_0_get_account_webhooks(self, bank_id, **kwargs):  # noqa: E501
        """Get Account Webhooks  # noqa: E501

        <p>Get Account Webhooks.</p><p>Possible custom URL parameters for pagination:</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>account_id=STRING (if null ignore)</li><li>user_id=STRING (if null ignore)</li></ul><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_1_0_get_account_webhooks(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: AccountWebhooksJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv3_1_0_get_account_webhooks_with_http_info(bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv3_1_0_get_account_webhooks_with_http_info(bank_id, **kwargs)  # noqa: E501
            return data

    def o_bpv3_1_0_get_account_webhooks_with_http_info(self, bank_id, **kwargs):  # noqa: E501
        """Get Account Webhooks  # noqa: E501

        <p>Get Account Webhooks.</p><p>Possible custom URL parameters for pagination:</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>account_id=STRING (if null ignore)</li><li>user_id=STRING (if null ignore)</li></ul><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv3_1_0_get_account_webhooks_with_http_info(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: AccountWebhooksJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv3_1_0_get_account_webhooks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `o_bpv3_1_0_get_account_webhooks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/account-web-hooks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountWebhooksJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_bpv4_0_0_create_bank_account_notification_webhook(self, body, bank_id, **kwargs):  # noqa: E501
        """Create bank level Account Notification Webhook  # noqa: E501

        <p>Create a notification Webhook that will fire for all accounts on the specified Bank.</p><p>Webhooks are used to call external web services when certain events happen.</p><p>For instance, a webhook can be used to notify an external service if a transaction is created on an account.</p><p>When an account notification webhook fires it will POST to the URL you specify during the creation of the webhook.</p><p>Inside the payload you will find account_id and transaction_id and also user_ids and customer_ids of the Users / Customers linked to the Account.</p><p>The webhook will POST the following structure to your service:</p><p>{<br />&quot;event_name&quot;: &quot;OnCreateTransaction&quot;,<br />&quot;event_id&quot;: &quot;9ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;bank_id&quot;: &quot;gh.29.uk&quot;,<br />&quot;account_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;transaction_id&quot;: &quot;7ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;related_entities&quot;: [<br />{<br />&quot;user_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;customer_ids&quot;: [&quot;3ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;]<br />}<br />]<br />}</p><p>Thus, your service should accept the above POST body structure.</p><p>In this way, your web service can be informed about an event on an account and act accordingly.</p><p>Further information about the account, transaction or related entities can then be retrieved using the standard REST APIs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_bank_account_notification_webhook(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountNotificationWebhookPostJson body: AccountNotificationWebhookPostJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BankAccountNotificationWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv4_0_0_create_bank_account_notification_webhook_with_http_info(body, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv4_0_0_create_bank_account_notification_webhook_with_http_info(body, bank_id, **kwargs)  # noqa: E501
            return data

    def o_bpv4_0_0_create_bank_account_notification_webhook_with_http_info(self, body, bank_id, **kwargs):  # noqa: E501
        """Create bank level Account Notification Webhook  # noqa: E501

        <p>Create a notification Webhook that will fire for all accounts on the specified Bank.</p><p>Webhooks are used to call external web services when certain events happen.</p><p>For instance, a webhook can be used to notify an external service if a transaction is created on an account.</p><p>When an account notification webhook fires it will POST to the URL you specify during the creation of the webhook.</p><p>Inside the payload you will find account_id and transaction_id and also user_ids and customer_ids of the Users / Customers linked to the Account.</p><p>The webhook will POST the following structure to your service:</p><p>{<br />&quot;event_name&quot;: &quot;OnCreateTransaction&quot;,<br />&quot;event_id&quot;: &quot;9ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;bank_id&quot;: &quot;gh.29.uk&quot;,<br />&quot;account_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;transaction_id&quot;: &quot;7ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;related_entities&quot;: [<br />{<br />&quot;user_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;customer_ids&quot;: [&quot;3ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;]<br />}<br />]<br />}</p><p>Thus, your service should accept the above POST body structure.</p><p>In this way, your web service can be informed about an event on an account and act accordingly.</p><p>Further information about the account, transaction or related entities can then be retrieved using the standard REST APIs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_bank_account_notification_webhook_with_http_info(body, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountNotificationWebhookPostJson body: AccountNotificationWebhookPostJson object that needs to be added. (required)
        :param str bank_id: The bank id (required)
        :return: BankAccountNotificationWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv4_0_0_create_bank_account_notification_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `o_bpv4_0_0_create_bank_account_notification_webhook`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `o_bpv4_0_0_create_bank_account_notification_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}
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
            '/obp/v5.0.0/banks/{BANK_ID}/web-hooks/account/notifications/on-create-transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BankAccountNotificationWebhookJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def o_bpv4_0_0_create_system_account_notification_webhook(self, body, **kwargs):  # noqa: E501
        """Create system level Account Notification Webhook  # noqa: E501

        <p>Create a notification Webhook that will fire for all accounts on the system.</p><p>Webhooks are used to call external web services when certain events happen.</p><p>For instance, a webhook can be used to notify an external service if a transaction is created on an account.</p><p>When an account notification webhook fires it will POST to the URL you specify during the creation of the webhook.</p><p>Inside the payload you will find account_id and transaction_id and also user_ids and customer_ids of the Users / Customers linked to the Account.</p><p>The webhook will POST the following structure to your service:</p><p>{<br />&quot;event_name&quot;: &quot;OnCreateTransaction&quot;,<br />&quot;event_id&quot;: &quot;9ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;bank_id&quot;: &quot;gh.29.uk&quot;,<br />&quot;account_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;transaction_id&quot;: &quot;7ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;related_entities&quot;: [<br />{<br />&quot;user_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;customer_ids&quot;: [&quot;3ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;]<br />}<br />]<br />}</p><p>Thus, your service should accept the above POST body structure.</p><p>In this way, your web service can be informed about an event on an account and act accordingly.</p><p>Further information about the account, transaction or related entities can then be retrieved using the standard REST APIs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_system_account_notification_webhook(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountNotificationWebhookPostJson body: AccountNotificationWebhookPostJson object that needs to be added. (required)
        :return: SystemAccountNotificationWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.o_bpv4_0_0_create_system_account_notification_webhook_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.o_bpv4_0_0_create_system_account_notification_webhook_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def o_bpv4_0_0_create_system_account_notification_webhook_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create system level Account Notification Webhook  # noqa: E501

        <p>Create a notification Webhook that will fire for all accounts on the system.</p><p>Webhooks are used to call external web services when certain events happen.</p><p>For instance, a webhook can be used to notify an external service if a transaction is created on an account.</p><p>When an account notification webhook fires it will POST to the URL you specify during the creation of the webhook.</p><p>Inside the payload you will find account_id and transaction_id and also user_ids and customer_ids of the Users / Customers linked to the Account.</p><p>The webhook will POST the following structure to your service:</p><p>{<br />&quot;event_name&quot;: &quot;OnCreateTransaction&quot;,<br />&quot;event_id&quot;: &quot;9ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;bank_id&quot;: &quot;gh.29.uk&quot;,<br />&quot;account_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;transaction_id&quot;: &quot;7ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;related_entities&quot;: [<br />{<br />&quot;user_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;customer_ids&quot;: [&quot;3ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;]<br />}<br />]<br />}</p><p>Thus, your service should accept the above POST body structure.</p><p>In this way, your web service can be informed about an event on an account and act accordingly.</p><p>Further information about the account, transaction or related entities can then be retrieved using the standard REST APIs.</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.o_bpv4_0_0_create_system_account_notification_webhook_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountNotificationWebhookPostJson body: AccountNotificationWebhookPostJson object that needs to be added. (required)
        :return: SystemAccountNotificationWebhookJson
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method o_bpv4_0_0_create_system_account_notification_webhook" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `o_bpv4_0_0_create_system_account_notification_webhook`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/obp/v5.0.0/web-hooks/account/notifications/on-create-transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SystemAccountNotificationWebhookJson',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
