# obp_python.PSD2Api

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_4_0_get_transaction_request_types**](PSD2Api.md#o_bpv1_4_0_get_transaction_request_types) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types | Get Transaction Request Types for Account
[**o_bpv2_0_0_get_transaction_types**](PSD2Api.md#o_bpv2_0_0_get_transaction_types) | **GET** /obp/v5.0.0/banks/{BANK_ID}/transaction-types | Get Transaction Types at Bank
[**o_bpv2_1_0_create_transaction_request_sandbox_tan**](PSD2Api.md#o_bpv2_1_0_create_transaction_request_sandbox_tan) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/SANDBOX_TAN/transaction-requests | Create Transaction Request (SANDBOX_TAN)
[**o_bpv3_0_0_core_private_accounts_all_banks**](PSD2Api.md#o_bpv3_0_0_core_private_accounts_all_banks) | **GET** /obp/v5.0.0/my/accounts | Get Accounts at all Banks (private)
[**o_bpv3_0_0_get_accounts_held**](PSD2Api.md#o_bpv3_0_0_get_accounts_held) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts-held | Get Accounts Held
[**o_bpv3_0_0_get_core_transactions_for_bank_account**](PSD2Api.md#o_bpv3_0_0_get_core_transactions_for_bank_account) | **GET** /obp/v5.0.0/my/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/transactions | Get Transactions for Account (Core)
[**o_bpv3_0_0_get_private_account_idsby_bank_id**](PSD2Api.md#o_bpv3_0_0_get_private_account_idsby_bank_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/account_ids/private | Get Accounts at Bank (IDs only)
[**o_bpv3_0_0_private_accounts_at_one_bank**](PSD2Api.md#o_bpv3_0_0_private_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/private | Get Accounts at Bank (Minimal)
[**o_bpv3_1_0_answer_consent_challenge**](PSD2Api.md#o_bpv3_1_0_answer_consent_challenge) | **POST** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID}/challenge | Answer Consent Challenge
[**o_bpv3_1_0_check_funds_available**](PSD2Api.md#o_bpv3_1_0_check_funds_available) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/funds-available | Check Available Funds
[**o_bpv3_1_0_create_consent_email**](PSD2Api.md#o_bpv3_1_0_create_consent_email) | **POST** /obp/v5.0.0/banks/{BANK_ID}/my/consents/EMAIL | Create Consent (EMAIL)
[**o_bpv3_1_0_create_consent_sms**](PSD2Api.md#o_bpv3_1_0_create_consent_sms) | **POST** /obp/v5.0.0/banks/{BANK_ID}/my/consents/SMS | Create Consent (SMS)
[**o_bpv3_1_0_get_server_jwk**](PSD2Api.md#o_bpv3_1_0_get_server_jwk) | **GET** /obp/v5.0.0/certs | Get JSON Web Key (JWK)
[**o_bpv3_1_0_revoke_consent**](PSD2Api.md#o_bpv3_1_0_revoke_consent) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consents/{CONSENT_ID}/revoke | Revoke Consent
[**o_bpv4_0_0_answer_transaction_request_challenge**](PSD2Api.md#o_bpv4_0_0_answer_transaction_request_challenge) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/{TRANSACTION_REQUEST_TYPE}/transaction-requests/{TRANSACTION_REQUEST_ID}/challenge | Answer Transaction Request Challenge
[**o_bpv4_0_0_create_transaction_request_account**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_account) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/ACCOUNT/transaction-requests | Create Transaction Request (ACCOUNT)
[**o_bpv4_0_0_create_transaction_request_account_otp**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_account_otp) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/ACCOUNT_OTP/transaction-requests | Create Transaction Request (ACCOUNT_OTP)
[**o_bpv4_0_0_create_transaction_request_card**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_card) | **POST** /obp/v5.0.0/transaction-request-types/CARD/transaction-requests | Create Transaction Request (CARD)
[**o_bpv4_0_0_create_transaction_request_counterparty**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_counterparty) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/COUNTERPARTY/transaction-requests | Create Transaction Request (COUNTERPARTY)
[**o_bpv4_0_0_create_transaction_request_refund**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_refund) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/REFUND/transaction-requests | Create Transaction Request (REFUND)
[**o_bpv4_0_0_create_transaction_request_sepa**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_sepa) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/SEPA/transaction-requests | Create Transaction Request (SEPA)
[**o_bpv4_0_0_create_transaction_request_simple**](PSD2Api.md#o_bpv4_0_0_create_transaction_request_simple) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/SIMPLE/transaction-requests | Create Transaction Request (SIMPLE)
[**o_bpv4_0_0_get_bank_account_balances**](PSD2Api.md#o_bpv4_0_0_get_bank_account_balances) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/balances | Get Account Balances
[**o_bpv4_0_0_get_bank_accounts_balances**](PSD2Api.md#o_bpv4_0_0_get_bank_accounts_balances) | **GET** /obp/v5.0.0/banks/{BANK_ID}/balances | Get Accounts Balances
[**o_bpv4_0_0_get_banks**](PSD2Api.md#o_bpv4_0_0_get_banks) | **GET** /obp/v5.0.0/banks | Get Banks
[**o_bpv4_0_0_get_consent_infos**](PSD2Api.md#o_bpv4_0_0_get_consent_infos) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consent-infos | Get Consents Info
[**o_bpv4_0_0_get_consents**](PSD2Api.md#o_bpv4_0_0_get_consents) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consents | Get Consents
[**o_bpv4_0_0_get_core_account_by_id**](PSD2Api.md#o_bpv4_0_0_get_core_account_by_id) | **GET** /obp/v5.0.0/my/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/account | Get Account by Id (Core)
[**o_bpv4_0_0_get_counterparties_for_any_account**](PSD2Api.md#o_bpv4_0_0_get_counterparties_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties for any account (Explicit)
[**o_bpv4_0_0_get_explict_counterparties_for_account**](PSD2Api.md#o_bpv4_0_0_get_explict_counterparties_for_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties (Explicit)
[**o_bpv4_0_0_get_explict_counterparty_by_id**](PSD2Api.md#o_bpv4_0_0_get_explict_counterparty_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Get Counterparty by Id (Explicit)
[**o_bpv4_0_0_get_settlement_accounts**](PSD2Api.md#o_bpv4_0_0_get_settlement_accounts) | **GET** /obp/v5.0.0/banks/{BANK_ID}/settlement-accounts | Get Settlement accounts at Bank
[**o_bpv4_0_0_get_transaction_request**](PSD2Api.md#o_bpv4_0_0_get_transaction_request) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-requests/{TRANSACTION_REQUEST_ID} | Get Transaction Request.
[**o_bpv5_0_0_create_consent_by_consent_request_id_email**](PSD2Api.md#o_bpv5_0_0_create_consent_by_consent_request_id_email) | **POST** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/EMAIL/consents | Create Consent By CONSENT_REQUEST_ID (EMAIL)
[**o_bpv5_0_0_create_consent_by_consent_request_id_sms**](PSD2Api.md#o_bpv5_0_0_create_consent_by_consent_request_id_sms) | **POST** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/SMS/consents | Create Consent By CONSENT_REQUEST_ID (SMS)
[**o_bpv5_0_0_create_consent_request**](PSD2Api.md#o_bpv5_0_0_create_consent_request) | **POST** /obp/v5.0.0/consumer/consent-requests | Create Consent Request
[**o_bpv5_0_0_get_bank**](PSD2Api.md#o_bpv5_0_0_get_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID} | Get Bank
[**o_bpv5_0_0_get_consent_by_consent_request_id**](PSD2Api.md#o_bpv5_0_0_get_consent_by_consent_request_id) | **GET** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/consents | Get Consent By Consent Request Id
[**o_bpv5_0_0_get_consent_request**](PSD2Api.md#o_bpv5_0_0_get_consent_request) | **GET** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID | Get Consent Request


# **o_bpv1_4_0_get_transaction_request_types**
> TransactionRequestTypesJsonV140 o_bpv1_4_0_get_transaction_request_types(body, view_id, account_id, bank_id)

Get Transaction Request Types for Account

<p>Returns the Transaction Request Types that the account specified by ACCOUNT_ID and view specified by VIEW_ID has access to.</p><p>These are the ways this API Server can create a Transaction via a Transaction Request<br />(as opposed to Transaction Types which include external types too e.g. for Transactions created by core banking etc.)</p><p>A Transaction Request Type internally determines:</p><ul><li>the required Transaction Request 'body' i.e. fields that define the 'what' and 'to' of a Transaction Request,</li><li>the type of security challenge that may be be raised before the Transaction Request proceeds, and</li><li>the threshold of that challenge.</li></ul><p>For instance in a 'SANDBOX_TAN' Transaction Request, for amounts over 1000 currency units, the user must supply a positive integer to complete the Transaction Request and create a Transaction.</p><p>This approach aims to provide only one endpoint for initiating transactions, and one that handles challenges, whilst still allowing flexibility with the payload and internal logic.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Request Types for Account
    api_response = api_instance.o_bpv1_4_0_get_transaction_request_types(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv1_4_0_get_transaction_request_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestTypesJsonV140**](TransactionRequestTypesJsonV140.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Types at Bank
    api_response = api_instance.o_bpv2_0_0_get_transaction_types(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv2_0_0_get_transaction_types: %s\n" % e)
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

# **o_bpv2_1_0_create_transaction_request_sandbox_tan**
> TransactionRequestWithChargeJSON210 o_bpv2_1_0_create_transaction_request_sandbox_tan(body, view_id, account_id, bank_id)

Create Transaction Request (SANDBOX_TAN)

<p>When using SANDBOX_TAN, the payee is set in the request body.</p><p>Money goes into the BANK_ID and ACCOUNT_ID specified in the request body.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to SANDBOX_TAN. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p>{<br />&quot;XAF&quot;:{<br />&quot;XAF&quot;:1.0,<br />&quot;HKD&quot;:0.0135503,<br />&quot;AUD&quot;:0.00228226,<br />&quot;KRW&quot;:1.87975,<br />&quot;JOD&quot;:0.00127784,<br />&quot;GBP&quot;:0.00131092,<br />&quot;MXN&quot;:0.0396,<br />&quot;AED&quot;:0.00601555,<br />&quot;INR&quot;:0.110241,<br />&quot;XBT&quot;:2.9074795E-8,<br />&quot;JPY&quot;:0.185328,<br />&quot;USD&quot;:0.00163773,<br />&quot;ILS&quot;:0.00641333,<br />&quot;EUR&quot;:0.00152449<br />},<br />&quot;HKD&quot;:{<br />&quot;XAF&quot;:73.8049,<br />&quot;HKD&quot;:1.0,<br />&quot;AUD&quot;:0.178137,<br />&quot;KRW&quot;:143.424,<br />&quot;JOD&quot;:0.0903452,<br />&quot;GBP&quot;:0.0985443,<br />&quot;MXN&quot;:2.8067,<br />&quot;AED&quot;:0.467977,<br />&quot;INR&quot;:9.09325,<br />&quot;XBT&quot;:2.164242461E-6,<br />&quot;JPY&quot;:14.0867,<br />&quot;USD&quot;:0.127427,<br />&quot;ILS&quot;:0.460862,<br />&quot;EUR&quot;:0.112495<br />},<br />&quot;AUD&quot;:{<br />&quot;XAF&quot;:438.162,<br />&quot;HKD&quot;:5.61346,<br />&quot;AUD&quot;:1.0,<br />&quot;KRW&quot;:895.304,<br />&quot;JOD&quot;:0.556152,<br />&quot;GBP&quot;:0.609788,<br />&quot;MXN&quot;:16.0826,<br />&quot;AED&quot;:2.88368,<br />&quot;INR&quot;:50.4238,<br />&quot;XBT&quot;:1.2284055924E-5,<br />&quot;JPY&quot;:87.0936,<br />&quot;USD&quot;:0.785256,<br />&quot;ILS&quot;:2.83558,<br />&quot;EUR&quot;:0.667969<br />},<br />&quot;KRW&quot;:{<br />&quot;XAF&quot;:0.531986,<br />&quot;HKD&quot;:0.00697233,<br />&quot;AUD&quot;:0.00111694,<br />&quot;KRW&quot;:1.0,<br />&quot;JOD&quot;:6.30634E-4,<br />&quot;GBP&quot;:6.97389E-4,<br />&quot;MXN&quot;:0.0183,<br />&quot;AED&quot;:0.00320019,<br />&quot;INR&quot;:0.0586469,<br />&quot;XBT&quot;:1.4234725E-8,<br />&quot;JPY&quot;:0.0985917,<br />&quot;USD&quot;:8.7125E-4,<br />&quot;ILS&quot;:0.00316552,<br />&quot;EUR&quot;:8.11008E-4<br />},<br />&quot;JOD&quot;:{<br />&quot;XAF&quot;:782.572,<br />&quot;HKD&quot;:11.0687,<br />&quot;AUD&quot;:1.63992,<br />&quot;KRW&quot;:1585.68,<br />&quot;JOD&quot;:1.0,<br />&quot;GBP&quot;:1.06757,<br />&quot;MXN&quot;:30.8336,<br />&quot;AED&quot;:5.18231,<br />&quot;INR&quot;:90.1236,<br />&quot;XBT&quot;:2.3803244006E-5,<br />&quot;JPY&quot;:156.304,<br />&quot;USD&quot;:1.41112,<br />&quot;ILS&quot;:5.02018,<br />&quot;EUR&quot;:0.237707<br />},<br />&quot;GBP&quot;:{<br />&quot;XAF&quot;:762.826,<br />&quot;HKD&quot;:10.1468,<br />&quot;AUD&quot;:1.63992,<br />&quot;KRW&quot;:1433.92,<br />&quot;JOD&quot;:0.936707,<br />&quot;GBP&quot;:1.0,<br />&quot;MXN&quot;:29.242,<br />&quot;AED&quot;:4.58882,<br />&quot;INR&quot;:84.095,<br />&quot;XBT&quot;:2.2756409956E-5,<br />&quot;JPY&quot;:141.373,<br />&quot;USD&quot;:1.2493,<br />&quot;ILS&quot;:4.7002,<br />&quot;EUR&quot;:1.16278<br />},<br />&quot;MXN&quot;:{<br />&quot;XAF&quot;:25.189,<br />&quot;HKD&quot;:0.3562,<br />&quot;AUD&quot;:0.0621,<br />&quot;KRW&quot;:54.4512,<br />&quot;JOD&quot;:0.0324,<br />&quot;GBP&quot;:0.0341,<br />&quot;MXN&quot;:1.0,<br />&quot;AED&quot;:0.1688,<br />&quot;INR&quot;:3.3513,<br />&quot;XBT&quot;:8.1112586E-7,<br />&quot;JPY&quot;:4.8687,<br />&quot;USD&quot;:0.0459,<br />&quot;ILS&quot;:0.1541,<br />&quot;EUR&quot;:0.0384<br />},<br />&quot;AED&quot;:{<br />&quot;XAF&quot;:166.236,<br />&quot;HKD&quot;:2.13685,<br />&quot;AUD&quot;:0.346779,<br />&quot;KRW&quot;:312.482,<br />&quot;JOD&quot;:0.1930565,<br />&quot;GBP&quot;:0.217921,<br />&quot;MXN&quot;:5.9217,<br />&quot;AED&quot;:1.0,<br />&quot;INR&quot;:18.3255,<br />&quot;XBT&quot;:4.603349217E-6,<br />&quot;JPY&quot;:30.8081,<br />&quot;USD&quot;:0.27225,<br />&quot;ILS&quot;:0.968033,<br />&quot;EUR&quot;:0.253425<br />},<br />&quot;INR&quot;:{<br />&quot;XAF&quot;:9.07101,<br />&quot;HKD&quot;:0.109972,<br />&quot;AUD&quot;:0.0198319,<br />&quot;KRW&quot;:17.0512,<br />&quot;JOD&quot;:0.0110959,<br />&quot;GBP&quot;:0.0118913,<br />&quot;MXN&quot;:0.2983,<br />&quot;AED&quot;:0.0545671,<br />&quot;INR&quot;:1.0,<br />&quot;XBT&quot;:2.2689396E-7,<br />&quot;JPY&quot;:1.68111,<br />&quot;USD&quot;:0.0148559,<br />&quot;ILS&quot;:0.0556764,<br />&quot;EUR&quot;:0.0138287<br />},<br />&quot;XBT&quot;:{<br />&quot;XAF&quot;:3.4353824E7,<br />&quot;HKD&quot;:460448.9,<br />&quot;AUD&quot;:81168.603,<br />&quot;KRW&quot;:7.0131575E7,<br />&quot;JOD&quot;:41960.111,<br />&quot;GBP&quot;:44188.118,<br />&quot;MXN&quot;:1230503.3,<br />&quot;AED&quot;:217414.47,<br />&quot;INR&quot;:4407607.74,<br />&quot;XBT&quot;:1.0,<br />&quot;JPY&quot;:6805170.8,<br />&quot;USD&quot;:59245.918,<br />&quot;ILS&quot;:182981.21,<br />&quot;EUR&quot;:52436.431<br />},<br />&quot;JPY&quot;:{<br />&quot;XAF&quot;:5.39585,<br />&quot;HKD&quot;:0.0709891,<br />&quot;AUD&quot;:0.0114819,<br />&quot;KRW&quot;:10.1428,<br />&quot;JOD&quot;:0.00639777,<br />&quot;GBP&quot;:0.0070735,<br />&quot;MXN&quot;:0.2053,<br />&quot;AED&quot;:0.032459,<br />&quot;INR&quot;:0.594846,<br />&quot;XBT&quot;:1.47171931E-7,<br />&quot;JPY&quot;:1.0,<br />&quot;USD&quot;:0.00883695,<br />&quot;ILS&quot;:0.0320926,<br />&quot;EUR&quot;:0.00822592<br />},<br />&quot;USD&quot;:{<br />&quot;XAF&quot;:610.601,<br />&quot;HKD&quot;:7.84766,<br />&quot;AUD&quot;:1.27347,<br />&quot;KRW&quot;:1147.78,<br />&quot;JOD&quot;:0.708659,<br />&quot;GBP&quot;:0.800446,<br />&quot;MXN&quot;:21.748,<br />&quot;AED&quot;:3.6731,<br />&quot;INR&quot;:67.3135,<br />&quot;XBT&quot;:1.69154E-5,<br />&quot;JPY&quot;:113.161,<br />&quot;USD&quot;:1.0,<br />&quot;ILS&quot;:3.55495,<br />&quot;EUR&quot;:0.930886<br />},<br />&quot;ILS&quot;:{<br />&quot;XAF&quot;:155.925,<br />&quot;HKD&quot;:2.16985,<br />&quot;AUD&quot;:0.352661,<br />&quot;KRW&quot;:315.903,<br />&quot;JOD&quot;:0.199196,<br />&quot;GBP&quot;:0.212763,<br />&quot;MXN&quot;:6.4871,<br />&quot;AED&quot;:1.03302,<br />&quot;INR&quot;:17.9609,<br />&quot;XBT&quot;:5.452272147E-6,<br />&quot;JPY&quot;:31.1599,<br />&quot;USD&quot;:0.281298,<br />&quot;ILS&quot;:1.0,<br />&quot;EUR&quot;:1.19318<br />},<br />&quot;EUR&quot;:{<br />&quot;XAF&quot;:655.957,<br />&quot;HKD&quot;:8.88926,<br />&quot;AUD&quot;:1.49707,<br />&quot;KRW&quot;:1233.03,<br />&quot;JOD&quot;:0.838098,<br />&quot;GBP&quot;:0.860011,<br />&quot;MXN&quot;:26.0359,<br />&quot;AED&quot;:3.94594,<br />&quot;INR&quot;:72.3136,<br />&quot;XBT&quot;:1.9087905636E-5,<br />&quot;JPY&quot;:121.567,<br />&quot;USD&quot;:1.07428,<br />&quot;ILS&quot;:4.20494,<br />&quot;EUR&quot;:1.0<br />}<br />}</p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyJsonV200() # TransactionRequestBodyJsonV200 | TransactionRequestBodyJsonV200 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (SANDBOX_TAN)
    api_response = api_instance.o_bpv2_1_0_create_transaction_request_sandbox_tan(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv2_1_0_create_transaction_request_sandbox_tan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyJsonV200**](TransactionRequestBodyJsonV200.md)| TransactionRequestBodyJsonV200 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON210**](TransactionRequestWithChargeJSON210.md)

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Get Accounts at all Banks (private)
    api_response = api_instance.o_bpv3_0_0_core_private_accounts_all_banks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_0_0_core_private_accounts_all_banks: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts Held
    api_response = api_instance.o_bpv3_0_0_get_accounts_held(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_0_0_get_accounts_held: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transactions for Account (Core)
    api_response = api_instance.o_bpv3_0_0_get_core_transactions_for_bank_account(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_0_0_get_core_transactions_for_bank_account: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank (IDs only)
    api_response = api_instance.o_bpv3_0_0_get_private_account_idsby_bank_id(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_0_0_get_private_account_idsby_bank_id: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts at Bank (Minimal)
    api_response = api_instance.o_bpv3_0_0_private_accounts_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_0_0_private_accounts_at_one_bank: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.PostConsentChallengeJsonV310() # PostConsentChallengeJsonV310 | PostConsentChallengeJsonV310 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Answer Consent Challenge
    api_response = api_instance.o_bpv3_1_0_answer_consent_challenge(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_1_0_answer_consent_challenge: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Check Available Funds
    api_response = api_instance.o_bpv3_1_0_check_funds_available(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_1_0_check_funds_available: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.PostConsentEmailJsonV310() # PostConsentEmailJsonV310 | PostConsentEmailJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Consent (EMAIL)
    api_response = api_instance.o_bpv3_1_0_create_consent_email(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_1_0_create_consent_email: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.PostConsentPhoneJsonV310() # PostConsentPhoneJsonV310 | PostConsentPhoneJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Consent (SMS)
    api_response = api_instance.o_bpv3_1_0_create_consent_sms(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_1_0_create_consent_sms: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Get JSON Web Key (JWK)
    api_response = api_instance.o_bpv3_1_0_get_server_jwk()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_1_0_get_server_jwk: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke Consent
    api_response = api_instance.o_bpv3_1_0_revoke_consent(consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv3_1_0_revoke_consent: %s\n" % e)
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

# **o_bpv4_0_0_answer_transaction_request_challenge**
> TransactionRequestWithChargeJSON210 o_bpv4_0_0_answer_transaction_request_challenge(body, transaction_request_id, transaction_request_type, view_id, account_id, bank_id)

Answer Transaction Request Challenge

<p>In Sandbox mode, any string that can be converted to a positive integer will be accepted as an answer.</p><p>This endpoint totally depends on createTransactionRequest, it need get the following data from createTransactionRequest response body.</p><p>1)<code>TRANSACTION_REQUEST_TYPE</code> : is the same as createTransactionRequest request URL .</p><p>2)<code>TRANSACTION_REQUEST_ID</code> : is the <code>id</code> field in createTransactionRequest response body.</p><p>3) <code>id</code> :  is <code>challenge.id</code> field in createTransactionRequest response body.</p><p>4) <code>answer</code> : must be <code>123</code> in case that Strong Customer Authentication method for OTP challenge is dummy.<br />For instance: SANDBOX_TAN_OTP_INSTRUCTION_TRANSPORT=dummy<br />Possible values are dummy,email and sms<br />In kafka mode, the answer can be got by phone message or other SCA methods.</p><p>Note that each Transaction Request Type can have its own OTP_INSTRUCTION_TRANSPORT method.<br />OTP_INSTRUCTION_TRANSPORT methods are set in Props. See sample.props.template for instructions.</p><p>Single or Multiple authorisations</p><p>OBP allows single or multi party authorisations.</p><p>Single party authorisation:</p><p>In the case that only one person needs to authorise i.e. answer a security challenge we have the following change of state of a <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED</p><p>Multiparty authorisation:</p><p>In the case that multiple parties (n persons) need to authorise a transaction request i.e. answer security challenges, we have the followings state flow for a <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in the case of a correct answer but the user is different than expected the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If Product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In the case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute, the default number of security challenges created is one.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.ChallengeAnswerJson400() # ChallengeAnswerJson400 | ChallengeAnswerJson400 object that needs to be added.
transaction_request_id = 'transaction_request_id_example' # str | The transaction request id
transaction_request_type = 'transaction_request_type_example' # str | The transaction request type
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Answer Transaction Request Challenge
    api_response = api_instance.o_bpv4_0_0_answer_transaction_request_challenge(body, transaction_request_id, transaction_request_type, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_answer_transaction_request_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChallengeAnswerJson400**](ChallengeAnswerJson400.md)| ChallengeAnswerJson400 object that needs to be added. | 
 **transaction_request_id** | **str**| The transaction request id | 
 **transaction_request_type** | **str**| The transaction request type | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON210**](TransactionRequestWithChargeJSON210.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_account**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_account(body, view_id, account_id, bank_id)

Create Transaction Request (ACCOUNT)

<p>When using ACCOUNT, the payee is set in the request body.</p><p>Money goes into the BANK_ID and ACCOUNT_ID specified in the request body.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyJsonV200() # TransactionRequestBodyJsonV200 | TransactionRequestBodyJsonV200 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (ACCOUNT)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyJsonV200**](TransactionRequestBodyJsonV200.md)| TransactionRequestBodyJsonV200 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_account_otp**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_account_otp(body, view_id, account_id, bank_id)

Create Transaction Request (ACCOUNT_OTP)

<p>When using ACCOUNT, the payee is set in the request body.</p><p>Money goes into the BANK_ID and ACCOUNT_ID specified in the request body.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyJsonV200() # TransactionRequestBodyJsonV200 | TransactionRequestBodyJsonV200 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (ACCOUNT_OTP)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_account_otp(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_account_otp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyJsonV200**](TransactionRequestBodyJsonV200.md)| TransactionRequestBodyJsonV200 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_card**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_card(body)

Create Transaction Request (CARD)

<p>When using CARD, the payee is set in the request body .</p><p>Money goes into the Counterparty in the request body.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyCardJsonV400() # TransactionRequestBodyCardJsonV400 | TransactionRequestBodyCardJsonV400 object that needs to be added.

try:
    # Create Transaction Request (CARD)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_card(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyCardJsonV400**](TransactionRequestBodyCardJsonV400.md)| TransactionRequestBodyCardJsonV400 object that needs to be added. | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_counterparty**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_counterparty(body, view_id, account_id, bank_id)

Create Transaction Request (COUNTERPARTY)

<p>Special instructions for COUNTERPARTY:</p><p>When using a COUNTERPARTY to create a Transaction Request, specificy the counterparty_id in the body of the request.<br />The routing details of the counterparty will be forwarded for the transfer.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyCounterpartyJSON() # TransactionRequestBodyCounterpartyJSON | TransactionRequestBodyCounterpartyJSON object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (COUNTERPARTY)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_counterparty(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyCounterpartyJSON**](TransactionRequestBodyCounterpartyJSON.md)| TransactionRequestBodyCounterpartyJSON object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_refund**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_refund(body, view_id, account_id, bank_id)

Create Transaction Request (REFUND)

<p>Either the <code>from</code> or the <code>to</code> field must be filled. Those fields refers to the information about the party that will be refunded.</p><p>In case the <code>from</code> object is used, it means that the refund comes from the part that sent you a transaction.<br />In the <code>from</code> object, you have two choices :<br />- Use <code>bank_id</code> and <code>account_id</code> fields if the other account is registered on the OBP-API<br />- Use the <code>counterparty_id</code> field in case the counterparty account is out of the OBP-API</p><p>In case the <code>to</code> object is used, it means you send a request to a counterparty to ask for a refund on a previous transaction you sent.<br />(This case is not managed by the OBP-API and require an external adapter)</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyRefundJsonV400() # TransactionRequestBodyRefundJsonV400 | TransactionRequestBodyRefundJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (REFUND)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_refund(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyRefundJsonV400**](TransactionRequestBodyRefundJsonV400.md)| TransactionRequestBodyRefundJsonV400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_sepa**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_sepa(body, view_id, account_id, bank_id)

Create Transaction Request (SEPA)

<p>Special instructions for SEPA:</p><p>When using a SEPA Transaction Request, you specify the IBAN of a Counterparty in the body of the request.<br />The routing details (IBAN) of the counterparty will be forwarded to the core banking system for the transfer.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodySEPAJsonV400() # TransactionRequestBodySEPAJsonV400 | TransactionRequestBodySEPAJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (SEPA)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_sepa(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_sepa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodySEPAJsonV400**](TransactionRequestBodySEPAJsonV400.md)| TransactionRequestBodySEPAJsonV400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_transaction_request_simple**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_simple(body, view_id, account_id, bank_id)

Create Transaction Request (SIMPLE)

<p>Special instructions for SIMPLE:</p><p>You can transfer money to the Bank Account Number or Iban directly.</p><p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodySimpleJsonV400() # TransactionRequestBodySimpleJsonV400 | TransactionRequestBodySimpleJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (SIMPLE)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_simple(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_create_transaction_request_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodySimpleJsonV400**](TransactionRequestBodySimpleJsonV400.md)| TransactionRequestBodySimpleJsonV400 object that needs to be added. | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON400**](TransactionRequestWithChargeJSON400.md)

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account Balances
    api_response = api_instance.o_bpv4_0_0_get_bank_account_balances(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_bank_account_balances: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Accounts Balances
    api_response = api_instance.o_bpv4_0_0_get_bank_accounts_balances(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_bank_accounts_balances: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Get Banks
    api_response = api_instance.o_bpv4_0_0_get_banks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_banks: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Consents Info
    api_response = api_instance.o_bpv4_0_0_get_consent_infos(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_consent_infos: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Consents
    api_response = api_instance.o_bpv4_0_0_get_consents(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_consents: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Account by Id (Core)
    api_response = api_instance.o_bpv4_0_0_get_core_account_by_id(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_core_account_by_id: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties for any account (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_counterparties_for_any_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_counterparties_for_any_account: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparties_for_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_explict_counterparties_for_account: %s\n" % e)
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

# **o_bpv4_0_0_get_explict_counterparty_by_id**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_get_explict_counterparty_by_id(counterparty_id, view_id, account_id, bank_id)

Get Counterparty by Id (Explicit)

<p>Information returned about the Counterparty specified by COUNTERPARTY_ID:</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by Id (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparty_by_id(counterparty_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_explict_counterparty_by_id: %s\n" % e)
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

# **o_bpv4_0_0_get_settlement_accounts**
> SettlementAccountsJson o_bpv4_0_0_get_settlement_accounts(bank_id)

Get Settlement accounts at Bank

<p>Get settlement accounts on this API instance<br />Returns a list of settlement accounts at this Bank</p><p>Note: a settlement account is considered as a bank account.<br />So you can update it and add account attributes to it using the regular account endpoints</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Settlement accounts at Bank
    api_response = api_instance.o_bpv4_0_0_get_settlement_accounts(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_settlement_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**SettlementAccountsJson**](SettlementAccountsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_transaction_request**
> TransactionRequestWithChargeJSON210 o_bpv4_0_0_get_transaction_request(transaction_request_id, view_id, account_id, bank_id)

Get Transaction Request.

<p>Returns transaction request for transaction specified by TRANSACTION_REQUEST_ID and for account specified by ACCOUNT_ID at bank specified by BANK_ID.</p><p>The VIEW_ID specified must be 'owner' and the user must have access to this view.</p><p>Version 2.0.0 now returns charge information.</p><p>Transaction Requests serve to initiate transactions that may or may not proceed. They contain information including:</p><ul><li>Transaction Request Id</li><li>Type</li><li>Status (INITIATED, COMPLETED)</li><li>Challenge (in order to confirm the request)</li><li>From Bank / Account</li><li>Details including Currency, Value, Description and other initiation information specific to each type. (Could potentialy include a list of future transactions.)</li><li>Related Transactions</li></ul><p>PSD2 Context: PSD2 requires transparency of charges to the customer.<br />This endpoint provides the charge that would be applied if the Transaction Request proceeds - and a record of that charge there after.<br />The customer can proceed with the Transaction by answering the security challenge.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
transaction_request_id = 'transaction_request_id_example' # str | The transaction request id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Request.
    api_response = api_instance.o_bpv4_0_0_get_transaction_request(transaction_request_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv4_0_0_get_transaction_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_request_id** | **str**| The transaction request id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSON210**](TransactionRequestWithChargeJSON210.md)

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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Create Consent By CONSENT_REQUEST_ID (EMAIL)
    api_response = api_instance.o_bpv5_0_0_create_consent_by_consent_request_id_email()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv5_0_0_create_consent_by_consent_request_id_email: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Create Consent By CONSENT_REQUEST_ID (SMS)
    api_response = api_instance.o_bpv5_0_0_create_consent_by_consent_request_id_sms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv5_0_0_create_consent_by_consent_request_id_sms: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
body = obp_python.PostConsentRequestJsonV500() # PostConsentRequestJsonV500 | PostConsentRequestJsonV500 object that needs to be added.

try:
    # Create Consent Request
    api_response = api_instance.o_bpv5_0_0_create_consent_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv5_0_0_create_consent_request: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank
    api_response = api_instance.o_bpv5_0_0_get_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv5_0_0_get_bank: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Get Consent By Consent Request Id
    api_response = api_instance.o_bpv5_0_0_get_consent_by_consent_request_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv5_0_0_get_consent_by_consent_request_id: %s\n" % e)
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
api_instance = obp_python.PSD2Api(obp_python.ApiClient(configuration))

try:
    # Get Consent Request
    api_response = api_instance.o_bpv5_0_0_get_consent_request()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PSD2Api->o_bpv5_0_0_get_consent_request: %s\n" % e)
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

