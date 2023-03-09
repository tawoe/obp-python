# obp_python.CounterpartyApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_2_1_add_counterparty_corporate_location**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_corporate_location) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/corporate_location | Add Corporate Location to Counterparty
[**o_bpv1_2_1_add_counterparty_image_url**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_image_url) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/image_url | Add image url to other bank account
[**o_bpv1_2_1_add_counterparty_more_info**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_more_info) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/more_info | Add Counterparty More Info
[**o_bpv1_2_1_add_counterparty_open_corporates_url**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_open_corporates_url) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/open_corporates_url | Add Open Corporates URL to Counterparty
[**o_bpv1_2_1_add_counterparty_physical_location**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_physical_location) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/physical_location | Add physical location to other bank account
[**o_bpv1_2_1_add_counterparty_public_alias**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_public_alias) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/public_alias | Add public alias to other bank account
[**o_bpv1_2_1_add_counterparty_url**](CounterpartyApi.md#o_bpv1_2_1_add_counterparty_url) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/url | Add url to other bank account
[**o_bpv1_2_1_add_other_account_private_alias**](CounterpartyApi.md#o_bpv1_2_1_add_other_account_private_alias) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/private_alias | Create Other Account Private Alias
[**o_bpv1_2_1_delete_counterparty_corporate_location**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_corporate_location) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/corporate_location | Delete Counterparty Corporate Location
[**o_bpv1_2_1_delete_counterparty_image_url**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_image_url) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/image_url | Delete Counterparty Image URL
[**o_bpv1_2_1_delete_counterparty_more_info**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_more_info) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/more_info | Delete more info of other bank account
[**o_bpv1_2_1_delete_counterparty_open_corporates_url**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_open_corporates_url) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/open_corporates_url | Delete Counterparty Open Corporates URL
[**o_bpv1_2_1_delete_counterparty_physical_location**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_physical_location) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/physical_location | Delete Counterparty Physical Location
[**o_bpv1_2_1_delete_counterparty_private_alias**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_private_alias) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/private_alias | Delete Counterparty Private Alias
[**o_bpv1_2_1_delete_counterparty_public_alias**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_public_alias) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/public_alias | Delete Counterparty Public Alias
[**o_bpv1_2_1_delete_counterparty_url**](CounterpartyApi.md#o_bpv1_2_1_delete_counterparty_url) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/url | Delete url of other bank account
[**o_bpv1_2_1_get_counterparty_public_alias**](CounterpartyApi.md#o_bpv1_2_1_get_counterparty_public_alias) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/public_alias | Get public alias of other bank account
[**o_bpv1_2_1_get_other_account_for_transaction**](CounterpartyApi.md#o_bpv1_2_1_get_other_account_for_transaction) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/transactions/{TRANSACTION_ID}/other_account | Get Other Account of Transaction
[**o_bpv1_2_1_get_other_account_metadata**](CounterpartyApi.md#o_bpv1_2_1_get_other_account_metadata) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata | Get Other Account Metadata
[**o_bpv1_2_1_get_other_account_private_alias**](CounterpartyApi.md#o_bpv1_2_1_get_other_account_private_alias) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/private_alias | Get Other Account Private Alias
[**o_bpv1_2_1_update_counterparty_corporate_location**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_corporate_location) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/corporate_location | Update Counterparty Corporate Location
[**o_bpv1_2_1_update_counterparty_image_url**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_image_url) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/image_url | Update Counterparty Image Url
[**o_bpv1_2_1_update_counterparty_more_info**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_more_info) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/more_info | Update Counterparty More Info
[**o_bpv1_2_1_update_counterparty_open_corporates_url**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_open_corporates_url) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/open_corporates_url | Update Open Corporates Url of Counterparty
[**o_bpv1_2_1_update_counterparty_physical_location**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_physical_location) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/physical_location | Update Counterparty Physical Location
[**o_bpv1_2_1_update_counterparty_private_alias**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_private_alias) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/private_alias | Update Counterparty Private Alias
[**o_bpv1_2_1_update_counterparty_public_alias**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_public_alias) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/public_alias | Update public alias of other bank account
[**o_bpv1_2_1_update_counterparty_url**](CounterpartyApi.md#o_bpv1_2_1_update_counterparty_url) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID}/metadata/url | Update url of other bank account
[**o_bpv3_0_0_get_other_account_by_id_for_bank_account**](CounterpartyApi.md#o_bpv3_0_0_get_other_account_by_id_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts/{OTHER_ACCOUNT_ID} | Get Other Account by Id
[**o_bpv3_0_0_get_other_accounts_for_bank_account**](CounterpartyApi.md#o_bpv3_0_0_get_other_accounts_for_bank_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/other_accounts | Get Other Accounts of one Account
[**o_bpv4_0_0_create_counterparty**](CounterpartyApi.md#o_bpv4_0_0_create_counterparty) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Create Counterparty (Explicit)
[**o_bpv4_0_0_create_counterparty_for_any_account**](CounterpartyApi.md#o_bpv4_0_0_create_counterparty_for_any_account) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Create Counterparty for any account (Explicit)
[**o_bpv4_0_0_delete_counterparty_for_any_account**](CounterpartyApi.md#o_bpv4_0_0_delete_counterparty_for_any_account) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Delete Counterparty for any account (Explicit)
[**o_bpv4_0_0_delete_explicit_counterparty**](CounterpartyApi.md#o_bpv4_0_0_delete_explicit_counterparty) | **POST** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Delete Counterparty (Explicit)
[**o_bpv4_0_0_get_counterparties_for_any_account**](CounterpartyApi.md#o_bpv4_0_0_get_counterparties_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties for any account (Explicit)
[**o_bpv4_0_0_get_counterparty_by_id_for_any_account**](CounterpartyApi.md#o_bpv4_0_0_get_counterparty_by_id_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Get Counterparty by Id for any account (Explicit) 
[**o_bpv4_0_0_get_counterparty_by_name_for_any_account**](CounterpartyApi.md#o_bpv4_0_0_get_counterparty_by_name_for_any_account) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparty-names/{COUNTERPARTY_NAME} | Get Counterparty by name for any account (Explicit) 
[**o_bpv4_0_0_get_explict_counterparties_for_account**](CounterpartyApi.md#o_bpv4_0_0_get_explict_counterparties_for_account) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties | Get Counterparties (Explicit)
[**o_bpv4_0_0_get_explict_counterparty_by_id**](CounterpartyApi.md#o_bpv4_0_0_get_explict_counterparty_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/{VIEW_ID}/counterparties/{COUNTERPARTY_ID} | Get Counterparty by Id (Explicit)


# **o_bpv1_2_1_add_counterparty_corporate_location**
> SuccessMessage o_bpv1_2_1_add_counterparty_corporate_location(body, other_account_id, view_id, account_id, bank_id)

Add Corporate Location to Counterparty

<p>Add the geolocation of the counterparty's registered address</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.CorporateLocationJSON() # CorporateLocationJSON | CorporateLocationJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add Corporate Location to Counterparty
    api_response = api_instance.o_bpv1_2_1_add_counterparty_corporate_location(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_corporate_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorporateLocationJSON**](CorporateLocationJSON.md)| CorporateLocationJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_counterparty_image_url**
> SuccessMessage o_bpv1_2_1_add_counterparty_image_url(body, other_account_id, view_id, account_id, bank_id)

Add image url to other bank account

<p>Add a url that points to the logo of the counterparty</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.ImageUrlJSON() # ImageUrlJSON | ImageUrlJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add image url to other bank account
    api_response = api_instance.o_bpv1_2_1_add_counterparty_image_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_image_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageUrlJSON**](ImageUrlJSON.md)| ImageUrlJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_counterparty_more_info**
> SuccessMessage o_bpv1_2_1_add_counterparty_more_info(body, other_account_id, view_id, account_id, bank_id)

Add Counterparty More Info

<p>Add a description of the counter party from the perpestive of the account e.g. My dentist</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.MoreInfoJSON() # MoreInfoJSON | MoreInfoJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add Counterparty More Info
    api_response = api_instance.o_bpv1_2_1_add_counterparty_more_info(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_more_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoreInfoJSON**](MoreInfoJSON.md)| MoreInfoJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_counterparty_open_corporates_url**
> SuccessMessage o_bpv1_2_1_add_counterparty_open_corporates_url(body, other_account_id, view_id, account_id, bank_id)

Add Open Corporates URL to Counterparty

<p>Add open corporates url to other bank account</p><p>Authentication is Optional</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.OpenCorporateUrlJSON() # OpenCorporateUrlJSON | OpenCorporateUrlJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add Open Corporates URL to Counterparty
    api_response = api_instance.o_bpv1_2_1_add_counterparty_open_corporates_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_open_corporates_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenCorporateUrlJSON**](OpenCorporateUrlJSON.md)| OpenCorporateUrlJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_counterparty_physical_location**
> SuccessMessage o_bpv1_2_1_add_counterparty_physical_location(body, other_account_id, view_id, account_id, bank_id)

Add physical location to other bank account

<p>Add geocoordinates of the counterparty's main location</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.PhysicalLocationJSON() # PhysicalLocationJSON | PhysicalLocationJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add physical location to other bank account
    api_response = api_instance.o_bpv1_2_1_add_counterparty_physical_location(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_physical_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhysicalLocationJSON**](PhysicalLocationJSON.md)| PhysicalLocationJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_counterparty_public_alias**
> SuccessMessage o_bpv1_2_1_add_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)

Add public alias to other bank account

<p>Creates the public alias for the other account OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p><p>Note: Public aliases are automatically generated for new 'other accounts / counterparties', so this call should only be used if<br />the public alias was deleted.</p><p>The VIEW_ID parameter should be a view the caller is permitted to access to and that has permission to create public aliases.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.AliasJSON() # AliasJSON | AliasJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add public alias to other bank account
    api_response = api_instance.o_bpv1_2_1_add_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_public_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AliasJSON**](AliasJSON.md)| AliasJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_counterparty_url**
> SuccessMessage o_bpv1_2_1_add_counterparty_url(body, other_account_id, view_id, account_id, bank_id)

Add url to other bank account

<p>A url which represents the counterparty (home page url etc.)</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.UrlJSON() # UrlJSON | UrlJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add url to other bank account
    api_response = api_instance.o_bpv1_2_1_add_counterparty_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_counterparty_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlJSON**](UrlJSON.md)| UrlJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_add_other_account_private_alias**
> SuccessMessage o_bpv1_2_1_add_other_account_private_alias(body, other_account_id, view_id, account_id, bank_id)

Create Other Account Private Alias

<p>Creates a private alias for the other account OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.AliasJSON() # AliasJSON | AliasJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Other Account Private Alias
    api_response = api_instance.o_bpv1_2_1_add_other_account_private_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_add_other_account_private_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AliasJSON**](AliasJSON.md)| AliasJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_corporate_location**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_corporate_location(body, other_account_id, view_id, account_id, bank_id)

Delete Counterparty Corporate Location

<p>Delete corporate location of other bank account. Delete the geolocation of the counterparty's registered address</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty Corporate Location
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_corporate_location(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_corporate_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_image_url**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_image_url(body, other_account_id, view_id, account_id, bank_id)

Delete Counterparty Image URL

<p>Delete image url of other bank account</p><p>Authentication is Optional</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty Image URL
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_image_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_image_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_more_info**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_more_info(body, other_account_id, view_id, account_id, bank_id)

Delete more info of other bank account

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete more info of other bank account
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_more_info(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_more_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_open_corporates_url**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_open_corporates_url(body, other_account_id, view_id, account_id, bank_id)

Delete Counterparty Open Corporates URL

<p>Delete open corporate url of other bank account</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty Open Corporates URL
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_open_corporates_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_open_corporates_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_physical_location**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_physical_location(body, other_account_id, view_id, account_id, bank_id)

Delete Counterparty Physical Location

<p>Delete physical location of other bank account</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty Physical Location
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_physical_location(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_physical_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_private_alias**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_private_alias(body, other_account_id, view_id, account_id, bank_id)

Delete Counterparty Private Alias

<p>Deletes the private alias of the other account OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty Private Alias
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_private_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_private_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_public_alias**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)

Delete Counterparty Public Alias

<p>Deletes the public alias of the other account OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty Public Alias
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_public_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_delete_counterparty_url**
> EmptyClassJson o_bpv1_2_1_delete_counterparty_url(body, other_account_id, view_id, account_id, bank_id)

Delete url of other bank account

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete url of other bank account
    api_response = api_instance.o_bpv1_2_1_delete_counterparty_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_delete_counterparty_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_get_counterparty_public_alias**
> AliasJSON o_bpv1_2_1_get_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)

Get public alias of other bank account

<p>Returns the public alias of the other account OTHER_ACCOUNT_ID.<br />Authentication is Optional<br />Authentication is Mandatory if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get public alias of other bank account
    api_response = api_instance.o_bpv1_2_1_get_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_get_counterparty_public_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AliasJSON**](AliasJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_other_account_for_transaction**
> OtherAccountJSON o_bpv1_2_1_get_other_account_for_transaction(body, transaction_id, view_id, account_id, bank_id)

Get Other Account of Transaction

<p>Get other account of a transaction.<br />Returns details of the other party involved in the transaction, moderated by the <a href=\"#1_2_1-getViewsForBankAccount\">view</a> (VIEW_ID).<br />Authentication via OAuth is required if the view is not public.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
transaction_id = 'transaction_id_example' # str | The transaction id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Account of Transaction
    api_response = api_instance.o_bpv1_2_1_get_other_account_for_transaction(body, transaction_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_get_other_account_for_transaction: %s\n" % e)
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

[**OtherAccountJSON**](OtherAccountJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_other_account_metadata**
> OtherAccountMetadataJSON o_bpv1_2_1_get_other_account_metadata(body, other_account_id, view_id, account_id, bank_id)

Get Other Account Metadata

<p>Get metadata of one other account.<br />Returns only the metadata about one other bank account (OTHER_ACCOUNT_ID) that had shared at least one transaction with ACCOUNT_ID at BANK_ID.</p><p>Authentication via OAuth is required if the view is not public.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Account Metadata
    api_response = api_instance.o_bpv1_2_1_get_other_account_metadata(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_get_other_account_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**OtherAccountMetadataJSON**](OtherAccountMetadataJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_get_other_account_private_alias**
> AliasJSON o_bpv1_2_1_get_other_account_private_alias(body, other_account_id, view_id, account_id, bank_id)

Get Other Account Private Alias

<p>Returns the private alias of the other account OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Account Private Alias
    api_response = api_instance.o_bpv1_2_1_get_other_account_private_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_get_other_account_private_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AliasJSON**](AliasJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_2_1_update_counterparty_corporate_location**
> SuccessMessage o_bpv1_2_1_update_counterparty_corporate_location(body, other_account_id, view_id, account_id, bank_id)

Update Counterparty Corporate Location

<p>Update the geolocation of the counterparty's registered address</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.CorporateLocationJSON() # CorporateLocationJSON | CorporateLocationJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Counterparty Corporate Location
    api_response = api_instance.o_bpv1_2_1_update_counterparty_corporate_location(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_corporate_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorporateLocationJSON**](CorporateLocationJSON.md)| CorporateLocationJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_image_url**
> SuccessMessage o_bpv1_2_1_update_counterparty_image_url(body, other_account_id, view_id, account_id, bank_id)

Update Counterparty Image Url

<p>Update the url that points to the logo of the counterparty</p><p>Authentication is Optional</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.ImageUrlJSON() # ImageUrlJSON | ImageUrlJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Counterparty Image Url
    api_response = api_instance.o_bpv1_2_1_update_counterparty_image_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_image_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageUrlJSON**](ImageUrlJSON.md)| ImageUrlJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_more_info**
> SuccessMessage o_bpv1_2_1_update_counterparty_more_info(body, other_account_id, view_id, account_id, bank_id)

Update Counterparty More Info

<p>Update the more info description of the counter party from the perpestive of the account e.g. My dentist</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.MoreInfoJSON() # MoreInfoJSON | MoreInfoJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Counterparty More Info
    api_response = api_instance.o_bpv1_2_1_update_counterparty_more_info(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_more_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MoreInfoJSON**](MoreInfoJSON.md)| MoreInfoJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_open_corporates_url**
> SuccessMessage o_bpv1_2_1_update_counterparty_open_corporates_url(body, other_account_id, view_id, account_id, bank_id)

Update Open Corporates Url of Counterparty

<p>Update open corporate url of other bank account</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.OpenCorporateUrlJSON() # OpenCorporateUrlJSON | OpenCorporateUrlJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Open Corporates Url of Counterparty
    api_response = api_instance.o_bpv1_2_1_update_counterparty_open_corporates_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_open_corporates_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenCorporateUrlJSON**](OpenCorporateUrlJSON.md)| OpenCorporateUrlJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_physical_location**
> SuccessMessage o_bpv1_2_1_update_counterparty_physical_location(body, other_account_id, view_id, account_id, bank_id)

Update Counterparty Physical Location

<p>Update geocoordinates of the counterparty's main location</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.PhysicalLocationJSON() # PhysicalLocationJSON | PhysicalLocationJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Counterparty Physical Location
    api_response = api_instance.o_bpv1_2_1_update_counterparty_physical_location(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_physical_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhysicalLocationJSON**](PhysicalLocationJSON.md)| PhysicalLocationJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_private_alias**
> SuccessMessage o_bpv1_2_1_update_counterparty_private_alias(body, other_account_id, view_id, account_id, bank_id)

Update Counterparty Private Alias

<p>Updates the private alias of the counterparty (AKA other account) OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.AliasJSON() # AliasJSON | AliasJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Counterparty Private Alias
    api_response = api_instance.o_bpv1_2_1_update_counterparty_private_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_private_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AliasJSON**](AliasJSON.md)| AliasJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_public_alias**
> SuccessMessage o_bpv1_2_1_update_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)

Update public alias of other bank account

<p>Updates the public alias of the other account / counterparty OTHER_ACCOUNT_ID.</p><p>Authentication is Optional<br />Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.AliasJSON() # AliasJSON | AliasJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update public alias of other bank account
    api_response = api_instance.o_bpv1_2_1_update_counterparty_public_alias(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_public_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AliasJSON**](AliasJSON.md)| AliasJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv1_2_1_update_counterparty_url**
> SuccessMessage o_bpv1_2_1_update_counterparty_url(body, other_account_id, view_id, account_id, bank_id)

Update url of other bank account

<p>A url which represents the counterparty (home page url etc.)</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.UrlJSON() # UrlJSON | UrlJSON object that needs to be added.
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update url of other bank account
    api_response = api_instance.o_bpv1_2_1_update_counterparty_url(body, other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv1_2_1_update_counterparty_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UrlJSON**](UrlJSON.md)| UrlJSON object that needs to be added. | 
 **other_account_id** | **str**| The other account id | 
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

# **o_bpv3_0_0_get_other_account_by_id_for_bank_account**
> OtherAccountJsonV300 o_bpv3_0_0_get_other_account_by_id_for_bank_account(other_account_id, view_id, account_id, bank_id)

Get Other Account by Id

<p>Returns data about the Other Account that has shared at least one transaction with ACCOUNT_ID at BANK_ID.<br />Authentication is Optional</p><p>Authentication is required if the view is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
other_account_id = 'other_account_id_example' # str | The other account id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Account by Id
    api_response = api_instance.o_bpv3_0_0_get_other_account_by_id_for_bank_account(other_account_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv3_0_0_get_other_account_by_id_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **other_account_id** | **str**| The other account id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**OtherAccountJsonV300**](OtherAccountJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_other_accounts_for_bank_account**
> OtherAccountsJsonV300 o_bpv3_0_0_get_other_accounts_for_bank_account(view_id, account_id, bank_id)

Get Other Accounts of one Account

<p>Returns data about all the other accounts that have shared at least one transaction with the ACCOUNT_ID at BANK_ID.<br />Authentication is Optional</p><p>Authentication is required if the view VIEW_ID is not public.</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Other Accounts of one Account
    api_response = api_instance.o_bpv3_0_0_get_other_accounts_for_bank_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv3_0_0_get_other_accounts_for_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**OtherAccountsJsonV300**](OtherAccountsJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_counterparty**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_create_counterparty(body, view_id, account_id, bank_id)

Create Counterparty (Explicit)

<p>Create Counterparty (Explicit) for an Account.</p><p>In OBP, there are two types of Counterparty.</p><ul><li><p>Explicit Counterparties (those here) which we create explicitly and are used in COUNTERPARTY Transaction Requests</p></li><li><p>Implicit Counterparties (AKA Other Accounts) which are generated automatically from the other sides of Transactions.</p></li></ul><p>Explicit Counterparties are created for the account / view<br />They are how the user of the view (e.g. account owner) refers to the other side of the transaction</p><p>name : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>description : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>currency : counterparty account currency (e.g. EUR, GBP, USD, ...)</p><p>bank_routing_scheme : eg: bankId or bankCode or any other strings</p><p>bank_routing_address : eg: <code>gh.29.uk</code>, must be valid sandbox bankIds</p><p>account_routing_scheme : eg: AccountId or AccountNumber or any other strings</p><p>account_routing_address : eg: <code>1d65db7c-a7b2-4839-af41-95</code>, must be valid accountIds</p><p>other_account_secondary_routing_scheme : eg: IBan or any other strings</p><p>other_account_secondary_routing_address : if it is an IBAN, it should be unique for each counterparty.</p><p>other_branch_routing_scheme : eg: branchId or any other strings or you can leave it empty, not useful in sandbox mode.</p><p>other_branch_routing_address : eg: <code>branch-id-123</code> or you can leave it empty, not useful in sandbox mode.</p><p>is_beneficiary : must be set to <code>true</code> in order to send payments to this counterparty</p><p>bespoke: It supports a list of key-value, you can add it to the counterparty.</p><p>bespoke.key : any info-key you want to add to this counterparty</p><p>bespoke.value : any info-value you want to add to this counterparty</p><p>The view specified by VIEW_ID must have the canAddCounterparty permission</p><p>A minimal example for TransactionRequestType == COUNTERPARTY<br />{<br />&quot;name&quot;: &quot;Tesobe1&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;&quot;,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>A minimal example for TransactionRequestType == SEPA</p><p>{<br />&quot;name&quot;: &quot;Tesobe2&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;IBAN&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;DE89 3704 0044 0532 0130 00&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.PostCounterpartyJson400() # PostCounterpartyJson400 | PostCounterpartyJson400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Counterparty (Explicit)
    api_response = api_instance.o_bpv4_0_0_create_counterparty(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_create_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCounterpartyJson400**](PostCounterpartyJson400.md)| PostCounterpartyJson400 object that needs to be added. | 
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

# **o_bpv4_0_0_create_counterparty_for_any_account**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_create_counterparty_for_any_account(body, view_id, account_id, bank_id)

Create Counterparty for any account (Explicit)

<p>Create Counterparty for any Account. (Explicit)</p><p>In OBP, there are two types of Counterparty.</p><ul><li><p>Explicit Counterparties (those here) which we create explicitly and are used in COUNTERPARTY Transaction Requests</p></li><li><p>Implicit Counterparties (AKA Other Accounts) which are generated automatically from the other sides of Transactions.</p></li></ul><p>Explicit Counterparties are created for the account / view<br />They are how the user of the view (e.g. account owner) refers to the other side of the transaction</p><p>name : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>description : the human readable name (e.g. Piano teacher, Miss Nipa)</p><p>currency : counterparty account currency (e.g. EUR, GBP, USD, ...)</p><p>bank_routing_scheme : eg: bankId or bankCode or any other strings</p><p>bank_routing_address : eg: <code>gh.29.uk</code>, must be valid sandbox bankIds</p><p>account_routing_scheme : eg: AccountId or AccountNumber or any other strings</p><p>account_routing_address : eg: <code>1d65db7c-a7b2-4839-af41-95</code>, must be valid accountIds</p><p>other_account_secondary_routing_scheme : eg: IBan or any other strings</p><p>other_account_secondary_routing_address : if it is an IBAN, it should be unique for each counterparty.</p><p>other_branch_routing_scheme : eg: branchId or any other strings or you can leave it empty, not useful in sandbox mode.</p><p>other_branch_routing_address : eg: <code>branch-id-123</code> or you can leave it empty, not useful in sandbox mode.</p><p>is_beneficiary : must be set to <code>true</code> in order to send payments to this counterparty</p><p>bespoke: It supports a list of key-value, you can add it to the counterparty.</p><p>bespoke.key : any info-key you want to add to this counterparty</p><p>bespoke.value : any info-value you want to add to this counterparty</p><p>The view specified by VIEW_ID must have the canAddCounterparty permission</p><p>A minimal example for TransactionRequestType == COUNTERPARTY<br />{<br />&quot;name&quot;: &quot;Tesobe1&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;&quot;,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>A minimal example for TransactionRequestType == SEPA</p><p>{<br />&quot;name&quot;: &quot;Tesobe2&quot;,<br />&quot;description&quot;: &quot;Good Company&quot;,<br />&quot;currency&quot;: &quot;EUR&quot;,<br />&quot;other_bank_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_bank_routing_address&quot;: &quot;gh.29.uk&quot;,<br />&quot;other_account_routing_scheme&quot;: &quot;OBP&quot;,<br />&quot;other_account_routing_address&quot;: &quot;8ca8a7e4-6d02-48e3-a029-0b2bf89de9f0&quot;,<br />&quot;other_account_secondary_routing_scheme&quot;: &quot;IBAN&quot;,<br />&quot;other_account_secondary_routing_address&quot;: &quot;DE89 3704 0044 0532 0130 00&quot;,<br />&quot;is_beneficiary&quot;: true,<br />&quot;other_branch_routing_scheme&quot;: &quot;&quot;,<br />&quot;other_branch_routing_address&quot;: &quot;&quot;,<br />&quot;bespoke&quot;: []<br />}</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
body = obp_python.PostCounterpartyJson400() # PostCounterpartyJson400 | PostCounterpartyJson400 object that needs to be added.
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Counterparty for any account (Explicit)
    api_response = api_instance.o_bpv4_0_0_create_counterparty_for_any_account(body, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_create_counterparty_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCounterpartyJson400**](PostCounterpartyJson400.md)| PostCounterpartyJson400 object that needs to be added. | 
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

# **o_bpv4_0_0_delete_counterparty_for_any_account**
> o_bpv4_0_0_delete_counterparty_for_any_account(counterparty_id, view_id, account_id, bank_id)

Delete Counterparty for any account (Explicit)

<p>Delete Counterparty (Explicit) for any account<br />and also delete the Metadata for its counterparty.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty for any account (Explicit)
    api_instance.o_bpv4_0_0_delete_counterparty_for_any_account(counterparty_id, view_id, account_id, bank_id)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_delete_counterparty_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| the counterparty id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_explicit_counterparty**
> o_bpv4_0_0_delete_explicit_counterparty(counterparty_id, view_id, account_id, bank_id)

Delete Counterparty (Explicit)

<p>Delete Counterparty (Explicit) for an Account.<br />and also delete the Metadata for its counterparty.</p><p>need the view permission <code>can_delete_counterparty</code><br />Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Counterparty (Explicit)
    api_instance.o_bpv4_0_0_delete_explicit_counterparty(counterparty_id, view_id, account_id, bank_id)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_delete_explicit_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_id** | **str**| the counterparty id | 
 **view_id** | **str**| The view id | 
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties for any account (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_counterparties_for_any_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_get_counterparties_for_any_account: %s\n" % e)
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

# **o_bpv4_0_0_get_counterparty_by_id_for_any_account**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_get_counterparty_by_id_for_any_account(counterparty_id, view_id, account_id, bank_id)

Get Counterparty by Id for any account (Explicit) 

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by Id for any account (Explicit) 
    api_response = api_instance.o_bpv4_0_0_get_counterparty_by_id_for_any_account(counterparty_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_get_counterparty_by_id_for_any_account: %s\n" % e)
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

# **o_bpv4_0_0_get_counterparty_by_name_for_any_account**
> CounterpartyWithMetadataJson400 o_bpv4_0_0_get_counterparty_by_name_for_any_account(counterparty_name, view_id, account_id, bank_id)

Get Counterparty by name for any account (Explicit) 

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
counterparty_name = 'counterparty_name_example' # str | the counterparty name
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by name for any account (Explicit) 
    api_response = api_instance.o_bpv4_0_0_get_counterparty_by_name_for_any_account(counterparty_name, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_get_counterparty_by_name_for_any_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **counterparty_name** | **str**| the counterparty name | 
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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparties (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparties_for_account(view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_get_explict_counterparties_for_account: %s\n" % e)
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
api_instance = obp_python.CounterpartyApi(obp_python.ApiClient(configuration))
counterparty_id = 'counterparty_id_example' # str | the counterparty id
view_id = 'view_id_example' # str | The view id
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Counterparty by Id (Explicit)
    api_response = api_instance.o_bpv4_0_0_get_explict_counterparty_by_id(counterparty_id, view_id, account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->o_bpv4_0_0_get_explict_counterparty_by_id: %s\n" % e)
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

