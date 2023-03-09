# obp_python.AuthenticationTypeValidationApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_authentication_type_validation**](AuthenticationTypeValidationApi.md#o_bpv4_0_0_create_authentication_type_validation) | **POST** /obp/v5.0.0/management/authentication-type-validations/OPERATION_ID | Create an Authentication Type Validation
[**o_bpv4_0_0_delete_authentication_type_validation**](AuthenticationTypeValidationApi.md#o_bpv4_0_0_delete_authentication_type_validation) | **DELETE** /obp/v5.0.0/management/authentication-type-validations/OPERATION_ID | Delete an Authentication Type Validation
[**o_bpv4_0_0_get_all_authentication_type_validations**](AuthenticationTypeValidationApi.md#o_bpv4_0_0_get_all_authentication_type_validations) | **GET** /obp/v5.0.0/management/authentication-type-validations | Get all Authentication Type Validations
[**o_bpv4_0_0_get_all_authentication_type_validations_public**](AuthenticationTypeValidationApi.md#o_bpv4_0_0_get_all_authentication_type_validations_public) | **GET** /obp/v5.0.0/endpoints/authentication-type-validations | Get all Authentication Type Validations - public
[**o_bpv4_0_0_get_authentication_type_validation**](AuthenticationTypeValidationApi.md#o_bpv4_0_0_get_authentication_type_validation) | **GET** /obp/v5.0.0/management/authentication-type-validations/OPERATION_ID | Get an Authentication Type Validation
[**o_bpv4_0_0_update_authentication_type_validation**](AuthenticationTypeValidationApi.md#o_bpv4_0_0_update_authentication_type_validation) | **PUT** /obp/v5.0.0/management/authentication-type-validations/OPERATION_ID | Update an Authentication Type Validation


# **o_bpv4_0_0_create_authentication_type_validation**
> JsonAuthTypeValidation o_bpv4_0_0_create_authentication_type_validation(body)

Create an Authentication Type Validation

<p>Create an Authentication Type Validation.</p><p>Please supply allowed authentication types.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AuthenticationTypeValidationApi(obp_python.ApiClient(configuration))
body = obp_python.Coloncolon() # Coloncolon | $colon$colon object that needs to be added.

try:
    # Create an Authentication Type Validation
    api_response = api_instance.o_bpv4_0_0_create_authentication_type_validation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationTypeValidationApi->o_bpv4_0_0_create_authentication_type_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Coloncolon**](Coloncolon.md)| $colon$colon object that needs to be added. | 

### Return type

[**JsonAuthTypeValidation**](JsonAuthTypeValidation.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_authentication_type_validation**
> bool o_bpv4_0_0_delete_authentication_type_validation()

Delete an Authentication Type Validation

<p>Delete an Authentication Type Validation by operation_id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AuthenticationTypeValidationApi(obp_python.ApiClient(configuration))

try:
    # Delete an Authentication Type Validation
    api_response = api_instance.o_bpv4_0_0_delete_authentication_type_validation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationTypeValidationApi->o_bpv4_0_0_delete_authentication_type_validation: %s\n" % e)
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

# **o_bpv4_0_0_get_all_authentication_type_validations**
> InlineResponse2001 o_bpv4_0_0_get_all_authentication_type_validations()

Get all Authentication Type Validations

<p>Get all Authentication Type Validations.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AuthenticationTypeValidationApi(obp_python.ApiClient(configuration))

try:
    # Get all Authentication Type Validations
    api_response = api_instance.o_bpv4_0_0_get_all_authentication_type_validations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationTypeValidationApi->o_bpv4_0_0_get_all_authentication_type_validations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_authentication_type_validations_public**
> InlineResponse2001 o_bpv4_0_0_get_all_authentication_type_validations_public()

Get all Authentication Type Validations - public

<p>Get all Authentication Type Validations - public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AuthenticationTypeValidationApi(obp_python.ApiClient(configuration))

try:
    # Get all Authentication Type Validations - public
    api_response = api_instance.o_bpv4_0_0_get_all_authentication_type_validations_public()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationTypeValidationApi->o_bpv4_0_0_get_all_authentication_type_validations_public: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_authentication_type_validation**
> JsonAuthTypeValidation o_bpv4_0_0_get_authentication_type_validation()

Get an Authentication Type Validation

<p>Get an Authentication Type Validation by operation_id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AuthenticationTypeValidationApi(obp_python.ApiClient(configuration))

try:
    # Get an Authentication Type Validation
    api_response = api_instance.o_bpv4_0_0_get_authentication_type_validation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationTypeValidationApi->o_bpv4_0_0_get_authentication_type_validation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonAuthTypeValidation**](JsonAuthTypeValidation.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_authentication_type_validation**
> JsonAuthTypeValidation o_bpv4_0_0_update_authentication_type_validation(body)

Update an Authentication Type Validation

<p>Update an Authentication Type Validation.</p><p>Please supply allowed authentication types.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AuthenticationTypeValidationApi(obp_python.ApiClient(configuration))
body = obp_python.Coloncolon() # Coloncolon | $colon$colon object that needs to be added.

try:
    # Update an Authentication Type Validation
    api_response = api_instance.o_bpv4_0_0_update_authentication_type_validation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationTypeValidationApi->o_bpv4_0_0_update_authentication_type_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Coloncolon**](Coloncolon.md)| $colon$colon object that needs to be added. | 

### Return type

[**JsonAuthTypeValidation**](JsonAuthTypeValidation.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

