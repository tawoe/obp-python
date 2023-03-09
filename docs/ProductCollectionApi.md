# obp_python.ProductCollectionApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_product_collection**](ProductCollectionApi.md#o_bpv3_1_0_create_product_collection) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/product-collections/{COLLECTION_CODE} | Create Product Collection
[**o_bpv3_1_0_get_product_collection**](ProductCollectionApi.md#o_bpv3_1_0_get_product_collection) | **GET** /obp/v5.0.0/banks/{BANK_ID}/product-collections/{COLLECTION_CODE} | Get Product Collection


# **o_bpv3_1_0_create_product_collection**
> ProductCollectionsJsonV310 o_bpv3_1_0_create_product_collection(body, collection_code, bank_id)

Create Product Collection

<p>Create or Update a Product Collection at the Bank.</p><p>Use Product Collections to create Product &quot;Baskets&quot;, &quot;Portfolios&quot;, &quot;Indices&quot;, &quot;Collections&quot;, &quot;Underlyings-lists&quot;, &quot;Buckets&quot; etc. etc.</p><p>There is a many to many relationship between Products and Product Collections:</p><ul><li><p>A Product can exist in many Collections</p></li><li><p>A Collection can contain many Products.</p></li></ul><p>A collection has collection code, one parent Product and one or more child Products.</p><p>Product hiearchy vs Product Collections:</p><ul><li><p>You can define a hierarchy of products - so that a child Product inherits attributes of its parent Product -  using the parent_product_code in Product.</p></li><li><p>You can define a collection (also known as baskets or buckets) of products using Product Collections.</p></li></ul><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductCollectionApi(obp_python.ApiClient(configuration))
body = obp_python.PutProductCollectionsV310() # PutProductCollectionsV310 | PutProductCollectionsV310 object that needs to be added.
collection_code = 'collection_code_example' # str | the collection code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Product Collection
    api_response = api_instance.o_bpv3_1_0_create_product_collection(body, collection_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCollectionApi->o_bpv3_1_0_create_product_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutProductCollectionsV310**](PutProductCollectionsV310.md)| PutProductCollectionsV310 object that needs to be added. | 
 **collection_code** | **str**| the collection code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductCollectionsJsonV310**](ProductCollectionsJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_product_collection**
> ProductCollectionJsonTreeV310 o_bpv3_1_0_get_product_collection(collection_code, bank_id)

Get Product Collection

<p>Returns information about the financial Product Collection specified by BANK_ID and COLLECTION_CODE:</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductCollectionApi(obp_python.ApiClient(configuration))
collection_code = 'collection_code_example' # str | the collection code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Collection
    api_response = api_instance.o_bpv3_1_0_get_product_collection(collection_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductCollectionApi->o_bpv3_1_0_get_product_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_code** | **str**| the collection code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductCollectionJsonTreeV310**](ProductCollectionJsonTreeV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

