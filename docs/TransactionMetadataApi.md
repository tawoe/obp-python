# obp_python.TransactionMetadataApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_2_1_add_comment_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_add_comment_for_view_on_transaction) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/comments | Add a Transaction Comment
[**o_bpv1_2_1_add_image_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_add_image_for_view_on_transaction) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/images | Add a Transaction Image
[**o_bpv1_2_1_add_tag_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_add_tag_for_view_on_transaction) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/tags | Add a Transaction Tag
[**o_bpv1_2_1_add_transaction_narrative**](TransactionMetadataApi.md#o_bpv1_2_1_add_transaction_narrative) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/narrative | Add a Transaction Narrative
[**o_bpv1_2_1_add_where_tag_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_add_where_tag_for_view_on_transaction) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/where | Add a Transaction where Tag
[**o_bpv1_2_1_delete_comment_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_delete_comment_for_view_on_transaction) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/comments/{COMMENT_ID} | Delete a Transaction Comment
[**o_bpv1_2_1_delete_image_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_delete_image_for_view_on_transaction) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/images/{IMAGE_ID} | Delete a Transaction Image
[**o_bpv1_2_1_delete_tag_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_delete_tag_for_view_on_transaction) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/tags/{TAG_ID} | Delete a Transaction Tag
[**o_bpv1_2_1_delete_transaction_narrative**](TransactionMetadataApi.md#o_bpv1_2_1_delete_transaction_narrative) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/narrative | Delete a Transaction Narrative
[**o_bpv1_2_1_delete_where_tag_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_delete_where_tag_for_view_on_transaction) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/where | Delete a Transaction Tag
[**o_bpv1_2_1_get_comments_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_get_comments_for_view_on_transaction) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/comments | Get Transaction Comments
[**o_bpv1_2_1_get_images_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_get_images_for_view_on_transaction) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/images | Get Transaction Images
[**o_bpv1_2_1_get_tags_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_get_tags_for_view_on_transaction) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/tags | Get Transaction Tags
[**o_bpv1_2_1_get_transaction_narrative**](TransactionMetadataApi.md#o_bpv1_2_1_get_transaction_narrative) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/narrative | Get a Transaction Narrative
[**o_bpv1_2_1_get_where_tag_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_get_where_tag_for_view_on_transaction) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/where | Get a Transaction where Tag
[**o_bpv1_2_1_update_transaction_narrative**](TransactionMetadataApi.md#o_bpv1_2_1_update_transaction_narrative) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/narrative | Update a Transaction Narrative
[**o_bpv1_2_1_update_where_tag_for_view_on_transaction**](TransactionMetadataApi.md#o_bpv1_2_1_update_where_tag_for_view_on_transaction) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/metadata/where | Update a Transaction where Tag


# **o_bpv1_2_1_add_comment_for_view_on_transaction**
> TransactionCommentJSON o_bpv1_2_1_add_comment_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Add a Transaction Comment

<p>Posts a comment about a transaction TRANSACTION_ID on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> VIEW_ID.</p><p>${authenticationRequiredMessage(false)}</p><p>Authentication is required since the comment is linked with the user.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.PostTransactionCommentJSON() # PostTransactionCommentJSON | PostTransactionCommentJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add a Transaction Comment
    api_response = api_instance.o_bpv1_2_1_add_comment_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_add_comment_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTransactionCommentJSON**](PostTransactionCommentJSON.md)| PostTransactionCommentJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionCommentJSON**](TransactionCommentJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_add_image_for_view_on_transaction**
> TransactionImageJSON o_bpv1_2_1_add_image_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Add a Transaction Image

<p>Posts an image about a transaction TRANSACTION_ID on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> VIEW_ID.</p><p>Authentication is Mandatory</p><p>The image is linked with the user.</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.PostTransactionImageJSON() # PostTransactionImageJSON | PostTransactionImageJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add a Transaction Image
    api_response = api_instance.o_bpv1_2_1_add_image_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_add_image_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTransactionImageJSON**](PostTransactionImageJSON.md)| PostTransactionImageJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionImageJSON**](TransactionImageJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_add_tag_for_view_on_transaction**
> TransactionTagJSON o_bpv1_2_1_add_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Add a Transaction Tag

<p>Posts a tag about a transaction TRANSACTION_ID on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> VIEW_ID.</p><p>Authentication is Mandatory</p><p>Authentication is required as the tag is linked with the user.</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.PostTransactionTagJSON() # PostTransactionTagJSON | PostTransactionTagJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add a Transaction Tag
    api_response = api_instance.o_bpv1_2_1_add_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_add_tag_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTransactionTagJSON**](PostTransactionTagJSON.md)| PostTransactionTagJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionTagJSON**](TransactionTagJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_add_transaction_narrative**
> SuccessMessage o_bpv1_2_1_add_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)

Add a Transaction Narrative

<p>Creates a description of the transaction TRANSACTION_ID.</p><p>Note: Unlike other items of metadata, there is only one &quot;narrative&quot; per transaction accross all views.<br />If you set narrative via a view e.g. view-x it will be seen via view-y (as long as view-y has permission to see the narrative).</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionNarrativeJSON() # TransactionNarrativeJSON | TransactionNarrativeJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add a Transaction Narrative
    api_response = api_instance.o_bpv1_2_1_add_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_add_transaction_narrative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionNarrativeJSON**](TransactionNarrativeJSON.md)| TransactionNarrativeJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_add_where_tag_for_view_on_transaction**
> SuccessMessage o_bpv1_2_1_add_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Add a Transaction where Tag

<p>Creates a &quot;where&quot; Geo tag on a transaction TRANSACTION_ID in a <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.</p><p>Authentication is Mandatory</p><p>The geo tag is linked with the user.</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.PostTransactionWhereJSON() # PostTransactionWhereJSON | PostTransactionWhereJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add a Transaction where Tag
    api_response = api_instance.o_bpv1_2_1_add_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_add_where_tag_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTransactionWhereJSON**](PostTransactionWhereJSON.md)| PostTransactionWhereJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_delete_comment_for_view_on_transaction**
> EmptyClassJson o_bpv1_2_1_delete_comment_for_view_on_transaction(body, comment_id, transaction_id, view_id, account_id, bank_id)

Delete a Transaction Comment

<p>Delete the comment COMMENT_ID about the transaction TRANSACTION_ID made on <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.</p><p>Authentication via OAuth is required. The user must either have owner privileges for this account, or must be the user that posted the comment.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
comment_id = 'comment_id_example' # str | The comment id
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete a Transaction Comment
    api_response = api_instance.o_bpv1_2_1_delete_comment_for_view_on_transaction(body, comment_id, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_delete_comment_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **comment_id** | **str**| The comment id | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_delete_image_for_view_on_transaction**
> EmptyClassJson o_bpv1_2_1_delete_image_for_view_on_transaction(body, image_id, transaction_id, view_id, account_id, bank_id)

Delete a Transaction Image

<p>Deletes the image IMAGE_ID about the transaction TRANSACTION_ID made on <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.</p><p>Authentication via OAuth is required. The user must either have owner privileges for this account, or must be the user that posted the image.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
image_id = 'image_id_example' # str | The image id
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete a Transaction Image
    api_response = api_instance.o_bpv1_2_1_delete_image_for_view_on_transaction(body, image_id, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_delete_image_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **image_id** | **str**| The image id | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_delete_tag_for_view_on_transaction**
> EmptyClassJson o_bpv1_2_1_delete_tag_for_view_on_transaction(body, tag_id, transaction_id, view_id, account_id, bank_id)

Delete a Transaction Tag

<p>Deletes the tag TAG_ID about the transaction TRANSACTION_ID made on <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.<br />Authentication via OAuth is required. The user must either have owner privileges for this account,<br />or must be the user that posted the tag.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
tag_id = 'tag_id_example' # str | The tag id
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete a Transaction Tag
    api_response = api_instance.o_bpv1_2_1_delete_tag_for_view_on_transaction(body, tag_id, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_delete_tag_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **tag_id** | **str**| The tag id | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_delete_transaction_narrative**
> EmptyClassJson o_bpv1_2_1_delete_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)

Delete a Transaction Narrative

<p>Deletes the description of the transaction TRANSACTION_ID.</p><p>Authentication via OAuth is required if the view is not public.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete a Transaction Narrative
    api_response = api_instance.o_bpv1_2_1_delete_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_delete_transaction_narrative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_delete_where_tag_for_view_on_transaction**
> EmptyClassJson o_bpv1_2_1_delete_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Delete a Transaction Tag

<p>Deletes the where tag of the transaction TRANSACTION_ID made on <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.</p><p>Authentication is Mandatory</p><p>The user must either have owner privileges for this account, or must be the user that posted the geo tag.</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete a Transaction Tag
    api_response = api_instance.o_bpv1_2_1_delete_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_delete_where_tag_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_comments_for_view_on_transaction**
> TransactionCommentsJSON o_bpv1_2_1_get_comments_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Get Transaction Comments

<p>Returns the transaction TRANSACTION_ID comments made on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> (VIEW_ID).</p><p>Authentication via OAuth is required if the view is not public.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Comments
    api_response = api_instance.o_bpv1_2_1_get_comments_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_get_comments_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionCommentsJSON**](TransactionCommentsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_images_for_view_on_transaction**
> TransactionImagesJSON o_bpv1_2_1_get_images_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Get Transaction Images

<p>Returns the transaction TRANSACTION_ID images made on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> (VIEW_ID).<br />Authentication via OAuth is required if the view is not public.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Images
    api_response = api_instance.o_bpv1_2_1_get_images_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_get_images_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionImagesJSON**](TransactionImagesJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_tags_for_view_on_transaction**
> TransactionTagJSON o_bpv1_2_1_get_tags_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Get Transaction Tags

<p>Returns the transaction TRANSACTION_ID tags made on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> (VIEW_ID).<br />Authentication via OAuth is required if the view is not public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Transaction Tags
    api_response = api_instance.o_bpv1_2_1_get_tags_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_get_tags_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionTagJSON**](TransactionTagJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_transaction_narrative**
> TransactionNarrativeJSON o_bpv1_2_1_get_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)

Get a Transaction Narrative

<p>Returns the account owner description of the transaction <a href=\"#1_2_1-getViewsForBankAccount\">moderated</a> by the view.</p><p>Authentication via OAuth is required if the view is not public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get a Transaction Narrative
    api_response = api_instance.o_bpv1_2_1_get_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_get_transaction_narrative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionNarrativeJSON**](TransactionNarrativeJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_where_tag_for_view_on_transaction**
> TransactionWhereJSON o_bpv1_2_1_get_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Get a Transaction where Tag

<p>Returns the &quot;where&quot; Geo tag added to the transaction TRANSACTION_ID made on a <a href=\"#1_2_1-getViewsForBankAccount\">view</a> (VIEW_ID).<br />It represents the location where the transaction has been initiated.</p><p>Authentication via OAuth is required if the view is not public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get a Transaction where Tag
    api_response = api_instance.o_bpv1_2_1_get_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_get_where_tag_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TransactionWhereJSON**](TransactionWhereJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_update_transaction_narrative**
> SuccessMessage o_bpv1_2_1_update_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)

Update a Transaction Narrative

<p>Updates the description of the transaction TRANSACTION_ID.</p><p>Authentication via OAuth is required if the view is not public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.TransactionNarrativeJSON() # TransactionNarrativeJSON | TransactionNarrativeJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update a Transaction Narrative
    api_response = api_instance.o_bpv1_2_1_update_transaction_narrative(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_update_transaction_narrative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionNarrativeJSON**](TransactionNarrativeJSON.md)| TransactionNarrativeJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_update_where_tag_for_view_on_transaction**
> SuccessMessage o_bpv1_2_1_update_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)

Update a Transaction where Tag

<p>Updates the &quot;where&quot; Geo tag on a transaction TRANSACTION_ID in a <a href=\"#1_2_1-getViewsForBankAccount\">view</a>.</p><p>Authentication is Mandatory</p><p>The geo tag is linked with the user.</p>

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
api_instance = obp_python.TransactionMetadataApi(obp_python.ApiClient(configuration))
body = obp_python.PostTransactionWhereJSON() # PostTransactionWhereJSON | PostTransactionWhereJSON object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update a Transaction where Tag
    api_response = api_instance.o_bpv1_2_1_update_where_tag_for_view_on_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionMetadataApi->o_bpv1_2_1_update_where_tag_for_view_on_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTransactionWhereJSON**](PostTransactionWhereJSON.md)| PostTransactionWhereJSON object that needs to be added. | 
 **transaction_id** | **str**| The transaction id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

