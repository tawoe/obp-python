# obp_python.ScopeApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_0_0_delete_scope**](ScopeApi.md#o_bpv3_0_0_delete_scope) | **DELETE** /obp/v5.0.0/consumers/{CONSUMER_ID}/scope/{SCOPE_ID} | Delete Consumer Scope
[**o_bpv4_0_0_add_scope**](ScopeApi.md#o_bpv4_0_0_add_scope) | **POST** /obp/v5.0.0/consumers/{CONSUMER_ID}/scopes | Create Scope for a Consumer
[**o_bpv4_0_0_get_scopes**](ScopeApi.md#o_bpv4_0_0_get_scopes) | **GET** /obp/v5.0.0/consumers/{CONSUMER_ID}/scopes | Get Scopes for Consumer


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
api_instance = obp_python.ScopeApi(obp_python.ApiClient(configuration))
scope_id = 'scope_id_example' # str | the scope id
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Delete Consumer Scope
    api_instance.o_bpv3_0_0_delete_scope(scope_id, consumer_id)
except ApiException as e:
    print("Exception when calling ScopeApi->o_bpv3_0_0_delete_scope: %s\n" % e)
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
api_instance = obp_python.ScopeApi(obp_python.ApiClient(configuration))
body = obp_python.CreateScopeJson() # CreateScopeJson | CreateScopeJson object that needs to be added.
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Create Scope for a Consumer
    api_response = api_instance.o_bpv4_0_0_add_scope(body, consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopeApi->o_bpv4_0_0_add_scope: %s\n" % e)
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
api_instance = obp_python.ScopeApi(obp_python.ApiClient(configuration))
consumer_id = 'consumer_id_example' # str | new consumer id

try:
    # Get Scopes for Consumer
    api_response = api_instance.o_bpv4_0_0_get_scopes(consumer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopeApi->o_bpv4_0_0_get_scopes: %s\n" % e)
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

