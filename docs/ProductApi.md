# obp_python.ProductApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_product_collection**](ProductApi.md#o_bpv3_1_0_create_product_collection) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/product-collections/{COLLECTION_CODE} | Create Product Collection
[**o_bpv3_1_0_delete_product_attribute**](ProductApi.md#o_bpv3_1_0_delete_product_attribute) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/attributes/{PRODUCT_ATTRIBUTE_ID} | Delete Product Attribute
[**o_bpv3_1_0_get_product_collection**](ProductApi.md#o_bpv3_1_0_get_product_collection) | **GET** /obp/v5.0.0/banks/{BANK_ID}/product-collections/{COLLECTION_CODE} | Get Product Collection
[**o_bpv3_1_0_get_product_tree**](ProductApi.md#o_bpv3_1_0_get_product_tree) | **GET** /obp/v5.0.0/banks/{BANK_ID}/product-tree/{PRODUCT_CODE} | Get Product Tree
[**o_bpv4_0_0_create_or_update_product_attribute_definition**](ProductApi.md#o_bpv4_0_0_create_or_update_product_attribute_definition) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/product | Create or Update Product Attribute Definition
[**o_bpv4_0_0_create_product_attribute**](ProductApi.md#o_bpv4_0_0_create_product_attribute) | **POST** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/attribute | Create Product Attribute
[**o_bpv4_0_0_create_product_fee**](ProductApi.md#o_bpv4_0_0_create_product_fee) | **POST** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/fee | Create Product Fee
[**o_bpv4_0_0_delete_product_attribute_definition**](ProductApi.md#o_bpv4_0_0_delete_product_attribute_definition) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/ATTRIBUTE_DEFINITION_ID/product | Delete Product Attribute Definition
[**o_bpv4_0_0_delete_product_cascade**](ProductApi.md#o_bpv4_0_0_delete_product_cascade) | **DELETE** /obp/v5.0.0/management/cascading/banks/{BANK_ID}/products/{PRODUCT_CODE} | Delete Product Cascade
[**o_bpv4_0_0_delete_product_fee**](ProductApi.md#o_bpv4_0_0_delete_product_fee) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/fees/PRODUCT_FEE_ID | Delete Product Fee
[**o_bpv4_0_0_get_product**](ProductApi.md#o_bpv4_0_0_get_product) | **GET** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE} | Get Bank Product
[**o_bpv4_0_0_get_product_attribute**](ProductApi.md#o_bpv4_0_0_get_product_attribute) | **GET** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/attributes/{PRODUCT_ATTRIBUTE_ID} | Get Product Attribute
[**o_bpv4_0_0_get_product_attribute_definition**](ProductApi.md#o_bpv4_0_0_get_product_attribute_definition) | **GET** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/product | Get Product Attribute Definition
[**o_bpv4_0_0_get_product_fee**](ProductApi.md#o_bpv4_0_0_get_product_fee) | **GET** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/fees/PRODUCT_FEE_ID | Get Product Fee
[**o_bpv4_0_0_get_product_fees**](ProductApi.md#o_bpv4_0_0_get_product_fees) | **GET** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/fees | Get Product Fees
[**o_bpv4_0_0_get_products**](ProductApi.md#o_bpv4_0_0_get_products) | **GET** /obp/v5.0.0/banks/{BANK_ID}/products | Get Products
[**o_bpv4_0_0_update_product_attribute**](ProductApi.md#o_bpv4_0_0_update_product_attribute) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/attributes/{PRODUCT_ATTRIBUTE_ID} | Update Product Attribute
[**o_bpv4_0_0_update_product_fee**](ProductApi.md#o_bpv4_0_0_update_product_fee) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE}/fees/PRODUCT_FEE_ID | Update Product Fee
[**o_bpv5_0_0_create_product**](ProductApi.md#o_bpv5_0_0_create_product) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/products/{PRODUCT_CODE} | Create Product


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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.PutProductCollectionsV310() # PutProductCollectionsV310 | PutProductCollectionsV310 object that needs to be added.
collection_code = 'collection_code_example' # str | the collection code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Product Collection
    api_response = api_instance.o_bpv3_1_0_create_product_collection(body, collection_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv3_1_0_create_product_collection: %s\n" % e)
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

# **o_bpv3_1_0_delete_product_attribute**
> o_bpv3_1_0_delete_product_attribute(product_attribute_id, product_code, bank_id)

Delete Product Attribute

<p>Delete Product Attribute</p><p>Product Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Product Attribute is linked to its Product by PRODUCT_CODE</p><p>Delete a Product Attribute by its id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_attribute_id = 'product_attribute_id_example' # str | the product attribute id
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Product Attribute
    api_instance.o_bpv3_1_0_delete_product_attribute(product_attribute_id, product_code, bank_id)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv3_1_0_delete_product_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_attribute_id** | **str**| the product attribute id | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
collection_code = 'collection_code_example' # str | the collection code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Collection
    api_response = api_instance.o_bpv3_1_0_get_product_collection(collection_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv3_1_0_get_product_collection: %s\n" % e)
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

# **o_bpv3_1_0_get_product_tree**
> ProductTreeJsonV310 o_bpv3_1_0_get_product_tree(product_code, bank_id)

Get Product Tree

<p>Returns information about a particular financial product specified by BANK_ID and PRODUCT_CODE<br />and it's parent product(s) recursively as specified by parent_product_code.</p><p>Each product includes the following information.</p><ul><li>Name</li><li>Code</li><li>Parent Product Code</li><li>Category</li><li>Family</li><li>Super Family</li><li>More info URL</li><li>Description</li><li>Terms and Conditions</li><li>License: The licence under which this product data is released. Licence can be an Open Data licence such as Open Data Commons Public Domain Dedication and License (PDDL) or Copyright etc.</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Tree
    api_response = api_instance.o_bpv3_1_0_get_product_tree(product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv3_1_0_get_product_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductTreeJsonV310**](ProductTreeJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_or_update_product_attribute_definition**
> AttributeDefinitionResponseJsonV400 o_bpv4_0_0_create_or_update_product_attribute_definition(body, bank_id)

Create or Update Product Attribute Definition

<p>Create or Update Product Attribute Definition</p><p>The category field must be Product</p><p>The type field must be one of; DOUBLE, STRING, INTEGER and DATE_WITH_DAY</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.AttributeDefinitionJsonV400() # AttributeDefinitionJsonV400 | AttributeDefinitionJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create or Update Product Attribute Definition
    api_response = api_instance.o_bpv4_0_0_create_or_update_product_attribute_definition(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_create_or_update_product_attribute_definition: %s\n" % e)
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

# **o_bpv4_0_0_create_product_attribute**
> ProductAttributeResponseJsonV400 o_bpv4_0_0_create_product_attribute(body, product_code, bank_id)

Create Product Attribute

<p>Create Product Attribute</p><p>Product Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Product Attribute is linked to its Product by PRODUCT_CODE</p><p>Typical product attributes might be:</p><p>ISIN (for International bonds)<br />VKN (for German bonds)<br />REDCODE (markit short code for credit derivative)<br />LOAN_ID (e.g. used for Anacredit reporting)</p><p>ISSUE_DATE (When the bond was issued in the market)<br />MATURITY_DATE (End of life time of a product)<br />TRADABLE</p><p>See <a href=\"http://www.fpml.org/\">FPML</a> for more examples.</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.ProductAttributeJsonV400() # ProductAttributeJsonV400 | ProductAttributeJsonV400 object that needs to be added.
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Product Attribute
    api_response = api_instance.o_bpv4_0_0_create_product_attribute(body, product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_create_product_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAttributeJsonV400**](ProductAttributeJsonV400.md)| ProductAttributeJsonV400 object that needs to be added. | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductAttributeResponseJsonV400**](ProductAttributeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_product_fee**
> ProductFeeResponseJsonV400 o_bpv4_0_0_create_product_fee(body, product_code, bank_id)

Create Product Fee

<p>Create Product Fee</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.ProductFeeJsonV400() # ProductFeeJsonV400 | ProductFeeJsonV400 object that needs to be added.
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Product Fee
    api_response = api_instance.o_bpv4_0_0_create_product_fee(body, product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_create_product_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductFeeJsonV400**](ProductFeeJsonV400.md)| ProductFeeJsonV400 object that needs to be added. | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductFeeResponseJsonV400**](ProductFeeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_product_attribute_definition**
> o_bpv4_0_0_delete_product_attribute_definition(bank_id)

Delete Product Attribute Definition

<p>Delete Product Attribute Definition by ATTRIBUTE_DEFINITION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Product Attribute Definition
    api_instance.o_bpv4_0_0_delete_product_attribute_definition(bank_id)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_delete_product_attribute_definition: %s\n" % e)
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

# **o_bpv4_0_0_delete_product_cascade**
> o_bpv4_0_0_delete_product_cascade(product_code, bank_id)

Delete Product Cascade

<p>Delete a Product Cascade specified by PRODUCT_CODE.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Product Cascade
    api_instance.o_bpv4_0_0_delete_product_cascade(product_code, bank_id)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_delete_product_cascade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_product_fee**
> bool o_bpv4_0_0_delete_product_fee(product_code, bank_id)

Delete Product Fee

<p>Delete Product Fee</p><p>Delete one product fee by its id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Product Fee
    api_response = api_instance.o_bpv4_0_0_delete_product_fee(product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_delete_product_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

**bool**

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_product**
> ProductJsonV400 o_bpv4_0_0_get_product(product_code, bank_id)

Get Bank Product

<p>Returns information about a financial Product offered by the bank specified by BANK_ID and PRODUCT_CODE including:</p><ul><li>Name</li><li>Code</li><li>Parent Product Code</li><li>More info URL</li><li>Description</li><li>Terms and Conditions</li><li>Description</li><li>Meta</li><li>Attributes</li><li>Fees</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Product
    api_response = api_instance.o_bpv4_0_0_get_product(product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductJsonV400**](ProductJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_product_attribute**
> ProductAttributeResponseJsonV400 o_bpv4_0_0_get_product_attribute(product_attribute_id, product_code, bank_id)

Get Product Attribute

<p>Get Product Attribute</p><p>Product Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Product Attribute is linked to its Product by PRODUCT_CODE</p><p>Get one product attribute by its id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_attribute_id = 'product_attribute_id_example' # str | the product attribute id
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Attribute
    api_response = api_instance.o_bpv4_0_0_get_product_attribute(product_attribute_id, product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_get_product_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_attribute_id** | **str**| the product attribute id | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductAttributeResponseJsonV400**](ProductAttributeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_product_attribute_definition**
> AttributeDefinitionsResponseJsonV400 o_bpv4_0_0_get_product_attribute_definition(bank_id)

Get Product Attribute Definition

<p>Get Product Attribute Definition</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Attribute Definition
    api_response = api_instance.o_bpv4_0_0_get_product_attribute_definition(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_get_product_attribute_definition: %s\n" % e)
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

# **o_bpv4_0_0_get_product_fee**
> ProductFeeResponseJsonV400 o_bpv4_0_0_get_product_fee(product_code, bank_id)

Get Product Fee

<p>Get Product Fee</p><p>Get one product fee by its id.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Fee
    api_response = api_instance.o_bpv4_0_0_get_product_fee(product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_get_product_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductFeeResponseJsonV400**](ProductFeeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_product_fees**
> ProductFeesResponseJsonV400 o_bpv4_0_0_get_product_fees(product_code, bank_id)

Get Product Fees

<p>Get Product Fees</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Product Fees
    api_response = api_instance.o_bpv4_0_0_get_product_fees(product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_get_product_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductFeesResponseJsonV400**](ProductFeesResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_products**
> ProductsJsonV400 o_bpv4_0_0_get_products(bank_id)

Get Products

<p>Returns information about the financial products offered by a bank specified by BANK_ID including:</p><ul><li>Name</li><li>Code</li><li>Parent Product Code</li><li>More info URL</li><li>Terms And Conditions URL</li><li>Description</li><li>Terms and Conditions</li><li>License the data under this endpoint is released under</li></ul><p>Can filter with attributes name and values.<br />URL params example: /banks/some-bank-id/products?manager=John&amp;count=8</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Products
    api_response = api_instance.o_bpv4_0_0_get_products(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductsJsonV400**](ProductsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_product_attribute**
> ProductAttributeResponseJsonV400 o_bpv4_0_0_update_product_attribute(body, product_attribute_id, product_code, bank_id)

Update Product Attribute

<p>Update Product Attribute.</p><p>Product Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Product Attribute is linked to its Product by PRODUCT_CODE</p><p>Update one Product Attribute by its id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.ProductAttributeJsonV400() # ProductAttributeJsonV400 | ProductAttributeJsonV400 object that needs to be added.
product_attribute_id = 'product_attribute_id_example' # str | the product attribute id
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Product Attribute
    api_response = api_instance.o_bpv4_0_0_update_product_attribute(body, product_attribute_id, product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_update_product_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductAttributeJsonV400**](ProductAttributeJsonV400.md)| ProductAttributeJsonV400 object that needs to be added. | 
 **product_attribute_id** | **str**| the product attribute id | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductAttributeResponseJsonV400**](ProductAttributeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_product_fee**
> ProductFeeResponseJsonV400 o_bpv4_0_0_update_product_fee(body, product_code, bank_id)

Update Product Fee

<p>Update Product Fee.</p><p>Update one Product Fee by its id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.ProductFeeJsonV400() # ProductFeeJsonV400 | ProductFeeJsonV400 object that needs to be added.
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Product Fee
    api_response = api_instance.o_bpv4_0_0_update_product_fee(body, product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv4_0_0_update_product_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProductFeeJsonV400**](ProductFeeJsonV400.md)| ProductFeeJsonV400 object that needs to be added. | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductFeeResponseJsonV400**](ProductFeeResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_product**
> ProductJsonV400 o_bpv5_0_0_create_product(body, product_code, bank_id)

Create Product

<p>Create or Update Product for the Bank.</p><p>Typical Super Family values / Asset classes are:</p><p>Debt<br />Equity<br />FX<br />Commodity<br />Derivative</p><p>Product hiearchy vs Product Collections:</p><ul><li><p>You can define a hierarchy of products - so that a child Product inherits attributes of its parent Product -  using the parent_product_code in Product.</p></li><li><p>You can define a collection (also known as baskets or buckets) of products using Product Collections.</p></li></ul><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ProductApi(obp_python.ApiClient(configuration))
body = obp_python.PutProductJsonV500() # PutProductJsonV500 | PutProductJsonV500 object that needs to be added.
product_code = 'product_code_example' # str | the product code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Product
    api_response = api_instance.o_bpv5_0_0_create_product(body, product_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->o_bpv5_0_0_create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutProductJsonV500**](PutProductJsonV500.md)| PutProductJsonV500 object that needs to be added. | 
 **product_code** | **str**| the product code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ProductJsonV400**](ProductJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

