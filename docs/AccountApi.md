# obp_python.AccountApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_2_1_delete_view_for_bank_account**](AccountApi.md#o_bpv1_2_1_delete_view_for_bank_account) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/views/{VIEW_ID} | Delete View
[**o_bpv2_0_0_get_permissions_for_bank_account**](AccountApi.md#o_bpv2_0_0_get_permissions_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/permissions | Get access
[**o_bpv2_0_0_public_accounts_all_banks**](AccountApi.md#o_bpv2_0_0_public_accounts_all_banks) | **GET** /obp/v5.0.0/accounts/public | Get Public Accounts at all Banks
[**o_bpv2_0_0_public_accounts_at_one_bank**](AccountApi.md#o_bpv2_0_0_public_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/public | Get Public Accounts at Bank
[**o_bpv3_0_0_core_private_accounts_all_banks**](AccountApi.md#o_bpv3_0_0_core_private_accounts_all_banks) | **GET** /obp/v5.0.0/my/accounts | Get Accounts at all Banks (private)
[**o_bpv3_0_0_create_view_for_bank_account**](AccountApi.md#o_bpv3_0_0_create_view_for_bank_account) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/views | Create View
[**o_bpv3_0_0_get_accounts_held**](AccountApi.md#o_bpv3_0_0_get_accounts_held) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts-held | Get Accounts Held
[**o_bpv3_0_0_get_core_transactions_for_bank_account**](AccountApi.md#o_bpv3_0_0_get_core_transactions_for_bank_account) | **GET** /obp/v5.0.0/my/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/transactions | Get Transactions for Account (Core)
[**o_bpv3_0_0_get_other_account_by_id_for_bank_account**](AccountApi.md#o_bpv3_0_0_get_other_account_by_id_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID} | Get Other Account by Id
[**o_bpv3_0_0_get_other_accounts_for_bank_account**](AccountApi.md#o_bpv3_0_0_get_other_accounts_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts | Get Other Accounts of one Account
[**o_bpv3_0_0_get_permission_for_user_for_bank_account**](AccountApi.md#o_bpv3_0_0_get_permission_for_user_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/permissions/{PROVIDER}/{PROVIDER_ID} | Get Account access for User
[**o_bpv3_0_0_get_private_account_idsby_bank_id**](AccountApi.md#o_bpv3_0_0_get_private_account_idsby_bank_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/account_ids/private | Get Accounts at Bank (IDs only)
[**o_bpv3_0_0_get_public_account_by_id**](AccountApi.md#o_bpv3_0_0_get_public_account_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/public/accounts/{ACCOUNT_ID}/{VIEW_ID}/account | Get Public Account by Id
[**o_bpv3_0_0_get_transactions_for_bank_account**](AccountApi.md#o_bpv3_0_0_get_transactions_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions | Get Transactions for Account (Full)
[**o_bpv3_0_0_private_accounts_at_one_bank**](AccountApi.md#o_bpv3_0_0_private_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/private | Get Accounts at Bank (Minimal)
[**o_bpv3_0_0_update_view_for_bank_account**](AccountApi.md#o_bpv3_0_0_update_view_for_bank_account) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/views/{VIEW_ID} | Update View
[**o_bpv3_1_0_check_funds_available**](AccountApi.md#o_bpv3_1_0_check_funds_available) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/funds-available | Check Available Funds
[**o_bpv3_1_0_create_account_application**](AccountApi.md#o_bpv3_1_0_create_account_application) | **POST** /obp/v5.0.0/banks/{BANK_ID}/account-applications | Create Account Application
[**o_bpv3_1_0_create_account_attribute**](AccountApi.md#o_bpv3_1_0_create_account_attribute) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/products/{PRODUCT_CODE}/attribute | Create Account Attribute
[**o_bpv3_1_0_get_account_application**](AccountApi.md#o_bpv3_1_0_get_account_application) | **GET** /obp/v5.0.0/banks/{BANK_ID}/account-applications/{ACCOUNT_APPLICATION_ID} | Get Account Application by Id
[**o_bpv3_1_0_get_account_applications**](AccountApi.md#o_bpv3_1_0_get_account_applications) | **GET** /obp/v5.0.0/banks/{BANK_ID}/account-applications | Get Account Applications
[**o_bpv3_1_0_get_checkbook_orders**](AccountApi.md#o_bpv3_1_0_get_checkbook_orders) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/checkbook/orders | Get Checkbook orders
[**o_bpv3_1_0_update_account**](AccountApi.md#o_bpv3_1_0_update_account) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID} | Update Account
[**o_bpv3_1_0_update_account_application_status**](AccountApi.md#o_bpv3_1_0_update_account_application_status) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/account-applications/{ACCOUNT_APPLICATION_ID} | Update Account Application Status
[**o_bpv3_1_0_update_account_attribute**](AccountApi.md#o_bpv3_1_0_update_account_attribute) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/products/{PRODUCT_CODE}/attributes/{ACCOUNT_ATTRIBUTE_ID} | Update Account Attribute
[**o_bpv4_0_0_add_account**](AccountApi.md#o_bpv4_0_0_add_account) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts | Create Account (POST)
[**o_bpv4_0_0_add_tag_for_view_on_account**](AccountApi.md#o_bpv4_0_0_add_tag_for_view_on_account) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/metadata/tags | Create a tag on account
[**o_bpv4_0_0_create_counterparty**](AccountApi.md#o_bpv4_0_0_create_counterparty) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Create Counterparty (Explicit)
[**o_bpv4_0_0_create_counterparty_for_any_account**](AccountApi.md#o_bpv4_0_0_create_counterparty_for_any_account) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Create Counterparty for any account (Explicit)
[**o_bpv4_0_0_create_direct_debit**](AccountApi.md#o_bpv4_0_0_create_direct_debit) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/direct-debit | Create Direct Debit
[**o_bpv4_0_0_create_direct_debit_management**](AccountApi.md#o_bpv4_0_0_create_direct_debit_management) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/direct-debit | Create Direct Debit (management)
[**o_bpv4_0_0_create_or_update_account_attribute_definition**](AccountApi.md#o_bpv4_0_0_create_or_update_account_attribute_definition) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/account | Create or Update Account Attribute Definition
[**o_bpv4_0_0_create_standing_order**](AccountApi.md#o_bpv4_0_0_create_standing_order) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/standing-order | Create Standing Order
[**o_bpv4_0_0_create_standing_order_management**](AccountApi.md#o_bpv4_0_0_create_standing_order_management) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/standing-order | Create Standing Order (management)
[**o_bpv4_0_0_create_user_with_account_access**](AccountApi.md#o_bpv4_0_0_create_user_with_account_access) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/user-account-access | Create (DAuth) User with Account Access
[**o_bpv4_0_0_delete_account_attribute_definition**](AccountApi.md#o_bpv4_0_0_delete_account_attribute_definition) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/ATTRIBUTE_DEFINITION_ID/account | Delete Account Attribute Definition
[**o_bpv4_0_0_delete_account_cascade**](AccountApi.md#o_bpv4_0_0_delete_account_cascade) | **DELETE** /obp/v5.0.0/management/cascading/banks/{BANK_ID}/accounts/{ACCOUNT_ID} | Delete Account Cascade
[**o_bpv4_0_0_delete_counterparty_for_any_account**](AccountApi.md#o_bpv4_0_0_delete_counterparty_for_any_account) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Delete Counterparty for any account (Explicit)
[**o_bpv4_0_0_delete_explicit_counterparty**](AccountApi.md#o_bpv4_0_0_delete_explicit_counterparty) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Delete Counterparty (Explicit)
[**o_bpv4_0_0_delete_tag_for_view_on_account**](AccountApi.md#o_bpv4_0_0_delete_tag_for_view_on_account) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/metadata/tags/{TAG_ID} | Delete a tag on account
[**o_bpv4_0_0_get_account_attribute_definition**](AccountApi.md#o_bpv4_0_0_get_account_attribute_definition) | **GET** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/account | Get Account Attribute Definition
[**o_bpv4_0_0_get_account_by_account_routing**](AccountApi.md#o_bpv4_0_0_get_account_by_account_routing) | **POST** /obp/v5.0.0/management/accounts/account-routing-query | Get Account by Account Routing
[**o_bpv4_0_0_get_accounts_by_account_routing_regex**](AccountApi.md#o_bpv4_0_0_get_accounts_by_account_routing_regex) | **POST** /obp/v5.0.0/management/accounts/account-routing-regex-query | Get Accounts by Account Routing Regex
[**o_bpv4_0_0_get_accounts_minimal_by_customer_id**](AccountApi.md#o_bpv4_0_0_get_accounts_minimal_by_customer_id) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/accounts-minimal | Get Accounts Minimal for a Customer
[**o_bpv4_0_0_get_bank_account_balances**](AccountApi.md#o_bpv4_0_0_get_bank_account_balances) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/balances | Get Account Balances
[**o_bpv4_0_0_get_bank_accounts_balances**](AccountApi.md#o_bpv4_0_0_get_bank_accounts_balances) | **GET** /obp/v5.0.0/banks/{BANK_ID}/balances | Get Accounts Balances
[**o_bpv4_0_0_get_core_account_by_id**](AccountApi.md#o_bpv4_0_0_get_core_account_by_id) | **GET** /obp/v5.0.0/my/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account | Get Account by Id (Core)
[**o_bpv4_0_0_get_counterparties_for_any_account**](AccountApi.md#o_bpv4_0_0_get_counterparties_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties for any account (Explicit)
[**o_bpv4_0_0_get_counterparty_by_id_for_any_account**](AccountApi.md#o_bpv4_0_0_get_counterparty_by_id_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Get Counterparty by Id for any account (Explicit) 
[**o_bpv4_0_0_get_counterparty_by_name_for_any_account**](AccountApi.md#o_bpv4_0_0_get_counterparty_by_name_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparty-names/{COUNTERPARTY_NAME} | Get Counterparty by name for any account (Explicit) 
[**o_bpv4_0_0_get_explict_counterparties_for_account**](AccountApi.md#o_bpv4_0_0_get_explict_counterparties_for_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties (Explicit)
[**o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank**](AccountApi.md#o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/fast-firehose/accounts | Get Fast Firehose Accounts at Bank
[**o_bpv4_0_0_get_firehose_accounts_at_one_bank**](AccountApi.md#o_bpv4_0_0_get_firehose_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/firehose/accounts/views/{VIEW_ID} | Get Firehose Accounts at Bank
[**o_bpv4_0_0_get_private_account_by_id_full**](AccountApi.md#o_bpv4_0_0_get_private_account_by_id_full) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/account | Get Account by Id (Full)
[**o_bpv4_0_0_get_private_accounts_at_one_bank**](AccountApi.md#o_bpv4_0_0_get_private_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts | Get Accounts at Bank
[**o_bpv4_0_0_get_tags_for_view_on_account**](AccountApi.md#o_bpv4_0_0_get_tags_for_view_on_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/metadata/tags | Get tags on account
[**o_bpv4_0_0_grant_user_access_to_view**](AccountApi.md#o_bpv4_0_0_grant_user_access_to_view) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account-access/grant | Grant User access to View
[**o_bpv4_0_0_iban_checker**](AccountApi.md#o_bpv4_0_0_iban_checker) | **POST** /obp/v5.0.0/account/check/scheme/iban | Validate and check IBAN number
[**o_bpv4_0_0_revoke_grant_user_access_to_views**](AccountApi.md#o_bpv4_0_0_revoke_grant_user_access_to_views) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account-access | Revoke/Grant User access to View
[**o_bpv4_0_0_revoke_user_access_to_view**](AccountApi.md#o_bpv4_0_0_revoke_user_access_to_view) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account-access/revoke | Revoke User access to View
[**o_bpv4_0_0_update_account_label**](AccountApi.md#o_bpv4_0_0_update_account_label) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID} | Update Account Label
[**o_bpv5_0_0_create_account**](AccountApi.md#o_bpv5_0_0_create_account) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID} | Create Account
[**o_bpv5_0_0_create_customer_account_link**](AccountApi.md#o_bpv5_0_0_create_customer_account_link) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customer-account-links | Create Customer Account Link
[**o_bpv5_0_0_get_views_for_bank_account**](AccountApi.md#o_bpv5_0_0_get_views_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/views | Get Views for Account


# **o_bpv1_2_1_delete_view_for_bank_account**
> EmptyClassJson o_bpv1_2_1_delete_view_for_bank_account(body, view_id, account_id, bank_id)

Delete View

<p>Deletes the view specified by VIEW_ID on the bank account specified by ACCOUNT_ID at bank BANK_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete View
    api_response = api_instance.o_bpv1_2_1_delete_view_for_bank_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv1_2_1_delete_view_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get access
    api_response = api_instance.o_bpv2_0_0_get_permissions_for_bank_account(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv2_0_0_get_permissions_for_bank_account: %s\n" % e)
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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Public Accounts at all Banks
    api_response = api_instance.o_bpv2_0_0_public_accounts_all_banks(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv2_0_0_public_accounts_all_banks: %s\n" % e)
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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Public Accounts at Bank
    api_response = api_instance.o_bpv2_0_0_public_accounts_at_one_bank(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv2_0_0_public_accounts_at_one_bank: %s\n" % e)
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

# **o_bpv3_0_0_core_private_accounts_all_banks**
> CoreAccountsJsonV300 o_bpv3_0_0_core_private_accounts_all_banks()

Get Accounts at all Banks (private)

<p>Returns the list of accounts containing private views for the user.<br />Each account lists the views available to the user.</p><p>optional request parameters:</p><ul><li>account_type_filter: one or many accountType value, split by comma</li><li>account_type_filter_operation: the filter type of account_type_filter, value must be INCLUDE or EXCLUDE</li></ul><p>whole url example:<br />/my/accounts?account_type_filter=330,CURRENT+PLUS&amp;account_type_filter_operation=INCLUDE</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))

try:
    # Get Accounts at all Banks (private)
    api_response = api_instance.o_bpv3_0_0_core_private_accounts_all_banks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_core_private_accounts_all_banks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CoreAccountsJsonV300**](CoreAccountsJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_create_view_for_bank_account**
> ViewJsonV300 o_bpv3_0_0_create_view_for_bank_account(body, account_id, bank_id)

Create View

<p>Create a view on bank account</p><p>Authentication is Mandatory and the user needs to have access to the owner view.<br />The 'alias' field in the JSON can take one of three values:</p><ul><li><em>public</em>: to use the public alias if there is one specified for the other account.</li><li><em>private</em>: to use the public alias if there is one specified for the other account.</li><li><p><em>''(empty string)</em>: to use no alias; the view shows the real name of the other account.</p></li></ul><p>The 'hide_metadata_if_alias_used' field in the JSON can take boolean values. If it is set to <code>true</code> and there is an alias on the other account then the other accounts' metadata (like more_info, url, image_url, open_corporates_url, etc.) will be hidden. Otherwise the metadata will be shown.</p><p>The 'allowed_actions' field is a list containing the name of the actions allowed on this view, all the actions contained will be set to <code>true</code> on the view creation, the rest will be set to <code>false</code>.</p><p>You MUST use a leading _ (underscore) in the view name because other view names are reserved for OBP <a href=\"/index#group-View-System\">system views</a>.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.CreateViewJsonV300() # CreateViewJsonV300 | CreateViewJsonV300 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create View
    api_response = api_instance.o_bpv3_0_0_create_view_for_bank_account(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_create_view_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewJsonV300**](CreateViewJsonV300.md)| CreateViewJsonV300 object that needs to be added. | 
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

# **o_bpv3_0_0_get_accounts_held**
> CoreAccountsHeldJsonV300 o_bpv3_0_0_get_accounts_held(bank_id)

Get Accounts Held

<p>Get Accounts held by the current User if even the User has not been assigned the owner View yet.</p><p>Can be used to onboard the account to the API - since all other account and transaction endpoints require views to be assigned.</p><p>optional request parameters:</p><ul><li>account_type_filter: one or many accountType value, split by comma</li><li>account_type_filter_operation: the filter type of account_type_filter, value must be INCLUDE or EXCLUDE</li></ul><p>whole url example:<br />/banks/BANK_ID/accounts-held?account_type_filter=330,CURRENT+PLUS&amp;account_type_filter_operation=INCLUDE</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts Held
    api_response = api_instance.o_bpv3_0_0_get_accounts_held(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_accounts_held: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CoreAccountsHeldJsonV300**](CoreAccountsHeldJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_core_transactions_for_bank_account**
> CoreTransactionsJsonV300 o_bpv3_0_0_get_core_transactions_for_bank_account(account_id, bank_id)

Get Transactions for Account (Core)

<p>Returns transactions list (Core info) of the account specified by ACCOUNT_ID.</p><p>Authentication is Mandatory</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>from_date=DATE =&gt; example value: 1970-01-01T00:00:00.000Z. NOTE! The default value is one year ago (1970-01-01T00:00:00.000Z).</li><li>to_date=DATE =&gt; example value: 2023-02-16T16:23:47.662Z. NOTE! The default value is now (2023-02-16T16:23:47.662Z).</li></ul><p>Date format parameter: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'(1100-01-01T01:01:01.000Z) ==&gt; time zone is UTC.</p><p>eg3:?sort_direction=ASC&amp;limit=100&amp;offset=0&amp;from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transactions for Account (Core)
    api_response = api_instance.o_bpv3_0_0_get_core_transactions_for_bank_account(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_core_transactions_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CoreTransactionsJsonV300**](CoreTransactionsJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_other_account_by_id_for_bank_account**
> OtherAccountJsonV300 o_bpv3_0_0_get_other_account_by_id_for_bank_account(other_account_id, view_id, account_id, bank_id)

Get Other Account by Id

<p>Returns data about the Other Account that has shared at least one transaction with ACCOUNT_ID at BANK_ID.<br />Authentication is Optional</p><p>Authentication is required if the view is not public.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Account by Id
    api_response = api_instance.o_bpv3_0_0_get_other_account_by_id_for_bank_account(other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_other_account_by_id_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_account_id** | **str**| The other account id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**OtherAccountJsonV300**](OtherAccountJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_other_accounts_for_bank_account**
> OtherAccountsJsonV300 o_bpv3_0_0_get_other_accounts_for_bank_account(view_id, account_id, bank_id)

Get Other Accounts of one Account

<p>Returns data about all the other accounts that have shared at least one transaction with the ACCOUNT_ID at BANK_ID.<br />Authentication is Optional</p><p>Authentication is required if the view VIEW_ID is not public.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Accounts of one Account
    api_response = api_instance.o_bpv3_0_0_get_other_accounts_for_bank_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_other_accounts_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**OtherAccountsJsonV300**](OtherAccountsJsonV300.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
provider = 'provider_example' # str | the user PROVIDER
provider_id = 'provider_id_example' # str | The provider id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account access for User
    api_response = api_instance.o_bpv3_0_0_get_permission_for_user_for_bank_account(provider, provider_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_permission_for_user_for_bank_account: %s\n" % e)
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

# **o_bpv3_0_0_get_private_account_idsby_bank_id**
> AccountsIdsJsonV300 o_bpv3_0_0_get_private_account_idsby_bank_id(bank_id)

Get Accounts at Bank (IDs only)

<p>Returns only the list of accounts ids at BANK_ID that the user has access to.</p><p>Each account must have at least one private View.</p><p>For each account the API returns its account ID.</p><p>If you want to see more information on the Views, use the Account Detail call.</p><p>optional request parameters:</p><ul><li>account_type_filter: one or many accountType value, split by comma</li><li>account_type_filter_operation: the filter type of account_type_filter, value must be INCLUDE or EXCLUDE</li></ul><p>whole url example:<br />/banks/BANK_ID/accounts/account_ids/private?account_type_filter=330,CURRENT+PLUS&amp;account_type_filter_operation=INCLUDE</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank (IDs only)
    api_response = api_instance.o_bpv3_0_0_get_private_account_idsby_bank_id(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_private_account_idsby_bank_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountsIdsJsonV300**](AccountsIdsJsonV300.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Public Account by Id
    api_response = api_instance.o_bpv3_0_0_get_public_account_by_id(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_public_account_by_id: %s\n" % e)
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

# **o_bpv3_0_0_get_transactions_for_bank_account**
> TransactionsJsonV300 o_bpv3_0_0_get_transactions_for_bank_account(view_id, account_id, bank_id)

Get Transactions for Account (Full)

<p>Returns transactions list of the account specified by ACCOUNT_ID and <a href=\"#1_2_1-getViewsForBankAccount\">moderated</a> by the view (VIEW_ID).</p><p>Authentication is Optional</p><p>Authentication is required if the view is not public.</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>from_date=DATE =&gt; example value: 1970-01-01T00:00:00.000Z. NOTE! The default value is one year ago (1970-01-01T00:00:00.000Z).</li><li>to_date=DATE =&gt; example value: 2023-02-16T16:23:47.663Z. NOTE! The default value is now (2023-02-16T16:23:47.663Z).</li></ul><p>Date format parameter: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'(1100-01-01T01:01:01.000Z) ==&gt; time zone is UTC.</p><p>eg3:?sort_direction=ASC&amp;limit=100&amp;offset=0&amp;from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transactions for Account (Full)
    api_response = api_instance.o_bpv3_0_0_get_transactions_for_bank_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_get_transactions_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionsJsonV300**](TransactionsJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_private_accounts_at_one_bank**
> CoreAccountsJsonV300 o_bpv3_0_0_private_accounts_at_one_bank(bank_id)

Get Accounts at Bank (Minimal)

<p>Returns the minimal list of private accounts at BANK_ID that the user has access to.<br />For each account, the API returns the ID, routing addresses and the views available to the current user.</p><p>If you want to see more information on the Views, use the Account Detail call.</p><p>optional request parameters:</p><ul><li>account_type_filter: one or many accountType value, split by comma</li><li>account_type_filter_operation: the filter type of account_type_filter, value must be INCLUDE or EXCLUDE</li></ul><p>whole url example:<br />/banks/BANK_ID/accounts/private?account_type_filter=330,CURRENT+PLUS&amp;account_type_filter_operation=INCLUDE</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank (Minimal)
    api_response = api_instance.o_bpv3_0_0_private_accounts_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_private_accounts_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CoreAccountsJsonV300**](CoreAccountsJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_update_view_for_bank_account**
> ViewJsonV300 o_bpv3_0_0_update_view_for_bank_account(body, view_id, account_id, bank_id)

Update View

<p>Update an existing view on a bank account</p><p>Authentication is Mandatory and the user needs to have access to the owner view.</p><p>The json sent is the same as during view creation (above), with one difference: the 'name' field<br />of a view is not editable (it is only set when a view is created)</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.UpdateViewJsonV300() # UpdateViewJsonV300 | UpdateViewJsonV300 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update View
    api_response = api_instance.o_bpv3_0_0_update_view_for_bank_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_0_0_update_view_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateViewJsonV300**](UpdateViewJsonV300.md)| UpdateViewJsonV300 object that needs to be added. | 
 **view_id** | **str**| The view id | 
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

# **o_bpv3_1_0_check_funds_available**
> CheckFundsAvailableJson o_bpv3_1_0_check_funds_available(view_id, account_id, bank_id)

Check Available Funds

<p>Check Available Funds<br />Mandatory URL parameters:</p><ul><li>amount=NUMBER</li><li>currency=STRING</li></ul><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Check Available Funds
    api_response = api_instance.o_bpv3_1_0_check_funds_available(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_check_funds_available: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CheckFundsAvailableJson**](CheckFundsAvailableJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.AccountApplicationJson() # AccountApplicationJson | AccountApplicationJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Account Application
    api_response = api_instance.o_bpv3_1_0_create_account_application(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_create_account_application: %s\n" % e)
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

# **o_bpv3_1_0_create_account_attribute**
> AccountAttributeResponseJson o_bpv3_1_0_create_account_attribute(body, product_code, account_id, bank_id)

Create Account Attribute

<p>Create Account Attribute</p><p>Account Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Account Attribute is linked to its Account by ACCOUNT_ID</p><p>Typical account attributes might be:</p><p>ISIN (for International bonds)<br />VKN (for German bonds)<br />REDCODE (markit short code for credit derivative)<br />LOAN_ID (e.g. used for Anacredit reporting)</p><p>ISSUE_DATE (When the bond was issued in the market)<br />MATURITY_DATE (End of life time of a product)<br />TRADABLE</p><p>See <a href=\"http://www.fpml.org/\">FPML</a> for more examples.</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.AccountAttributeJson() # AccountAttributeJson | AccountAttributeJson object that needs to be added.
product_code = 'product_code_example' # str | the product code
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Account Attribute
    api_response = api_instance.o_bpv3_1_0_create_account_attribute(body, product_code, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_create_account_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountAttributeJson**](AccountAttributeJson.md)| AccountAttributeJson object that needs to be added. | 
 **product_code** | **str**| the product code | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountAttributeResponseJson**](AccountAttributeResponseJson.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
account_application_id = 'account_application_id_example' # str | the account application id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Application by Id
    api_response = api_instance.o_bpv3_1_0_get_account_application(account_application_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_get_account_application: %s\n" % e)
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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Applications
    api_response = api_instance.o_bpv3_1_0_get_account_applications(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_get_account_applications: %s\n" % e)
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

# **o_bpv3_1_0_get_checkbook_orders**
> CheckbookOrdersJson o_bpv3_1_0_get_checkbook_orders(view_id, account_id, bank_id)

Get Checkbook orders

<pre><code>  Get all checkbook orders</code></pre><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Checkbook orders
    api_response = api_instance.o_bpv3_1_0_get_checkbook_orders(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_get_checkbook_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CheckbookOrdersJson**](CheckbookOrdersJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_account**
> UpdateAccountResponseJsonV310 o_bpv3_1_0_update_account(body, account_id, bank_id)

Update Account

<p>Update the account.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.UpdateAccountRequestJsonV310() # UpdateAccountRequestJsonV310 | UpdateAccountRequestJsonV310 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Account
    api_response = api_instance.o_bpv3_1_0_update_account(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAccountRequestJsonV310**](UpdateAccountRequestJsonV310.md)| UpdateAccountRequestJsonV310 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UpdateAccountResponseJsonV310**](UpdateAccountResponseJsonV310.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.AccountApplicationUpdateStatusJson() # AccountApplicationUpdateStatusJson | AccountApplicationUpdateStatusJson object that needs to be added.
account_application_id = 'account_application_id_example' # str | the account application id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Account Application Status
    api_response = api_instance.o_bpv3_1_0_update_account_application_status(body, account_application_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_update_account_application_status: %s\n" % e)
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

# **o_bpv3_1_0_update_account_attribute**
> AccountAttributeResponseJson o_bpv3_1_0_update_account_attribute(body, account_attribute_id, product_code, account_id, bank_id)

Update Account Attribute

<p>Update Account Attribute</p><p>Account Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Account Attribute is linked to its Account by ACCOUNT_ID</p><p>Typical account attributes might be:</p><p>ISIN (for International bonds)<br />VKN (for German bonds)<br />REDCODE (markit short code for credit derivative)<br />LOAN_ID (e.g. used for Anacredit reporting)</p><p>ISSUE_DATE (When the bond was issued in the market)<br />MATURITY_DATE (End of life time of a product)<br />TRADABLE</p><p>See <a href=\"http://www.fpml.org/\">FPML</a> for more examples.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.AccountAttributeJson() # AccountAttributeJson | AccountAttributeJson object that needs to be added.
account_attribute_id = 'account_attribute_id_example' # str | the account attribute id 
product_code = 'product_code_example' # str | the product code
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Account Attribute
    api_response = api_instance.o_bpv3_1_0_update_account_attribute(body, account_attribute_id, product_code, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv3_1_0_update_account_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountAttributeJson**](AccountAttributeJson.md)| AccountAttributeJson object that needs to be added. | 
 **account_attribute_id** | **str**| the account attribute id  | 
 **product_code** | **str**| the product code | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountAttributeResponseJson**](AccountAttributeResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_add_account**
> CreateAccountResponseJsonV310 o_bpv4_0_0_add_account(body, bank_id)

Create Account (POST)

<p>Create Account at bank specified by BANK_ID.</p><p>The User can create an Account for himself  - or -  the User that has the USER_ID specified in the POST body.</p><p>If the POST body USER_ID <em>is</em> specified, the logged in user must have the Role CanCreateAccount. Once created, the Account will be owned by the User specified by USER_ID.</p><p>If the POST body USER_ID is <em>not</em> specified, the account will be owned by the logged in User.</p><p>The 'product_code' field SHOULD be a product_code from Product.<br />If the product_code matches a product_code from Product, account attributes will be created that match the Product Attributes.</p><p>Note: The Amount MUST be zero.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.CreateAccountRequestJsonV310() # CreateAccountRequestJsonV310 | CreateAccountRequestJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Account (POST)
    api_response = api_instance.o_bpv4_0_0_add_account(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAccountRequestJsonV310**](CreateAccountRequestJsonV310.md)| CreateAccountRequestJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CreateAccountResponseJsonV310**](CreateAccountResponseJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_add_tag_for_view_on_account**
> AccountTagJSON o_bpv4_0_0_add_tag_for_view_on_account(body, view_id, account_id, bank_id)

Create a tag on account

<p>Posts a tag about an account ACCOUNT_ID on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> VIEW_ID.</p><p>Authentication is Mandatory</p><p>Authentication is required as the tag is linked with the user.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostAccountTagJSON() # PostAccountTagJSON | PostAccountTagJSON object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create a tag on account
    api_response = api_instance.o_bpv4_0_0_add_tag_for_view_on_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_add_tag_for_view_on_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostAccountTagJSON**](PostAccountTagJSON.md)| PostAccountTagJSON object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountTagJSON**](AccountTagJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_counterparty**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_create_counterparty(body, view_id, account_id, bank_id)

Create Counterparty (Explicit)

<p>Create Counterparty (Explicit) for an Account.</p><p>In OBP, there are two types of Counterparty.</p><ul><li><p>Explicit Counterparties (those here) which we create explicitly and are used in COUNTERPARTY Transaction Requests</p></li><li><p>Implicit Counterparties (AKA Other Accounts) which are generated automatically from the other sides of Transactions.</p></li></ul><p>Explicit Counterparties are created for the account / view<br />They are how the user of the view (e.g. account owner) refers to the other side of the transaction</p><p>name : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>description : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>currency : counterparty account currency (e.g. EUR, GBP, USD, ...)</p><p>bank_routing_scheme : eg: bankId or bankCode or any other strings</p><p>bank_routing_address : eg: <code>gh.29.uk</code>, must be valid sandbox bankIds</p><p>account_routing_scheme : eg: AccountId or AccountNumber or any other strings</p><p>account_routing_address : eg: <code>1d65db7c-a7b2-4839-af41-95</code>, must be valid accountIds</p><p>other_account_secondary_routing_scheme : eg: IBan or any other strings</p><p>other_account_secondary_routing_address : if it is an IBAN, it should be unique for each counterparty.</p><p>other_branch_routing_scheme : eg: branchId or any other strings or you can leave it empty, not useful in sandbox mode.</p><p>other_branch_routing_address : eg: <code>branch-id-123</code> or you can leave it empty, not useful in sandbox mode.</p><p>is_beneficiary : must be set to <code>true</code> in order to send payments to this counterparty</p><p>bespoke: It supports a list of key-value, you can add it to the counterparty.</p><p>bespoke.key : any info-key you want to add to this counterparty</p><p>bespoke.value : any info-value you want to add to this counterparty</p><p>The view specified by VIEW_ID must have the canAddCounterparty permission</p><p>A minimal example for TransactionRequestType == COUNTERPARTY<br />{<br />&quot;name&quot;: &quot;Tesobe1&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;&quot;,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>A minimal example for TransactionRequestType == SEPA</p><p>{<br />&quot;name&quot;: &quot;Tesobe2&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;IBAN&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;DE89 3704 0044 0532 0130 00&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostCounterpartyJson400() # PostCounterpartyJson400 | PostCounterpartyJson400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Counterparty (Explicit)
    api_response = api_instance.o_bpv4_0_0_create_counterparty(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCounterpartyJson400**](PostCounterpartyJson400.md)| PostCounterpartyJson400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CounterpartyWithMetadataJson400**](CounterpartyWithMetadataJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_counterparty_for_any_account**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_create_counterparty_for_any_account(body, view_id, account_id, bank_id)

Create Counterparty for any account (Explicit)

<p>Create Counterparty for any Account. (Explicit)</p><p>In OBP, there are two types of Counterparty.</p><ul><li><p>Explicit Counterparties (those here) which we create explicitly and are used in COUNTERPARTY Transaction Requests</p></li><li><p>Implicit Counterparties (AKA Other Accounts) which are generated automatically from the other sides of Transactions.</p></li></ul><p>Explicit Counterparties are created for the account / view<br />They are how the user of the view (e.g. account owner) refers to the other side of the transaction</p><p>name : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>description : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>currency : counterparty account currency (e.g. EUR, GBP, USD, ...)</p><p>bank_routing_scheme : eg: bankId or bankCode or any other strings</p><p>bank_routing_address : eg: <code>gh.29.uk</code>, must be valid sandbox bankIds</p><p>account_routing_scheme : eg: AccountId or AccountNumber or any other strings</p><p>account_routing_address : eg: <code>1d65db7c-a7b2-4839-af41-95</code>, must be valid accountIds</p><p>other_account_secondary_routing_scheme : eg: IBan or any other strings</p><p>other_account_secondary_routing_address : if it is an IBAN, it should be unique for each counterparty.</p><p>other_branch_routing_scheme : eg: branchId or any other strings or you can leave it empty, not useful in sandbox mode.</p><p>other_branch_routing_address : eg: <code>branch-id-123</code> or you can leave it empty, not useful in sandbox mode.</p><p>is_beneficiary : must be set to <code>true</code> in order to send payments to this counterparty</p><p>bespoke: It supports a list of key-value, you can add it to the counterparty.</p><p>bespoke.key : any info-key you want to add to this counterparty</p><p>bespoke.value : any info-value you want to add to this counterparty</p><p>The view specified by VIEW_ID must have the canAddCounterparty permission</p><p>A minimal example for TransactionRequestType == COUNTERPARTY<br />{<br />&quot;name&quot;: &quot;Tesobe1&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;&quot;,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>A minimal example for TransactionRequestType == SEPA</p><p>{<br />&quot;name&quot;: &quot;Tesobe2&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;IBAN&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;DE89 3704 0044 0532 0130 00&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostCounterpartyJson400() # PostCounterpartyJson400 | PostCounterpartyJson400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Counterparty for any account (Explicit)
    api_response = api_instance.o_bpv4_0_0_create_counterparty_for_any_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_counterparty_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCounterpartyJson400**](PostCounterpartyJson400.md)| PostCounterpartyJson400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CounterpartyWithMetadataJson400**](CounterpartyWithMetadataJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostDirectDebitJsonV400() # PostDirectDebitJsonV400 | PostDirectDebitJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Direct Debit
    api_response = api_instance.o_bpv4_0_0_create_direct_debit(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_direct_debit: %s\n" % e)
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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostDirectDebitJsonV400() # PostDirectDebitJsonV400 | PostDirectDebitJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Direct Debit (management)
    api_response = api_instance.o_bpv4_0_0_create_direct_debit_management(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_direct_debit_management: %s\n" % e)
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

# **o_bpv4_0_0_create_or_update_account_attribute_definition**
> AttributeDefinitionResponseJsonV400 o_bpv4_0_0_create_or_update_account_attribute_definition(body, bank_id)

Create or Update Account Attribute Definition

<p>Create or Update Account Attribute Definition</p><p>The category field must be Account</p><p>The type field must be one of; DOUBLE, STRING, INTEGER and DATE_WITH_DAY</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.AttributeDefinitionJsonV400() # AttributeDefinitionJsonV400 | AttributeDefinitionJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create or Update Account Attribute Definition
    api_response = api_instance.o_bpv4_0_0_create_or_update_account_attribute_definition(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_or_update_account_attribute_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeDefinitionJsonV400**](AttributeDefinitionJsonV400.md)| AttributeDefinitionJsonV400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AttributeDefinitionResponseJsonV400**](AttributeDefinitionResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_standing_order**
> StandingOrderJsonV400 o_bpv4_0_0_create_standing_order(body, view_id, account_id, bank_id)

Create Standing Order

<p>Create standing order for an account.</p><p>when -&gt; frequency = {‘YEARLY’,’MONTHLY, ‘WEEKLY’, ‘BI-WEEKLY’, DAILY’}<br />when -&gt; detail = { ‘FIRST_MONDAY’, ‘FIRST_DAY’, ‘LAST_DAY’}}</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostStandingOrderJsonV400() # PostStandingOrderJsonV400 | PostStandingOrderJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Standing Order
    api_response = api_instance.o_bpv4_0_0_create_standing_order(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_standing_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostStandingOrderJsonV400**](PostStandingOrderJsonV400.md)| PostStandingOrderJsonV400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**StandingOrderJsonV400**](StandingOrderJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_standing_order_management**
> StandingOrderJsonV400 o_bpv4_0_0_create_standing_order_management(body, account_id, bank_id)

Create Standing Order (management)

<p>Create standing order for an account.</p><p>when -&gt; frequency = {‘YEARLY’,’MONTHLY, ‘WEEKLY’, ‘BI-WEEKLY’, DAILY’}<br />when -&gt; detail = { ‘FIRST_MONDAY’, ‘FIRST_DAY’, ‘LAST_DAY’}}</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostStandingOrderJsonV400() # PostStandingOrderJsonV400 | PostStandingOrderJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Standing Order (management)
    api_response = api_instance.o_bpv4_0_0_create_standing_order_management(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_standing_order_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostStandingOrderJsonV400**](PostStandingOrderJsonV400.md)| PostStandingOrderJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**StandingOrderJsonV400**](StandingOrderJsonV400.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostCreateUserAccountAccessJsonV400() # PostCreateUserAccountAccessJsonV400 | PostCreateUserAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create (DAuth) User with Account Access
    api_response = api_instance.o_bpv4_0_0_create_user_with_account_access(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_create_user_with_account_access: %s\n" % e)
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

# **o_bpv4_0_0_delete_account_attribute_definition**
> o_bpv4_0_0_delete_account_attribute_definition(bank_id)

Delete Account Attribute Definition

<p>Delete Account Attribute Definition by ATTRIBUTE_DEFINITION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Account Attribute Definition
    api_instance.o_bpv4_0_0_delete_account_attribute_definition(bank_id)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_delete_account_attribute_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_account_cascade**
> o_bpv4_0_0_delete_account_cascade(account_id, bank_id)

Delete Account Cascade

<p>Delete an Account Cascade specified by ACCOUNT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Account Cascade
    api_instance.o_bpv4_0_0_delete_account_cascade(account_id, bank_id)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_delete_account_cascade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_counterparty_for_any_account**
> o_bpv4_0_0_delete_counterparty_for_any_account(counterparty_id, view_id, account_id, bank_id)

Delete Counterparty for any account (Explicit)

<p>Delete Counterparty (Explicit) for any account<br />and also delete the Metadata for its counterparty.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty for any account (Explicit)
    api_instance.o_bpv4_0_0_delete_counterparty_for_any_account(counterparty_id, view_id, account_id, bank_id)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_delete_counterparty_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| the counterparty id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_explicit_counterparty**
> o_bpv4_0_0_delete_explicit_counterparty(counterparty_id, view_id, account_id, bank_id)

Delete Counterparty (Explicit)

<p>Delete Counterparty (Explicit) for an Account.<br />and also delete the Metadata for its counterparty.</p><p>need the view permission <code>can_delete_counterparty</code><br />Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty (Explicit)
    api_instance.o_bpv4_0_0_delete_explicit_counterparty(counterparty_id, view_id, account_id, bank_id)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_delete_explicit_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| the counterparty id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_tag_for_view_on_account**
> o_bpv4_0_0_delete_tag_for_view_on_account(tag_id, view_id, account_id, bank_id)

Delete a tag on account

<p>Deletes the tag TAG_ID about the account ACCOUNT_ID made on <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.</p><p>Authentication is Mandatory</p><p>Authentication is required as the tag is linked with the user.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
tag_id = 'tag_id_example' # str | The tag id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete a tag on account
    api_instance.o_bpv4_0_0_delete_tag_for_view_on_account(tag_id, view_id, account_id, bank_id)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_delete_tag_for_view_on_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The tag id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_account_attribute_definition**
> AttributeDefinitionsResponseJsonV400 o_bpv4_0_0_get_account_attribute_definition(bank_id)

Get Account Attribute Definition

<p>Get Account Attribute Definition</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Attribute Definition
    api_response = api_instance.o_bpv4_0_0_get_account_attribute_definition(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_account_attribute_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AttributeDefinitionsResponseJsonV400**](AttributeDefinitionsResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_account_by_account_routing**
> ModeratedAccountJSON400 o_bpv4_0_0_get_account_by_account_routing(body)

Get Account by Account Routing

<p>This endpoint returns the account (if it exists) linked with the provided scheme and address.</p><p>The <code>bank_id</code> field is optional, but if it's not provided, we don't guarantee that the returned account is unique across all the banks.</p><p>Example of account routing scheme: <code>IBAN</code>, &quot;OBP&quot;, &quot;AccountNumber&quot;, ...<br />Example of account routing address: <code>DE17500105178275645584</code>, &quot;321774cc-fccd-11ea-adc1-0242ac120002&quot;, &quot;55897106215&quot;, ...</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.BankAccountRoutingJson() # BankAccountRoutingJson | BankAccountRoutingJson object that needs to be added.

try:
    # Get Account by Account Routing
    api_response = api_instance.o_bpv4_0_0_get_account_by_account_routing(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_account_by_account_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankAccountRoutingJson**](BankAccountRoutingJson.md)| BankAccountRoutingJson object that needs to be added. | 

### Return type

[**ModeratedAccountJSON400**](ModeratedAccountJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_accounts_by_account_routing_regex**
> ModeratedAccountsJSON400 o_bpv4_0_0_get_accounts_by_account_routing_regex(body)

Get Accounts by Account Routing Regex

<p>This endpoint returns an array of accounts matching the provided routing scheme and the routing address regex.</p><p>The <code>bank_id</code> field is optional.</p><p>Example of account routing scheme: <code>IBAN</code>, <code>OBP</code>, <code>AccountNumber</code>, ...<br />Example of account routing address regex: <code>DE175.*</code>, <code>55897106215-[A-Z]{3}</code>, ...</p><p>This endpoint can be used to retrieve multiples accounts matching a same account routing address pattern.<br />For example, if you want to link multiple accounts having different currencies, you can create an account<br />with <code>123456789-EUR</code> as Account Number and an other account with <code>123456789-USD</code> as Account Number.<br />So we can identify the Account Number as <code>123456789</code>, so to get all the accounts with the same account number<br />and the different currencies, we can use this body in the request :</p><pre><code>{   &quot;bank_id&quot;: &quot;BANK_ID&quot;,   &quot;account_routing&quot;: {       &quot;scheme&quot;: &quot;AccountNumber&quot;,       &quot;address&quot;: &quot;123456789-[A-Z]{3}&quot;   }}</code></pre><p>This request will returns the accounts matching the routing address regex (<code>123456789-EUR</code> and <code>123456789-USD</code>).</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.BankAccountRoutingJson() # BankAccountRoutingJson | BankAccountRoutingJson object that needs to be added.

try:
    # Get Accounts by Account Routing Regex
    api_response = api_instance.o_bpv4_0_0_get_accounts_by_account_routing_regex(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_accounts_by_account_routing_regex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankAccountRoutingJson**](BankAccountRoutingJson.md)| BankAccountRoutingJson object that needs to be added. | 

### Return type

[**ModeratedAccountsJSON400**](ModeratedAccountsJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_accounts_minimal_by_customer_id**
> AccountsMinimalJson400 o_bpv4_0_0_get_accounts_minimal_by_customer_id(customer_id)

Get Accounts Minimal for a Customer

<p>Get Accounts Minimal by CUSTOMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Accounts Minimal for a Customer
    api_response = api_instance.o_bpv4_0_0_get_accounts_minimal_by_customer_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_accounts_minimal_by_customer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 

### Return type

[**AccountsMinimalJson400**](AccountsMinimalJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_account_balances**
> AccountBalanceJsonV400 o_bpv4_0_0_get_bank_account_balances(account_id, bank_id)

Get Account Balances

<p>Get the Balances for one Account of the current User at one bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Balances
    api_response = api_instance.o_bpv4_0_0_get_bank_account_balances(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_bank_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountBalanceJsonV400**](AccountBalanceJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_accounts_balances**
> AccountsBalancesJsonV400 o_bpv4_0_0_get_bank_accounts_balances(bank_id)

Get Accounts Balances

<p>Get the Balances for the Accounts of the current User at one bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts Balances
    api_response = api_instance.o_bpv4_0_0_get_bank_accounts_balances(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_bank_accounts_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountsBalancesJsonV400**](AccountsBalancesJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_core_account_by_id**
> ModeratedCoreAccountJsonV400 o_bpv4_0_0_get_core_account_by_id(account_id, bank_id)

Get Account by Id (Core)

<p>Information returned about the account specified by ACCOUNT_ID:</p><ul><li>Number - The human readable account number given by the bank that identifies the account.</li><li>Label - A label given by the owner of the account</li><li>Owners - Users that own this account</li><li>Type - The type of account</li><li>Balance - Currency and Value</li><li>Account Routings - A list that might include IBAN or national account identifiers</li><li>Account Rules - A list that might include Overdraft and other bank specific rules</li><li>Tags - A list of Tags assigned to this account</li></ul><p>This call returns the owner view and requires access to that view.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account by Id (Core)
    api_response = api_instance.o_bpv4_0_0_get_core_account_by_id(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_core_account_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ModeratedCoreAccountJsonV400**](ModeratedCoreAccountJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_counterparties_for_any_account**
> CounterpartiesJson400 o_bpv4_0_0_get_counterparties_for_any_account(view_id, account_id, bank_id)

Get Counterparties for any account (Explicit)

<p>Get the Counterparties (Explicit) for any account .</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties for any account (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_counterparties_for_any_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_counterparties_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CounterpartiesJson400**](CounterpartiesJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_counterparty_by_id_for_any_account**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_get_counterparty_by_id_for_any_account(counterparty_id, view_id, account_id, bank_id)

Get Counterparty by Id for any account (Explicit) 

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by Id for any account (Explicit) 
    api_response = api_instance.o_bpv4_0_0_get_counterparty_by_id_for_any_account(counterparty_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_counterparty_by_id_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| the counterparty id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CounterpartyWithMetadataJson400**](CounterpartyWithMetadataJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_counterparty_by_name_for_any_account**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_get_counterparty_by_name_for_any_account(counterparty_name, view_id, account_id, bank_id)

Get Counterparty by name for any account (Explicit) 

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
counterparty_name = 'counterparty_name_example' # str | the counterparty name
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by name for any account (Explicit) 
    api_response = api_instance.o_bpv4_0_0_get_counterparty_by_name_for_any_account(counterparty_name, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_counterparty_by_name_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_name** | **str**| the counterparty name | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CounterpartyWithMetadataJson400**](CounterpartyWithMetadataJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_explict_counterparties_for_account**
> CounterpartiesJson400 o_bpv4_0_0_get_explict_counterparties_for_account(view_id, account_id, bank_id)

Get Counterparties (Explicit)

<p>Get the Counterparties (Explicit) for the account / view.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparties_for_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_explict_counterparties_for_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CounterpartiesJson400**](CounterpartiesJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank**
> FastFirehoseAccountsJsonV400 o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank(bank_id)

Get Fast Firehose Accounts at Bank

<p>This endpoint allows bulk access to accounts.</p><p>optional pagination parameters for filter with accounts</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Fast Firehose Accounts at Bank
    api_response = api_instance.o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**FastFirehoseAccountsJsonV400**](FastFirehoseAccountsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_firehose_accounts_at_one_bank**
> ModeratedFirehoseAccountsJsonV400 o_bpv4_0_0_get_firehose_accounts_at_one_bank(view_id, bank_id)

Get Firehose Accounts at Bank

<p>Get Accounts which have a firehose view assigned to them.</p><p>This endpoint allows bulk access to accounts.</p><p>Requires the CanUseFirehoseAtAnyBank Role</p><p>To be shown on the list, each Account must have a firehose View linked to it.</p><p>A firehose view has is_firehose = true</p><p>For VIEW_ID try 'owner'</p><p>optional request parameters for filter with attributes<br />URL params example:<br />/banks/some-bank-id/firehose/accounts/views/owner?manager=John&amp;count=8</p><p>to invalid Browser cache, add timestamp query parameter as follow, the parameter name must be <code>_timestamp_</code><br />URL params example:<br /><code>/banks/some-bank-id/firehose/accounts/views/owner?manager=John&amp;count=8&amp;_timestamp_=1596762180358</code></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Firehose Accounts at Bank
    api_response = api_instance.o_bpv4_0_0_get_firehose_accounts_at_one_bank(view_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_firehose_accounts_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ModeratedFirehoseAccountsJsonV400**](ModeratedFirehoseAccountsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_private_account_by_id_full**
> ModeratedAccountJSON400 o_bpv4_0_0_get_private_account_by_id_full(view_id, account_id, bank_id)

Get Account by Id (Full)

<p>Information returned about an account specified by ACCOUNT_ID as moderated by the view (VIEW_ID):</p><ul><li>Number</li><li>Owners</li><li>Type</li><li>Balance</li><li>IBAN</li><li>Available views (sorted by short_name)</li></ul><p>More details about the data moderation by the view <a href=\"#1_2_1-getViewsForBankAccount\">here</a>.</p><p>PSD2 Context: PSD2 requires customers to have access to their account information via third party applications.<br />This call provides balance and other account information via delegated authentication using OAuth.</p><p>Authentication is required if the 'is_public' field in view (VIEW_ID) is not set to <code>true</code>.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account by Id (Full)
    api_response = api_instance.o_bpv4_0_0_get_private_account_by_id_full(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_private_account_by_id_full: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ModeratedAccountJSON400**](ModeratedAccountJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_private_accounts_at_one_bank**
> BasicAccountsJSON o_bpv4_0_0_get_private_accounts_at_one_bank(bank_id)

Get Accounts at Bank

<p>Returns the list of accounts at BANK_ID that the user has access to.<br />For each account the API returns the account ID and the views available to the user..<br />Each account must have at least one private View.</p><p>optional request parameters for filter with attributes<br />URL params example: /banks/some-bank-id/accounts?manager=John&amp;count=8</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank
    api_response = api_instance.o_bpv4_0_0_get_private_accounts_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_private_accounts_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**BasicAccountsJSON**](BasicAccountsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_tags_for_view_on_account**
> AccountTagsJSON o_bpv4_0_0_get_tags_for_view_on_account(view_id, account_id, bank_id)

Get tags on account

<p>Returns the account ACCOUNT_ID tags made on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> (VIEW_ID).<br />Authentication is Mandatory</p><p>Authentication is required as the tag is linked with the user.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get tags on account
    api_response = api_instance.o_bpv4_0_0_get_tags_for_view_on_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_get_tags_for_view_on_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AccountTagsJSON**](AccountTagsJSON.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostAccountAccessJsonV400() # PostAccountAccessJsonV400 | PostAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Grant User access to View
    api_response = api_instance.o_bpv4_0_0_grant_user_access_to_view(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_grant_user_access_to_view: %s\n" % e)
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

# **o_bpv4_0_0_iban_checker**
> IbanCheckerJsonV400 o_bpv4_0_0_iban_checker(body)

Validate and check IBAN number

<p>Validate and check IBAN number for errors</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.IbanAddress() # IbanAddress | IbanAddress object that needs to be added.

try:
    # Validate and check IBAN number
    api_response = api_instance.o_bpv4_0_0_iban_checker(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_iban_checker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IbanAddress**](IbanAddress.md)| IbanAddress object that needs to be added. | 

### Return type

[**IbanCheckerJsonV400**](IbanCheckerJsonV400.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostRevokeGrantAccountAccessJsonV400() # PostRevokeGrantAccountAccessJsonV400 | PostRevokeGrantAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke/Grant User access to View
    api_response = api_instance.o_bpv4_0_0_revoke_grant_user_access_to_views(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_revoke_grant_user_access_to_views: %s\n" % e)
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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.PostAccountAccessJsonV400() # PostAccountAccessJsonV400 | PostAccountAccessJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke User access to View
    api_response = api_instance.o_bpv4_0_0_revoke_user_access_to_view(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_revoke_user_access_to_view: %s\n" % e)
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

# **o_bpv4_0_0_update_account_label**
> SuccessMessage o_bpv4_0_0_update_account_label(body, account_id, bank_id)

Update Account Label

<p>Update the label for the account. The label is how the account is known to the account owner e.g. 'My savings account'</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.UpdateAccountJsonV400() # UpdateAccountJsonV400 | UpdateAccountJsonV400 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Account Label
    api_response = api_instance.o_bpv4_0_0_update_account_label(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv4_0_0_update_account_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAccountJsonV400**](UpdateAccountJsonV400.md)| UpdateAccountJsonV400 object that needs to be added. | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.CreateAccountRequestJsonV500() # CreateAccountRequestJsonV500 | CreateAccountRequestJsonV500 object that needs to be added.
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Account
    api_response = api_instance.o_bpv5_0_0_create_account(body, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv5_0_0_create_account: %s\n" % e)
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

# **o_bpv5_0_0_create_customer_account_link**
> CustomerAccountLinkJson o_bpv5_0_0_create_customer_account_link(body, bank_id)

Create Customer Account Link

<p>Link a Customer to a Account</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
body = obp_python.CreateCustomerAccountLinkJson() # CreateCustomerAccountLinkJson | CreateCustomerAccountLinkJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Account Link
    api_response = api_instance.o_bpv5_0_0_create_customer_account_link(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv5_0_0_create_customer_account_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerAccountLinkJson**](CreateCustomerAccountLinkJson.md)| CreateCustomerAccountLinkJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAccountLinkJson**](CustomerAccountLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_views_for_bank_account**
> ViewsJsonV500 o_bpv5_0_0_get_views_for_bank_account(account_id, bank_id)

Get Views for Account

<h1><a href=\"#views\" id=\"views\">Views</a></h1><p>Views in Open Bank Project provide a mechanism for fine grained access control and delegation to Accounts and Transactions. Account holders use the 'owner' view by default. Delegated access is made through other views for example 'accountants', 'share-holders' or 'tagging-application'. Views can be created via the API and each view has a list of entitlements.</p><p>Views on accounts and transactions filter the underlying data to redact certain fields for certain users. For instance the balance on an account may be hidden from the public. The way to know what is possible on a view is determined in the following JSON.</p><p><strong>Data:</strong> When a view moderates a set of data, some fields my contain the value <code>null</code> rather than the original value. This indicates either that the user is not allowed to see the original data or the field is empty.</p><p>There is currently one exception to this rule; the 'holder' field in the JSON contains always a value which is either an alias or the real name - indicated by the 'is_alias' field.</p><p><strong>Action:</strong> When a user performs an action like trying to post a comment (with POST API call), if he is not allowed, the body response will contain an error message.</p><p><strong>Metadata:</strong><br />Transaction metadata (like images, tags, comments, etc.) will appears <em>ONLY</em> on the view where they have been created e.g. comments posted to the public view only appear on the public view.</p><p>The other account metadata fields (like image_URL, more_info, etc.) are unique through all the views. Example, if a user edits the 'more_info' field in the 'team' view, then the view 'authorities' will show the new value (if it is allowed to do it).</p><h1><a href=\"#all\" id=\"all\">All</a></h1><p><em>Optional</em></p><p>Returns the list of the views created for account ACCOUNT_ID at BANK_ID.</p><p>Authentication is Mandatory and the user needs to have access to the owner view.</p>

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
api_instance = obp_python.AccountApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Views for Account
    api_response = api_instance.o_bpv5_0_0_get_views_for_bank_account(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->o_bpv5_0_0_get_views_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ViewsJsonV500**](ViewsJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

