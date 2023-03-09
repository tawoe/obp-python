# obp_python.DynamicEndpointManageApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_bank_level_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_create_bank_level_dynamic_endpoint) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints | Create Bank Level Dynamic Endpoint
[**o_bpv4_0_0_create_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_create_dynamic_endpoint) | **POST** /obp/v5.0.0/management/dynamic-endpoints | Create Dynamic Endpoint
[**o_bpv4_0_0_delete_bank_level_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_delete_bank_level_dynamic_endpoint) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints/DYNAMIC_ENDPOINT_ID |  Delete Bank Level Dynamic Endpoint
[**o_bpv4_0_0_delete_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_delete_dynamic_endpoint) | **DELETE** /obp/v5.0.0/management/dynamic-endpoints/DYNAMIC_ENDPOINT_ID |  Delete Dynamic Endpoint
[**o_bpv4_0_0_delete_my_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_delete_my_dynamic_endpoint) | **DELETE** /obp/v5.0.0/my/dynamic-endpoints/DYNAMIC_ENDPOINT_ID | Delete My Dynamic Endpoint
[**o_bpv4_0_0_get_bank_level_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_get_bank_level_dynamic_endpoint) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints/DYNAMIC_ENDPOINT_ID |  Get Bank Level Dynamic Endpoint
[**o_bpv4_0_0_get_bank_level_dynamic_endpoints**](DynamicEndpointManageApi.md#o_bpv4_0_0_get_bank_level_dynamic_endpoints) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints | Get Bank Level Dynamic Endpoints
[**o_bpv4_0_0_get_dynamic_endpoint**](DynamicEndpointManageApi.md#o_bpv4_0_0_get_dynamic_endpoint) | **GET** /obp/v5.0.0/management/dynamic-endpoints/DYNAMIC_ENDPOINT_ID | Get Dynamic Endpoint
[**o_bpv4_0_0_get_dynamic_endpoints**](DynamicEndpointManageApi.md#o_bpv4_0_0_get_dynamic_endpoints) | **GET** /obp/v5.0.0/management/dynamic-endpoints |  Get Dynamic Endpoints
[**o_bpv4_0_0_get_my_dynamic_endpoints**](DynamicEndpointManageApi.md#o_bpv4_0_0_get_my_dynamic_endpoints) | **GET** /obp/v5.0.0/my/dynamic-endpoints | Get My Dynamic Endpoints
[**o_bpv4_0_0_update_bank_level_dynamic_endpoint_host**](DynamicEndpointManageApi.md#o_bpv4_0_0_update_bank_level_dynamic_endpoint_host) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints/DYNAMIC_ENDPOINT_ID/host |  Update Bank Level Dynamic Endpoint Host
[**o_bpv4_0_0_update_dynamic_endpoint_host**](DynamicEndpointManageApi.md#o_bpv4_0_0_update_dynamic_endpoint_host) | **PUT** /obp/v5.0.0/management/dynamic-endpoints/DYNAMIC_ENDPOINT_ID/host |  Update Dynamic Endpoint Host


# **o_bpv4_0_0_create_bank_level_dynamic_endpoint**
> InlineResponse201 o_bpv4_0_0_create_bank_level_dynamic_endpoint(body, bank_id)

Create Bank Level Dynamic Endpoint

<p>Create dynamic endpoints.</p><p>Create dynamic endpoints with one json format swagger content.</p><p>If the host of swagger is <code>dynamic_entity</code>, then you need link the swagger fields to the dynamic entity fields,<br />please check <code>Endpoint Mapping</code> endpoints.</p><p>If the host of swagger is <code>obp_mock</code>, every dynamic endpoint will return example response of swagger,</p><p>when create MethodRouting for given dynamic endpoint, it will be routed to given url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
body = obp_python.Body() # Body | JObject object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_create_bank_level_dynamic_endpoint(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_create_bank_level_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| JObject object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_dynamic_endpoint**
> InlineResponse2011 o_bpv4_0_0_create_dynamic_endpoint(body)

Create Dynamic Endpoint

<p>Create dynamic endpoints.</p><p>Create dynamic endpoints with one json format swagger content.</p><p>If the host of swagger is <code>dynamic_entity</code>, then you need link the swagger fields to the dynamic entity fields,<br />please check <code>Endpoint Mapping</code> endpoints.</p><p>If the host of swagger is <code>obp_mock</code>, every dynamic endpoint will return example response of swagger,</p><p>when create MethodRouting for given dynamic endpoint, it will be routed to given url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
body = obp_python.Body3() # Body3 | JObject object that needs to be added.

try:
    # Create Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_create_dynamic_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_create_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| JObject object that needs to be added. | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_dynamic_endpoint**
> o_bpv4_0_0_delete_bank_level_dynamic_endpoint(bank_id)

 Delete Bank Level Dynamic Endpoint

<p>Delete a Bank Level DynamicEndpoint specified by DYNAMIC_ENDPOINT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    #  Delete Bank Level Dynamic Endpoint
    api_instance.o_bpv4_0_0_delete_bank_level_dynamic_endpoint(bank_id)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_delete_bank_level_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_dynamic_endpoint**
> o_bpv4_0_0_delete_dynamic_endpoint()

 Delete Dynamic Endpoint

<p>Delete a DynamicEndpoint specified by DYNAMIC_ENDPOINT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))

try:
    #  Delete Dynamic Endpoint
    api_instance.o_bpv4_0_0_delete_dynamic_endpoint()
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_delete_dynamic_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_dynamic_endpoint**
> o_bpv4_0_0_delete_my_dynamic_endpoint()

Delete My Dynamic Endpoint

<p>Delete a DynamicEndpoint specified by DYNAMIC_ENDPOINT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))

try:
    # Delete My Dynamic Endpoint
    api_instance.o_bpv4_0_0_delete_my_dynamic_endpoint()
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_delete_my_dynamic_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_endpoint**
> InlineResponse201 o_bpv4_0_0_get_bank_level_dynamic_endpoint(bank_id)

 Get Bank Level Dynamic Endpoint

<p>Get a Bank Level Dynamic Endpoint.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    #  Get Bank Level Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_endpoint(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_get_bank_level_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_endpoints**
> InlineResponse2003 o_bpv4_0_0_get_bank_level_dynamic_endpoints(bank_id)

Get Bank Level Dynamic Endpoints

<p>Get Bank Level Dynamic Endpoints.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Endpoints
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_endpoints(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_get_bank_level_dynamic_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_dynamic_endpoint**
> InlineResponse2011 o_bpv4_0_0_get_dynamic_endpoint()

Get Dynamic Endpoint

<p>Get a Dynamic Endpoint.</p><p>Get one DynamicEndpoint,</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))

try:
    # Get Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_get_dynamic_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_get_dynamic_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_dynamic_endpoints**
> InlineResponse2009 o_bpv4_0_0_get_dynamic_endpoints()

 Get Dynamic Endpoints

<p>Get Dynamic Endpoints.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))

try:
    #  Get Dynamic Endpoints
    api_response = api_instance.o_bpv4_0_0_get_dynamic_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_get_dynamic_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_dynamic_endpoints**
> InlineResponse20012 o_bpv4_0_0_get_my_dynamic_endpoints()

Get My Dynamic Endpoints

<p>Get My Dynamic Endpoints.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))

try:
    # Get My Dynamic Endpoints
    api_response = api_instance.o_bpv4_0_0_get_my_dynamic_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_get_my_dynamic_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_dynamic_endpoint_host**
> DynamicEndpointHostJson400 o_bpv4_0_0_update_bank_level_dynamic_endpoint_host(body, bank_id)

 Update Bank Level Dynamic Endpoint Host

<p>Update Bank Level  dynamic endpoint Host.<br />The value can be obp_mock, dynamic_entity, or some service url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEndpointHostJson400() # DynamicEndpointHostJson400 | DynamicEndpointHostJson400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    #  Update Bank Level Dynamic Endpoint Host
    api_response = api_instance.o_bpv4_0_0_update_bank_level_dynamic_endpoint_host(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_update_bank_level_dynamic_endpoint_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)| DynamicEndpointHostJson400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_dynamic_endpoint_host**
> DynamicEndpointHostJson400 o_bpv4_0_0_update_dynamic_endpoint_host(body)

 Update Dynamic Endpoint Host

<p>Update dynamic endpoint Host.<br />The value can be obp_mock, dynamic_entity, or some service url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEndpointManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEndpointHostJson400() # DynamicEndpointHostJson400 | DynamicEndpointHostJson400 object that needs to be added.

try:
    #  Update Dynamic Endpoint Host
    api_response = api_instance.o_bpv4_0_0_update_dynamic_endpoint_host(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEndpointManageApi->o_bpv4_0_0_update_dynamic_endpoint_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)| DynamicEndpointHostJson400 object that needs to be added. | 

### Return type

[**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

