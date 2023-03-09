# obp_python.EndpointMappingApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_bank_level_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_create_bank_level_endpoint_mapping) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/endpoint-mappings | Create Bank Level Endpoint Mapping
[**o_bpv4_0_0_create_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_create_endpoint_mapping) | **POST** /obp/v5.0.0/management/endpoint-mappings | Create Endpoint Mapping
[**o_bpv4_0_0_delete_bank_level_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_delete_bank_level_endpoint_mapping) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/endpoint-mappings/ENDPOINT_MAPPING_ID | Delete Bank Level Endpoint Mapping
[**o_bpv4_0_0_delete_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_delete_endpoint_mapping) | **DELETE** /obp/v5.0.0/management/endpoint-mappings/ENDPOINT_MAPPING_ID | Delete Endpoint Mapping
[**o_bpv4_0_0_get_all_bank_level_endpoint_mappings**](EndpointMappingApi.md#o_bpv4_0_0_get_all_bank_level_endpoint_mappings) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/endpoint-mappings | Get all Bank Level Endpoint Mappings
[**o_bpv4_0_0_get_all_endpoint_mappings**](EndpointMappingApi.md#o_bpv4_0_0_get_all_endpoint_mappings) | **GET** /obp/v5.0.0/management/endpoint-mappings | Get all Endpoint Mappings
[**o_bpv4_0_0_get_bank_level_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_get_bank_level_endpoint_mapping) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/endpoint-mappings/ENDPOINT_MAPPING_ID | Get Bank Level Endpoint Mapping
[**o_bpv4_0_0_get_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_get_endpoint_mapping) | **GET** /obp/v5.0.0/management/endpoint-mappings/ENDPOINT_MAPPING_ID | Get Endpoint Mapping by Id
[**o_bpv4_0_0_update_bank_level_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_update_bank_level_endpoint_mapping) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/endpoint-mappings/ENDPOINT_MAPPING_ID | Update Bank Level Endpoint Mapping
[**o_bpv4_0_0_update_endpoint_mapping**](EndpointMappingApi.md#o_bpv4_0_0_update_endpoint_mapping) | **PUT** /obp/v5.0.0/management/endpoint-mappings/ENDPOINT_MAPPING_ID | Update Endpoint Mapping


# **o_bpv4_0_0_create_bank_level_endpoint_mapping**
> Body1 o_bpv4_0_0_create_bank_level_endpoint_mapping(body, bank_id)

Create Bank Level Endpoint Mapping

<p>Create an Bank Level Endpoint Mapping.</p><p>Note: at moment only support the dynamic endpoints</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
body = obp_python.Body1() # Body1 | JObject object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_create_bank_level_endpoint_mapping(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_create_bank_level_endpoint_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)| JObject object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**Body1**](Body1.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_endpoint_mapping**
> Body4 o_bpv4_0_0_create_endpoint_mapping(body)

Create Endpoint Mapping

<p>Create an Endpoint Mapping.</p><p>Note: at moment only support the dynamic endpoints</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
body = obp_python.Body4() # Body4 | JObject object that needs to be added.

try:
    # Create Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_create_endpoint_mapping(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_create_endpoint_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| JObject object that needs to be added. | 

### Return type

[**Body4**](Body4.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_endpoint_mapping**
> bool o_bpv4_0_0_delete_bank_level_endpoint_mapping(bank_id)

Delete Bank Level Endpoint Mapping

<p>Delete a Bank Level Endpoint Mapping.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_delete_bank_level_endpoint_mapping(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_delete_bank_level_endpoint_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

**bool**

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_endpoint_mapping**
> bool o_bpv4_0_0_delete_endpoint_mapping()

Delete Endpoint Mapping

<p>Delete a Endpoint Mapping.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))

try:
    # Delete Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_delete_endpoint_mapping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_delete_endpoint_mapping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_bank_level_endpoint_mappings**
> InlineResponse2007 o_bpv4_0_0_get_all_bank_level_endpoint_mappings(bank_id)

Get all Bank Level Endpoint Mappings

<p>Get all Bank Level Endpoint Mappings.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get all Bank Level Endpoint Mappings
    api_response = api_instance.o_bpv4_0_0_get_all_bank_level_endpoint_mappings(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_get_all_bank_level_endpoint_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_endpoint_mappings**
> InlineResponse2007 o_bpv4_0_0_get_all_endpoint_mappings()

Get all Endpoint Mappings

<p>Get all Endpoint Mappings.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))

try:
    # Get all Endpoint Mappings
    api_response = api_instance.o_bpv4_0_0_get_all_endpoint_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_get_all_endpoint_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_endpoint_mapping**
> InlineResponse2007Endpointmappings o_bpv4_0_0_get_bank_level_endpoint_mapping(bank_id)

Get Bank Level Endpoint Mapping

<p>Get an Bank Level Endpoint Mapping by ENDPOINT_MAPPING_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_get_bank_level_endpoint_mapping(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_get_bank_level_endpoint_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2007Endpointmappings**](InlineResponse2007Endpointmappings.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_endpoint_mapping**
> InlineResponse2007Endpointmappings o_bpv4_0_0_get_endpoint_mapping()

Get Endpoint Mapping by Id

<p>Get an Endpoint Mapping by ENDPOINT_MAPPING_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))

try:
    # Get Endpoint Mapping by Id
    api_response = api_instance.o_bpv4_0_0_get_endpoint_mapping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_get_endpoint_mapping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2007Endpointmappings**](InlineResponse2007Endpointmappings.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_endpoint_mapping**
> InlineResponse2007Endpointmappings o_bpv4_0_0_update_bank_level_endpoint_mapping(body, bank_id)

Update Bank Level Endpoint Mapping

<p>Update an Bank Level Endpoint Mapping.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
body = obp_python.Body2() # Body2 | JObject object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_update_bank_level_endpoint_mapping(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_update_bank_level_endpoint_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| JObject object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2007Endpointmappings**](InlineResponse2007Endpointmappings.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_endpoint_mapping**
> InlineResponse2007Endpointmappings o_bpv4_0_0_update_endpoint_mapping(body)

Update Endpoint Mapping

<p>Update an Endpoint Mapping.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.EndpointMappingApi(obp_python.ApiClient(configuration))
body = obp_python.Body5() # Body5 | JObject object that needs to be added.

try:
    # Update Endpoint Mapping
    api_response = api_instance.o_bpv4_0_0_update_endpoint_mapping(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointMappingApi->o_bpv4_0_0_update_endpoint_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)| JObject object that needs to be added. | 

### Return type

[**InlineResponse2007Endpointmappings**](InlineResponse2007Endpointmappings.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

