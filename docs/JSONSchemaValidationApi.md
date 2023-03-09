# obp_python.JSONSchemaValidationApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_json_schema_validation**](JSONSchemaValidationApi.md#o_bpv4_0_0_create_json_schema_validation) | **POST** /obp/v5.0.0/management/json-schema-validations/OPERATION_ID | Create a JSON Schema Validation
[**o_bpv4_0_0_delete_json_schema_validation**](JSONSchemaValidationApi.md#o_bpv4_0_0_delete_json_schema_validation) | **DELETE** /obp/v5.0.0/management/json-schema-validations/OPERATION_ID | Delete a JSON Schema Validation
[**o_bpv4_0_0_get_all_json_schema_validations**](JSONSchemaValidationApi.md#o_bpv4_0_0_get_all_json_schema_validations) | **GET** /obp/v5.0.0/management/json-schema-validations | Get all JSON Schema Validations
[**o_bpv4_0_0_get_all_json_schema_validations_public**](JSONSchemaValidationApi.md#o_bpv4_0_0_get_all_json_schema_validations_public) | **GET** /obp/v5.0.0/endpoints/json-schema-validations | Get all JSON Schema Validations - public
[**o_bpv4_0_0_get_json_schema_validation**](JSONSchemaValidationApi.md#o_bpv4_0_0_get_json_schema_validation) | **GET** /obp/v5.0.0/management/json-schema-validations/OPERATION_ID | Get a JSON Schema Validation
[**o_bpv4_0_0_update_json_schema_validation**](JSONSchemaValidationApi.md#o_bpv4_0_0_update_json_schema_validation) | **PUT** /obp/v5.0.0/management/json-schema-validations/OPERATION_ID | Update a JSON Schema Validation


# **o_bpv4_0_0_create_json_schema_validation**
> JsonValidationV400 o_bpv4_0_0_create_json_schema_validation(body)

Create a JSON Schema Validation

<p>Create a JSON Schema Validation.</p><p>Please supply a json-schema as request body.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.JSONSchemaValidationApi(obp_python.ApiClient(configuration))
body = obp_python.JsonSchemaV400() # JsonSchemaV400 | JsonSchemaV400 object that needs to be added.

try:
    # Create a JSON Schema Validation
    api_response = api_instance.o_bpv4_0_0_create_json_schema_validation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONSchemaValidationApi->o_bpv4_0_0_create_json_schema_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonSchemaV400**](JsonSchemaV400.md)| JsonSchemaV400 object that needs to be added. | 

### Return type

[**JsonValidationV400**](JsonValidationV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_json_schema_validation**
> bool o_bpv4_0_0_delete_json_schema_validation()

Delete a JSON Schema Validation

<p>Delete a JSON Schema Validation by operation_id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.JSONSchemaValidationApi(obp_python.ApiClient(configuration))

try:
    # Delete a JSON Schema Validation
    api_response = api_instance.o_bpv4_0_0_delete_json_schema_validation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONSchemaValidationApi->o_bpv4_0_0_delete_json_schema_validation: %s\n" % e)
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

# **o_bpv4_0_0_get_all_json_schema_validations**
> InlineResponse2002 o_bpv4_0_0_get_all_json_schema_validations()

Get all JSON Schema Validations

<p>Get all JSON Schema Validations.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.JSONSchemaValidationApi(obp_python.ApiClient(configuration))

try:
    # Get all JSON Schema Validations
    api_response = api_instance.o_bpv4_0_0_get_all_json_schema_validations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONSchemaValidationApi->o_bpv4_0_0_get_all_json_schema_validations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_json_schema_validations_public**
> InlineResponse2002 o_bpv4_0_0_get_all_json_schema_validations_public()

Get all JSON Schema Validations - public

<p>Get all JSON Schema Validations - public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.JSONSchemaValidationApi(obp_python.ApiClient(configuration))

try:
    # Get all JSON Schema Validations - public
    api_response = api_instance.o_bpv4_0_0_get_all_json_schema_validations_public()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONSchemaValidationApi->o_bpv4_0_0_get_all_json_schema_validations_public: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_json_schema_validation**
> JsonValidationV400 o_bpv4_0_0_get_json_schema_validation()

Get a JSON Schema Validation

<p>Get a JSON Schema Validation by operation_id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.JSONSchemaValidationApi(obp_python.ApiClient(configuration))

try:
    # Get a JSON Schema Validation
    api_response = api_instance.o_bpv4_0_0_get_json_schema_validation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONSchemaValidationApi->o_bpv4_0_0_get_json_schema_validation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonValidationV400**](JsonValidationV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_json_schema_validation**
> JsonValidationV400 o_bpv4_0_0_update_json_schema_validation(body)

Update a JSON Schema Validation

<p>Update a JSON Schema Validation.</p><p>Please supply a json-schema as request body</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.JSONSchemaValidationApi(obp_python.ApiClient(configuration))
body = obp_python.JsonSchemaV400() # JsonSchemaV400 | JsonSchemaV400 object that needs to be added.

try:
    # Update a JSON Schema Validation
    api_response = api_instance.o_bpv4_0_0_update_json_schema_validation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONSchemaValidationApi->o_bpv4_0_0_update_json_schema_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonSchemaV400**](JsonSchemaV400.md)| JsonSchemaV400 object that needs to be added. | 

### Return type

[**JsonValidationV400**](JsonValidationV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

