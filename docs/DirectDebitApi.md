# obp_python.DirectDebitApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_direct_debit**](DirectDebitApi.md#o_bpv4_0_0_create_direct_debit) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/direct-debit | Create Direct Debit
[**o_bpv4_0_0_create_direct_debit_management**](DirectDebitApi.md#o_bpv4_0_0_create_direct_debit_management) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/direct-debit | Create Direct Debit (management)


# **o_bpv4_0_0_create_direct_debit**
> DirectDebitJsonV400 o_bpv4_0_0_create_direct_debit(body, view_id, account_id, bank_id)

Create Direct Debit

<p>Create direct debit for an account.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DirectDebitApi(obp_python.ApiClient(configuration))
body = obp_python.PostDirectDebitJsonV400() # PostDirectDebitJsonV400 | PostDirectDebitJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Direct Debit
    api_response = api_instance.o_bpv4_0_0_create_direct_debit(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectDebitApi->o_bpv4_0_0_create_direct_debit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDirectDebitJsonV400**](PostDirectDebitJsonV400.md)| PostDirectDebitJsonV400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DirectDebitJsonV400**](DirectDebitJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_direct_debit_management**
> DirectDebitJsonV400 o_bpv4_0_0_create_direct_debit_management(body, account_id, bank_id)

Create Direct Debit (management)

<p>Create direct debit for an account.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DirectDebitApi(obp_python.ApiClient(configuration))
body = obp_python.PostDirectDebitJsonV400() # PostDirectDebitJsonV400 | PostDirectDebitJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Direct Debit (management)
    api_response = api_instance.o_bpv4_0_0_create_direct_debit_management(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectDebitApi->o_bpv4_0_0_create_direct_debit_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostDirectDebitJsonV400**](PostDirectDebitJsonV400.md)| PostDirectDebitJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DirectDebitJsonV400**](DirectDebitJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

