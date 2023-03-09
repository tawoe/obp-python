# obp_python.AccountPublicApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_0_0_public_accounts_all_banks**](AccountPublicApi.md#o_bpv2_0_0_public_accounts_all_banks) | **GET** /obp/v5.0.0/accounts/public | Get Public Accounts at all Banks
[**o_bpv2_0_0_public_accounts_at_one_bank**](AccountPublicApi.md#o_bpv2_0_0_public_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/public | Get Public Accounts at Bank
[**o_bpv3_0_0_get_public_account_by_id**](AccountPublicApi.md#o_bpv3_0_0_get_public_account_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/public/accounts/{ACCOUNT_ID}/{VIEW_ID}/account | Get Public Account by Id


# **o_bpv2_0_0_public_accounts_all_banks**
> BasicAccountsJSON o_bpv2_0_0_public_accounts_all_banks(body)

Get Public Accounts at all Banks

<p>Get public accounts at all banks (Anonymous access).<br />Returns accounts that contain at least one public view (a view where is_public is true)<br />For each account the API returns the ID and the available views.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountPublicApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Public Accounts at all Banks
    api_response = api_instance.o_bpv2_0_0_public_accounts_all_banks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountPublicApi->o_bpv2_0_0_public_accounts_all_banks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**BasicAccountsJSON**](BasicAccountsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_public_accounts_at_one_bank**
> BasicAccountsJSON o_bpv2_0_0_public_accounts_at_one_bank(body, bank_id)

Get Public Accounts at Bank

<p>Returns a list of the public accounts (Anonymous access) at BANK_ID. For each account the API returns the ID and the available views.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountPublicApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Public Accounts at Bank
    api_response = api_instance.o_bpv2_0_0_public_accounts_at_one_bank(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountPublicApi->o_bpv2_0_0_public_accounts_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BasicAccountsJSON**](BasicAccountsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_public_account_by_id**
> ModeratedCoreAccountJsonV300 o_bpv3_0_0_get_public_account_by_id(view_id, account_id, bank_id)

Get Public Account by Id

<p>Returns information about an account that has a public view.</p><p>The account is specified by ACCOUNT_ID. The information is moderated by the view specified by VIEW_ID.</p><ul><li>Number</li><li>Owners</li><li>Type</li><li>Balance</li><li>Routing</li></ul><p>PSD2 Context: PSD2 requires customers to have access to their account information via third party applications.<br />This call provides balance and other account information via delegated authentication using OAuth.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountPublicApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Public Account by Id
    api_response = api_instance.o_bpv3_0_0_get_public_account_by_id(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountPublicApi->o_bpv3_0_0_get_public_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ModeratedCoreAccountJsonV300**](ModeratedCoreAccountJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

