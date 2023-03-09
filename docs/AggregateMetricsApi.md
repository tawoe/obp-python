# obp_python.AggregateMetricsApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_0_0_get_aggregate_metrics**](AggregateMetricsApi.md#o_bpv3_0_0_get_aggregate_metrics) | **GET** /obp/v5.0.0/management/aggregate-metrics | Get Aggregate Metrics


# **o_bpv3_0_0_get_aggregate_metrics**
> AggregateMetricJSON o_bpv3_0_0_get_aggregate_metrics()

Get Aggregate Metrics

<p>Returns aggregate metrics on api usage eg. total count, response time (in ms), etc.</p><p>Should be able to filter on the following fields</p><p>eg: /management/aggregate-metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;consumer_id=5<br />&amp;user_id=66214b8e-259e-44ad-8868-3eb47be70646&amp;implemented_by_partial_function=getTransactionsForBankAccount<br />&amp;implemented_in_version=v3.0.0&amp;url=/obp/v3.0.0/banks/gh.29.uk/accounts/8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0/owner/transactions<br />&amp;verb=GET&amp;anon=false&amp;app_name=MapperPostman<br />&amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>1 from_date (defaults to the day before the current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to the current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 consumer_id  (if null ignore)</p><p>4 user_id (if null ignore)</p><p>5 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>6 url (if null ignore), note: can not contain '&amp;'.</p><p>7 app_name (if null ignore)</p><p>8 implemented_by_partial_function (if null ignore),</p><p>9 implemented_in_version (if null ignore)</p><p>10 verb (if null ignore)</p><p>11 correlation_id (if null ignore)</p><p>12 duration (if null ignore) non digit chars will be silently omitted</p><p>13 exclude_app_names (if null ignore).eg: &amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>14 exclude_url_patterns (if null ignore).you can design you own SQL NOT LIKE pattern. eg: &amp;exclude_url_patterns=%management/metrics%,%management/aggregate-metrics%</p><p>15 exclude_implemented_by_partial_functions (if null ignore).eg: &amp;exclude_implemented_by_partial_functions=getMetrics,getConnectorMetrics,getAggregateMetrics</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.AggregateMetricsApi(obp_python.ApiClient(configuration))

try:
    # Get Aggregate Metrics
    api_response = api_instance.o_bpv3_0_0_get_aggregate_metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregateMetricsApi->o_bpv3_0_0_get_aggregate_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AggregateMetricJSON**](AggregateMetricJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

