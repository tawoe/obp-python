# obp_python.DynamicMessageDocApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_bank_level_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_create_bank_level_dynamic_message_doc) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs | Create Bank Level Dynamic Message Doc
[**o_bpv4_0_0_create_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_create_dynamic_message_doc) | **POST** /obp/v5.0.0/management/dynamic-message-docs | Create Dynamic Message Doc
[**o_bpv4_0_0_delete_bank_level_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_delete_bank_level_dynamic_message_doc) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID | Delete Bank Level Dynamic Message Doc
[**o_bpv4_0_0_delete_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_delete_dynamic_message_doc) | **DELETE** /obp/v5.0.0/management/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID | Delete Dynamic Message Doc
[**o_bpv4_0_0_get_all_bank_level_dynamic_message_docs**](DynamicMessageDocApi.md#o_bpv4_0_0_get_all_bank_level_dynamic_message_docs) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs | Get all Bank Level Dynamic Message Docs
[**o_bpv4_0_0_get_all_dynamic_message_docs**](DynamicMessageDocApi.md#o_bpv4_0_0_get_all_dynamic_message_docs) | **GET** /obp/v5.0.0/management/dynamic-message-docs | Get all Dynamic Message Docs
[**o_bpv4_0_0_get_bank_level_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_get_bank_level_dynamic_message_doc) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID | Get Bank Level Dynamic Message Doc
[**o_bpv4_0_0_get_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_get_dynamic_message_doc) | **GET** /obp/v5.0.0/management/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID | Get Dynamic Message Doc
[**o_bpv4_0_0_update_bank_level_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_update_bank_level_dynamic_message_doc) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID | Update Bank Level Dynamic Message Doc
[**o_bpv4_0_0_update_dynamic_message_doc**](DynamicMessageDocApi.md#o_bpv4_0_0_update_dynamic_message_doc) | **PUT** /obp/v5.0.0/management/dynamic-message-docs/DYNAMIC_MESSAGE_DOC_ID | Update Dynamic Message Doc


# **o_bpv4_0_0_create_bank_level_dynamic_message_doc**
> JsonDynamicMessageDoc o_bpv4_0_0_create_bank_level_dynamic_message_doc(body, bank_id)

Create Bank Level Dynamic Message Doc

<p>Create a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicMessageDoc() # JsonDynamicMessageDoc | JsonDynamicMessageDoc object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_create_bank_level_dynamic_message_doc(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_create_bank_level_dynamic_message_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)| JsonDynamicMessageDoc object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_dynamic_message_doc**
> JsonDynamicMessageDoc o_bpv4_0_0_create_dynamic_message_doc(body)

Create Dynamic Message Doc

<p>Create a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicMessageDoc() # JsonDynamicMessageDoc | JsonDynamicMessageDoc object that needs to be added.

try:
    # Create Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_create_dynamic_message_doc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_create_dynamic_message_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)| JsonDynamicMessageDoc object that needs to be added. | 

### Return type

[**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_dynamic_message_doc**
> bool o_bpv4_0_0_delete_bank_level_dynamic_message_doc(bank_id)

Delete Bank Level Dynamic Message Doc

<p>Delete a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_delete_bank_level_dynamic_message_doc(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_delete_bank_level_dynamic_message_doc: %s\n" % e)
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

# **o_bpv4_0_0_delete_dynamic_message_doc**
> bool o_bpv4_0_0_delete_dynamic_message_doc()

Delete Dynamic Message Doc

<p>Delete a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))

try:
    # Delete Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_delete_dynamic_message_doc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_delete_dynamic_message_doc: %s\n" % e)
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

# **o_bpv4_0_0_get_all_bank_level_dynamic_message_docs**
> InlineResponse2005 o_bpv4_0_0_get_all_bank_level_dynamic_message_docs(bank_id)

Get all Bank Level Dynamic Message Docs

<p>Get all Bank Level Dynamic Message Docs.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get all Bank Level Dynamic Message Docs
    api_response = api_instance.o_bpv4_0_0_get_all_bank_level_dynamic_message_docs(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_get_all_bank_level_dynamic_message_docs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_dynamic_message_docs**
> InlineResponse2005 o_bpv4_0_0_get_all_dynamic_message_docs()

Get all Dynamic Message Docs

<p>Get all Dynamic Message Docs.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))

try:
    # Get all Dynamic Message Docs
    api_response = api_instance.o_bpv4_0_0_get_all_dynamic_message_docs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_get_all_dynamic_message_docs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_message_doc**
> JsonDynamicMessageDoc o_bpv4_0_0_get_bank_level_dynamic_message_doc(bank_id)

Get Bank Level Dynamic Message Doc

<p>Get a Bank Level Dynamic Message Doc by DYNAMIC_MESSAGE_DOC_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_message_doc(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_get_bank_level_dynamic_message_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_dynamic_message_doc**
> JsonDynamicMessageDoc o_bpv4_0_0_get_dynamic_message_doc()

Get Dynamic Message Doc

<p>Get a Dynamic Message Doc by DYNAMIC_MESSAGE_DOC_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))

try:
    # Get Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_get_dynamic_message_doc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_get_dynamic_message_doc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_dynamic_message_doc**
> JsonDynamicMessageDoc o_bpv4_0_0_update_bank_level_dynamic_message_doc(body, bank_id)

Update Bank Level Dynamic Message Doc

<p>Update a Bank Level Dynamic Message Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicMessageDoc() # JsonDynamicMessageDoc | JsonDynamicMessageDoc object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_update_bank_level_dynamic_message_doc(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_update_bank_level_dynamic_message_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)| JsonDynamicMessageDoc object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_dynamic_message_doc**
> JsonDynamicMessageDoc o_bpv4_0_0_update_dynamic_message_doc(body)

Update Dynamic Message Doc

<p>Update a Dynamic Message Doc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicMessageDocApi(obp_python.ApiClient(configuration))
body = obp_python.JsonDynamicMessageDoc() # JsonDynamicMessageDoc | JsonDynamicMessageDoc object that needs to be added.

try:
    # Update Dynamic Message Doc
    api_response = api_instance.o_bpv4_0_0_update_dynamic_message_doc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicMessageDocApi->o_bpv4_0_0_update_dynamic_message_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)| JsonDynamicMessageDoc object that needs to be added. | 

### Return type

[**JsonDynamicMessageDoc**](JsonDynamicMessageDoc.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

