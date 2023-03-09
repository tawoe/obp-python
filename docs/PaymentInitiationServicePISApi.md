# obp_python.PaymentInitiationServicePISApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_4_0_get_transaction_request_types**](PaymentInitiationServicePISApi.md#o_bpv1_4_0_get_transaction_request_types) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types | Get Transaction Request Types for Account
[**o_bpv2_1_0_create_transaction_request_sandbox_tan**](PaymentInitiationServicePISApi.md#o_bpv2_1_0_create_transaction_request_sandbox_tan) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/SANDBOX_TAN/transaction-requests | Create Transaction Request (SANDBOX_TAN)
[**o_bpv3_1_0_get_transaction_requests**](PaymentInitiationServicePISApi.md#o_bpv3_1_0_get_transaction_requests) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-requests | Get Transaction Requests.
[**o_bpv4_0_0_answer_transaction_request_challenge**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_answer_transaction_request_challenge) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/{TRANSACTION_REQUEST_TYPE}/transaction-requests/{TRANSACTION_REQUEST_ID}/challenge | Answer Transaction Request Challenge
[**o_bpv4_0_0_create_transaction_request_account**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_account) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/ACCOUNT/transaction-requests | Create Transaction Request (ACCOUNT)
[**o_bpv4_0_0_create_transaction_request_account_otp**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_account_otp) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/ACCOUNT_OTP/transaction-requests | Create Transaction Request (ACCOUNT_OTP)
[**o_bpv4_0_0_create_transaction_request_card**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_card) | **POST** /obp/v5.0.0/transaction-request-types/CARD/transaction-requests | Create Transaction Request (CARD)
[**o_bpv4_0_0_create_transaction_request_counterparty**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_counterparty) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/COUNTERPARTY/transaction-requests | Create Transaction Request (COUNTERPARTY)
[**o_bpv4_0_0_create_transaction_request_free_form**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_free_form) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/FREE_FORM/transaction-requests | Create Transaction Request (FREE_FORM)
[**o_bpv4_0_0_create_transaction_request_refund**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_refund) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/REFUND/transaction-requests | Create Transaction Request (REFUND)
[**o_bpv4_0_0_create_transaction_request_sepa**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_sepa) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/SEPA/transaction-requests | Create Transaction Request (SEPA)
[**o_bpv4_0_0_create_transaction_request_simple**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_create_transaction_request_simple) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-request-types/SIMPLE/transaction-requests | Create Transaction Request (SIMPLE)
[**o_bpv4_0_0_get_counterparties_for_any_account**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_get_counterparties_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties for any account (Explicit)
[**o_bpv4_0_0_get_explict_counterparties_for_account**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_get_explict_counterparties_for_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties (Explicit)
[**o_bpv4_0_0_get_explict_counterparty_by_id**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_get_explict_counterparty_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Get Counterparty by Id (Explicit)
[**o_bpv4_0_0_get_transaction_request**](PaymentInitiationServicePISApi.md#o_bpv4_0_0_get_transaction_request) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transaction-requests/{TRANSACTION_REQUEST_ID} | Get Transaction Request.


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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Request Types for Account
    api_response = api_instance.o_bpv1_4_0_get_transaction_request_types(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv1_4_0_get_transaction_request_types: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyJsonV200() # TransactionRequestBodyJsonV200 | TransactionRequestBodyJsonV200 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (SANDBOX_TAN)
    api_response = api_instance.o_bpv2_1_0_create_transaction_request_sandbox_tan(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv2_1_0_create_transaction_request_sandbox_tan: %s\n" % e)
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

# **o_bpv3_1_0_get_transaction_requests**
> TransactionRequestWithChargeJSONs210 o_bpv3_1_0_get_transaction_requests(view_id, account_id, bank_id)

Get Transaction Requests.

<p>Returns transaction requests for account specified by ACCOUNT_ID at bank specified by BANK_ID.</p><p>The VIEW_ID specified must be 'owner' and the user must have access to this view.</p><p>Version 2.0.0 now returns charge information.</p><p>Transaction Requests serve to initiate transactions that may or may not proceed. They contain information including:</p><ul><li>Transaction Request Id</li><li>Type</li><li>Status (INITIATED, COMPLETED)</li><li>Challenge (in order to confirm the request)</li><li>From Bank / Account</li><li>Details including Currency, Value, Description and other initiation information specific to each type. (Could potentialy include a list of future transactions.)</li><li>Related Transactions</li></ul><p>PSD2 Context: PSD2 requires transparency of charges to the customer.<br />This endpoint provides the charge that would be applied if the Transaction Request proceeds - and a record of that charge there after.<br />The customer can proceed with the Transaction by answering the security challenge.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Requests.
    api_response = api_instance.o_bpv3_1_0_get_transaction_requests(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv3_1_0_get_transaction_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionRequestWithChargeJSONs210**](TransactionRequestWithChargeJSONs210.md)

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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
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
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_answer_transaction_request_challenge: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyJsonV200() # TransactionRequestBodyJsonV200 | TransactionRequestBodyJsonV200 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (ACCOUNT)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_account: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyJsonV200() # TransactionRequestBodyJsonV200 | TransactionRequestBodyJsonV200 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (ACCOUNT_OTP)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_account_otp(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_account_otp: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyCardJsonV400() # TransactionRequestBodyCardJsonV400 | TransactionRequestBodyCardJsonV400 object that needs to be added.

try:
    # Create Transaction Request (CARD)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_card(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_card: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyCounterpartyJSON() # TransactionRequestBodyCounterpartyJSON | TransactionRequestBodyCounterpartyJSON object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (COUNTERPARTY)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_counterparty(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_counterparty: %s\n" % e)
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

# **o_bpv4_0_0_create_transaction_request_free_form**
> TransactionRequestWithChargeJSON400 o_bpv4_0_0_create_transaction_request_free_form(body, view_id, account_id, bank_id)

Create Transaction Request (FREE_FORM)

<p>Initiate a Payment via creating a Transaction Request.</p><p>In OBP, a <code>transaction request</code> may or may not result in a <code>transaction</code>. However, a <code>transaction</code> only has one possible state: completed.</p><p>A <code>Transaction Request</code> can have one of several states: INITIATED, NEXT_CHALLENGE_PENDING etc.</p><p><code>Transactions</code> are modeled on items in a bank statement that represent the movement of money.</p><p><code>Transaction Requests</code> are requests to move money which may or may not succeed and thus result in a <code>Transaction</code>.</p><p>A <code>Transaction Request</code> might create a security challenge that needs to be answered before the <code>Transaction Request</code> proceeds.<br />In case 1 person needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; COMPLETED<br />In case n persons needs to answer security challenge we have next flow of state of an <code>transaction request</code>:<br />INITIATED =&gt; NEXT_CHALLENGE_PENDING =&gt; ... =&gt; NEXT_CHALLENGE_PENDING =&gt; COMPLETED</p><p>The security challenge is bound to a user i.e. in case of right answer and the user is different than expected one the challenge will fail.</p><p>Rule for calculating number of security challenges:<br />If product Account attribute REQUIRED_CHALLENGE_ANSWERS=N then create N challenges<br />(one for every user that has a View where permission &quot;can_add_transaction_request_to_any_account&quot;=true)<br />In case REQUIRED_CHALLENGE_ANSWERS is not defined as an account attribute default value is 1.</p><p>Transaction Requests contain charge information giving the client the opportunity to proceed or not (as long as the challenge level is appropriate).</p><p>Transaction Requests can have one of several Transaction Request Types which expect different bodies. The escaped body is returned in the details key of the GET response.<br />This provides some commonality and one URL for many different payment or transfer types with enough flexibility to validate them differently.</p><p>The payer is set in the URL. Money comes out of the BANK_ID and ACCOUNT_ID specified in the URL.</p><p>In sandbox mode, TRANSACTION_REQUEST_TYPE is commonly set to ACCOUNT. See getTransactionRequestTypesSupportedByBank for all supported types.</p><p>In sandbox mode, if the amount is less than 1000 EUR (any currency, unless it is set differently on this server), the transaction request will create a transaction without a challenge, else the Transaction Request will be set to INITIALISED and a challenge will need to be answered.</p><p>If a challenge is created you must answer it using Answer Transaction Request Challenge before the Transaction is created.</p><p>You can transfer between different currency accounts. (new in 2.0.0). The currency in body must match the sending account.</p><p>The following static FX rates are available in sandbox mode:</p><p><a href=\"https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate\">https://test-explorer.openbankproject.com/more?version=OBPv4.0.0&amp;list-all-banks=false&amp;core=&amp;psd2=&amp;obwg=#OBPv2_2_0-getCurrentFxRate</a></p><p>Transaction Requests satisfy PSD2 requirements thus:</p><p>1) A transaction can be initiated by a third party application.</p><p>2) The customer is informed of the charge that will incurred.</p><p>3) The call supports delegated authentication (OAuth)</p><p>See <a href=\"https://github.com/OpenBankProject/Hello-OBP-DirectLogin-Python/blob/master/hello_payments.py\">this python code</a> for a complete example of this flow.</p><p>There is further documentation <a href=\"https://github.com/OpenBankProject/OBP-API/wiki/Transaction-Requests\">here</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyFreeFormJSON() # TransactionRequestBodyFreeFormJSON | TransactionRequestBodyFreeFormJSON object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (FREE_FORM)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_free_form(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_free_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionRequestBodyFreeFormJSON**](TransactionRequestBodyFreeFormJSON.md)| TransactionRequestBodyFreeFormJSON object that needs to be added. | 
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodyRefundJsonV400() # TransactionRequestBodyRefundJsonV400 | TransactionRequestBodyRefundJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (REFUND)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_refund(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_refund: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodySEPAJsonV400() # TransactionRequestBodySEPAJsonV400 | TransactionRequestBodySEPAJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (SEPA)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_sepa(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_sepa: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionRequestBodySimpleJsonV400() # TransactionRequestBodySimpleJsonV400 | TransactionRequestBodySimpleJsonV400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Transaction Request (SIMPLE)
    api_response = api_instance.o_bpv4_0_0_create_transaction_request_simple(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_create_transaction_request_simple: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties for any account (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_counterparties_for_any_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_get_counterparties_for_any_account: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparties_for_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_get_explict_counterparties_for_account: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by Id (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparty_by_id(counterparty_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_get_explict_counterparty_by_id: %s\n" % e)
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
api_instance = obp_python.PaymentInitiationServicePISApi(obp_python.ApiClient(configuration))
transaction_request_id = 'transaction_request_id_example' # str | The transaction request id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Request.
    api_response = api_instance.o_bpv4_0_0_get_transaction_request(transaction_request_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentInitiationServicePISApi->o_bpv4_0_0_get_transaction_request: %s\n" % e)
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

