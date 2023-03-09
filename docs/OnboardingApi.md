# obp_python.OnboardingApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_0_0_create_user**](OnboardingApi.md#o_bpv2_0_0_create_user) | **POST** /obp/v5.0.0/users | Create User
[**o_bpv5_0_0_create_account**](OnboardingApi.md#o_bpv5_0_0_create_account) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID} | Create Account


# **o_bpv2_0_0_create_user**
> UserJsonV200 o_bpv2_0_0_create_user(body)

Create User

<p>Creates OBP user.<br />No authorisation (currently) required.</p><p>Mimics current webform to Register.</p><p>Requires username(email) and password.</p><p>Returns 409 error if username not unique.</p><p>May require validation of email address.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.OnboardingApi(obp_python.ApiClient(configuration))
body = obp_python.CreateUserJson() # CreateUserJson | CreateUserJson object that needs to be added.

try:
    # Create User
    api_response = api_instance.o_bpv2_0_0_create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnboardingApi->o_bpv2_0_0_create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserJson**](CreateUserJson.md)| CreateUserJson object that needs to be added. | 

### Return type

[**UserJsonV200**](UserJsonV200.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_account**
> CreateAccountResponseJsonV310 o_bpv5_0_0_create_account(body, account_id, bank_id)

Create Account

<p>Create Account at bank specified by BANK_ID with Id specified by ACCOUNT_ID.</p><p>The User can create an Account for themself  - or -  the User that has the USER_ID specified in the POST body.</p><p>If the PUT body USER_ID <em>is</em> specified, the logged in user must have the Role canCreateAccount. Once created, the Account will be owned by the User specified by USER_ID.</p><p>If the PUT body USER_ID is <em>not</em> specified, the account will be owned by the logged in User.</p><p>The 'product_code' field SHOULD be a product_code from Product.<br />If the 'product_code' matches a product_code from Product, account attributes will be created that match the Product Attributes.</p><p>Note: The Amount MUST be zero.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.OnboardingApi(obp_python.ApiClient(configuration))
body = obp_python.CreateAccountRequestJsonV500() # CreateAccountRequestJsonV500 | CreateAccountRequestJsonV500 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Account
    api_response = api_instance.o_bpv5_0_0_create_account(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OnboardingApi->o_bpv5_0_0_create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAccountRequestJsonV500**](CreateAccountRequestJsonV500.md)| CreateAccountRequestJsonV500 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CreateAccountResponseJsonV310**](CreateAccountResponseJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

