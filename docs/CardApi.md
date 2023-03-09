# obp_python.CardApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_3_0_get_cards**](CardApi.md#o_bpv1_3_0_get_cards) | **GET** /obp/v5.0.0/cards | Get cards for the current user
[**o_bpv3_1_0_create_card_attribute**](CardApi.md#o_bpv3_1_0_create_card_attribute) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/cards/{CARD_ID}/attribute | Create Card Attribute
[**o_bpv3_1_0_delete_card_for_bank**](CardApi.md#o_bpv3_1_0_delete_card_for_bank) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/cards/{CARD_ID} | Delete Card
[**o_bpv3_1_0_get_card_for_bank**](CardApi.md#o_bpv3_1_0_get_card_for_bank) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/cards/{CARD_ID} | Get Card By Id
[**o_bpv3_1_0_get_cards_for_bank**](CardApi.md#o_bpv3_1_0_get_cards_for_bank) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/cards | Get Cards for the specified bank
[**o_bpv3_1_0_get_status_of_credit_card_order**](CardApi.md#o_bpv3_1_0_get_status_of_credit_card_order) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/credit_cards/orders | Get status of Credit Card order 
[**o_bpv3_1_0_update_card_attribute**](CardApi.md#o_bpv3_1_0_update_card_attribute) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/cards/{CARD_ID}/attributes/{CARD_ATTRIBUTE_ID} | Update Card Attribute
[**o_bpv3_1_0_updated_card_for_bank**](CardApi.md#o_bpv3_1_0_updated_card_for_bank) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/cards/{CARD_ID} | Update Card
[**o_bpv4_0_0_create_or_update_card_attribute_definition**](CardApi.md#o_bpv4_0_0_create_or_update_card_attribute_definition) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/card | Create or Update Card Attribute Definition
[**o_bpv4_0_0_delete_card_attribute_definition**](CardApi.md#o_bpv4_0_0_delete_card_attribute_definition) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/ATTRIBUTE_DEFINITION_ID/card | Delete Card Attribute Definition
[**o_bpv4_0_0_get_card_attribute_definition**](CardApi.md#o_bpv4_0_0_get_card_attribute_definition) | **GET** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/card | Get Card Attribute Definition
[**o_bpv5_0_0_add_card_for_bank**](CardApi.md#o_bpv5_0_0_add_card_for_bank) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/cards | Create Card


# **o_bpv1_3_0_get_cards**
> PhysicalCardsJSON o_bpv1_3_0_get_cards(body)

Get cards for the current user

<p>Returns data about all the physical cards a user has been issued. These could be debit cards, credit cards, etc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get cards for the current user
    api_response = api_instance.o_bpv1_3_0_get_cards(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv1_3_0_get_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**PhysicalCardsJSON**](PhysicalCardsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_card_attribute**
> CardAttributeCommons o_bpv3_1_0_create_card_attribute(body, card_id, bank_id)

Create Card Attribute

<p>Create Card Attribute</p><p>Card Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Card Attribute is linked to its Card by CARD_ID</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
body = obp_python.CardAttributeJson() # CardAttributeJson | CardAttributeJson object that needs to be added.
card_id = 'card_id_example' # str | the card id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Card Attribute
    api_response = api_instance.o_bpv3_1_0_create_card_attribute(body, card_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_create_card_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardAttributeJson**](CardAttributeJson.md)| CardAttributeJson object that needs to be added. | 
 **card_id** | **str**| the card id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CardAttributeCommons**](CardAttributeCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_card_for_bank**
> o_bpv3_1_0_delete_card_for_bank(card_id, bank_id)

Delete Card

<p>Delete a Card at bank specified by CARD_ID .</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
card_id = 'card_id_example' # str | the card id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Card
    api_instance.o_bpv3_1_0_delete_card_for_bank(card_id, bank_id)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_delete_card_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**| the card id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_card_for_bank**
> PhysicalCardWithAttributesJsonV310 o_bpv3_1_0_get_card_for_bank(card_id, bank_id)

Get Card By Id

<p>This will the datails of the card.<br />It shows the account infomation which linked the the card.<br />Also shows the card attributes of the card.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
card_id = 'card_id_example' # str | the card id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Card By Id
    api_response = api_instance.o_bpv3_1_0_get_card_for_bank(card_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_get_card_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**| the card id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**PhysicalCardWithAttributesJsonV310**](PhysicalCardWithAttributesJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_cards_for_bank**
> PhysicalCardsJsonV310 o_bpv3_1_0_get_cards_for_bank(bank_id)

Get Cards for the specified bank

<p>Should be able to filter on the following fields</p><p>eg:/management/banks/BANK_ID/cards?customer_id=66214b8e-259e-44ad-8868-3eb47be70646&amp;account_id=8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0</p><p>1 customer_id should be valid customer_id, otherwise, it will return an empty card list.</p><p>2 account_id should be valid account_id , otherwise, it will return an empty card list.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Cards for the specified bank
    api_response = api_instance.o_bpv3_1_0_get_cards_for_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_get_cards_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**PhysicalCardsJsonV310**](PhysicalCardsJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_status_of_credit_card_order**
> CreditCardOrderStatusResponseJson o_bpv3_1_0_get_status_of_credit_card_order(view_id, account_id, bank_id)

Get status of Credit Card order 

<pre><code>  Get status of Credit Card orders</code></pre><p>Get all orders</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get status of Credit Card order 
    api_response = api_instance.o_bpv3_1_0_get_status_of_credit_card_order(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_get_status_of_credit_card_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CreditCardOrderStatusResponseJson**](CreditCardOrderStatusResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_card_attribute**
> CardAttributeCommons o_bpv3_1_0_update_card_attribute(body, card_attribute_id, card_id, bank_id)

Update Card Attribute

<p>Update Card Attribute</p><p>Card Attributes are used to describe a financial Product with a list of typed key value pairs.</p><p>Each Card Attribute is linked to its Card by CARD_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
body = obp_python.CardAttributeJson() # CardAttributeJson | CardAttributeJson object that needs to be added.
card_attribute_id = 'card_attribute_id_example' # str | the card attribute id
card_id = 'card_id_example' # str | the card id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Card Attribute
    api_response = api_instance.o_bpv3_1_0_update_card_attribute(body, card_attribute_id, card_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_update_card_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CardAttributeJson**](CardAttributeJson.md)| CardAttributeJson object that needs to be added. | 
 **card_attribute_id** | **str**| the card attribute id | 
 **card_id** | **str**| the card id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CardAttributeCommons**](CardAttributeCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_updated_card_for_bank**
> PhysicalCardJsonV310 o_bpv3_1_0_updated_card_for_bank(body, card_id, bank_id)

Update Card

<p>Update Card at bank specified by CARD_ID .<br />Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
body = obp_python.UpdatePhysicalCardJsonV310() # UpdatePhysicalCardJsonV310 | UpdatePhysicalCardJsonV310 object that needs to be added.
card_id = 'card_id_example' # str | the card id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Card
    api_response = api_instance.o_bpv3_1_0_updated_card_for_bank(body, card_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv3_1_0_updated_card_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePhysicalCardJsonV310**](UpdatePhysicalCardJsonV310.md)| UpdatePhysicalCardJsonV310 object that needs to be added. | 
 **card_id** | **str**| the card id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**PhysicalCardJsonV310**](PhysicalCardJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_or_update_card_attribute_definition**
> AttributeDefinitionResponseJsonV400 o_bpv4_0_0_create_or_update_card_attribute_definition(body, bank_id)

Create or Update Card Attribute Definition

<p>Create or Update Card Attribute Definition</p><p>The category field must be Card</p><p>The type field must be one of; DOUBLE, STRING, INTEGER and DATE_WITH_DAY</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
body = obp_python.AttributeDefinitionJsonV400() # AttributeDefinitionJsonV400 | AttributeDefinitionJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create or Update Card Attribute Definition
    api_response = api_instance.o_bpv4_0_0_create_or_update_card_attribute_definition(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv4_0_0_create_or_update_card_attribute_definition: %s\n" % e)
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

# **o_bpv4_0_0_delete_card_attribute_definition**
> o_bpv4_0_0_delete_card_attribute_definition(bank_id)

Delete Card Attribute Definition

<p>Delete Card Attribute Definition by ATTRIBUTE_DEFINITION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Card Attribute Definition
    api_instance.o_bpv4_0_0_delete_card_attribute_definition(bank_id)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv4_0_0_delete_card_attribute_definition: %s\n" % e)
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

# **o_bpv4_0_0_get_card_attribute_definition**
> AttributeDefinitionsResponseJsonV400 o_bpv4_0_0_get_card_attribute_definition(bank_id)

Get Card Attribute Definition

<p>Get Card Attribute Definition</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Card Attribute Definition
    api_response = api_instance.o_bpv4_0_0_get_card_attribute_definition(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv4_0_0_get_card_attribute_definition: %s\n" % e)
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

# **o_bpv5_0_0_add_card_for_bank**
> PhysicalCardJsonV500 o_bpv5_0_0_add_card_for_bank(body, bank_id)

Create Card

<p>Create Card at bank specified by BANK_ID .</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CardApi(obp_python.ApiClient(configuration))
body = obp_python.CreatePhysicalCardJsonV500() # CreatePhysicalCardJsonV500 | CreatePhysicalCardJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Card
    api_response = api_instance.o_bpv5_0_0_add_card_for_bank(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardApi->o_bpv5_0_0_add_card_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePhysicalCardJsonV500**](CreatePhysicalCardJsonV500.md)| CreatePhysicalCardJsonV500 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**PhysicalCardJsonV500**](PhysicalCardJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

