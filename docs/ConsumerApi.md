# obp_python.ConsumerApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_1_0_update_consumer_redirect_url**](ConsumerApi.md#o_bpv2_1_0_update_consumer_redirect_url) | **PUT** /obp/v5.0.0/management/consumers/{CONSUMER_ID}/consumer/redirect_url | Update Consumer RedirectUrl
[**o_bpv3_0_0_delete_scope**](ConsumerApi.md#o_bpv3_0_0_delete_scope) | **DELETE** /obp/v5.0.0/consumers/{CONSUMER_ID}/scope/{SCOPE_ID} | Delete Consumer Scope
[**o_bpv3_1_0_enable_disable_consumers**](ConsumerApi.md#o_bpv3_1_0_enable_disable_consumers) | **PUT** /obp/v5.0.0/management/consumers/{CONSUMER_ID} | Enable or Disable Consumers
[**o_bpv3_1_0_get_calls_limit**](ConsumerApi.md#o_bpv3_1_0_get_calls_limit) | **GET** /obp/v5.0.0/management/consumers/{CONSUMER_ID}/consumer/call-limits | Get Call Limits for a Consumer
[**o_bpv3_1_0_get_consumer**](ConsumerApi.md#o_bpv3_1_0_get_consumer) | **GET** /obp/v5.0.0/management/consumers/{CONSUMER_ID} | Get Consumer
[**o_bpv3_1_0_get_consumers**](ConsumerApi.md#o_bpv3_1_0_get_consumers) | **GET** /obp/v5.0.0/management/consumers | Get Consumers
[**o_bpv3_1_0_get_consumers_for_current_user**](ConsumerApi.md#o_bpv3_1_0_get_consumers_for_current_user) | **GET** /obp/v5.0.0/management/users/current/consumers | Get Consumers (logged in User)
[**o_bpv4_0_0_add_scope**](ConsumerApi.md#o_bpv4_0_0_add_scope) | **POST** /obp/v5.0.0/consumers/{CONSUMER_ID}/scopes | Create Scope for a Consumer
[**o_bpv4_0_0_calls_limit**](ConsumerApi.md#o_bpv4_0_0_calls_limit) | **PUT** /obp/v5.0.0/management/consumers/{CONSUMER_ID}/consumer/call-limits | Set Calls Limit for a Consumer
[**o_bpv4_0_0_create_consumer**](ConsumerApi.md#o_bpv4_0_0_create_consumer) | **POST** /obp/v5.0.0/management/consumers | Post a Consumer
[**o_bpv4_0_0_get_scopes**](ConsumerApi.md#o_bpv4_0_0_get_scopes) | **GET** /obp/v5.0.0/consumers/{CONSUMER_ID}/scopes | Get Scopes for Consumer


# **o_bpv2_1_0_update_consumer_redirect_url**
> ConsumerJSON o_bpv2_1_0_update_consumer_redirect_url(body, consumer_id)

Update Consumer RedirectUrl

<p>Update an existing redirectUrl for a Consumer specified by CONSUMER_ID.</p><p>CONSUMER_ID can be obtained after you register the application.</p><p>Or use the endpoint 'Get Consumers' to get it</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
body = obp_python.ConsumerRedirectUrlJSON() # ConsumerRedirectUrlJSON | ConsumerRedirectUrlJSON object that needs to be added.
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Update Consumer RedirectUrl
    api_response = api_instance.o_bpv2_1_0_update_consumer_redirect_url(body, consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv2_1_0_update_consumer_redirect_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsumerRedirectUrlJSON**](ConsumerRedirectUrlJSON.md)| ConsumerRedirectUrlJSON object that needs to be added. | 
 **consumer_id** | **str**| new consumer id | 

### Return type

[**ConsumerJSON**](ConsumerJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_delete_scope**
> o_bpv3_0_0_delete_scope(scope_id, consumer_id)

Delete Consumer Scope

<p>Delete Consumer Scope specified by SCOPE_ID for an consumer specified by CONSUMER_ID</p><p>Authentication is required and the user needs to be a Super Admin.<br />Super Admins are listed in the Props file.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
scope_id = 'scope_id_example' # str | the scope id
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Delete Consumer Scope
    api_instance.o_bpv3_0_0_delete_scope(scope_id, consumer_id)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv3_0_0_delete_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| the scope id | 
 **consumer_id** | **str**| new consumer id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_enable_disable_consumers**
> PutEnabledJSON o_bpv3_1_0_enable_disable_consumers(body, consumer_id)

Enable or Disable Consumers

<p>Enable/Disable a Consumer specified by CONSUMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
body = obp_python.PutEnabledJSON() # PutEnabledJSON | PutEnabledJSON object that needs to be added.
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Enable or Disable Consumers
    api_response = api_instance.o_bpv3_1_0_enable_disable_consumers(body, consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv3_1_0_enable_disable_consumers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutEnabledJSON**](PutEnabledJSON.md)| PutEnabledJSON object that needs to be added. | 
 **consumer_id** | **str**| new consumer id | 

### Return type

[**PutEnabledJSON**](PutEnabledJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_calls_limit**
> CallLimitJson o_bpv3_1_0_get_calls_limit(consumer_id)

Get Call Limits for a Consumer

<p>Get Calls limits per Consumer.<br />Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Get Call Limits for a Consumer
    api_response = api_instance.o_bpv3_1_0_get_calls_limit(consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv3_1_0_get_calls_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| new consumer id | 

### Return type

[**CallLimitJson**](CallLimitJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_consumer**
> ConsumerJSON o_bpv3_1_0_get_consumer(consumer_id)

Get Consumer

<p>Get the Consumer specified by CONSUMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Get Consumer
    api_response = api_instance.o_bpv3_1_0_get_consumer(consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv3_1_0_get_consumer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| new consumer id | 

### Return type

[**ConsumerJSON**](ConsumerJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_consumers**
> ConsumersJsonV310 o_bpv3_1_0_get_consumers()

Get Consumers

<p>Get the all Consumers.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))

try:
    # Get Consumers
    api_response = api_instance.o_bpv3_1_0_get_consumers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv3_1_0_get_consumers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsumersJsonV310**](ConsumersJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_consumers_for_current_user**
> ConsumersJsonV310 o_bpv3_1_0_get_consumers_for_current_user()

Get Consumers (logged in User)

<p>Get the Consumers for logged in User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))

try:
    # Get Consumers (logged in User)
    api_response = api_instance.o_bpv3_1_0_get_consumers_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv3_1_0_get_consumers_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsumersJsonV310**](ConsumersJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_add_scope**
> ScopeJson o_bpv4_0_0_add_scope(body, consumer_id)

Create Scope for a Consumer

<p>Create Scope. Grant Role to Consumer.</p><p>Scopes are used to grant System or Bank level roles to the Consumer (App). (For Account level privileges, see Views)</p><p>For a System level Role (.e.g CanGetAnyUser), set bank_id to an empty string i.e. &quot;bank_id&quot;:&quot;&quot;</p><p>For a Bank level Role (e.g. CanCreateAccount), set bank_id to a valid value e.g. &quot;bank_id&quot;:&quot;my-bank-id&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
body = obp_python.CreateScopeJson() # CreateScopeJson | CreateScopeJson object that needs to be added.
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Create Scope for a Consumer
    api_response = api_instance.o_bpv4_0_0_add_scope(body, consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv4_0_0_add_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateScopeJson**](CreateScopeJson.md)| CreateScopeJson object that needs to be added. | 
 **consumer_id** | **str**| new consumer id | 

### Return type

[**ScopeJson**](ScopeJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_calls_limit**
> CallLimitPostJsonV400 o_bpv4_0_0_calls_limit(body, consumer_id)

Set Calls Limit for a Consumer

<p>Set the API call limits for a Consumer:</p><p>Per Second<br />Per Minute<br />Per Hour<br />Per Week<br />Per Month</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
body = obp_python.CallLimitPostJsonV400() # CallLimitPostJsonV400 | CallLimitPostJsonV400 object that needs to be added.
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Set Calls Limit for a Consumer
    api_response = api_instance.o_bpv4_0_0_calls_limit(body, consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv4_0_0_calls_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CallLimitPostJsonV400**](CallLimitPostJsonV400.md)| CallLimitPostJsonV400 object that needs to be added. | 
 **consumer_id** | **str**| new consumer id | 

### Return type

[**CallLimitPostJsonV400**](CallLimitPostJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_consumer**
> ConsumerJson o_bpv4_0_0_create_consumer(body)

Post a Consumer

<p>Create a Consumer (Authenticated access).</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
body = obp_python.ConsumerPostJSON() # ConsumerPostJSON | ConsumerPostJSON object that needs to be added.

try:
    # Post a Consumer
    api_response = api_instance.o_bpv4_0_0_create_consumer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv4_0_0_create_consumer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsumerPostJSON**](ConsumerPostJSON.md)| ConsumerPostJSON object that needs to be added. | 

### Return type

[**ConsumerJson**](ConsumerJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_scopes**
> ScopeJsons o_bpv4_0_0_get_scopes(consumer_id)

Get Scopes for Consumer

<p>Get all the scopes for an consumer specified by CONSUMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsumerApi(obp_python.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Get Scopes for Consumer
    api_response = api_instance.o_bpv4_0_0_get_scopes(consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumerApi->o_bpv4_0_0_get_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_id** | **str**| new consumer id | 

### Return type

[**ScopeJsons**](ScopeJsons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

