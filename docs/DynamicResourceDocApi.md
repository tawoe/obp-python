# obp_python.DynamicResourceDocApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_build_dynamic_endpoint_template**](DynamicResourceDocApi.md#o_bpv4_0_0_build_dynamic_endpoint_template) | **POST** /obp/v5.0.0/management/dynamic-resource-docs/endpoint-code | Create Dynamic Resource Doc endpoint code
[**o_bpv4_0_0_create_bank_level_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_create_bank_level_dynamic_resource_doc) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-resource-docs | Create Bank Level Dynamic Resource Doc
[**o_bpv4_0_0_create_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_create_dynamic_resource_doc) | **POST** /obp/v5.0.0/management/dynamic-resource-docs | Create Dynamic Resource Doc
[**o_bpv4_0_0_delete_bank_level_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_delete_bank_level_dynamic_resource_doc) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID | Delete Bank Level Dynamic Resource Doc
[**o_bpv4_0_0_delete_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_delete_dynamic_resource_doc) | **DELETE** /obp/v5.0.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID | Delete Dynamic Resource Doc
[**o_bpv4_0_0_get_all_bank_level_dynamic_resource_docs**](DynamicResourceDocApi.md#o_bpv4_0_0_get_all_bank_level_dynamic_resource_docs) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-resource-docs | Get all Bank Level Dynamic Resource Docs
[**o_bpv4_0_0_get_all_dynamic_resource_docs**](DynamicResourceDocApi.md#o_bpv4_0_0_get_all_dynamic_resource_docs) | **GET** /obp/v5.0.0/management/dynamic-resource-docs | Get all Dynamic Resource Docs
[**o_bpv4_0_0_get_bank_level_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_get_bank_level_dynamic_resource_doc) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID | Get Bank Level Dynamic Resource Doc by Id
[**o_bpv4_0_0_get_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_get_dynamic_resource_doc) | **GET** /obp/v5.0.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID | Get Dynamic Resource Doc by Id
[**o_bpv4_0_0_test_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_test_dynamic_resource_doc) | **POST** /test-dynamic-resource-doc/my_user/MY_USER_ID | A test endpoint
[**o_bpv4_0_0_update_bank_level_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_update_bank_level_dynamic_resource_doc) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID | Update Bank Level Dynamic Resource Doc
[**o_bpv4_0_0_update_dynamic_resource_doc**](DynamicResourceDocApi.md#o_bpv4_0_0_update_dynamic_resource_doc) | **PUT** /obp/v5.0.0/management/dynamic-resource-docs/DYNAMIC-RESOURCE-DOC-ID | Update Dynamic Resource Doc


# **o_bpv4_0_0_build_dynamic_endpoint_template**
> Tuple2 o_bpv4_0_0_build_dynamic_endpoint_template(body)

Create Dynamic Resource Doc endpoint code

<p>Create a Dynamic Resource Doc endpoint code.</p><p>copy the response and past to PractiseEndpoint, So you can have the benefits of<br />auto compilation and debug</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
body = obp_python.ResourceDocFragment() # ResourceDocFragment | ResourceDocFragment object that needs to be added.

try:
    # Create Dynamic Resource Doc endpoint code
    api_response = api_instance.o_bpv4_0_0_build_dynamic_endpoint_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_build_dynamic_endpoint_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceDocFragment**](ResourceDocFragment.md)| ResourceDocFragment object that needs to be added. | 

### Return type

[**Tuple2**](Tuple2.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_bank_level_dynamic_resource_doc**
> JsonDynamicResourceDoc o_bpv4_0_0_create_bank_level_dynamic_resource_doc(body, bank_id)

Create Bank Level Dynamic Resource Doc

<p>Create a Bank Level Dynamic Resource Doc.</p><p>The connector_method_body is URL-encoded format String</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicResourceDoc() # JsonDynamicResourceDoc | JsonDynamicResourceDoc object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Dynamic Resource Doc
    api_response = api_instance.o_bpv4_0_0_create_bank_level_dynamic_resource_doc(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_create_bank_level_dynamic_resource_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)| JsonDynamicResourceDoc object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_dynamic_resource_doc**
> JsonDynamicResourceDoc o_bpv4_0_0_create_dynamic_resource_doc(body)

Create Dynamic Resource Doc

<p>Create a Dynamic Resource Doc.</p><p>The connector_method_body is URL-encoded format String</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicResourceDoc() # JsonDynamicResourceDoc | JsonDynamicResourceDoc object that needs to be added.

try:
    # Create Dynamic Resource Doc
    api_response = api_instance.o_bpv4_0_0_create_dynamic_resource_doc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_create_dynamic_resource_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)| JsonDynamicResourceDoc object that needs to be added. | 

### Return type

[**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_dynamic_resource_doc**
> bool o_bpv4_0_0_delete_bank_level_dynamic_resource_doc(bank_id)

Delete Bank Level Dynamic Resource Doc

<p>Delete a Bank Level Dynamic Resource Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Dynamic Resource Doc
    api_response = api_instance.o_bpv4_0_0_delete_bank_level_dynamic_resource_doc(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_delete_bank_level_dynamic_resource_doc: %s\n" % e)
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

# **o_bpv4_0_0_delete_dynamic_resource_doc**
> bool o_bpv4_0_0_delete_dynamic_resource_doc()

Delete Dynamic Resource Doc

<p>Delete a Dynamic Resource Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))

try:
    # Delete Dynamic Resource Doc
    api_response = api_instance.o_bpv4_0_0_delete_dynamic_resource_doc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_delete_dynamic_resource_doc: %s\n" % e)
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

# **o_bpv4_0_0_get_all_bank_level_dynamic_resource_docs**
> InlineResponse2006 o_bpv4_0_0_get_all_bank_level_dynamic_resource_docs(bank_id)

Get all Bank Level Dynamic Resource Docs

<p>Get all Bank Level Dynamic Resource Docs.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get all Bank Level Dynamic Resource Docs
    api_response = api_instance.o_bpv4_0_0_get_all_bank_level_dynamic_resource_docs(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_get_all_bank_level_dynamic_resource_docs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_dynamic_resource_docs**
> InlineResponse2006 o_bpv4_0_0_get_all_dynamic_resource_docs()

Get all Dynamic Resource Docs

<p>Get all Dynamic Resource Docs.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))

try:
    # Get all Dynamic Resource Docs
    api_response = api_instance.o_bpv4_0_0_get_all_dynamic_resource_docs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_get_all_dynamic_resource_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_resource_doc**
> JsonDynamicResourceDoc o_bpv4_0_0_get_bank_level_dynamic_resource_doc(bank_id)

Get Bank Level Dynamic Resource Doc by Id

<p>Get a Bank Level Dynamic Resource Doc by DYNAMIC-RESOURCE-DOC-ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Resource Doc by Id
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_resource_doc(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_get_bank_level_dynamic_resource_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_dynamic_resource_doc**
> JsonDynamicResourceDoc o_bpv4_0_0_get_dynamic_resource_doc()

Get Dynamic Resource Doc by Id

<p>Get a Dynamic Resource Doc by DYNAMIC-RESOURCE-DOC-ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))

try:
    # Get Dynamic Resource Doc by Id
    api_response = api_instance.o_bpv4_0_0_get_dynamic_resource_doc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_get_dynamic_resource_doc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_test_dynamic_resource_doc**
> RequestRootJsonClass o_bpv4_0_0_test_dynamic_resource_doc(body)

A test endpoint

<p>A test endpoint.</p><p>Just for debug method body of dynamic resource doc.<br />better watch the following introduction video first<br />* <a href=\"https://vimeo.com/623381607\">Dynamic resourceDoc version1</a></p><p>The endpoint return the response from PractiseEndpoint code.<br />Here, code.api.DynamicEndpoints.dynamic.practise.PractiseEndpoint.process<br />You can test the method body grammar, and try the business logic, but need to restart the OBP-API code .</p><p>Authentication is Optional</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
body = obp_python.RequestRootJsonClass() # RequestRootJsonClass | RequestRootJsonClass object that needs to be added.

try:
    # A test endpoint
    api_response = api_instance.o_bpv4_0_0_test_dynamic_resource_doc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_test_dynamic_resource_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestRootJsonClass**](RequestRootJsonClass.md)| RequestRootJsonClass object that needs to be added. | 

### Return type

[**RequestRootJsonClass**](RequestRootJsonClass.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_dynamic_resource_doc**
> JsonDynamicResourceDoc o_bpv4_0_0_update_bank_level_dynamic_resource_doc(body, bank_id)

Update Bank Level Dynamic Resource Doc

<p>Update a Bank Level Dynamic Resource Doc.</p><p>The connector_method_body is URL-encoded format String</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicResourceDoc() # JsonDynamicResourceDoc | JsonDynamicResourceDoc object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Dynamic Resource Doc
    api_response = api_instance.o_bpv4_0_0_update_bank_level_dynamic_resource_doc(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_update_bank_level_dynamic_resource_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)| JsonDynamicResourceDoc object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_dynamic_resource_doc**
> JsonDynamicResourceDoc o_bpv4_0_0_update_dynamic_resource_doc(body)

Update Dynamic Resource Doc

<p>Update a Dynamic Resource Doc.</p><p>The connector_method_body is URL-encoded format String</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicResourceDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicResourceDoc() # JsonDynamicResourceDoc | JsonDynamicResourceDoc object that needs to be added.

try:
    # Update Dynamic Resource Doc
    api_response = api_instance.o_bpv4_0_0_update_dynamic_resource_doc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicResourceDocApi->o_bpv4_0_0_update_dynamic_resource_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)| JsonDynamicResourceDoc object that needs to be added. | 

### Return type

[**JsonDynamicResourceDoc**](JsonDynamicResourceDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

