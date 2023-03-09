# obp_python.MetricApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_0_0_elastic_search_metrics**](MetricApi.md#o_bpv2_0_0_elastic_search_metrics) | **GET** /obp/v5.0.0/search/metrics | Search API Metrics via Elasticsearch
[**o_bpv2_1_0_get_metrics**](MetricApi.md#o_bpv2_1_0_get_metrics) | **GET** /obp/v5.0.0/management/metrics | Get Metrics
[**o_bpv2_2_0_get_connector_metrics**](MetricApi.md#o_bpv2_2_0_get_connector_metrics) | **GET** /obp/v5.0.0/management/connector/metrics | Get Connector Metrics
[**o_bpv3_0_0_get_aggregate_metrics**](MetricApi.md#o_bpv3_0_0_get_aggregate_metrics) | **GET** /obp/v5.0.0/management/aggregate-metrics | Get Aggregate Metrics
[**o_bpv3_1_0_get_metrics_top_consumers**](MetricApi.md#o_bpv3_1_0_get_metrics_top_consumers) | **GET** /obp/v5.0.0/management/metrics/top-consumers | Get Top Consumers
[**o_bpv3_1_0_get_top_apis**](MetricApi.md#o_bpv3_1_0_get_top_apis) | **GET** /obp/v5.0.0/management/metrics/top-apis | Get Top APIs
[**o_bpv5_0_0_get_metrics_at_bank**](MetricApi.md#o_bpv5_0_0_get_metrics_at_bank) | **GET** /obp/v5.0.0/management/metrics/banks/{BANK_ID} | Get Metrics at Bank


# **o_bpv2_0_0_elastic_search_metrics**
> EmptyClassJson o_bpv2_0_0_elastic_search_metrics(body)

Search API Metrics via Elasticsearch

<p>Search the API calls made to this API instance via Elastic Search.</p><p>Login is required.</p><p>CanSearchMetrics entitlement is required to search metrics data.</p><p>parameters:</p><p>esType  - elasticsearch type</p><p>simple query:</p><p>q       - plain_text_query</p><p>df      - default field to search</p><p>sort    - field to sort on</p><p>size    - number of hits returned, default 10</p><p>from    - show hits starting from</p><p>json query:</p><p>source  - JSON_query_(URL-escaped)</p><p>example usage:</p><p>/search/metrics/q=findThis</p><p>or:</p><p>/search/metrics/source={&quot;query&quot;:{&quot;query_string&quot;:{&quot;query&quot;:&quot;findThis&quot;}}}</p><p>Note!!</p><p>The whole JSON query string MUST be URL-encoded:</p><ul><li>For {  use %7B</li><li>For }  use %7D</li><li>For : use %3A</li><li>For &quot; use %22</li></ul><p>etc..</p><p>Only q, source and esType are passed to Elastic</p><p>Elastic simple query: <a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/search-uri-request.html\">https://www.elastic.co/guide/en/elasticsearch/reference/current/search-uri-request.html</a></p><p>Elastic JSON query: <a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html\">https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Search API Metrics via Elasticsearch
    api_response = api_instance.o_bpv2_0_0_elastic_search_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv2_0_0_elastic_search_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_1_0_get_metrics**
> MetricsJson o_bpv2_1_0_get_metrics(body)

Get Metrics

<p>Get the all metrics</p><p>require CanReadMetrics role</p><p>Filters Part 1.<em>filtering</em> (no wilde cards etc.) parameters to GET /management/metrics</p><p>Should be able to filter on the following metrics fields</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=50&amp;offset=2</p><p>1 from_date (defaults to one week before current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 limit (for pagination: defaults to 50)  eg:limit=200</p><p>4 offset (for pagination: zero index, defaults to 0) eg: offset=10</p><p>5 sort_by (defaults to date field) eg: sort_by=date<br />possible values:<br />&quot;url&quot;,<br />&quot;date&quot;,<br />&quot;user_name&quot;,<br />&quot;app_name&quot;,<br />&quot;developer_email&quot;,<br />&quot;implemented_by_partial_function&quot;,<br />&quot;implemented_in_version&quot;,<br />&quot;consumer_id&quot;,<br />&quot;verb&quot;</p><p>6 direction (defaults to date desc) eg: direction=desc</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:<a href=\"&#109;&#97;&#x69;&#108;&#x74;&#x6f;&#x3a;&#48;&#49;.&#48;&#48;&#x30;&#90;&#38;&#108;&#105;m&#x69;&#x74;&#x3d;&#x31;&#48;&#x30;&#x30;&#x30;&#38;o&#x66;&#102;&#x73;&#101;&#116;&#61;0&amp;a&#110;&#111;&#x6e;=&#x66;&#97;l&#115;&#x65;&amp;ap&#112;&#95;&#110;&#97;m&#x65;&#61;&#84;&#101;a&#116;A&#x70;&#112;&#38;&#105;&#x6d;&#x70;l&#101;&#x6d;e&#110;&#116;e&#x64;&#x5f;&#x69;&#x6e;&#x5f;v&#x65;&#114;s&#x69;&#x6f;&#x6e;&#x3d;&#118;2.&#49;.&#x30;&#x26;&#x76;&#101;&#x72;&#98;&#x3d;&#80;O&#x53;&#84;&#38;&#117;&#115;e&#114;_i&#x64;&#x3d;&#x63;&#x37;&#x62;6c&#x62;&#x34;7-&#99;&#98;&#57;&#x36;&#45;&#x34;&#52;&#52;&#x31;-8&#56;&#48;1&#x2d;&#x33;5&#x62;&#53;&#55;45&#x36;&#x37;&#x35;&#x33;&#x61;&#x26;&#117;&#115;&#x65;r&#95;n&#97;me&#61;s&#117;&#115;&#97;&#110;&#46;&#117;&#107;&#x2e;&#50;&#x39;@&#x65;&#120;&#97;&#109;&#112;l&#101;&#x2e;&#99;o&#109;\">&#x30;1.0&#x30;&#48;Z&#x26;&#x6c;i&#x6d;&#x69;&#116;&#61;&#x31;&#48;&#x30;0&#x30;&#38;&#x6f;&#x66;&#x66;&#x73;&#x65;&#116;&#x3d;&#x30;&#x26;&#x61;&#x6e;&#x6f;&#110;&#x3d;f&#x61;&#x6c;&#x73;e&amp;&#x61;&#x70;p&#x5f;n&#97;&#x6d;e&#61;&#84;&#101;&#97;&#x74;&#65;&#x70;&#x70;&#38;&#x69;&#x6d;&#112;&#x6c;&#x65;&#x6d;&#101;&#110;&#x74;ed&#x5f;&#105;&#x6e;&#x5f;v&#x65;&#x72;&#x73;&#x69;&#x6f;&#x6e;&#61;&#x76;2&#x2e;&#x31;&#x2e;&#x30;&#38;&#118;er&#x62;=&#80;&#79;S&#x54;&#38;&#117;&#115;&#101;&#114;&#x5f;i&#x64;&#x3d;&#x63;&#x37;&#x62;&#54;c&#98;&#x34;7&#x2d;&#99;&#x62;&#57;&#54;&#45;4&#52;&#x34;&#49;&#x2d;&#x38;&#x38;&#x30;&#49;&#45;&#x33;&#x35;&#x62;&#x35;7&#52;&#x35;67&#53;&#51;a&#x26;&#117;&#115;&#101;&#x72;_&#110;&#97;&#x6d;&#101;&#x3d;&#x73;&#x75;s&#x61;&#x6e;&#x2e;&#117;&#107;&#46;29&#64;&#101;&#120;&#97;&#109;&#112;&#x6c;&#101;&#46;&#99;o&#109;</a>&amp;consumer_id=78</p><p>Other filters:</p><p>7 consumer_id  (if null ignore)</p><p>8 user_id (if null ignore)</p><p>9 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>10 url (if null ignore), note: can not contain '&amp;'.</p><p>11 app_name (if null ignore)</p><p>12 implemented_by_partial_function (if null ignore),</p><p>13 implemented_in_version (if null ignore)</p><p>14 verb (if null ignore)</p><p>15 correlation_id (if null ignore)</p><p>16 duration (if null ignore) non digit chars will be silently omitted</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Metrics
    api_response = api_instance.o_bpv2_1_0_get_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv2_1_0_get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**MetricsJson**](MetricsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_2_0_get_connector_metrics**
> ConnectorMetricsJson o_bpv2_2_0_get_connector_metrics(body)

Get Connector Metrics

<p>Get the all metrics</p><p>require CanGetConnectorMetrics role</p><p>Filters Part 1.<em>filtering</em> (no wilde cards etc.) parameters to GET /management/connector/metrics</p><p>Should be able to filter on the following metrics fields</p><p>eg: /management/connector/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=50&amp;offset=2</p><p>1 from_date (defaults to one week before current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 limit (for pagination: defaults to 1000)  eg:limit=2000</p><p>4 offset (for pagination: zero index, defaults to 0) eg: offset=10</p><p>eg: /management/connector/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=100&amp;offset=300</p><p>Other filters:</p><p>5 connector_name  (if null ignore)</p><p>6 function_name (if null ignore)</p><p>7 correlation_id (if null ignore)</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Connector Metrics
    api_response = api_instance.o_bpv2_2_0_get_connector_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv2_2_0_get_connector_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**ConnectorMetricsJson**](ConnectorMetricsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))

try:
    # Get Aggregate Metrics
    api_response = api_instance.o_bpv3_0_0_get_aggregate_metrics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv3_0_0_get_aggregate_metrics: %s\n" % e)
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

# **o_bpv3_1_0_get_metrics_top_consumers**
> TopConsumersJson o_bpv3_1_0_get_metrics_top_consumers()

Get Top Consumers

<p>Get metrics about the top consumers of the API usage e.g. total count, consumer_id and app_name.</p><p>Should be able to filter on the following fields</p><p>e.g.: /management/metrics/top-consumers?from_date=1970-01-01T00:00:00.000Z&amp;to_date=2023-02-16T16:23:47.687Z&amp;consumer_id=5<br />&amp;user_id=66214b8e-259e-44ad-8868-3eb47be70646&amp;implemented_by_partial_function=getTransactionsForBankAccount<br />&amp;implemented_in_version=v3.0.0&amp;url=/obp/v3.0.0/banks/gh.29.uk/accounts/8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0/owner/transactions<br />&amp;verb=GET&amp;anon=false&amp;app_name=MapperPostman<br />&amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null<br />&amp;limit=100</p><p>1 from_date (defaults to the one year ago): eg:from_date=1970-01-01T00:00:00.000Z</p><p>2 to_date (defaults to the current date) eg:to_date=2023-02-16T16:23:47.687Z</p><p>3 consumer_id  (if null ignore)</p><p>4 user_id (if null ignore)</p><p>5 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>6 url (if null ignore), note: can not contain '&amp;'.</p><p>7 app_name (if null ignore)</p><p>8 implemented_by_partial_function (if null ignore),</p><p>9 implemented_in_version (if null ignore)</p><p>10 verb (if null ignore)</p><p>11 correlation_id (if null ignore)</p><p>12 duration (if null ignore) non digit chars will be silently omitted</p><p>13 exclude_app_names (if null ignore).eg: &amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>14 exclude_url_patterns (if null ignore).you can design you own SQL NOT LIKE pattern. eg: &amp;exclude_url_patterns=%management/metrics%,%management/aggregate-metrics%</p><p>15 exclude_implemented_by_partial_functions (if null ignore).eg: &amp;exclude_implemented_by_partial_functions=getMetrics,getConnectorMetrics,getAggregateMetrics</p><p>16 limit (for pagination: defaults to 50)  eg:limit=200</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))

try:
    # Get Top Consumers
    api_response = api_instance.o_bpv3_1_0_get_metrics_top_consumers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv3_1_0_get_metrics_top_consumers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TopConsumersJson**](TopConsumersJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_top_apis**
> TopApisJson o_bpv3_1_0_get_top_apis()

Get Top APIs

<p>Get metrics about the most popular APIs. e.g.: total count, response time (in ms), etc.</p><p>Should be able to filter on the following fields</p><p>eg: /management/metrics/top-apis?from_date=1970-01-01T00:00:00.000Z&amp;to_date=2023-02-16T16:23:47.686Z&amp;consumer_id=5<br />&amp;user_id=66214b8e-259e-44ad-8868-3eb47be70646&amp;implemented_by_partial_function=getTransactionsForBankAccount<br />&amp;implemented_in_version=v3.0.0&amp;url=/obp/v3.0.0/banks/gh.29.uk/accounts/8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0/owner/transactions<br />&amp;verb=GET&amp;anon=false&amp;app_name=MapperPostman<br />&amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>1 from_date (defaults to the one year ago): eg:from_date=1970-01-01T00:00:00.000Z</p><p>2 to_date (defaults to the current date) eg:to_date=2023-02-16T16:23:47.686Z</p><p>3 consumer_id  (if null ignore)</p><p>4 user_id (if null ignore)</p><p>5 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>6 url (if null ignore), note: can not contain '&amp;'.</p><p>7 app_name (if null ignore)</p><p>8 implemented_by_partial_function (if null ignore),</p><p>9 implemented_in_version (if null ignore)</p><p>10 verb (if null ignore)</p><p>11 correlation_id (if null ignore)</p><p>12 duration (if null ignore) non digit chars will be silently omitted</p><p>13 exclude_app_names (if null ignore).eg: &amp;exclude_app_names=API-EXPLORER,API-Manager,SOFI,null</p><p>14 exclude_url_patterns (if null ignore).you can design you own SQL NOT LIKE pattern. eg: &amp;exclude_url_patterns=%management/metrics%,%management/aggregate-metrics%</p><p>15 exclude_implemented_by_partial_functions (if null ignore).eg: &amp;exclude_implemented_by_partial_functions=getMetrics,getConnectorMetrics,getAggregateMetrics</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))

try:
    # Get Top APIs
    api_response = api_instance.o_bpv3_1_0_get_top_apis()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv3_1_0_get_top_apis: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TopApisJson**](TopApisJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_metrics_at_bank**
> MetricsJson o_bpv5_0_0_get_metrics_at_bank(bank_id)

Get Metrics at Bank

<p>Get the all metrics at the Bank specified by BANK_ID</p><p>require CanReadMetrics role</p><p>Filters Part 1.<em>filtering</em> (no wilde cards etc.) parameters to GET /management/metrics</p><p>Should be able to filter on the following metrics fields</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=50&amp;offset=2</p><p>1 from_date (defaults to one week before current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 limit (for pagination: defaults to 50)  eg:limit=200</p><p>4 offset (for pagination: zero index, defaults to 0) eg: offset=10</p><p>5 sort_by (defaults to date field) eg: sort_by=date<br />possible values:<br />&quot;url&quot;,<br />&quot;date&quot;,<br />&quot;user_name&quot;,<br />&quot;app_name&quot;,<br />&quot;developer_email&quot;,<br />&quot;implemented_by_partial_function&quot;,<br />&quot;implemented_in_version&quot;,<br />&quot;consumer_id&quot;,<br />&quot;verb&quot;</p><p>6 direction (defaults to date desc) eg: direction=desc</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:<a href=\"&#109;&#97;&#105;&#x6c;&#x74;&#x6f;&#58;&#x30;&#49;&#x2e;&#48;&#48;&#x30;&#x5a;&amp;&#108;&#x69;&#x6d;&#x69;&#x74;&#61;&#49;&#48;&#x30;&#x30;&#48;&#38;&#111;&#x66;&#102;&#x73;&#101;t&#x3d;&#48;&#x26;&#x61;no&#110;&#61;&#x66;&#97;&#x6c;&#115;&#x65;&#38;&#97;&#112;&#x70;&#x5f;&#110;&#x61;&#109;&#x65;&#x3d;&#84;&#101;&#97;&#x74;&#x41;p&#112;&amp;&#105;&#109;&#112;l&#x65;&#x6d;&#101;&#x6e;&#116;&#101;&#100;_&#105;n&#95;v&#101;&#114;&#115;&#x69;&#111;n&#x3d;&#x76;&#x32;&#x2e;&#49;&#x2e;&#48;&#38;&#118;&#101;&#114;&#98;&#x3d;&#80;&#79;&#83;T&amp;&#117;&#x73;&#x65;&#x72;&#x5f;&#105;d=&#x63;&#x37;&#x62;&#x36;&#x63;&#98;&#52;&#x37;&#45;c&#x62;&#57;&#54;&#x2d;&#52;&#52;&#x34;1&#x2d;88&#48;&#x31;&#45;&#51;5&#x62;5&#x37;4&#x35;&#54;&#55;&#53;&#x33;&#97;&#x26;&#117;&#115;&#x65;&#x72;_&#x6e;&#97;&#x6d;&#101;&#61;s&#117;&#x73;a&#x6e;&#x2e;&#117;&#x6b;&#46;&#x32;&#x39;&#x40;e&#120;a&#x6d;p&#x6c;&#x65;&#x2e;&#x63;&#x6f;m\">&#48;&#x31;&#46;&#48;&#48;&#x30;&#90;&#38;&#108;&#105;&#x6d;i&#x74;=1&#x30;&#x30;0&#48;&#x26;&#111;&#102;&#102;&#x73;&#101;&#116;&#x3d;&#x30;&#x26;a&#110;&#111;n&#61;f&#x61;l&#x73;&#101;&#x26;&#97;&#x70;p&#95;n&#x61;&#109;e&#x3d;&#x54;&#x65;&#97;&#x74;&#65;p&#112;&#38;&#105;&#109;p&#x6c;&#101;&#109;e&#110;&#x74;&#x65;&#x64;&#95;&#x69;&#110;&#95;&#118;er&#115;&#x69;o&#x6e;&#61;&#118;2&#46;1&#x2e;&#48;&#38;&#118;&#x65;r&#x62;&#61;&#80;OS&#x54;&#x26;&#117;&#115;&#101;r&#x5f;&#105;d&#x3d;&#99;&#55;&#98;&#54;cb&#52;7&#x2d;&#99;&#x62;9&#54;&#x2d;&#x34;&#52;&#52;&#x31;&#45;8&#56;&#48;&#49;&#45;&#x33;5&#98;&#x35;&#x37;&#52;56&#x37;5&#51;a&amp;&#117;&#x73;&#x65;&#114;&#x5f;&#110;a&#x6d;&#x65;&#x3d;&#x73;&#x75;&#115;&#97;&#x6e;.&#x75;&#x6b;.29&#64;&#101;&#120;&#97;&#x6d;&#x70;l&#101;&#46;&#x63;&#x6f;&#109;</a>&amp;consumer_id=78</p><p>Other filters:</p><p>7 consumer_id  (if null ignore)</p><p>8 user_id (if null ignore)</p><p>9 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>10 url (if null ignore), note: can not contain '&amp;'.</p><p>11 app_name (if null ignore)</p><p>12 implemented_by_partial_function (if null ignore),</p><p>13 implemented_in_version (if null ignore)</p><p>14 verb (if null ignore)</p><p>15 correlation_id (if null ignore)</p><p>16 duration (if null ignore) non digit chars will be silently omitted</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MetricApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Metrics at Bank
    api_response = api_instance.o_bpv5_0_0_get_metrics_at_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricApi->o_bpv5_0_0_get_metrics_at_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**MetricsJson**](MetricsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

