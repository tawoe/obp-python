# obp_python.AccountInformationServiceAISApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_0_0_get_transaction_types**](AccountInformationServiceAISApi.md#o_bpv2_0_0_get_transaction_types) | **GET** /obp/v5.0.0/banks/{BANK_ID}/transaction-types | Get Transaction Types at Bank
[**o_bpv3_0_0_core_private_accounts_all_banks**](AccountInformationServiceAISApi.md#o_bpv3_0_0_core_private_accounts_all_banks) | **GET** /obp/v5.0.0/my/accounts | Get Accounts at all Banks (private)
[**o_bpv3_0_0_get_accounts_held**](AccountInformationServiceAISApi.md#o_bpv3_0_0_get_accounts_held) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts-held | Get Accounts Held
[**o_bpv3_0_0_get_core_transactions_for_bank_account**](AccountInformationServiceAISApi.md#o_bpv3_0_0_get_core_transactions_for_bank_account) | **GET** /obp/v5.0.0/my/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/transactions | Get Transactions for Account (Core)
[**o_bpv3_0_0_get_private_account_idsby_bank_id**](AccountInformationServiceAISApi.md#o_bpv3_0_0_get_private_account_idsby_bank_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/account_ids/private | Get Accounts at Bank (IDs only)
[**o_bpv3_0_0_private_accounts_at_one_bank**](AccountInformationServiceAISApi.md#o_bpv3_0_0_private_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/private | Get Accounts at Bank (Minimal)
[**o_bpv3_1_0_answer_consent_challenge**](AccountInformationServiceAISApi.md#o_bpv3_1_0_answer_consent_challenge) | **POST** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID}/challenge | Answer Consent Challenge
[**o_bpv3_1_0_create_consent_email**](AccountInformationServiceAISApi.md#o_bpv3_1_0_create_consent_email) | **POST** /obp/v5.0.0/banks/{BANK_ID}/my/consents/EMAIL | Create Consent (EMAIL)
[**o_bpv3_1_0_create_consent_sms**](AccountInformationServiceAISApi.md#o_bpv3_1_0_create_consent_sms) | **POST** /obp/v5.0.0/banks/{BANK_ID}/my/consents/SMS | Create Consent (SMS)
[**o_bpv3_1_0_get_server_jwk**](AccountInformationServiceAISApi.md#o_bpv3_1_0_get_server_jwk) | **GET** /obp/v5.0.0/certs | Get JSON Web Key (JWK)
[**o_bpv3_1_0_revoke_consent**](AccountInformationServiceAISApi.md#o_bpv3_1_0_revoke_consent) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consents/{CONSENT_ID}/revoke | Revoke Consent
[**o_bpv4_0_0_add_consent_user**](AccountInformationServiceAISApi.md#o_bpv4_0_0_add_consent_user) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID}/user-update-request | Add User to a Consent
[**o_bpv4_0_0_get_bank_account_balances**](AccountInformationServiceAISApi.md#o_bpv4_0_0_get_bank_account_balances) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/balances | Get Account Balances
[**o_bpv4_0_0_get_bank_accounts_balances**](AccountInformationServiceAISApi.md#o_bpv4_0_0_get_bank_accounts_balances) | **GET** /obp/v5.0.0/banks/{BANK_ID}/balances | Get Accounts Balances
[**o_bpv4_0_0_get_banks**](AccountInformationServiceAISApi.md#o_bpv4_0_0_get_banks) | **GET** /obp/v5.0.0/banks | Get Banks
[**o_bpv4_0_0_get_consent_infos**](AccountInformationServiceAISApi.md#o_bpv4_0_0_get_consent_infos) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consent-infos | Get Consents Info
[**o_bpv4_0_0_get_consents**](AccountInformationServiceAISApi.md#o_bpv4_0_0_get_consents) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consents | Get Consents
[**o_bpv4_0_0_get_core_account_by_id**](AccountInformationServiceAISApi.md#o_bpv4_0_0_get_core_account_by_id) | **GET** /obp/v5.0.0/my/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account | Get Account by Id (Core)
[**o_bpv4_0_0_update_consent_status**](AccountInformationServiceAISApi.md#o_bpv4_0_0_update_consent_status) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID} | Update Consent Status
[**o_bpv5_0_0_create_consent_by_consent_request_id_email**](AccountInformationServiceAISApi.md#o_bpv5_0_0_create_consent_by_consent_request_id_email) | **POST** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/EMAIL/consents | Create Consent By CONSENT_REQUEST_ID (EMAIL)
[**o_bpv5_0_0_create_consent_by_consent_request_id_sms**](AccountInformationServiceAISApi.md#o_bpv5_0_0_create_consent_by_consent_request_id_sms) | **POST** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/SMS/consents | Create Consent By CONSENT_REQUEST_ID (SMS)
[**o_bpv5_0_0_create_consent_request**](AccountInformationServiceAISApi.md#o_bpv5_0_0_create_consent_request) | **POST** /obp/v5.0.0/consumer/consent-requests | Create Consent Request
[**o_bpv5_0_0_get_bank**](AccountInformationServiceAISApi.md#o_bpv5_0_0_get_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID} | Get Bank
[**o_bpv5_0_0_get_consent_by_consent_request_id**](AccountInformationServiceAISApi.md#o_bpv5_0_0_get_consent_by_consent_request_id) | **GET** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/consents | Get Consent By Consent Request Id
[**o_bpv5_0_0_get_consent_request**](AccountInformationServiceAISApi.md#o_bpv5_0_0_get_consent_request) | **GET** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID | Get Consent Request


# **o_bpv2_0_0_get_transaction_types**
> TransactionTypesJsonV200 o_bpv2_0_0_get_transaction_types(body, bank_id)

Get Transaction Types at Bank

<p>Get Transaction Types for the bank specified by BANK_ID:</p><p>Lists the possible Transaction Types available at the bank (as opposed to Transaction Request Types which are the possible ways Transactions can be created by this API Server).</p><ul><li>id : Unique transaction type id across the API instance. SHOULD be a UUID. MUST be unique.</li><li>bank_id : The bank that supports this TransactionType</li><li>short_code : A short code (SHOULD have no-spaces) which MUST be unique across the bank. May be stored with Transactions to link here</li><li>summary : A succinct summary</li><li>description : A longer description</li><li>charge : The charge to the customer for each one of these</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Types at Bank
    api_response = api_instance.o_bpv2_0_0_get_transaction_types(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv2_0_0_get_transaction_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionTypesJsonV200**](TransactionTypesJsonV200.md)

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Get Accounts at all Banks (private)
    api_response = api_instance.o_bpv3_0_0_core_private_accounts_all_banks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_0_0_core_private_accounts_all_banks: %s\n" % e)
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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts Held
    api_response = api_instance.o_bpv3_0_0_get_accounts_held(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_0_0_get_accounts_held: %s\n" % e)
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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transactions for Account (Core)
    api_response = api_instance.o_bpv3_0_0_get_core_transactions_for_bank_account(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_0_0_get_core_transactions_for_bank_account: %s\n" % e)
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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank (IDs only)
    api_response = api_instance.o_bpv3_0_0_get_private_account_idsby_bank_id(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_0_0_get_private_account_idsby_bank_id: %s\n" % e)
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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank (Minimal)
    api_response = api_instance.o_bpv3_0_0_private_accounts_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_0_0_private_accounts_at_one_bank: %s\n" % e)
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

# **o_bpv3_1_0_answer_consent_challenge**
> ConsentChallengeJsonV310 o_bpv3_1_0_answer_consent_challenge(body, consent_id, bank_id)

Answer Consent Challenge

<p>An OBP Consent allows the holder of the Consent to call one or more endpoints.</p><p>Consents must be created and authorisied using SCA (Strong Customer Authentication).</p><p>That is, Consents can be created by an authorised User via the OBP REST API but they must be confirmed via an out of band (OOB) mechanism such as a code sent to a mobile phone.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Each Consent is bound to a consumer i.e. you need to identify yourself over request header value Consumer-Key.<br />For example:<br />GET /obp/v4.0.0/users/current HTTP/1.1<br />Host: 127.0.0.1:8080<br />Consent-JWT: eyJhbGciOiJIUzI1NiJ9.eyJlbnRpdGxlbWVudHMiOlt7InJvbGVfbmFtZSI6IkNhbkdldEFueVVzZXIiLCJiYW5rX2lkIjoiIn<br />1dLCJjcmVhdGVkQnlVc2VySWQiOiJhYjY1MzlhOS1iMTA1LTQ0ODktYTg4My0wYWQ4ZDZjNjE2NTciLCJzdWIiOiIzNDc1MDEzZi03YmY5LTQyNj<br />EtOWUxYy0xZTdlNWZjZTJlN2UiLCJhdWQiOiI4MTVhMGVmMS00YjZhLTQyMDUtYjExMi1lNDVmZDZmNGQzYWQiLCJuYmYiOjE1ODA3NDE2NjcsIml<br />zcyI6Imh0dHA6XC9cLzEyNy4wLjAuMTo4MDgwIiwiZXhwIjoxNTgwNzQ1MjY3LCJpYXQiOjE1ODA3NDE2NjcsImp0aSI6ImJkYzVjZTk5LTE2ZTY<br />tNDM4Yi1hNjllLTU3MTAzN2RhMTg3OCIsInZpZXdzIjpbXX0.L3fEEEhdCVr3qnmyRKBBUaIQ7dk1VjiFaEBW8hUNjfg</p><p>Consumer-Key: ejznk505d132ryomnhbx1qmtohurbsbb0kijajsk<br />cache-control: no-cache</p><p>Maximum time to live of the token is specified over props value consents.max_time_to_live. In case isn't defined default value is 3600 seconds.</p><p>Example of POST JSON:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;&#x6c;&#x74;o&#x3a;&#101;&#118;&#101;&#x6c;&#x69;&#x6e;&#x65;&#x40;&#x65;&#120;&#x61;&#109;pl&#101;&#x2e;&#99;&#111;m\">&#101;&#118;&#x65;&#108;i&#110;&#x65;&#x40;&#101;&#120;a&#109;&#x70;&#108;&#101;&#x2e;c&#x6f;&#109;</a>&quot;,<br />&quot;valid_from&quot;: &quot;2020-02-07T08:43:34Z&quot;,<br />&quot;time_to_live&quot;: 3600<br />}<br />Please note that only optional fields are: consumer_id, valid_from and time_to_live.<br />In case you omit they the default values are used:<br />consumer_id = consumer of current user<br />valid_from = current time<br />time_to_live = consents.max_time_to_live</p><p>This endpoint is used to confirm a Consent previously created.</p><p>The User must supply a code that was sent out of band (OOB) for example via an SMS.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentChallengeJsonV310() # PostConsentChallengeJsonV310 | PostConsentChallengeJsonV310 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Answer Consent Challenge
    api_response = api_instance.o_bpv3_1_0_answer_consent_challenge(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_1_0_answer_consent_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentChallengeJsonV310**](PostConsentChallengeJsonV310.md)| PostConsentChallengeJsonV310 object that needs to be added. | 
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentChallengeJsonV310**](ConsentChallengeJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_consent_email**
> ConsentJsonV310 o_bpv3_1_0_create_consent_email(body, bank_id)

Create Consent (EMAIL)

<p>This endpoint starts the process of creating a Consent.</p><p>The Consent is created in an INITIATED state.</p><p>A One Time Password (OTP) (AKA security challenge) is sent Out of band (OOB) to the User via the transport defined in SCA_METHOD<br />SCA_METHOD is typically &quot;SMS&quot; or &quot;EMAIL&quot;. &quot;EMAIL&quot; is used for testing purposes.</p><p>When the Consent is created, OBP (or a backend system) stores the challenge so it can be checked later against the value supplied by the User with the Answer Consent Challenge endpoint.</p><p>An OBP Consent allows the holder of the Consent to call one or more endpoints.</p><p>Consents must be created and authorisied using SCA (Strong Customer Authentication).</p><p>That is, Consents can be created by an authorised User via the OBP REST API but they must be confirmed via an out of band (OOB) mechanism such as a code sent to a mobile phone.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Each Consent is bound to a consumer i.e. you need to identify yourself over request header value Consumer-Key.<br />For example:<br />GET /obp/v4.0.0/users/current HTTP/1.1<br />Host: 127.0.0.1:8080<br />Consent-JWT: eyJhbGciOiJIUzI1NiJ9.eyJlbnRpdGxlbWVudHMiOlt7InJvbGVfbmFtZSI6IkNhbkdldEFueVVzZXIiLCJiYW5rX2lkIjoiIn<br />1dLCJjcmVhdGVkQnlVc2VySWQiOiJhYjY1MzlhOS1iMTA1LTQ0ODktYTg4My0wYWQ4ZDZjNjE2NTciLCJzdWIiOiIzNDc1MDEzZi03YmY5LTQyNj<br />EtOWUxYy0xZTdlNWZjZTJlN2UiLCJhdWQiOiI4MTVhMGVmMS00YjZhLTQyMDUtYjExMi1lNDVmZDZmNGQzYWQiLCJuYmYiOjE1ODA3NDE2NjcsIml<br />zcyI6Imh0dHA6XC9cLzEyNy4wLjAuMTo4MDgwIiwiZXhwIjoxNTgwNzQ1MjY3LCJpYXQiOjE1ODA3NDE2NjcsImp0aSI6ImJkYzVjZTk5LTE2ZTY<br />tNDM4Yi1hNjllLTU3MTAzN2RhMTg3OCIsInZpZXdzIjpbXX0.L3fEEEhdCVr3qnmyRKBBUaIQ7dk1VjiFaEBW8hUNjfg</p><p>Consumer-Key: ejznk505d132ryomnhbx1qmtohurbsbb0kijajsk<br />cache-control: no-cache</p><p>Maximum time to live of the token is specified over props value consents.max_time_to_live. In case isn't defined default value is 3600 seconds.</p><p>Example of POST JSON:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#x61;i&#108;&#x74;&#x6f;&#58;e&#x76;&#101;&#108;&#105;&#110;&#101;&#x40;&#x65;&#x78;&#x61;&#109;&#112;&#108;e&#x2e;&#x63;&#x6f;&#109;\">&#x65;&#118;&#x65;li&#x6e;&#101;&#64;&#x65;&#120;&#x61;&#x6d;&#112;&#108;&#101;&#x2e;&#x63;o&#109;</a>&quot;,<br />&quot;valid_from&quot;: &quot;2020-02-07T08:43:34Z&quot;,<br />&quot;time_to_live&quot;: 3600<br />}<br />Please note that only optional fields are: consumer_id, valid_from and time_to_live.<br />In case you omit they the default values are used:<br />consumer_id = consumer of current user<br />valid_from = current time<br />time_to_live = consents.max_time_to_live</p><p>Authentication is Mandatory</p><p>Example 1:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;l&#x74;&#111;&#x3a;e&#118;&#101;&#x6c;&#x69;&#110;&#x65;&#x40;&#x65;&#x78;&#x61;&#x6d;p&#x6c;&#x65;&#x2e;&#x63;&#x6f;&#109;\">&#101;v&#101;&#108;&#105;&#110;&#101;@&#101;&#x78;&#97;&#109;&#x70;&#x6c;&#101;.&#x63;&#x6f;&#x6d;</a>&quot;<br />}</p><p>Please note that consumer_id is optional field<br />Example 2:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;lto&#x3a;&#x65;&#118;e&#x6c;&#x69;n&#x65;&#x40;&#x65;&#120;&#97;&#x6d;p&#108;&#x65;&#x2e;&#x63;&#x6f;&#x6d;\">&#x65;&#x76;&#101;&#108;&#x69;&#110;&#101;&#64;&#x65;x&#x61;&#x6d;&#112;&#x6c;&#101;&#x2e;&#x63;&#111;&#109;</a>&quot;<br />}</p><p>Please note if everything=false you need to explicitly specify views and entitlements<br />Example 3:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#x61;&#105;&#108;&#116;&#x6f;&#x3a;&#x65;&#x76;&#101;&#x6c;&#x69;&#x6e;&#x65;&#64;&#101;&#x78;&#97;&#x6d;p&#x6c;&#x65;&#46;&#99;&#111;&#109;\">&#x65;&#x76;&#101;&#x6c;&#105;&#110;&#101;&#x40;&#x65;&#x78;&#97;&#x6d;&#x70;&#x6c;&#101;&#x2e;&#99;&#x6f;&#109;</a>&quot;<br />}</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentEmailJsonV310() # PostConsentEmailJsonV310 | PostConsentEmailJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Consent (EMAIL)
    api_response = api_instance.o_bpv3_1_0_create_consent_email(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_1_0_create_consent_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentEmailJsonV310**](PostConsentEmailJsonV310.md)| PostConsentEmailJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentJsonV310**](ConsentJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_consent_sms**
> ConsentJsonV310 o_bpv3_1_0_create_consent_sms(body, bank_id)

Create Consent (SMS)

<p>This endpoint starts the process of creating a Consent.</p><p>The Consent is created in an INITIATED state.</p><p>A One Time Password (OTP) (AKA security challenge) is sent Out of Band (OOB) to the User via the transport defined in SCA_METHOD<br />SCA_METHOD is typically &quot;SMS&quot; or &quot;EMAIL&quot;. &quot;EMAIL&quot; is used for testing purposes.</p><p>When the Consent is created, OBP (or a backend system) stores the challenge so it can be checked later against the value supplied by the User with the Answer Consent Challenge endpoint.</p><p>An OBP Consent allows the holder of the Consent to call one or more endpoints.</p><p>Consents must be created and authorisied using SCA (Strong Customer Authentication).</p><p>That is, Consents can be created by an authorised User via the OBP REST API but they must be confirmed via an out of band (OOB) mechanism such as a code sent to a mobile phone.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Each Consent is bound to a consumer i.e. you need to identify yourself over request header value Consumer-Key.<br />For example:<br />GET /obp/v4.0.0/users/current HTTP/1.1<br />Host: 127.0.0.1:8080<br />Consent-JWT: eyJhbGciOiJIUzI1NiJ9.eyJlbnRpdGxlbWVudHMiOlt7InJvbGVfbmFtZSI6IkNhbkdldEFueVVzZXIiLCJiYW5rX2lkIjoiIn<br />1dLCJjcmVhdGVkQnlVc2VySWQiOiJhYjY1MzlhOS1iMTA1LTQ0ODktYTg4My0wYWQ4ZDZjNjE2NTciLCJzdWIiOiIzNDc1MDEzZi03YmY5LTQyNj<br />EtOWUxYy0xZTdlNWZjZTJlN2UiLCJhdWQiOiI4MTVhMGVmMS00YjZhLTQyMDUtYjExMi1lNDVmZDZmNGQzYWQiLCJuYmYiOjE1ODA3NDE2NjcsIml<br />zcyI6Imh0dHA6XC9cLzEyNy4wLjAuMTo4MDgwIiwiZXhwIjoxNTgwNzQ1MjY3LCJpYXQiOjE1ODA3NDE2NjcsImp0aSI6ImJkYzVjZTk5LTE2ZTY<br />tNDM4Yi1hNjllLTU3MTAzN2RhMTg3OCIsInZpZXdzIjpbXX0.L3fEEEhdCVr3qnmyRKBBUaIQ7dk1VjiFaEBW8hUNjfg</p><p>Consumer-Key: ejznk505d132ryomnhbx1qmtohurbsbb0kijajsk<br />cache-control: no-cache</p><p>Maximum time to live of the token is specified over props value consents.max_time_to_live. In case isn't defined default value is 3600 seconds.</p><p>Example of POST JSON:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"ma&#105;&#108;&#x74;&#111;:&#x65;&#x76;e&#x6c;i&#x6e;&#101;&#64;&#x65;&#x78;&#97;&#x6d;&#x70;&#108;e&#46;c&#111;&#109;\">&#x65;&#x76;&#101;&#x6c;&#105;&#110;&#101;&#64;e&#120;&#x61;&#109;p&#108;&#101;&#x2e;&#x63;o&#109;</a>&quot;,<br />&quot;valid_from&quot;: &quot;2020-02-07T08:43:34Z&quot;,<br />&quot;time_to_live&quot;: 3600<br />}<br />Please note that only optional fields are: consumer_id, valid_from and time_to_live.<br />In case you omit they the default values are used:<br />consumer_id = consumer of current user<br />valid_from = current time<br />time_to_live = consents.max_time_to_live</p><p>Authentication is Mandatory</p><p>Example 1:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"m&#x61;&#x69;&#108;&#116;o&#x3a;e&#118;&#x65;&#108;&#x69;&#110;&#101;&#x40;ex&#x61;&#x6d;&#112;&#x6c;&#101;&#46;&#x63;&#111;&#x6d;\">&#x65;&#118;el&#x69;&#110;&#101;&#64;&#101;x&#97;&#x6d;&#x70;le&#46;&#99;&#111;&#x6d;</a>&quot;<br />}</p><p>Please note that consumer_id is optional field<br />Example 2:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;email&quot;: &quot;<a href=\"m&#97;&#x69;&#108;&#116;o:&#101;&#x76;&#x65;&#x6c;i&#x6e;&#101;&#64;&#101;&#120;&#x61;&#109;&#x70;l&#101;&#46;&#x63;&#111;&#109;\">ev&#101;&#x6c;&#x69;&#110;&#x65;&#64;&#101;&#x78;&#x61;&#109;p&#x6c;&#x65;.c&#111;&#x6d;</a>&quot;<br />}</p><p>Please note if everything=false you need to explicitly specify views and entitlements<br />Example 3:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;lto&#58;&#101;&#x76;&#x65;&#x6c;i&#x6e;&#101;&#64;&#101;&#x78;&#x61;&#x6d;pl&#101;&#x2e;&#x63;&#111;&#109;\">e&#x76;&#101;&#108;&#x69;&#x6e;&#x65;&#64;e&#120;a&#x6d;&#112;&#108;&#x65;.c&#x6f;&#x6d;</a>&quot;<br />}</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentPhoneJsonV310() # PostConsentPhoneJsonV310 | PostConsentPhoneJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Consent (SMS)
    api_response = api_instance.o_bpv3_1_0_create_consent_sms(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_1_0_create_consent_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentPhoneJsonV310**](PostConsentPhoneJsonV310.md)| PostConsentPhoneJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentJsonV310**](ConsentJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_server_jwk**
> SeverJWK o_bpv3_1_0_get_server_jwk()

Get JSON Web Key (JWK)

<p>Get the server's public JSON Web Key (JWK) set and certificate chain.<br />It is required by client applications to validate ID tokens, self-contained access tokens and other issued objects.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Get JSON Web Key (JWK)
    api_response = api_instance.o_bpv3_1_0_get_server_jwk()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_1_0_get_server_jwk: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SeverJWK**](SeverJWK.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_revoke_consent**
> ConsentJsonV310 o_bpv3_1_0_revoke_consent(consent_id, bank_id)

Revoke Consent

<p>Revoke Consent for current user specified by CONSENT_ID</p><p>There are a few reasons you might need to revoke an application’s access to a user’s account:<br />- The user explicitly wishes to revoke the application’s access<br />- You as the service provider have determined an application is compromised or malicious, and want to disable it<br />- etc.</p><p>Please note that this endpoint only supports the case:: &quot;The user explicitly wishes to revoke the application’s access&quot;</p><p>OBP as a resource server stores access tokens in a database, then it is relatively easy to revoke some token that belongs to a particular user.<br />The status of the token is changed to &quot;REVOKED&quot; so the next time the revoked client makes a request, their token will fail to validate.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke Consent
    api_response = api_instance.o_bpv3_1_0_revoke_consent(consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv3_1_0_revoke_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentJsonV310**](ConsentJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_add_consent_user**
> ConsentChallengeJsonV310 o_bpv4_0_0_add_consent_user(body, consent_id, bank_id)

Add User to a Consent

<p>This endpoint is used to add the User of Consent.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.PutConsentUserJsonV400() # PutConsentUserJsonV400 | PutConsentUserJsonV400 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add User to a Consent
    api_response = api_instance.o_bpv4_0_0_add_consent_user(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_add_consent_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutConsentUserJsonV400**](PutConsentUserJsonV400.md)| PutConsentUserJsonV400 object that needs to be added. | 
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentChallengeJsonV310**](ConsentChallengeJsonV310.md)

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Balances
    api_response = api_instance.o_bpv4_0_0_get_bank_account_balances(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_get_bank_account_balances: %s\n" % e)
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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts Balances
    api_response = api_instance.o_bpv4_0_0_get_bank_accounts_balances(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_get_bank_accounts_balances: %s\n" % e)
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

# **o_bpv4_0_0_get_banks**
> BanksJson400 o_bpv4_0_0_get_banks()

Get Banks

<p>Get banks on this API instance<br />Returns a list of banks supported on this server:</p><ul><li>ID used as parameter in URLs</li><li>Short and full name of bank</li><li>Logo URL</li><li>Website</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Get Banks
    api_response = api_instance.o_bpv4_0_0_get_banks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_get_banks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BanksJson400**](BanksJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_consent_infos**
> ConsentInfosJsonV400 o_bpv4_0_0_get_consent_infos(bank_id)

Get Consents Info

<p>This endpoint gets the Consents that the current User created.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Consents Info
    api_response = api_instance.o_bpv4_0_0_get_consent_infos(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_get_consent_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentInfosJsonV400**](ConsentInfosJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_consents**
> ConsentsJsonV400 o_bpv4_0_0_get_consents(bank_id)

Get Consents

<p>This endpoint gets the Consents that the current User created.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Consents
    api_response = api_instance.o_bpv4_0_0_get_consents(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_get_consents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentsJsonV400**](ConsentsJsonV400.md)

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account by Id (Core)
    api_response = api_instance.o_bpv4_0_0_get_core_account_by_id(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_get_core_account_by_id: %s\n" % e)
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

# **o_bpv4_0_0_update_consent_status**
> ConsentChallengeJsonV310 o_bpv4_0_0_update_consent_status(body, consent_id, bank_id)

Update Consent Status

<p>This endpoint is used to update the Status of Consent.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.PutConsentStatusJsonV400() # PutConsentStatusJsonV400 | PutConsentStatusJsonV400 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Consent Status
    api_response = api_instance.o_bpv4_0_0_update_consent_status(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv4_0_0_update_consent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutConsentStatusJsonV400**](PutConsentStatusJsonV400.md)| PutConsentStatusJsonV400 object that needs to be added. | 
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentChallengeJsonV310**](ConsentChallengeJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_consent_by_consent_request_id_email**
> ConsentJsonV500 o_bpv5_0_0_create_consent_by_consent_request_id_email()

Create Consent By CONSENT_REQUEST_ID (EMAIL)

<p>This endpoint continues the process of creating a Consent. It starts the SCA flow which changes the status of the consent from INITIATED to ACCEPTED or REJECTED.<br />Please note that the Consent cannot elevate the privileges logged in user already have.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Create Consent By CONSENT_REQUEST_ID (EMAIL)
    api_response = api_instance.o_bpv5_0_0_create_consent_by_consent_request_id_email()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv5_0_0_create_consent_by_consent_request_id_email: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentJsonV500**](ConsentJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_consent_by_consent_request_id_sms**
> ConsentJsonV500 o_bpv5_0_0_create_consent_by_consent_request_id_sms()

Create Consent By CONSENT_REQUEST_ID (SMS)

<p>This endpoint continues the process of creating a Consent. It starts the SCA flow which changes the status of the consent from INITIATED to ACCEPTED or REJECTED.<br />Please note that the Consent cannot elevate the privileges logged in user already have.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Create Consent By CONSENT_REQUEST_ID (SMS)
    api_response = api_instance.o_bpv5_0_0_create_consent_by_consent_request_id_sms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv5_0_0_create_consent_by_consent_request_id_sms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentJsonV500**](ConsentJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_consent_request**
> ConsentRequestResponseJson o_bpv5_0_0_create_consent_request(body)

Create Consent Request

<p>Client Authentication (mandatory)</p><p>It is used when applications request an access token to access their own resources, not on behalf of a user.</p><p>The client needs to authenticate themselves for this request.<br />In case of public client we use client_id and private kew to obtain access token, otherwise we use client_id and client_secret.<br />The obtained access token is used in the HTTP Bearer auth header of our request.</p><p>Example:<br />Authorization: Bearer eXtneO-THbQtn3zvK_kQtXXfvOZyZFdBCItlPDbR2Bk.dOWqtXCtFX-tqGTVR0YrIjvAolPIVg7GZ-jz83y6nA0</p><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentRequestJsonV500() # PostConsentRequestJsonV500 | PostConsentRequestJsonV500 object that needs to be added.

try:
    # Create Consent Request
    api_response = api_instance.o_bpv5_0_0_create_consent_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv5_0_0_create_consent_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentRequestJsonV500**](PostConsentRequestJsonV500.md)| PostConsentRequestJsonV500 object that needs to be added. | 

### Return type

[**ConsentRequestResponseJson**](ConsentRequestResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_bank**
> BankJson500 o_bpv5_0_0_get_bank(bank_id)

Get Bank

<p>Get the bank specified by BANK_ID<br />Returns information about a single bank specified by BANK_ID including:</p><ul><li>Bank code and full name of bank</li><li>Logo URL</li><li>Website</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank
    api_response = api_instance.o_bpv5_0_0_get_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv5_0_0_get_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**BankJson500**](BankJson500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_consent_by_consent_request_id**
> ConsentJsonV500 o_bpv5_0_0_get_consent_by_consent_request_id()

Get Consent By Consent Request Id

<p>This endpoint gets the Consent By consent request id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Get Consent By Consent Request Id
    api_response = api_instance.o_bpv5_0_0_get_consent_by_consent_request_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv5_0_0_get_consent_by_consent_request_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentJsonV500**](ConsentJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_consent_request**
> ConsentRequestResponseJson o_bpv5_0_0_get_consent_request()

Get Consent Request

<p>Authentication is Optional</p>

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
api_instance = obp_python.AccountInformationServiceAISApi(obp_python.ApiClient(configuration))

try:
    # Get Consent Request
    api_response = api_instance.o_bpv5_0_0_get_consent_request()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountInformationServiceAISApi->o_bpv5_0_0_get_consent_request: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentRequestResponseJson**](ConsentRequestResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

