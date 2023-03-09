# obp_python.DataWarehouseApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_0_0_data_warehouse_search**](DataWarehouseApi.md#o_bpv3_0_0_data_warehouse_search) | **POST** /obp/v5.0.0/search/warehouse/{INDEX} | Data Warehouse Search
[**o_bpv3_0_0_data_warehouse_statistics**](DataWarehouseApi.md#o_bpv3_0_0_data_warehouse_statistics) | **POST** /obp/v5.0.0/search/warehouse/statistics/{INDEX}/{FIELD} | Data Warehouse Statistics


# **o_bpv3_0_0_data_warehouse_search**
> EmptyClassJson o_bpv3_0_0_data_warehouse_search(body, index)

Data Warehouse Search

<p>Search the data warehouse and get row level results.</p><p>Authentication is Mandatory</p><p>CanSearchWarehouse entitlement is required. You can request the Role below.</p><p>Elastic (search) is used in the background. See links below for syntax.</p><p>Examples of usage:</p><p>POST /search/warehouse/THE_INDEX_YOU_WANT_TO_USE</p><p>POST /search/warehouse/INDEX1,INDEX2</p><p>POST /search/warehouse/ALL</p><p>{ Any valid elasticsearch query DSL in the body }</p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html\">Elasticsearch query DSL</a></p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/6.2/search-request-body.html\">Elastic simple query</a></p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/6.2/search-aggregations.html\">Elastic aggregations</a></p>

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
api_instance = obp_python.DataWarehouseApi(obp_python.ApiClient(configuration))
body = obp_python.ElasticSearchJsonV300() # ElasticSearchJsonV300 | ElasticSearchJsonV300 object that needs to be added.
index = 'index_example' # str | the elastic search index

try:
    # Data Warehouse Search
    api_response = api_instance.o_bpv3_0_0_data_warehouse_search(body, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataWarehouseApi->o_bpv3_0_0_data_warehouse_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElasticSearchJsonV300**](ElasticSearchJsonV300.md)| ElasticSearchJsonV300 object that needs to be added. | 
 **index** | **str**| the elastic search index | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_data_warehouse_statistics**
> EmptyClassJson o_bpv3_0_0_data_warehouse_statistics(body, field, index)

Data Warehouse Statistics

<p>Search the data warehouse and get statistical aggregations over a warehouse field</p><p>Does a stats aggregation over some numeric field:</p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-stats-aggregation.html\">https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-metrics-stats-aggregation.html</a></p><p>Authentication is Mandatory</p><p>CanSearchWarehouseStats Role is required. You can request this below.</p><p>Elastic (search) is used in the background. See links below for syntax.</p><p>Examples of usage:</p><p>POST /search/warehouse/statistics/INDEX/FIELD</p><p>POST /search/warehouse/statistics/ALL/FIELD</p><p>{ Any valid elasticsearch query DSL in the body }</p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html\">Elasticsearch query DSL</a></p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/6.2/search-request-body.html\">Elastic simple query</a></p><p><a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/6.2/search-aggregations.html\">Elastic aggregations</a></p>

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
api_instance = obp_python.DataWarehouseApi(obp_python.ApiClient(configuration))
body = obp_python.ElasticSearchJsonV300() # ElasticSearchJsonV300 | ElasticSearchJsonV300 object that needs to be added.
field = 'field_example' # str | the elastic search field
index = 'index_example' # str | the elastic search index

try:
    # Data Warehouse Statistics
    api_response = api_instance.o_bpv3_0_0_data_warehouse_statistics(body, field, index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataWarehouseApi->o_bpv3_0_0_data_warehouse_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElasticSearchJsonV300**](ElasticSearchJsonV300.md)| ElasticSearchJsonV300 object that needs to be added. | 
 **field** | **str**| the elastic search field | 
 **index** | **str**| the elastic search index | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

