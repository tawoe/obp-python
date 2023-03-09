# obp_python.AccountFirehoseApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_0_0_get_firehose_transactions_for_bank_account**](AccountFirehoseApi.md#o_bpv3_0_0_get_firehose_transactions_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/firehose/accounts/{ACCOUNT_ID}/views/{VIEW_ID}/transactions | Get Firehose Transactions for Account
[**o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank**](AccountFirehoseApi.md#o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/fast-firehose/accounts | Get Fast Firehose Accounts at Bank
[**o_bpv4_0_0_get_firehose_accounts_at_one_bank**](AccountFirehoseApi.md#o_bpv4_0_0_get_firehose_accounts_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/firehose/accounts/views/{VIEW_ID} | Get Firehose Accounts at Bank


# **o_bpv3_0_0_get_firehose_transactions_for_bank_account**
> TransactionsJsonV300 o_bpv3_0_0_get_firehose_transactions_for_bank_account(view_id, account_id, bank_id)

Get Firehose Transactions for Account

<p>Get Transactions for an Account that has a firehose View.</p><p>Allows bulk access to an account's transactions.<br />User must have the CanUseFirehoseAtAnyBank Role</p><p>To find ACCOUNT_IDs, use the getFirehoseAccountsAtOneBank call.</p><p>For VIEW_ID try 'owner'</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>from_date=DATE =&gt; example value: 1970-01-01T00:00:00.000Z. NOTE! The default value is one year ago (1970-01-01T00:00:00.000Z).</li><li>to_date=DATE =&gt; example value: 2023-02-16T16:23:47.662Z. NOTE! The default value is now (2023-02-16T16:23:47.662Z).</li></ul><p>Date format parameter: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'(1100-01-01T01:01:01.000Z) ==&gt; time zone is UTC.</p><p>eg3:?sort_direction=ASC&amp;limit=100&amp;offset=0&amp;from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AccountFirehoseApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Firehose Transactions for Account
    api_response = api_instance.o_bpv3_0_0_get_firehose_transactions_for_bank_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountFirehoseApi->o_bpv3_0_0_get_firehose_transactions_for_bank_account: %s\n" % e)
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
api_instance = obp_python.AccountFirehoseApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Fast Firehose Accounts at Bank
    api_response = api_instance.o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountFirehoseApi->o_bpv4_0_0_get_fast_firehose_accounts_at_one_bank: %s\n" % e)
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
api_instance = obp_python.AccountFirehoseApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Firehose Accounts at Bank
    api_response = api_instance.o_bpv4_0_0_get_firehose_accounts_at_one_bank(view_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountFirehoseApi->o_bpv4_0_0_get_firehose_accounts_at_one_bank: %s\n" % e)
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

