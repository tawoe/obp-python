# obp_python.WebhookApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_account_webhook**](WebhookApi.md#o_bpv3_1_0_create_account_webhook) | **POST** /obp/v5.0.0/banks/{BANK_ID}/account-web-hooks | Create an Account Webhook
[**o_bpv3_1_0_enable_disable_account_webhook**](WebhookApi.md#o_bpv3_1_0_enable_disable_account_webhook) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/account-web-hooks | Enable/Disable an Account Webhook
[**o_bpv3_1_0_get_account_webhooks**](WebhookApi.md#o_bpv3_1_0_get_account_webhooks) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/account-web-hooks | Get Account Webhooks
[**o_bpv4_0_0_create_bank_account_notification_webhook**](WebhookApi.md#o_bpv4_0_0_create_bank_account_notification_webhook) | **POST** /obp/v5.0.0/banks/{BANK_ID}/web-hooks/account/notifications/on-create-transaction | Create bank level Account Notification Webhook
[**o_bpv4_0_0_create_system_account_notification_webhook**](WebhookApi.md#o_bpv4_0_0_create_system_account_notification_webhook) | **POST** /obp/v5.0.0/web-hooks/account/notifications/on-create-transaction | Create system level Account Notification Webhook


# **o_bpv3_1_0_create_account_webhook**
> AccountWebhookJson o_bpv3_1_0_create_account_webhook(body, bank_id)

Create an Account Webhook

<p>Create an Account Webhook</p><p>Webhooks are used to call external URLs when certain events happen.</p><p>Account Webhooks focus on events around accounts.</p><p>For instance, a webhook could be used to notify an external service if a balance changes on an account.</p><p>This functionality is work in progress! Please note that only implemented trigger is: OnBalanceChange</p><p>Authentication is Mandatory</p>

### Example
```python
from __future__ import print_function
import time
import obp_python
from obp_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: directLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: gatewayLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = obp_python.WebhookApi(obp_python.ApiClient(configuration))
body = obp_python.AccountWebhookPostJson() # AccountWebhookPostJson | AccountWebhookPostJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create an Account Webhook
    api_response = api_instance.o_bpv3_1_0_create_account_webhook(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->o_bpv3_1_0_create_account_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountWebhookPostJson**](AccountWebhookPostJson.md)| AccountWebhookPostJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountWebhookJson**](AccountWebhookJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_enable_disable_account_webhook**
> AccountWebhookJson o_bpv3_1_0_enable_disable_account_webhook(body, bank_id)

Enable/Disable an Account Webhook

<p>Enable/Disable an Account Webhook</p><p>Webhooks are used to call external URLs when certain events happen.</p><p>Account Webhooks focus on events around accounts.</p><p>For instance, a webhook could be used to notify an external service if a balance changes on an account.</p><p>This functionality is work in progress! Please note that only implemented trigger is: OnBalanceChange</p><p>Authentication is Mandatory</p>

### Example
```python
from __future__ import print_function
import time
import obp_python
from obp_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: directLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: gatewayLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = obp_python.WebhookApi(obp_python.ApiClient(configuration))
body = obp_python.AccountWebhookPutJson() # AccountWebhookPutJson | AccountWebhookPutJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Enable/Disable an Account Webhook
    api_response = api_instance.o_bpv3_1_0_enable_disable_account_webhook(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->o_bpv3_1_0_enable_disable_account_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountWebhookPutJson**](AccountWebhookPutJson.md)| AccountWebhookPutJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountWebhookJson**](AccountWebhookJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_account_webhooks**
> AccountWebhooksJson o_bpv3_1_0_get_account_webhooks(bank_id)

Get Account Webhooks

<p>Get Account Webhooks.</p><p>Possible custom URL parameters for pagination:</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>account_id=STRING (if null ignore)</li><li>user_id=STRING (if null ignore)</li></ul><p>Authentication is Mandatory</p>

### Example
```python
from __future__ import print_function
import time
import obp_python
from obp_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: directLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: gatewayLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = obp_python.WebhookApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Webhooks
    api_response = api_instance.o_bpv3_1_0_get_account_webhooks(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->o_bpv3_1_0_get_account_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountWebhooksJson**](AccountWebhooksJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_bank_account_notification_webhook**
> BankAccountNotificationWebhookJson o_bpv4_0_0_create_bank_account_notification_webhook(body, bank_id)

Create bank level Account Notification Webhook

<p>Create a notification Webhook that will fire for all accounts on the specified Bank.</p><p>Webhooks are used to call external web services when certain events happen.</p><p>For instance, a webhook can be used to notify an external service if a transaction is created on an account.</p><p>When an account notification webhook fires it will POST to the URL you specify during the creation of the webhook.</p><p>Inside the payload you will find account_id and transaction_id and also user_ids and customer_ids of the Users / Customers linked to the Account.</p><p>The webhook will POST the following structure to your service:</p><p>{<br />&quot;event_name&quot;: &quot;OnCreateTransaction&quot;,<br />&quot;event_id&quot;: &quot;9ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;bank_id&quot;: &quot;gh.29.uk&quot;,<br />&quot;account_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;transaction_id&quot;: &quot;7ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;related_entities&quot;: [<br />{<br />&quot;user_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;customer_ids&quot;: [&quot;3ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;]<br />}<br />]<br />}</p><p>Thus, your service should accept the above POST body structure.</p><p>In this way, your web service can be informed about an event on an account and act accordingly.</p><p>Further information about the account, transaction or related entities can then be retrieved using the standard REST APIs.</p><p>Authentication is Mandatory</p>

### Example
```python
from __future__ import print_function
import time
import obp_python
from obp_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: directLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: gatewayLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = obp_python.WebhookApi(obp_python.ApiClient(configuration))
body = obp_python.AccountNotificationWebhookPostJson() # AccountNotificationWebhookPostJson | AccountNotificationWebhookPostJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create bank level Account Notification Webhook
    api_response = api_instance.o_bpv4_0_0_create_bank_account_notification_webhook(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->o_bpv4_0_0_create_bank_account_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountNotificationWebhookPostJson**](AccountNotificationWebhookPostJson.md)| AccountNotificationWebhookPostJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BankAccountNotificationWebhookJson**](BankAccountNotificationWebhookJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_system_account_notification_webhook**
> SystemAccountNotificationWebhookJson o_bpv4_0_0_create_system_account_notification_webhook(body)

Create system level Account Notification Webhook

<p>Create a notification Webhook that will fire for all accounts on the system.</p><p>Webhooks are used to call external web services when certain events happen.</p><p>For instance, a webhook can be used to notify an external service if a transaction is created on an account.</p><p>When an account notification webhook fires it will POST to the URL you specify during the creation of the webhook.</p><p>Inside the payload you will find account_id and transaction_id and also user_ids and customer_ids of the Users / Customers linked to the Account.</p><p>The webhook will POST the following structure to your service:</p><p>{<br />&quot;event_name&quot;: &quot;OnCreateTransaction&quot;,<br />&quot;event_id&quot;: &quot;9ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;bank_id&quot;: &quot;gh.29.uk&quot;,<br />&quot;account_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;transaction_id&quot;: &quot;7ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;related_entities&quot;: [<br />{<br />&quot;user_id&quot;: &quot;8ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;,<br />&quot;customer_ids&quot;: [&quot;3ca9a7e4-6d02-40e3-a129-0b2bf89de9b1&quot;]<br />}<br />]<br />}</p><p>Thus, your service should accept the above POST body structure.</p><p>In this way, your web service can be informed about an event on an account and act accordingly.</p><p>Further information about the account, transaction or related entities can then be retrieved using the standard REST APIs.</p><p>Authentication is Mandatory</p>

### Example
```python
from __future__ import print_function
import time
import obp_python
from obp_python.rest import ApiException
from pprint import pprint

# Configure API key authorization: directLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure API key authorization: gatewayLogin
configuration = obp_python.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = obp_python.WebhookApi(obp_python.ApiClient(configuration))
body = obp_python.AccountNotificationWebhookPostJson() # AccountNotificationWebhookPostJson | AccountNotificationWebhookPostJson object that needs to be added.

try:
    # Create system level Account Notification Webhook
    api_response = api_instance.o_bpv4_0_0_create_system_account_notification_webhook(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->o_bpv4_0_0_create_system_account_notification_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountNotificationWebhookPostJson**](AccountNotificationWebhookPostJson.md)| AccountNotificationWebhookPostJson object that needs to be added. | 

### Return type

[**SystemAccountNotificationWebhookJson**](SystemAccountNotificationWebhookJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

