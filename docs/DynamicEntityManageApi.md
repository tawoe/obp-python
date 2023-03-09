# obp_python.DynamicEntityManageApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_bank_level_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_create_bank_level_dynamic_entity) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities | Create Bank Level Dynamic Entity
[**o_bpv4_0_0_create_system_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_create_system_dynamic_entity) | **POST** /obp/v5.0.0/management/system-dynamic-entities | Create System Level Dynamic Entity
[**o_bpv4_0_0_delete_bank_level_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_delete_bank_level_dynamic_entity) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities/{DYNAMIC_ENTITY_ID} | Delete Bank Level Dynamic Entity
[**o_bpv4_0_0_delete_my_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_delete_my_dynamic_entity) | **DELETE** /obp/v5.0.0/my/dynamic-entities/{DYNAMIC_ENTITY_ID} | Delete My Dynamic Entity
[**o_bpv4_0_0_delete_system_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_delete_system_dynamic_entity) | **DELETE** /obp/v5.0.0/management/system-dynamic-entities/{DYNAMIC_ENTITY_ID} | Delete System Level Dynamic Entity
[**o_bpv4_0_0_get_bank_level_dynamic_entities**](DynamicEntityManageApi.md#o_bpv4_0_0_get_bank_level_dynamic_entities) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities | Get Bank Level Dynamic Entities
[**o_bpv4_0_0_get_my_dynamic_entities**](DynamicEntityManageApi.md#o_bpv4_0_0_get_my_dynamic_entities) | **GET** /obp/v5.0.0/my/dynamic-entities | Get My Dynamic Entities
[**o_bpv4_0_0_get_system_dynamic_entities**](DynamicEntityManageApi.md#o_bpv4_0_0_get_system_dynamic_entities) | **GET** /obp/v5.0.0/management/system-dynamic-entities | Get System Dynamic Entities
[**o_bpv4_0_0_update_bank_level_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_update_bank_level_dynamic_entity) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities/{DYNAMIC_ENTITY_ID} | Update Bank Level Dynamic Entity
[**o_bpv4_0_0_update_my_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_update_my_dynamic_entity) | **PUT** /obp/v5.0.0/my/dynamic-entities/{DYNAMIC_ENTITY_ID} | Update My Dynamic Entity
[**o_bpv4_0_0_update_system_dynamic_entity**](DynamicEntityManageApi.md#o_bpv4_0_0_update_system_dynamic_entity) | **PUT** /obp/v5.0.0/management/system-dynamic-entities/{DYNAMIC_ENTITY_ID} | Update System Level Dynamic Entity


# **o_bpv4_0_0_create_bank_level_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_create_bank_level_dynamic_entity(body, bank_id)

Create Bank Level Dynamic Entity

<p>Create a Bank Level DynamicEntity.</p><p>Authentication is Mandatory</p><p>Create a DynamicEntity. If creation is successful, the corresponding POST, GET, PUT and DELETE (Create, Read, Update, Delete or CRUD for short) endpoints will be generated automatically</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>The DATE_WITH_DAY format is: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;branchId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;atmId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;accountId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;productCode=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;cardId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;accountId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&amp;transactionId=19f67d44-5abb-464d-a8a4-86892a7d24ae&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;accountId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&amp;counterpartyId=19f67d44-5abb-464d-a8a4-86892a7d24ae&quot;}</code></pre><p>Note: if you set <code>hasPersonalEntity</code> = false, then OBP will not generate the CRUD my FooBar endpoints.</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_create_bank_level_dynamic_entity(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_create_bank_level_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_system_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_create_system_dynamic_entity(body)

Create System Level Dynamic Entity

<p>Create a system level Dynamic Entity.</p><p>Authentication is Mandatory</p><p>Create a DynamicEntity. If creation is successful, the corresponding POST, GET, PUT and DELETE (Create, Read, Update, Delete or CRUD for short) endpoints will be generated automatically</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>The DATE_WITH_DAY format is: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />See the following list of currently available reference types and examples of how to construct key values correctly. Note: As more Dynamic Entities are created on this instance, this list will grow:</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;branchId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;atmId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;accountId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;productCode=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;cardId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;accountId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&amp;transactionId=45a74569-c3a2-4b82-8111-3f68a32e5d95&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;accountId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&amp;counterpartyId=45a74569-c3a2-4b82-8111-3f68a32e5d95&quot;}</code></pre><p>Note: if you set <code>hasPersonalEntity</code> = false, then OBP will not generate the CRUD my FooBar endpoints.</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.

try:
    # Create System Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_create_system_dynamic_entity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_create_system_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_dynamic_entity**
> o_bpv4_0_0_delete_bank_level_dynamic_entity(dynamic_entity_id, bank_id)

Delete Bank Level Dynamic Entity

<p>Delete a Bank Level DynamicEntity specified by DYNAMIC_ENTITY_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Dynamic Entity
    api_instance.o_bpv4_0_0_delete_bank_level_dynamic_entity(dynamic_entity_id, bank_id)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_delete_bank_level_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_entity_id** | **str**| the dynamic entity id  | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_dynamic_entity**
> o_bpv4_0_0_delete_my_dynamic_entity(dynamic_entity_id)

Delete My Dynamic Entity

<p>Delete my DynamicEntity specified by DYNAMIC_ENTITY_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Delete My Dynamic Entity
    api_instance.o_bpv4_0_0_delete_my_dynamic_entity(dynamic_entity_id)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_delete_my_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_system_dynamic_entity**
> o_bpv4_0_0_delete_system_dynamic_entity(dynamic_entity_id)

Delete System Level Dynamic Entity

<p>Delete a DynamicEntity specified by DYNAMIC_ENTITY_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Delete System Level Dynamic Entity
    api_instance.o_bpv4_0_0_delete_system_dynamic_entity(dynamic_entity_id)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_delete_system_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_entities**
> InlineResponse2004 o_bpv4_0_0_get_bank_level_dynamic_entities(bank_id)

Get Bank Level Dynamic Entities

<p>Get all the bank level Dynamic Entities for one bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Entities
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_entities(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_get_bank_level_dynamic_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_dynamic_entities**
> InlineResponse2004 o_bpv4_0_0_get_my_dynamic_entities()

Get My Dynamic Entities

<p>Get all my Dynamic Entities.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))

try:
    # Get My Dynamic Entities
    api_response = api_instance.o_bpv4_0_0_get_my_dynamic_entities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_get_my_dynamic_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_system_dynamic_entities**
> InlineResponse2004 o_bpv4_0_0_get_system_dynamic_entities()

Get System Dynamic Entities

<p>Get all System Dynamic Entities</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))

try:
    # Get System Dynamic Entities
    api_response = api_instance.o_bpv4_0_0_get_system_dynamic_entities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_get_system_dynamic_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_update_bank_level_dynamic_entity(body, dynamic_entity_id, bank_id)

Update Bank Level Dynamic Entity

<p>Update a Bank Level DynamicEntity.</p><p>Authentication is Mandatory</p><p>Update one DynamicEntity, after update finished, the corresponding CRUD endpoints will be changed.</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>DATE_WITH_DAY format: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;branchId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;atmId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;accountId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;productCode=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;cardId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;accountId=6b433d26-692d-47d9-8433-bf8c8b249a4b&amp;transactionId=d69c95e9-6d71-4219-9d8a-d0dbe4014817&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;accountId=6b433d26-692d-47d9-8433-bf8c8b249a4b&amp;counterpartyId=d69c95e9-6d71-4219-9d8a-d0dbe4014817&quot;}</code></pre>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_update_bank_level_dynamic_entity(body, dynamic_entity_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_update_bank_level_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **dynamic_entity_id** | **str**| the dynamic entity id  | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_my_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_update_my_dynamic_entity(body, dynamic_entity_id)

Update My Dynamic Entity

<p>Update my DynamicEntity.</p><p>Authentication is Mandatory</p><p>Update one of my DynamicEntity, after update finished, the corresponding CRUD endpoints will be changed.</p><p>Current support filed types as follow:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>DATE_WITH_DAY format: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;branchId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;atmId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;accountId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;productCode=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;cardId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;accountId=26617f71-1ba3-4ecb-94d1-e784071c7e24&amp;transactionId=e0c520f5-8a29-4554-9a8b-8321b15bf478&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;accountId=26617f71-1ba3-4ecb-94d1-e784071c7e24&amp;counterpartyId=e0c520f5-8a29-4554-9a8b-8321b15bf478&quot;}</code></pre>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Update My Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_update_my_dynamic_entity(body, dynamic_entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_update_my_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_system_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_update_system_dynamic_entity(body, dynamic_entity_id)

Update System Level Dynamic Entity

<p>Update a System Level Dynamic Entity.</p><p>Authentication is Mandatory</p><p>Update one DynamicEntity, after update finished, the corresponding CRUD endpoints will be changed.</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>DATE_WITH_DAY format: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;branchId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;atmId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;accountId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;productCode=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;cardId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;accountId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&amp;transactionId=cad30b93-7ba0-4287-9942-6e9c81925f8d&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;accountId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&amp;counterpartyId=cad30b93-7ba0-4287-9942-6e9c81925f8d&quot;}</code></pre>

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
api_instance = obp_python.DynamicEntityManageApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Update System Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_update_system_dynamic_entity(body, dynamic_entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DynamicEntityManageApi->o_bpv4_0_0_update_system_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

