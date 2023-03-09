# obp_python.AccountApplicationApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_account_application**](AccountApplicationApi.md#o_bpv3_1_0_create_account_application) | **POST** /obp/v5.0.0/banks/{BANK_ID}/account-applications | Create Account Application
[**o_bpv3_1_0_get_account_application**](AccountApplicationApi.md#o_bpv3_1_0_get_account_application) | **GET** /obp/v5.0.0/banks/{BANK_ID}/account-applications/{ACCOUNT_APPLICATION_ID} | Get Account Application by Id
[**o_bpv3_1_0_get_account_applications**](AccountApplicationApi.md#o_bpv3_1_0_get_account_applications) | **GET** /obp/v5.0.0/banks/{BANK_ID}/account-applications | Get Account Applications
[**o_bpv3_1_0_update_account_application_status**](AccountApplicationApi.md#o_bpv3_1_0_update_account_application_status) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/account-applications/{ACCOUNT_APPLICATION_ID} | Update Account Application Status


# **o_bpv3_1_0_create_account_application**
> AccountApplicationResponseJson o_bpv3_1_0_create_account_application(body, bank_id)

Create Account Application

<p>Create Account Application</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApplicationApi(obp_python.ApiClient(configuration))
body = obp_python.AccountApplicationJson() # AccountApplicationJson | AccountApplicationJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Account Application
    api_response = api_instance.o_bpv3_1_0_create_account_application(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApplicationApi->o_bpv3_1_0_create_account_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountApplicationJson**](AccountApplicationJson.md)| AccountApplicationJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountApplicationResponseJson**](AccountApplicationResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_account_application**
> AccountApplicationResponseJson o_bpv3_1_0_get_account_application(account_application_id, bank_id)

Get Account Application by Id

<p>Get the Account Application.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApplicationApi(obp_python.ApiClient(configuration))
account_application_id = 'account_application_id_example' # str | the account application id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Application by Id
    api_response = api_instance.o_bpv3_1_0_get_account_application(account_application_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApplicationApi->o_bpv3_1_0_get_account_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_application_id** | **str**| the account application id  | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountApplicationResponseJson**](AccountApplicationResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_account_applications**
> AccountApplicationsJsonV310 o_bpv3_1_0_get_account_applications(bank_id)

Get Account Applications

<p>Get the Account Applications.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApplicationApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Applications
    api_response = api_instance.o_bpv3_1_0_get_account_applications(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApplicationApi->o_bpv3_1_0_get_account_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountApplicationsJsonV310**](AccountApplicationsJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_account_application_status**
> AccountApplicationResponseJson o_bpv3_1_0_update_account_application_status(body, account_application_id, bank_id)

Update Account Application Status

<p>Update an Account Application status</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApplicationApi(obp_python.ApiClient(configuration))
body = obp_python.AccountApplicationUpdateStatusJson() # AccountApplicationUpdateStatusJson | AccountApplicationUpdateStatusJson object that needs to be added.
account_application_id = 'account_application_id_example' # str | the account application id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Account Application Status
    api_response = api_instance.o_bpv3_1_0_update_account_application_status(body, account_application_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApplicationApi->o_bpv3_1_0_update_account_application_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountApplicationUpdateStatusJson**](AccountApplicationUpdateStatusJson.md)| AccountApplicationUpdateStatusJson object that needs to be added. | 
 **account_application_id** | **str**| the account application id  | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountApplicationResponseJson**](AccountApplicationResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

