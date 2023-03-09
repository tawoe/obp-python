# obp_python.UserApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_0_0_add_entitlement**](UserApi.md#o_bpv2_0_0_add_entitlement) | **POST** /obp/v5.0.0/users/{USER_ID}/entitlements | Add Entitlement for a User
[**o_bpv2_0_0_create_user**](UserApi.md#o_bpv2_0_0_create_user) | **POST** /obp/v5.0.0/users | Create User
[**o_bpv2_0_0_delete_entitlement**](UserApi.md#o_bpv2_0_0_delete_entitlement) | **DELETE** /obp/v5.0.0/users/{USER_ID}/entitlement/{ENTITLEMENT_ID} | Delete Entitlement
[**o_bpv2_0_0_get_permissions_for_bank_account**](UserApi.md#o_bpv2_0_0_get_permissions_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/permissions | Get access
[**o_bpv2_1_0_get_entitlements_by_bank_and_user**](UserApi.md#o_bpv2_1_0_get_entitlements_by_bank_and_user) | **GET** /obp/v5.0.0/banks/{BANK_ID}/users/{USER_ID}/entitlements | Get Entitlements for User at Bank
[**o_bpv3_0_0_add_entitlement_request**](UserApi.md#o_bpv3_0_0_add_entitlement_request) | **POST** /obp/v5.0.0/entitlement-requests | Create Entitlement Request for current User
[**o_bpv3_0_0_delete_entitlement_request**](UserApi.md#o_bpv3_0_0_delete_entitlement_request) | **DELETE** /obp/v5.0.0/entitlement-requests/{ENTITLEMENT_REQUEST_ID} | Delete Entitlement Request
[**o_bpv3_0_0_get_all_entitlement_requests**](UserApi.md#o_bpv3_0_0_get_all_entitlement_requests) | **GET** /obp/v5.0.0/entitlement-requests | Get all Entitlement Requests
[**o_bpv3_0_0_get_current_user**](UserApi.md#o_bpv3_0_0_get_current_user) | **GET** /obp/v5.0.0/users/current | Get User (Current)
[**o_bpv3_0_0_get_customers_for_user**](UserApi.md#o_bpv3_0_0_get_customers_for_user) | **GET** /obp/v5.0.0/users/current/customers | Get Customers for Current User
[**o_bpv3_0_0_get_entitlement_requests**](UserApi.md#o_bpv3_0_0_get_entitlement_requests) | **GET** /obp/v5.0.0/users/{USER_ID}/entitlement-requests | Get Entitlement Requests for a User
[**o_bpv3_0_0_get_entitlement_requests_for_current_user**](UserApi.md#o_bpv3_0_0_get_entitlement_requests_for_current_user) | **GET** /obp/v5.0.0/my/entitlement-requests | Get Entitlement Requests for the current User
[**o_bpv3_0_0_get_entitlements_for_current_user**](UserApi.md#o_bpv3_0_0_get_entitlements_for_current_user) | **GET** /obp/v5.0.0/my/entitlements | Get Entitlements for the current User
[**o_bpv3_0_0_get_permission_for_user_for_bank_account**](UserApi.md#o_bpv3_0_0_get_permission_for_user_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/permissions/{PROVIDER}/{PROVIDER_ID} | Get Account access for User
[**o_bpv3_1_0_delete_user_auth_context_by_id**](UserApi.md#o_bpv3_1_0_delete_user_auth_context_by_id) | **DELETE** /obp/v5.0.0/users/{USER_ID}/auth-context/{USER_AUTH_CONTEXT_ID} | Delete User Auth Context
[**o_bpv3_1_0_delete_user_auth_contexts**](UserApi.md#o_bpv3_1_0_delete_user_auth_contexts) | **DELETE** /obp/v5.0.0/users/{USER_ID}/auth-context | Delete User&#39;s Auth Contexts
[**o_bpv3_1_0_get_bad_login_status**](UserApi.md#o_bpv3_1_0_get_bad_login_status) | **GET** /obp/v5.0.0/users/{USERNAME}/lock-status | Get User Lock Status
[**o_bpv3_1_0_refresh_user**](UserApi.md#o_bpv3_1_0_refresh_user) | **POST** /obp/v5.0.0/users/{USER_ID}/refresh | Refresh User
[**o_bpv3_1_0_unlock_user**](UserApi.md#o_bpv3_1_0_unlock_user) | **PUT** /obp/v5.0.0/users/{USERNAME}/lock-status | Unlock the user
[**o_bpv4_0_0_create_current_user_attribute**](UserApi.md#o_bpv4_0_0_create_current_user_attribute) | **POST** /obp/v5.0.0/my/user/attributes | Create User Attribute for current user
[**o_bpv4_0_0_create_user_customer_links**](UserApi.md#o_bpv4_0_0_create_user_customer_links) | **POST** /obp/v5.0.0/banks/{BANK_ID}/user_customer_links | Create User Customer Link
[**o_bpv4_0_0_create_user_with_account_access**](UserApi.md#o_bpv4_0_0_create_user_with_account_access) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/user-account-access | Create (DAuth) User with Account Access
[**o_bpv4_0_0_create_user_with_roles**](UserApi.md#o_bpv4_0_0_create_user_with_roles) | **POST** /obp/v5.0.0/user-entitlements | Create (DAuth) User with Roles
[**o_bpv4_0_0_delete_user**](UserApi.md#o_bpv4_0_0_delete_user) | **DELETE** /obp/v5.0.0/users/{USER_ID} | Delete a User
[**o_bpv4_0_0_get_current_user_attributes**](UserApi.md#o_bpv4_0_0_get_current_user_attributes) | **GET** /obp/v5.0.0/my/user/attributes | Get User Attributes for current user
[**o_bpv4_0_0_get_current_user_id**](UserApi.md#o_bpv4_0_0_get_current_user_id) | **GET** /obp/v5.0.0/users/current/user_id | Get User Id (Current)
[**o_bpv4_0_0_get_customers_at_any_bank**](UserApi.md#o_bpv4_0_0_get_customers_at_any_bank) | **GET** /obp/v5.0.0/customers | Get Customers at Any Bank
[**o_bpv4_0_0_get_customers_minimal_at_any_bank**](UserApi.md#o_bpv4_0_0_get_customers_minimal_at_any_bank) | **GET** /obp/v5.0.0/customers-minimal | Get Customers Minimal at Any Bank
[**o_bpv4_0_0_get_entitlements**](UserApi.md#o_bpv4_0_0_get_entitlements) | **GET** /obp/v5.0.0/users/{USER_ID}/entitlements | Get Entitlements for User
[**o_bpv4_0_0_get_entitlements_for_bank**](UserApi.md#o_bpv4_0_0_get_entitlements_for_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/entitlements | Get Entitlements for One Bank
[**o_bpv4_0_0_get_logout_link**](UserApi.md#o_bpv4_0_0_get_logout_link) | **GET** /obp/v5.0.0/users/current/logout-link | Get Logout Link
[**o_bpv4_0_0_get_my_spaces**](UserApi.md#o_bpv4_0_0_get_my_spaces) | **GET** /obp/v5.0.0/my/spaces | Get My Spaces
[**o_bpv4_0_0_get_user_by_user_id**](UserApi.md#o_bpv4_0_0_get_user_by_user_id) | **GET** /obp/v5.0.0/users/user_id/{USER_ID} | Get User by USER_ID
[**o_bpv4_0_0_get_user_by_username**](UserApi.md#o_bpv4_0_0_get_user_by_username) | **GET** /obp/v5.0.0/users/username/{USERNAME} | Get User by USERNAME
[**o_bpv4_0_0_get_user_with_attributes**](UserApi.md#o_bpv4_0_0_get_user_with_attributes) | **GET** /obp/v5.0.0/users/{USER_ID}/attributes | Get User Attributes for the user
[**o_bpv4_0_0_get_users**](UserApi.md#o_bpv4_0_0_get_users) | **GET** /obp/v5.0.0/users | Get all Users
[**o_bpv4_0_0_get_users_by_email**](UserApi.md#o_bpv4_0_0_get_users_by_email) | **GET** /obp/v5.0.0/users/email/EMAIL/terminator | Get Users by Email Address
[**o_bpv4_0_0_grant_user_access_to_view**](UserApi.md#o_bpv4_0_0_grant_user_access_to_view) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account-access/grant | Grant User access to View
[**o_bpv4_0_0_lock_user**](UserApi.md#o_bpv4_0_0_lock_user) | **POST** /obp/v5.0.0/users/{USERNAME}/locks | Lock the user
[**o_bpv4_0_0_reset_password_url**](UserApi.md#o_bpv4_0_0_reset_password_url) | **POST** /obp/v5.0.0/management/user/reset-password-url | Create password reset url
[**o_bpv4_0_0_revoke_grant_user_access_to_views**](UserApi.md#o_bpv4_0_0_revoke_grant_user_access_to_views) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account-access | Revoke/Grant User access to View
[**o_bpv4_0_0_revoke_user_access_to_view**](UserApi.md#o_bpv4_0_0_revoke_user_access_to_view) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account-access/revoke | Revoke User access to View
[**o_bpv4_0_0_update_current_user_attribute**](UserApi.md#o_bpv4_0_0_update_current_user_attribute) | **PUT** /obp/v5.0.0/my/user/attributes/USER_ATTRIBUTE_ID | Update User Attribute for current user
[**o_bpv5_0_0_answer_user_auth_context_update_challenge**](UserApi.md#o_bpv5_0_0_answer_user_auth_context_update_challenge) | **POST** /obp/v5.0.0/banks/{BANK_ID}/users/current/auth-context-updates/{AUTH_CONTEXT_UPDATE_ID}/challenge | Answer User Auth Context Update Challenge
[**o_bpv5_0_0_create_user_auth_context**](UserApi.md#o_bpv5_0_0_create_user_auth_context) | **POST** /obp/v5.0.0/users/{USER_ID}/auth-context | Create User Auth Context
[**o_bpv5_0_0_create_user_auth_context_update_request**](UserApi.md#o_bpv5_0_0_create_user_auth_context_update_request) | **POST** /obp/v5.0.0/banks/{BANK_ID}/users/current/auth-context-updates/{SCA_METHOD} | Create User Auth Context Update Request
[**o_bpv5_0_0_get_customers_at_one_bank**](UserApi.md#o_bpv5_0_0_get_customers_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers | Get Customers at Bank
[**o_bpv5_0_0_get_customers_minimal_at_one_bank**](UserApi.md#o_bpv5_0_0_get_customers_minimal_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers-minimal | Get Customers Minimal at Bank
[**o_bpv5_0_0_get_my_customers_at_any_bank**](UserApi.md#o_bpv5_0_0_get_my_customers_at_any_bank) | **GET** /obp/v5.0.0/my/customers | Get My Customers
[**o_bpv5_0_0_get_user_auth_contexts**](UserApi.md#o_bpv5_0_0_get_user_auth_contexts) | **GET** /obp/v5.0.0/users/{USER_ID}/auth-context | Get User Auth Contexts


# **o_bpv2_0_0_add_entitlement**
> EntitlementJSON o_bpv2_0_0_add_entitlement(body, user_id)

Add Entitlement for a User

<p>Create Entitlement. Grant Role to User.</p><p>Entitlements are used to grant System or Bank level roles to Users. (For Account level privileges, see Views)</p><p>For a System level Role (.e.g CanGetAnyUser), set bank_id to an empty string i.e. &quot;bank_id&quot;:&quot;&quot;</p><p>For a Bank level Role (e.g. CanCreateAccount), set bank_id to a valid value e.g. &quot;bank_id&quot;:&quot;my-bank-id&quot;</p><p>Authentication is required and the user needs to be a Super Admin. Super Admins are listed in the Props file.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.CreateEntitlementJSON() # CreateEntitlementJSON | CreateEntitlementJSON object that needs to be added.
user_id = 'user_id_example' # str | The user id

try:
    # Add Entitlement for a User
    api_response = api_instance.o_bpv2_0_0_add_entitlement(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv2_0_0_add_entitlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntitlementJSON**](CreateEntitlementJSON.md)| CreateEntitlementJSON object that needs to be added. | 
 **user_id** | **str**| The user id | 

### Return type

[**EntitlementJSON**](EntitlementJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.CreateUserJson() # CreateUserJson | CreateUserJson object that needs to be added.

try:
    # Create User
    api_response = api_instance.o_bpv2_0_0_create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv2_0_0_create_user: %s\n" % e)
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

# **o_bpv2_0_0_delete_entitlement**
> EmptyClassJson o_bpv2_0_0_delete_entitlement(body, entitlement_id, user_id)

Delete Entitlement

<p>Delete Entitlement specified by ENTITLEMENT_ID for an user specified by USER_ID</p><p>Authentication is required and the user needs to be a Super Admin.<br />Super Admins are listed in the Props file.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
entitlement_id = 'entitlement_id_example' # str | The entitblement id
user_id = 'user_id_example' # str | The user id

try:
    # Delete Entitlement
    api_response = api_instance.o_bpv2_0_0_delete_entitlement(body, entitlement_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv2_0_0_delete_entitlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **entitlement_id** | **str**| The entitblement id | 
 **user_id** | **str**| The user id | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_get_permissions_for_bank_account**
> PermissionsJSON o_bpv2_0_0_get_permissions_for_bank_account(body, account_id, bank_id)

Get access

<p>Returns the list of the permissions at BANK_ID for account ACCOUNT_ID, with each time a pair composed of the user and the views that he has access to.</p><p>Authentication is Mandatory<br />and the user needs to have access to the owner view.</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get access
    api_response = api_instance.o_bpv2_0_0_get_permissions_for_bank_account(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv2_0_0_get_permissions_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**PermissionsJSON**](PermissionsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_1_0_get_entitlements_by_bank_and_user**
> EntitlementJSONs o_bpv2_1_0_get_entitlements_by_bank_and_user(body, user_id, bank_id)

Get Entitlements for User at Bank

<p>Get Entitlements specified by BANK_ID and USER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
user_id = 'user_id_example' # str | The user id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Entitlements for User at Bank
    api_response = api_instance.o_bpv2_1_0_get_entitlements_by_bank_and_user(body, user_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv2_1_0_get_entitlements_by_bank_and_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **user_id** | **str**| The user id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**EntitlementJSONs**](EntitlementJSONs.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_add_entitlement_request**
> EntitlementRequestJSON o_bpv3_0_0_add_entitlement_request(body)

Create Entitlement Request for current User

<p>Create Entitlement Request.</p><p>Any logged in User can use this endpoint to request an Entitlement</p><p>Entitlements are used to grant System or Bank level roles to Users. (For Account level privileges, see Views)</p><p>For a System level Role (.e.g CanGetAnyUser), set bank_id to an empty string i.e. &quot;bank_id&quot;:&quot;&quot;</p><p>For a Bank level Role (e.g. CanCreateAccount), set bank_id to a valid value e.g. &quot;bank_id&quot;:&quot;my-bank-id&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.CreateEntitlementJSON() # CreateEntitlementJSON | CreateEntitlementJSON object that needs to be added.

try:
    # Create Entitlement Request for current User
    api_response = api_instance.o_bpv3_0_0_add_entitlement_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_add_entitlement_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEntitlementJSON**](CreateEntitlementJSON.md)| CreateEntitlementJSON object that needs to be added. | 

### Return type

[**EntitlementRequestJSON**](EntitlementRequestJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_delete_entitlement_request**
> o_bpv3_0_0_delete_entitlement_request(entitlement_request_id)

Delete Entitlement Request

<p>Delete the Entitlement Request specified by ENTITLEMENT_REQUEST_ID for a user specified by USER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
entitlement_request_id = 'entitlement_request_id_example' # str | the entitlement request id

try:
    # Delete Entitlement Request
    api_instance.o_bpv3_0_0_delete_entitlement_request(entitlement_request_id)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_delete_entitlement_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlement_request_id** | **str**| the entitlement request id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_all_entitlement_requests**
> EntitlementRequestsJSON o_bpv3_0_0_get_all_entitlement_requests()

Get all Entitlement Requests

<p>Get all Entitlement Requests</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get all Entitlement Requests
    api_response = api_instance.o_bpv3_0_0_get_all_entitlement_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_all_entitlement_requests: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EntitlementRequestsJSON**](EntitlementRequestsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_current_user**
> UserJsonV200 o_bpv3_0_0_get_current_user()

Get User (Current)

<p>Get the logged in user</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get User (Current)
    api_response = api_instance.o_bpv3_0_0_get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserJsonV200**](UserJsonV200.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_customers_for_user**
> CustomersWithAttributesJsonV300 o_bpv3_0_0_get_customers_for_user()

Get Customers for Current User

<p>Gets all Customers that are linked to a User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Customers for Current User
    api_response = api_instance.o_bpv3_0_0_get_customers_for_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_customers_for_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomersWithAttributesJsonV300**](CustomersWithAttributesJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_entitlement_requests**
> EntitlementRequestsJSON o_bpv3_0_0_get_entitlement_requests(user_id)

Get Entitlement Requests for a User

<p>Get Entitlement Requests for a User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Get Entitlement Requests for a User
    api_response = api_instance.o_bpv3_0_0_get_entitlement_requests(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_entitlement_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**EntitlementRequestsJSON**](EntitlementRequestsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_entitlement_requests_for_current_user**
> EntitlementRequestsJSON o_bpv3_0_0_get_entitlement_requests_for_current_user()

Get Entitlement Requests for the current User

<p>Get Entitlement Requests for the current User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Entitlement Requests for the current User
    api_response = api_instance.o_bpv3_0_0_get_entitlement_requests_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_entitlement_requests_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EntitlementRequestsJSON**](EntitlementRequestsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_entitlements_for_current_user**
> EntitlementJSONs o_bpv3_0_0_get_entitlements_for_current_user()

Get Entitlements for the current User

<p>Get Entitlements for the current User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Entitlements for the current User
    api_response = api_instance.o_bpv3_0_0_get_entitlements_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_entitlements_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EntitlementJSONs**](EntitlementJSONs.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_permission_for_user_for_bank_account**
> ViewsJsonV300 o_bpv3_0_0_get_permission_for_user_for_bank_account(provider, provider_id, account_id, bank_id)

Get Account access for User

<p>Returns the list of the views at BANK_ID for account ACCOUNT_ID that a user identified by PROVIDER_ID at their provider PROVIDER has access to.<br />All url parameters must be <a href=\"http://en.wikipedia.org/wiki/Percent-encoding\">%-encoded</a>, which is often especially relevant for USER_ID and PROVIDER.</p><p>Authentication is Mandatory</p><p>The user needs to have access to the owner view.</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
provider = 'provider_example' # str | the user PROVIDER
provider_id = 'provider_id_example' # str | The provider id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account access for User
    api_response = api_instance.o_bpv3_0_0_get_permission_for_user_for_bank_account(provider, provider_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_0_0_get_permission_for_user_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| the user PROVIDER | 
 **provider_id** | **str**| The provider id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ViewsJsonV300**](ViewsJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_user_auth_context_by_id**
> o_bpv3_1_0_delete_user_auth_context_by_id(user_auth_context_id, user_id)

Delete User Auth Context

<p>Delete a User AuthContext of the User specified by USER_AUTH_CONTEXT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_auth_context_id = 'user_auth_context_id_example' # str | the user auth context id
user_id = 'user_id_example' # str | The user id

try:
    # Delete User Auth Context
    api_instance.o_bpv3_1_0_delete_user_auth_context_by_id(user_auth_context_id, user_id)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_1_0_delete_user_auth_context_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_auth_context_id** | **str**| the user auth context id | 
 **user_id** | **str**| The user id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_user_auth_contexts**
> o_bpv3_1_0_delete_user_auth_contexts(user_id)

Delete User's Auth Contexts

<p>Delete the Auth Contexts of a User specified by USER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Delete User's Auth Contexts
    api_instance.o_bpv3_1_0_delete_user_auth_contexts(user_id)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_1_0_delete_user_auth_contexts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_bad_login_status**
> BadLoginStatusJson o_bpv3_1_0_get_bad_login_status(username)

Get User Lock Status

<p>Get User Login Status.<br />Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
username = 'username_example' # str | the user name

try:
    # Get User Lock Status
    api_response = api_instance.o_bpv3_1_0_get_bad_login_status(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_1_0_get_bad_login_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the user name | 

### Return type

[**BadLoginStatusJson**](BadLoginStatusJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_refresh_user**
> RefreshUserJson o_bpv3_1_0_refresh_user(user_id)

Refresh User

<p>The endpoint is used for updating the accounts, views, account holders for the user.<br />As to the Json body, you can leave it as Empty.<br />This call will get data from backend, no need to prepare the json body in api side.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Refresh User
    api_response = api_instance.o_bpv3_1_0_refresh_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_1_0_refresh_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**RefreshUserJson**](RefreshUserJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_unlock_user**
> BadLoginStatusJson o_bpv3_1_0_unlock_user(username)

Unlock the user

<p>Unlock a User.</p><p>(Perhaps the user was locked due to multiple failed login attempts)</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
username = 'username_example' # str | the user name

try:
    # Unlock the user
    api_response = api_instance.o_bpv3_1_0_unlock_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv3_1_0_unlock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the user name | 

### Return type

[**BadLoginStatusJson**](BadLoginStatusJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_current_user_attribute**
> UserAttributeResponseJsonV400 o_bpv4_0_0_create_current_user_attribute(body)

Create User Attribute for current user

<p>Create User Attribute for current user</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.UserAttributeJsonV400() # UserAttributeJsonV400 | UserAttributeJsonV400 object that needs to be added.

try:
    # Create User Attribute for current user
    api_response = api_instance.o_bpv4_0_0_create_current_user_attribute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_create_current_user_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAttributeJsonV400**](UserAttributeJsonV400.md)| UserAttributeJsonV400 object that needs to be added. | 

### Return type

[**UserAttributeResponseJsonV400**](UserAttributeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_user_customer_links**
> UserCustomerLinkJson o_bpv4_0_0_create_user_customer_links(body, bank_id)

Create User Customer Link

<p>Link a User to a Customer</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.CreateUserCustomerLinkJson() # CreateUserCustomerLinkJson | CreateUserCustomerLinkJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create User Customer Link
    api_response = api_instance.o_bpv4_0_0_create_user_customer_links(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_create_user_customer_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserCustomerLinkJson**](CreateUserCustomerLinkJson.md)| CreateUserCustomerLinkJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserCustomerLinkJson**](UserCustomerLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_user_with_account_access**
> Coloncolon o_bpv4_0_0_create_user_with_account_access(body, account_id, bank_id)

Create (DAuth) User with Account Access

<p>This endpoint is used as part of the DAuth solution to grant access to account and transaction data to a smart contract on the blockchain.</p><p>Put the smart contract address in username</p><p>For provider use &quot;dauth&quot;</p><p>This endpoint will create the (DAuth) User with username and provider if the User does not already exist.</p><p>Authentication is Mandatory and the logged in user needs to be account holder.</p><p>For information about DAuth see below:</p><details>  <summary style=\"display:list-item;cursor:s-resize;\">DAuth</summary>  <h3><a href=\"#dauth-introduction-setup-and-usage\" id=\"dauth-introduction-setup-and-usage\">DAuth Introduction, Setup and Usage</a></h3><p>DAuth is an experimental authentication mechanism that aims to pin an ethereum or other blockchain Smart Contract to an OBP &quot;User&quot;.</p><p>In the future, it might be possible to be more specific and pin specific actors (wallets) that are acting within the smart contract, but so far, one smart contract acts on behalf of one User.</p><p>Thus, if a smart contract &quot;X&quot; calls the OBP API using the DAuth header, OBP will get or create a user called X and the call will proceed in the context of that User &quot;X&quot;.</p><p>DAuth is invoked by the REST client (caller) including a specific header (see step 3 below) in any OBP REST call.</p><p>When OBP receives the DAuth token, it creates or gets a User with a username based on the smart_contract_address and the provider based on the network_name. The combination of username and provider is unique in OBP.</p><p>If you are calling OBP-API via an API3 Airnode, the Airnode will take care of constructing the required header.</p><p>When OBP detects a DAuth header / token it first checks if the Consumer is allowed to make such a call. OBP will validate the Consumer ip address and signature etc.</p><p>Note: The DAuth flow does <em>not</em> require an explicit POST like Direct Login to create the token.</p><p>Permissions may be assigned to an OBP User at any time, via the UserAuthContext, Views, Entitlements to Roles or Consents.</p><p>Note: <em>DAuth is NOT enabled on this instance!</em></p><p>Note: <em>The DAuth client is responsible for creating a token which will be trusted by OBP absolutely</em>!</p><p>To use DAuth:</p><h3><a href=\"#1-configure-obp-api-to-accept-dauth\" id=\"1-configure-obp-api-to-accept-dauth\">1) Configure OBP API to accept DAuth.</a></h3><p>Set up properties in your props file</p><pre><code># -- DAuth --------------------------------------# Define secret used to validate JWT token# jwt.public_key_rsa=path-to-the-pem-file# Enable/Disable DAuth communication at all# In case isn't defined default value is false# allow_dauth=false# Define comma separated list of allowed IP addresses# dauth.host=127.0.0.1# -------------------------------------- DAuth--</code></pre><p>Please keep in mind that property jwt.public_key_rsa is used to validate JWT token to check it is not changed or corrupted during transport.</p><h3><a href=\"#2-create-have-access-to-a-jwt\" id=\"2-create-have-access-to-a-jwt\">2) Create / have access to a JWT</a></h3><p>The following videos are available:<br />* <a href=\"https://vimeo.com/644315074\">DAuth in local environment</a></p><p>HEADER:ALGORITHM &amp; TOKEN TYPE</p><pre><code>{  &quot;alg&quot;: &quot;RS256&quot;,  &quot;typ&quot;: &quot;JWT&quot;}</code></pre><p>PAYLOAD:DATA</p><pre><code>{  &quot;smart_contract_address&quot;: &quot;0xe123425E7734CE288F8367e1Bb143E90bb3F051224&quot;,  &quot;network_name&quot;: &quot;AIRNODE.TESTNET.ETHEREUM&quot;,  &quot;msg_sender&quot;: &quot;0xe12340927f1725E7734CE288F8367e1Bb143E90fhku767&quot;,  &quot;consumer_key&quot;: &quot;0x1234a4ec31e89cea54d1f125db7536e874ab4a96b4d4f6438668b6bb10a6adb&quot;,  &quot;timestamp&quot;: &quot;2021-11-04T14:13:40Z&quot;,  &quot;request_id&quot;: &quot;0Xe876987694328763492876348928736497869273649&quot;}</code></pre><p>VERIFY SIGNATURE</p><pre><code>RSASHA256(  base64UrlEncode(header) + &quot;.&quot; +  base64UrlEncode(payload),<p>) your-RSA-key-pair</p></code></pre><p>Here is an example token:</p><pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbWFydF9jb250cmFjdF9hZGRyZXNzIjoiMHhlMTIzNDI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGJiM0YwNTEyMjQiLCJuZXR3b3JrX25hbWUiOiJFVEhFUkVVTSIsIm1zZ19zZW5kZXIiOiIweGUxMjM0MDkyN2YxNzI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGZoa3U3NjciLCJjb25zdW1lcl9rZXkiOiIweDEyMzRhNGVjMzFlODljZWE1NGQxZjEyNWRiNzUzNmU4NzRhYjRhOTZiNGQ0ZjY0Mzg2NjhiNmJiMTBhNmFkYiIsInRpbWVzdGFtcCI6IjIwMjEtMTEtMDRUMTQ6MTM6NDBaIiwicmVxdWVzdF9pZCI6IjBYZTg3Njk4NzY5NDMyODc2MzQ5Mjg3NjM0ODkyODczNjQ5Nzg2OTI3MzY0OSJ9.XSiQxjEVyCouf7zT8MubEKsbOBZuReGVhnt9uck6z6k</code></pre><h3><a href=\"#3-try-a-rest-call-using-the-header\" id=\"3-try-a-rest-call-using-the-header\">3) Try a REST call using the header</a></h3><p>Using your favorite http client:</p><p>GET <a href=\"https://test.openbankproject.com/obp/v3.0.0/users/current\">https://test.openbankproject.com/obp/v3.0.0/users/current</a></p><p>Body</p><p>Leave Empty!</p><p>Headers:</p><pre><code>   DAuth: your-jwt-from-step-above</code></pre><p>Here is it all together:</p><p>GET <a href=\"https://test.openbankproject.com/obp/v3.0.0/users/current\">https://test.openbankproject.com/obp/v3.0.0/users/current</a> HTTP/1.1<br />Host: localhost:8080<br />User-Agent: curl/7.47.0<br />Accept: <em>/</em><br />DAuth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbWFydF9jb250cmFjdF9hZGRyZXNzIjoiMHhlMTIzNDI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGJiM0YwNTEyMjQiLCJuZXR3b3JrX25hbWUiOiJFVEhFUkVVTSIsIm1zZ19zZW5kZXIiOiIweGUxMjM0MDkyN2YxNzI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGZoa3U3NjciLCJjb25zdW1lcl9rZXkiOiIweDEyMzRhNGVjMzFlODljZWE1NGQxZjEyNWRiNzUzNmU4NzRhYjRhOTZiNGQ0ZjY0Mzg2NjhiNmJiMTBhNmFkYiIsInRpbWVzdGFtcCI6IjIwMjEtMTEtMDRUMTQ6MTM6NDBaIiwicmVxdWVzdF9pZCI6IjBYZTg3Njk4NzY5NDMyODc2MzQ5Mjg3NjM0ODkyODczNjQ5Nzg2OTI3MzY0OSJ9.XSiQxjEVyCouf7zT8MubEKsbOBZuReGVhnt9uck6z6k</p><p>CURL example</p><pre><code>curl -v -H 'DAuth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbWFydF9jb250cmFjdF9hZGRyZXNzIjoiMHhlMTIzNDI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGJiM0YwNTEyMjQiLCJuZXR3b3JrX25hbWUiOiJFVEhFUkVVTSIsIm1zZ19zZW5kZXIiOiIweGUxMjM0MDkyN2YxNzI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGZoa3U3NjciLCJjb25zdW1lcl9rZXkiOiIweDEyMzRhNGVjMzFlODljZWE1NGQxZjEyNWRiNzUzNmU4NzRhYjRhOTZiNGQ0ZjY0Mzg2NjhiNmJiMTBhNmFkYiIsInRpbWVzdGFtcCI6IjIwMjEtMTEtMDRUMTQ6MTM6NDBaIiwicmVxdWVzdF9pZCI6IjBYZTg3Njk4NzY5NDMyODc2MzQ5Mjg3NjM0ODkyODczNjQ5Nzg2OTI3MzY0OSJ9.XSiQxjEVyCouf7zT8MubEKsbOBZuReGVhnt9uck6z6k' https://test.openbankproject.com/obp/v3.0.0/users/current</code></pre><p>You should receive a response like:</p><pre><code>{    &quot;user_id&quot;: &quot;4c4d3175-1e5c-4cfd-9b08-dcdc209d8221&quot;,    &quot;email&quot;: &quot;&quot;,    &quot;provider_id&quot;: &quot;0xe123425E7734CE288F8367e1Bb143E90bb3F051224&quot;,    &quot;provider&quot;: &quot;ETHEREUM&quot;,    &quot;username&quot;: &quot;0xe123425E7734CE288F8367e1Bb143E90bb3F051224&quot;,    &quot;entitlements&quot;: {        &quot;list&quot;: []    }}</code></pre><h3><a href=\"#under-the-hood\" id=\"under-the-hood\">Under the hood</a></h3><p>The file, dauth.scala handles the DAuth,</p><p>We:</p><pre><code>-&gt; Check if Props allow_dauth is true  -&gt; Check if DAuth header exists    -&gt; Check if getRemoteIpAddress is OK      -&gt; Look for &quot;token&quot;        -&gt; parse the JWT token and getOrCreate the user          -&gt; get the data of the user</code></pre><h3><a href=\"#more-information\" id=\"more-information\">More information</a></h3><p>Parameter names and values are case sensitive.<br />Each parameter MUST NOT appear more than once per request.</p></details><br></br>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostCreateUserAccountAccessJsonV400() # PostCreateUserAccountAccessJsonV400 | PostCreateUserAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create (DAuth) User with Account Access
    api_response = api_instance.o_bpv4_0_0_create_user_with_account_access(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_create_user_with_account_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCreateUserAccountAccessJsonV400**](PostCreateUserAccountAccessJsonV400.md)| PostCreateUserAccountAccessJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**Coloncolon**](Coloncolon.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_user_with_roles**
> EntitlementsJsonV400 o_bpv4_0_0_create_user_with_roles(body)

Create (DAuth) User with Roles

<p>This endpoint is used as part of the DAuth solution to grant Entitlements for Roles to a smart contract on the blockchain.</p><p>Put the smart contract address in username</p><p>For provider use &quot;dauth&quot;</p><p>This endpoint will create the User with username and provider if the User does not already exist.</p><p>Then it will create Entitlements i.e. grant Roles to the User.</p><p>Entitlements are used to grant System or Bank level roles to Users. (For Account level privileges, see Views)</p><p>i.e. Entitlements are used to create / consume system or bank level resources where as views / account access are used to consume / create customer level resources.</p><p>For a System level Role (.e.g CanGetAnyUser), set bank_id to an empty string i.e. &quot;bank_id&quot;:&quot;&quot;</p><p>For a Bank level Role (e.g. CanCreateAccount), set bank_id to a valid value e.g. &quot;bank_id&quot;:&quot;my-bank-id&quot;</p><p>Note: The Roles actually granted will depend on the Roles that the calling user has.</p><p>If you try to grant Entitlements to a user that already exist (duplicate entitilements) you will get an error.</p><p>For information about DAuth see below:</p><details>  <summary style=\"display:list-item;cursor:s-resize;\">DAuth</summary>  <h3><a href=\"#dauth-introduction-setup-and-usage\" id=\"dauth-introduction-setup-and-usage\">DAuth Introduction, Setup and Usage</a></h3><p>DAuth is an experimental authentication mechanism that aims to pin an ethereum or other blockchain Smart Contract to an OBP &quot;User&quot;.</p><p>In the future, it might be possible to be more specific and pin specific actors (wallets) that are acting within the smart contract, but so far, one smart contract acts on behalf of one User.</p><p>Thus, if a smart contract &quot;X&quot; calls the OBP API using the DAuth header, OBP will get or create a user called X and the call will proceed in the context of that User &quot;X&quot;.</p><p>DAuth is invoked by the REST client (caller) including a specific header (see step 3 below) in any OBP REST call.</p><p>When OBP receives the DAuth token, it creates or gets a User with a username based on the smart_contract_address and the provider based on the network_name. The combination of username and provider is unique in OBP.</p><p>If you are calling OBP-API via an API3 Airnode, the Airnode will take care of constructing the required header.</p><p>When OBP detects a DAuth header / token it first checks if the Consumer is allowed to make such a call. OBP will validate the Consumer ip address and signature etc.</p><p>Note: The DAuth flow does <em>not</em> require an explicit POST like Direct Login to create the token.</p><p>Permissions may be assigned to an OBP User at any time, via the UserAuthContext, Views, Entitlements to Roles or Consents.</p><p>Note: <em>DAuth is NOT enabled on this instance!</em></p><p>Note: <em>The DAuth client is responsible for creating a token which will be trusted by OBP absolutely</em>!</p><p>To use DAuth:</p><h3><a href=\"#1-configure-obp-api-to-accept-dauth\" id=\"1-configure-obp-api-to-accept-dauth\">1) Configure OBP API to accept DAuth.</a></h3><p>Set up properties in your props file</p><pre><code># -- DAuth --------------------------------------# Define secret used to validate JWT token# jwt.public_key_rsa=path-to-the-pem-file# Enable/Disable DAuth communication at all# In case isn't defined default value is false# allow_dauth=false# Define comma separated list of allowed IP addresses# dauth.host=127.0.0.1# -------------------------------------- DAuth--</code></pre><p>Please keep in mind that property jwt.public_key_rsa is used to validate JWT token to check it is not changed or corrupted during transport.</p><h3><a href=\"#2-create-have-access-to-a-jwt\" id=\"2-create-have-access-to-a-jwt\">2) Create / have access to a JWT</a></h3><p>The following videos are available:<br />* <a href=\"https://vimeo.com/644315074\">DAuth in local environment</a></p><p>HEADER:ALGORITHM &amp; TOKEN TYPE</p><pre><code>{  &quot;alg&quot;: &quot;RS256&quot;,  &quot;typ&quot;: &quot;JWT&quot;}</code></pre><p>PAYLOAD:DATA</p><pre><code>{  &quot;smart_contract_address&quot;: &quot;0xe123425E7734CE288F8367e1Bb143E90bb3F051224&quot;,  &quot;network_name&quot;: &quot;AIRNODE.TESTNET.ETHEREUM&quot;,  &quot;msg_sender&quot;: &quot;0xe12340927f1725E7734CE288F8367e1Bb143E90fhku767&quot;,  &quot;consumer_key&quot;: &quot;0x1234a4ec31e89cea54d1f125db7536e874ab4a96b4d4f6438668b6bb10a6adb&quot;,  &quot;timestamp&quot;: &quot;2021-11-04T14:13:40Z&quot;,  &quot;request_id&quot;: &quot;0Xe876987694328763492876348928736497869273649&quot;}</code></pre><p>VERIFY SIGNATURE</p><pre><code>RSASHA256(  base64UrlEncode(header) + &quot;.&quot; +  base64UrlEncode(payload),<p>) your-RSA-key-pair</p></code></pre><p>Here is an example token:</p><pre><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbWFydF9jb250cmFjdF9hZGRyZXNzIjoiMHhlMTIzNDI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGJiM0YwNTEyMjQiLCJuZXR3b3JrX25hbWUiOiJFVEhFUkVVTSIsIm1zZ19zZW5kZXIiOiIweGUxMjM0MDkyN2YxNzI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGZoa3U3NjciLCJjb25zdW1lcl9rZXkiOiIweDEyMzRhNGVjMzFlODljZWE1NGQxZjEyNWRiNzUzNmU4NzRhYjRhOTZiNGQ0ZjY0Mzg2NjhiNmJiMTBhNmFkYiIsInRpbWVzdGFtcCI6IjIwMjEtMTEtMDRUMTQ6MTM6NDBaIiwicmVxdWVzdF9pZCI6IjBYZTg3Njk4NzY5NDMyODc2MzQ5Mjg3NjM0ODkyODczNjQ5Nzg2OTI3MzY0OSJ9.XSiQxjEVyCouf7zT8MubEKsbOBZuReGVhnt9uck6z6k</code></pre><h3><a href=\"#3-try-a-rest-call-using-the-header\" id=\"3-try-a-rest-call-using-the-header\">3) Try a REST call using the header</a></h3><p>Using your favorite http client:</p><p>GET <a href=\"https://test.openbankproject.com/obp/v3.0.0/users/current\">https://test.openbankproject.com/obp/v3.0.0/users/current</a></p><p>Body</p><p>Leave Empty!</p><p>Headers:</p><pre><code>   DAuth: your-jwt-from-step-above</code></pre><p>Here is it all together:</p><p>GET <a href=\"https://test.openbankproject.com/obp/v3.0.0/users/current\">https://test.openbankproject.com/obp/v3.0.0/users/current</a> HTTP/1.1<br />Host: localhost:8080<br />User-Agent: curl/7.47.0<br />Accept: <em>/</em><br />DAuth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbWFydF9jb250cmFjdF9hZGRyZXNzIjoiMHhlMTIzNDI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGJiM0YwNTEyMjQiLCJuZXR3b3JrX25hbWUiOiJFVEhFUkVVTSIsIm1zZ19zZW5kZXIiOiIweGUxMjM0MDkyN2YxNzI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGZoa3U3NjciLCJjb25zdW1lcl9rZXkiOiIweDEyMzRhNGVjMzFlODljZWE1NGQxZjEyNWRiNzUzNmU4NzRhYjRhOTZiNGQ0ZjY0Mzg2NjhiNmJiMTBhNmFkYiIsInRpbWVzdGFtcCI6IjIwMjEtMTEtMDRUMTQ6MTM6NDBaIiwicmVxdWVzdF9pZCI6IjBYZTg3Njk4NzY5NDMyODc2MzQ5Mjg3NjM0ODkyODczNjQ5Nzg2OTI3MzY0OSJ9.XSiQxjEVyCouf7zT8MubEKsbOBZuReGVhnt9uck6z6k</p><p>CURL example</p><pre><code>curl -v -H 'DAuth: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzbWFydF9jb250cmFjdF9hZGRyZXNzIjoiMHhlMTIzNDI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGJiM0YwNTEyMjQiLCJuZXR3b3JrX25hbWUiOiJFVEhFUkVVTSIsIm1zZ19zZW5kZXIiOiIweGUxMjM0MDkyN2YxNzI1RTc3MzRDRTI4OEY4MzY3ZTFCYjE0M0U5MGZoa3U3NjciLCJjb25zdW1lcl9rZXkiOiIweDEyMzRhNGVjMzFlODljZWE1NGQxZjEyNWRiNzUzNmU4NzRhYjRhOTZiNGQ0ZjY0Mzg2NjhiNmJiMTBhNmFkYiIsInRpbWVzdGFtcCI6IjIwMjEtMTEtMDRUMTQ6MTM6NDBaIiwicmVxdWVzdF9pZCI6IjBYZTg3Njk4NzY5NDMyODc2MzQ5Mjg3NjM0ODkyODczNjQ5Nzg2OTI3MzY0OSJ9.XSiQxjEVyCouf7zT8MubEKsbOBZuReGVhnt9uck6z6k' https://test.openbankproject.com/obp/v3.0.0/users/current</code></pre><p>You should receive a response like:</p><pre><code>{    &quot;user_id&quot;: &quot;4c4d3175-1e5c-4cfd-9b08-dcdc209d8221&quot;,    &quot;email&quot;: &quot;&quot;,    &quot;provider_id&quot;: &quot;0xe123425E7734CE288F8367e1Bb143E90bb3F051224&quot;,    &quot;provider&quot;: &quot;ETHEREUM&quot;,    &quot;username&quot;: &quot;0xe123425E7734CE288F8367e1Bb143E90bb3F051224&quot;,    &quot;entitlements&quot;: {        &quot;list&quot;: []    }}</code></pre><h3><a href=\"#under-the-hood\" id=\"under-the-hood\">Under the hood</a></h3><p>The file, dauth.scala handles the DAuth,</p><p>We:</p><pre><code>-&gt; Check if Props allow_dauth is true  -&gt; Check if DAuth header exists    -&gt; Check if getRemoteIpAddress is OK      -&gt; Look for &quot;token&quot;        -&gt; parse the JWT token and getOrCreate the user          -&gt; get the data of the user</code></pre><h3><a href=\"#more-information\" id=\"more-information\">More information</a></h3><p>Parameter names and values are case sensitive.<br />Each parameter MUST NOT appear more than once per request.</p></details><br></br><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostCreateUserWithRolesJsonV400() # PostCreateUserWithRolesJsonV400 | PostCreateUserWithRolesJsonV400 object that needs to be added.

try:
    # Create (DAuth) User with Roles
    api_response = api_instance.o_bpv4_0_0_create_user_with_roles(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_create_user_with_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCreateUserWithRolesJsonV400**](PostCreateUserWithRolesJsonV400.md)| PostCreateUserWithRolesJsonV400 object that needs to be added. | 

### Return type

[**EntitlementsJsonV400**](EntitlementsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_user**
> o_bpv4_0_0_delete_user(user_id)

Delete a User

<p>Delete a User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Delete a User
    api_instance.o_bpv4_0_0_delete_user(user_id)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_current_user_attributes**
> UserAttributesResponseJson o_bpv4_0_0_get_current_user_attributes()

Get User Attributes for current user

<p>Get User Attributes for current user.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get User Attributes for current user
    api_response = api_instance.o_bpv4_0_0_get_current_user_attributes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_current_user_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAttributesResponseJson**](UserAttributesResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_current_user_id**
> UserIdJsonV400 o_bpv4_0_0_get_current_user_id()

Get User Id (Current)

<p>Get the USER_ID of the logged in user</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get User Id (Current)
    api_response = api_instance.o_bpv4_0_0_get_current_user_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_current_user_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserIdJsonV400**](UserIdJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customers_at_any_bank**
> CustomerJSONsV300 o_bpv4_0_0_get_customers_at_any_bank()

Get Customers at Any Bank

<p>Get Customers at Any Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Customers at Any Bank
    api_response = api_instance.o_bpv4_0_0_get_customers_at_any_bank()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_customers_at_any_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerJSONsV300**](CustomerJSONsV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customers_minimal_at_any_bank**
> CustomersMinimalJsonV400 o_bpv4_0_0_get_customers_minimal_at_any_bank()

Get Customers Minimal at Any Bank

<p>Get Customers Minimal at Any Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Customers Minimal at Any Bank
    api_response = api_instance.o_bpv4_0_0_get_customers_minimal_at_any_bank()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_customers_minimal_at_any_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomersMinimalJsonV400**](CustomersMinimalJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_entitlements**
> EntitlementsJsonV400 o_bpv4_0_0_get_entitlements(user_id)

Get Entitlements for User

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Get Entitlements for User
    api_response = api_instance.o_bpv4_0_0_get_entitlements(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_entitlements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**EntitlementsJsonV400**](EntitlementsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_entitlements_for_bank**
> EntitlementsJsonV400 o_bpv4_0_0_get_entitlements_for_bank(bank_id)

Get Entitlements for One Bank

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Entitlements for One Bank
    api_response = api_instance.o_bpv4_0_0_get_entitlements_for_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_entitlements_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**EntitlementsJsonV400**](EntitlementsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_logout_link**
> LogoutLinkJson o_bpv4_0_0_get_logout_link()

Get Logout Link

<p>Get the Logout Link</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Logout Link
    api_response = api_instance.o_bpv4_0_0_get_logout_link()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_logout_link: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogoutLinkJson**](LogoutLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_spaces**
> MySpaces o_bpv4_0_0_get_my_spaces()

Get My Spaces

<p>Get My Spaces.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get My Spaces
    api_response = api_instance.o_bpv4_0_0_get_my_spaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_my_spaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MySpaces**](MySpaces.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_by_user_id**
> UserJsonV400 o_bpv4_0_0_get_user_by_user_id(user_id)

Get User by USER_ID

<p>Get user by USER_ID</p><p>Authentication is Mandatory<br />CanGetAnyUser entitlement is required,</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Get User by USER_ID
    api_response = api_instance.o_bpv4_0_0_get_user_by_user_id(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_user_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**UserJsonV400**](UserJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_by_username**
> UserJsonV400 o_bpv4_0_0_get_user_by_username(username)

Get User by USERNAME

<p>Get user by USERNAME</p><p>Authentication is Mandatory</p><p>CanGetAnyUser entitlement is required,</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
username = 'username_example' # str | the user name

try:
    # Get User by USERNAME
    api_response = api_instance.o_bpv4_0_0_get_user_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_user_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the user name | 

### Return type

[**UserJsonV400**](UserJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_with_attributes**
> UserWithAttributesResponseJson o_bpv4_0_0_get_user_with_attributes(user_id)

Get User Attributes for the user

<p>Get User Attributes for the user defined via USER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Get User Attributes for the user
    api_response = api_instance.o_bpv4_0_0_get_user_with_attributes(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_user_with_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**UserWithAttributesResponseJson**](UserWithAttributesResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_users**
> UsersJsonV400 o_bpv4_0_0_get_users()

Get all Users

<p>Get all users</p><p>Authentication is Mandatory</p><p>CanGetAnyUser entitlement is required,</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>locked_status (if null ignore)</li></ul>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get all Users
    api_response = api_instance.o_bpv4_0_0_get_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UsersJsonV400**](UsersJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_users_by_email**
> UsersJsonV400 o_bpv4_0_0_get_users_by_email()

Get Users by Email Address

<p>Get users by email address</p><p>Authentication is Mandatory<br />CanGetAnyUser entitlement is required,</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get Users by Email Address
    api_response = api_instance.o_bpv4_0_0_get_users_by_email()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_get_users_by_email: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UsersJsonV400**](UsersJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_grant_user_access_to_view**
> ViewJsonV300 o_bpv4_0_0_grant_user_access_to_view(body, account_id, bank_id)

Grant User access to View

<p>Grants the User identified by USER_ID access to the view identified by VIEW_ID.</p><p>Authentication is Mandatory and the user needs to be account holder.</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostAccountAccessJsonV400() # PostAccountAccessJsonV400 | PostAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Grant User access to View
    api_response = api_instance.o_bpv4_0_0_grant_user_access_to_view(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_grant_user_access_to_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountAccessJsonV400**](PostAccountAccessJsonV400.md)| PostAccountAccessJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ViewJsonV300**](ViewJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_lock_user**
> UserLockStatusJson o_bpv4_0_0_lock_user(username)

Lock the user

<p>Lock a User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
username = 'username_example' # str | the user name

try:
    # Lock the user
    api_response = api_instance.o_bpv4_0_0_lock_user(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_lock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| the user name | 

### Return type

[**UserLockStatusJson**](UserLockStatusJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_reset_password_url**
> ResetPasswordUrlJsonV400 o_bpv4_0_0_reset_password_url(body)

Create password reset url

<p>Create password reset url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostResetPasswordUrlJsonV400() # PostResetPasswordUrlJsonV400 | PostResetPasswordUrlJsonV400 object that needs to be added.

try:
    # Create password reset url
    api_response = api_instance.o_bpv4_0_0_reset_password_url(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_reset_password_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostResetPasswordUrlJsonV400**](PostResetPasswordUrlJsonV400.md)| PostResetPasswordUrlJsonV400 object that needs to be added. | 

### Return type

[**ResetPasswordUrlJsonV400**](ResetPasswordUrlJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_revoke_grant_user_access_to_views**
> RevokedJsonV400 o_bpv4_0_0_revoke_grant_user_access_to_views(body, account_id, bank_id)

Revoke/Grant User access to View

<p>Revoke/Grant the logged in User access to the views identified by json.</p><p>Authentication is Mandatory and the user needs to be an account holder or has owner view access.</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostRevokeGrantAccountAccessJsonV400() # PostRevokeGrantAccountAccessJsonV400 | PostRevokeGrantAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke/Grant User access to View
    api_response = api_instance.o_bpv4_0_0_revoke_grant_user_access_to_views(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_revoke_grant_user_access_to_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostRevokeGrantAccountAccessJsonV400**](PostRevokeGrantAccountAccessJsonV400.md)| PostRevokeGrantAccountAccessJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**RevokedJsonV400**](RevokedJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_revoke_user_access_to_view**
> RevokedJsonV400 o_bpv4_0_0_revoke_user_access_to_view(body, account_id, bank_id)

Revoke User access to View

<p>Revoke the User identified by USER_ID access to the view identified by VIEW_ID.</p><p>Authentication is Mandatory and the user needs to be account holder.</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostAccountAccessJsonV400() # PostAccountAccessJsonV400 | PostAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke User access to View
    api_response = api_instance.o_bpv4_0_0_revoke_user_access_to_view(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_revoke_user_access_to_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountAccessJsonV400**](PostAccountAccessJsonV400.md)| PostAccountAccessJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**RevokedJsonV400**](RevokedJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_current_user_attribute**
> UserAttributeResponseJsonV400 o_bpv4_0_0_update_current_user_attribute(body)

Update User Attribute for current user

<p>Update User Attribute for current user by USER_ATTRIBUTE_ID</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.UserAttributeJsonV400() # UserAttributeJsonV400 | UserAttributeJsonV400 object that needs to be added.

try:
    # Update User Attribute for current user
    api_response = api_instance.o_bpv4_0_0_update_current_user_attribute(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv4_0_0_update_current_user_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserAttributeJsonV400**](UserAttributeJsonV400.md)| UserAttributeJsonV400 object that needs to be added. | 

### Return type

[**UserAttributeResponseJsonV400**](UserAttributeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_answer_user_auth_context_update_challenge**
> UserAuthContextUpdateJsonV500 o_bpv5_0_0_answer_user_auth_context_update_challenge(body, auth_context_update_id, bank_id)

Answer User Auth Context Update Challenge

<p>Answer User Auth Context Update Challenge.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserAuthContextUpdateJsonV310() # PostUserAuthContextUpdateJsonV310 | PostUserAuthContextUpdateJsonV310 object that needs to be added.
auth_context_update_id = 'auth_context_update_id_example' # str | the auth context update id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Answer User Auth Context Update Challenge
    api_response = api_instance.o_bpv5_0_0_answer_user_auth_context_update_challenge(body, auth_context_update_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_answer_user_auth_context_update_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserAuthContextUpdateJsonV310**](PostUserAuthContextUpdateJsonV310.md)| PostUserAuthContextUpdateJsonV310 object that needs to be added. | 
 **auth_context_update_id** | **str**| the auth context update id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserAuthContextUpdateJsonV500**](UserAuthContextUpdateJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_user_auth_context**
> UserAuthContextJsonV500 o_bpv5_0_0_create_user_auth_context(body, user_id)

Create User Auth Context

<p>Create User Auth Context. These key value pairs will be propagated over connector to adapter. Normally used for mapping OBP user and<br />Bank User/Customer.<br />Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserAuthContextJson() # PostUserAuthContextJson | PostUserAuthContextJson object that needs to be added.
user_id = 'user_id_example' # str | The user id

try:
    # Create User Auth Context
    api_response = api_instance.o_bpv5_0_0_create_user_auth_context(body, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_create_user_auth_context: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserAuthContextJson**](PostUserAuthContextJson.md)| PostUserAuthContextJson object that needs to be added. | 
 **user_id** | **str**| The user id | 

### Return type

[**UserAuthContextJsonV500**](UserAuthContextJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_user_auth_context_update_request**
> UserAuthContextUpdateJsonV500 o_bpv5_0_0_create_user_auth_context_update_request(body, sca_method, bank_id)

Create User Auth Context Update Request

<p>Create User Auth Context Update Request.<br />Authentication is Mandatory</p><p>A One Time Password (OTP) (AKA security challenge) is sent Out of Band (OOB) to the User via the transport defined in SCA_METHOD<br />SCA_METHOD is typically &quot;SMS&quot; or &quot;EMAIL&quot;. &quot;EMAIL&quot; is used for testing purposes.</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserAuthContextJson() # PostUserAuthContextJson | PostUserAuthContextJson object that needs to be added.
sca_method = 'sca_method_example' # str | the sca method
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create User Auth Context Update Request
    api_response = api_instance.o_bpv5_0_0_create_user_auth_context_update_request(body, sca_method, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_create_user_auth_context_update_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserAuthContextJson**](PostUserAuthContextJson.md)| PostUserAuthContextJson object that needs to be added. | 
 **sca_method** | **str**| the sca method | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserAuthContextUpdateJsonV500**](UserAuthContextUpdateJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customers_at_one_bank**
> CustomerJSONsV300 o_bpv5_0_0_get_customers_at_one_bank(bank_id)

Get Customers at Bank

<p>Get Customers at Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customers at Bank
    api_response = api_instance.o_bpv5_0_0_get_customers_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_get_customers_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJSONsV300**](CustomerJSONsV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customers_minimal_at_one_bank**
> CustomersMinimalJsonV400 o_bpv5_0_0_get_customers_minimal_at_one_bank(bank_id)

Get Customers Minimal at Bank

<p>Get Customers Minimal at Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customers Minimal at Bank
    api_response = api_instance.o_bpv5_0_0_get_customers_minimal_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_get_customers_minimal_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomersMinimalJsonV400**](CustomersMinimalJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_my_customers_at_any_bank**
> CustomerJsonV210 o_bpv5_0_0_get_my_customers_at_any_bank()

Get My Customers

<p>Gets all Customers that are linked to me.</p><p>Authentication via OAuth is required.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))

try:
    # Get My Customers
    api_response = api_instance.o_bpv5_0_0_get_my_customers_at_any_bank()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_get_my_customers_at_any_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerJsonV210**](CustomerJsonV210.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_user_auth_contexts**
> UserAuthContextJsonV500 o_bpv5_0_0_get_user_auth_contexts(user_id)

Get User Auth Contexts

<p>Get User Auth Contexts for a User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Get User Auth Contexts
    api_response = api_instance.o_bpv5_0_0_get_user_auth_contexts(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->o_bpv5_0_0_get_user_auth_contexts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**UserAuthContextJsonV500**](UserAuthContextJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

