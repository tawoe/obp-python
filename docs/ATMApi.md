# obp_python.ATMApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_atm**](ATMApi.md#o_bpv4_0_0_create_atm) | **POST** /obp/v5.0.0/banks/{BANK_ID}/atms | Create ATM
[**o_bpv4_0_0_delete_atm**](ATMApi.md#o_bpv4_0_0_delete_atm) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID} | Delete ATM
[**o_bpv4_0_0_get_atm**](ATMApi.md#o_bpv4_0_0_get_atm) | **GET** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID} | Get Bank ATM
[**o_bpv4_0_0_get_atms**](ATMApi.md#o_bpv4_0_0_get_atms) | **GET** /obp/v5.0.0/banks/{BANK_ID}/atms | Get Bank ATMS
[**o_bpv4_0_0_update_atm**](ATMApi.md#o_bpv4_0_0_update_atm) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID} | UPDATE ATM
[**o_bpv4_0_0_update_atm_accessibility_features**](ATMApi.md#o_bpv4_0_0_update_atm_accessibility_features) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID}/accessibility-features | Update ATM Accessibility Features
[**o_bpv4_0_0_update_atm_location_categories**](ATMApi.md#o_bpv4_0_0_update_atm_location_categories) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID}/location-categories | Update ATM Location Categories
[**o_bpv4_0_0_update_atm_notes**](ATMApi.md#o_bpv4_0_0_update_atm_notes) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID}/notes | Update ATM Notes
[**o_bpv4_0_0_update_atm_services**](ATMApi.md#o_bpv4_0_0_update_atm_services) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID}/services | Update ATM Services
[**o_bpv4_0_0_update_atm_supported_currencies**](ATMApi.md#o_bpv4_0_0_update_atm_supported_currencies) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID}/supported-currencies | Update ATM Supported Currencies
[**o_bpv4_0_0_update_atm_supported_languages**](ATMApi.md#o_bpv4_0_0_update_atm_supported_languages) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/atms/{ATM_ID}/supported-languages | Update ATM Supported Languages
[**o_bpv5_0_0_head_atms**](ATMApi.md#o_bpv5_0_0_head_atms) | **HEAD** /obp/v5.0.0/banks/{BANK_ID}/atms | Head Bank ATMS


# **o_bpv4_0_0_create_atm**
> AtmJsonV400 o_bpv4_0_0_create_atm(body, bank_id)

Create ATM

<p>Create ATM.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AtmJsonV400() # AtmJsonV400 | AtmJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create ATM
    api_response = api_instance.o_bpv4_0_0_create_atm(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_create_atm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmJsonV400**](AtmJsonV400.md)| AtmJsonV400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmJsonV400**](AtmJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_atm**
> AtmJsonV400 o_bpv4_0_0_delete_atm(body, atm_id, bank_id)

Delete ATM

<p>Delete ATM.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AtmJsonV400() # AtmJsonV400 | AtmJsonV400 object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete ATM
    api_response = api_instance.o_bpv4_0_0_delete_atm(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_delete_atm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmJsonV400**](AtmJsonV400.md)| AtmJsonV400 object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmJsonV400**](AtmJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_atm**
> AtmJsonV400 o_bpv4_0_0_get_atm(atm_id, bank_id)

Get Bank ATM

<p>Returns information about ATM for a single bank specified by BANK_ID and ATM_ID including:</p><ul><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under<br />Authentication is Optional</li></ul>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank ATM
    api_response = api_instance.o_bpv4_0_0_get_atm(atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_get_atm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmJsonV400**](AtmJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_atms**
> AtmsJsonV400 o_bpv4_0_0_get_atms(bank_id)

Get Bank ATMS

<p>Get Bank ATMS.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank ATMS
    api_response = api_instance.o_bpv4_0_0_get_atms(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_get_atms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmsJsonV400**](AtmsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm**
> AtmJsonV400 o_bpv4_0_0_update_atm(body, atm_id, bank_id)

UPDATE ATM

<p>Update ATM.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AtmJsonV400() # AtmJsonV400 | AtmJsonV400 object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # UPDATE ATM
    api_response = api_instance.o_bpv4_0_0_update_atm(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmJsonV400**](AtmJsonV400.md)| AtmJsonV400 object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmJsonV400**](AtmJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm_accessibility_features**
> AtmAccessibilityFeaturesJson o_bpv4_0_0_update_atm_accessibility_features(body, atm_id, bank_id)

Update ATM Accessibility Features

<p>Update ATM Accessibility Features.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AccessibilityFeaturesJson() # AccessibilityFeaturesJson | AccessibilityFeaturesJson object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update ATM Accessibility Features
    api_response = api_instance.o_bpv4_0_0_update_atm_accessibility_features(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm_accessibility_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessibilityFeaturesJson**](AccessibilityFeaturesJson.md)| AccessibilityFeaturesJson object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmAccessibilityFeaturesJson**](AtmAccessibilityFeaturesJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm_location_categories**
> AtmLocationCategoriesResponseJsonV400 o_bpv4_0_0_update_atm_location_categories(body, atm_id, bank_id)

Update ATM Location Categories

<p>Update ATM Location Categories.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AtmLocationCategoriesJsonV400() # AtmLocationCategoriesJsonV400 | AtmLocationCategoriesJsonV400 object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update ATM Location Categories
    api_response = api_instance.o_bpv4_0_0_update_atm_location_categories(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm_location_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmLocationCategoriesJsonV400**](AtmLocationCategoriesJsonV400.md)| AtmLocationCategoriesJsonV400 object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmLocationCategoriesResponseJsonV400**](AtmLocationCategoriesResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm_notes**
> AtmNotesResponseJsonV400 o_bpv4_0_0_update_atm_notes(body, atm_id, bank_id)

Update ATM Notes

<p>Update ATM Notes.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AtmNotesJsonV400() # AtmNotesJsonV400 | AtmNotesJsonV400 object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update ATM Notes
    api_response = api_instance.o_bpv4_0_0_update_atm_notes(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmNotesJsonV400**](AtmNotesJsonV400.md)| AtmNotesJsonV400 object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmNotesResponseJsonV400**](AtmNotesResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm_services**
> AtmServicesResponseJsonV400 o_bpv4_0_0_update_atm_services(body, atm_id, bank_id)

Update ATM Services

<p>Update ATM Services.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.AtmServicesJsonV400() # AtmServicesJsonV400 | AtmServicesJsonV400 object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update ATM Services
    api_response = api_instance.o_bpv4_0_0_update_atm_services(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AtmServicesJsonV400**](AtmServicesJsonV400.md)| AtmServicesJsonV400 object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmServicesResponseJsonV400**](AtmServicesResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm_supported_currencies**
> AtmSupportedCurrenciesJson o_bpv4_0_0_update_atm_supported_currencies(body, atm_id, bank_id)

Update ATM Supported Currencies

<p>Update ATM Supported Currencies.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.SupportedCurrenciesJson() # SupportedCurrenciesJson | SupportedCurrenciesJson object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update ATM Supported Currencies
    api_response = api_instance.o_bpv4_0_0_update_atm_supported_currencies(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm_supported_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportedCurrenciesJson**](SupportedCurrenciesJson.md)| SupportedCurrenciesJson object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmSupportedCurrenciesJson**](AtmSupportedCurrenciesJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_atm_supported_languages**
> AtmSupportedLanguagesJson o_bpv4_0_0_update_atm_supported_languages(body, atm_id, bank_id)

Update ATM Supported Languages

<p>Update ATM Supported Languages.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
body = obp_python.SupportedLanguagesJson() # SupportedLanguagesJson | SupportedLanguagesJson object that needs to be added.
atm_id = 'atm_id_example' # str | the atm id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update ATM Supported Languages
    api_response = api_instance.o_bpv4_0_0_update_atm_supported_languages(body, atm_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv4_0_0_update_atm_supported_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupportedLanguagesJson**](SupportedLanguagesJson.md)| SupportedLanguagesJson object that needs to be added. | 
 **atm_id** | **str**| the atm id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmSupportedLanguagesJson**](AtmSupportedLanguagesJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_head_atms**
> AtmsJsonV400 o_bpv5_0_0_head_atms(bank_id)

Head Bank ATMS

<p>Head Bank ATMS.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ATMApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Head Bank ATMS
    api_response = api_instance.o_bpv5_0_0_head_atms(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ATMApi->o_bpv5_0_0_head_atms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AtmsJsonV400**](AtmsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

