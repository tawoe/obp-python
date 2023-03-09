# obp_python.ViewSystemApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv5_0_0_create_system_view**](ViewSystemApi.md#o_bpv5_0_0_create_system_view) | **POST** /obp/v5.0.0/system-views | Create System View
[**o_bpv5_0_0_delete_system_view**](ViewSystemApi.md#o_bpv5_0_0_delete_system_view) | **DELETE** /obp/v5.0.0/system-views/{VIEW_ID} | Delete System View
[**o_bpv5_0_0_get_system_view**](ViewSystemApi.md#o_bpv5_0_0_get_system_view) | **GET** /obp/v5.0.0/system-views/{VIEW_ID} | Get System View
[**o_bpv5_0_0_get_system_views_ids**](ViewSystemApi.md#o_bpv5_0_0_get_system_views_ids) | **GET** /obp/v5.0.0/system-views-ids | Get Ids of System Views
[**o_bpv5_0_0_update_system_view**](ViewSystemApi.md#o_bpv5_0_0_update_system_view) | **PUT** /obp/v5.0.0/system-views/{VIEW_ID} | Update System View


# **o_bpv5_0_0_create_system_view**
> ViewJsonV500 o_bpv5_0_0_create_system_view(body)

Create System View

<p>Create a system view</p><p>Authentication is Mandatory and the user needs to have access to the CanCreateSystemView entitlement.<br />The 'alias' field in the JSON can take one of two values:</p><ul><li><em>public</em>: to use the public alias if there is one specified for the other account.</li><li><em>private</em>: to use the public alias if there is one specified for the other account.</li><li><p><em>''(empty string)</em>: to use no alias; the view shows the real name of the other account.</p></li></ul><p>The 'hide_metadata_if_alias_used' field in the JSON can take boolean values. If it is set to <code>true</code> and there is an alias on the other account then the other accounts' metadata (like more_info, url, image_url, open_corporates_url, etc.) will be hidden. Otherwise the metadata will be shown.</p><p>The 'allowed_actions' field is a list containing the name of the actions allowed on this view, all the actions contained will be set to <code>true</code> on the view creation, the rest will be set to <code>false</code>.</p><p>Please note that system views cannot be public. In case you try to set it you will get the error OBP-30258: System view cannot be public</p>

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
api_instance = obp_python.ViewSystemApi(obp_python.ApiClient(configuration))
body = obp_python.CreateViewJsonV500() # CreateViewJsonV500 | CreateViewJsonV500 object that needs to be added.

try:
    # Create System View
    api_response = api_instance.o_bpv5_0_0_create_system_view(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewSystemApi->o_bpv5_0_0_create_system_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateViewJsonV500**](CreateViewJsonV500.md)| CreateViewJsonV500 object that needs to be added. | 

### Return type

[**ViewJsonV500**](ViewJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_delete_system_view**
> o_bpv5_0_0_delete_system_view(view_id)

Delete System View

<p>Deletes the system view specified by VIEW_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ViewSystemApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id

try:
    # Delete System View
    api_instance.o_bpv5_0_0_delete_system_view(view_id)
except ApiException as e:
    print("Exception when calling ViewSystemApi->o_bpv5_0_0_delete_system_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_system_view**
> ViewJsonV500 o_bpv5_0_0_get_system_view(view_id)

Get System View

<p>Get System View</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ViewSystemApi(obp_python.ApiClient(configuration))
view_id = 'view_id_example' # str | The view id

try:
    # Get System View
    api_response = api_instance.o_bpv5_0_0_get_system_view(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewSystemApi->o_bpv5_0_0_get_system_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| The view id | 

### Return type

[**ViewJsonV500**](ViewJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_system_views_ids**
> ViewsIdsJsonV500 o_bpv5_0_0_get_system_views_ids()

Get Ids of System Views

<p>Get Ids of System Views</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ViewSystemApi(obp_python.ApiClient(configuration))

try:
    # Get Ids of System Views
    api_response = api_instance.o_bpv5_0_0_get_system_views_ids()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewSystemApi->o_bpv5_0_0_get_system_views_ids: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ViewsIdsJsonV500**](ViewsIdsJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_update_system_view**
> ViewJsonV500 o_bpv5_0_0_update_system_view(body, view_id)

Update System View

<p>Update an existing view on a bank account</p><p>Authentication is Mandatory and the user needs to have access to the owner view.</p><p>The json sent is the same as during view creation (above), with one difference: the 'name' field<br />of a view is not editable (it is only set when a view is created)</p>

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
api_instance = obp_python.ViewSystemApi(obp_python.ApiClient(configuration))
body = obp_python.UpdateViewJsonV500() # UpdateViewJsonV500 | UpdateViewJsonV500 object that needs to be added.
view_id = 'view_id_example' # str | The view id

try:
    # Update System View
    api_response = api_instance.o_bpv5_0_0_update_system_view(body, view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewSystemApi->o_bpv5_0_0_update_system_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateViewJsonV500**](UpdateViewJsonV500.md)| UpdateViewJsonV500 object that needs to be added. | 
 **view_id** | **str**| The view id | 

### Return type

[**ViewJsonV500**](ViewJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

