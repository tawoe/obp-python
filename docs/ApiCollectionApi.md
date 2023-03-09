# obp_python.ApiCollectionApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_my_api_collection**](ApiCollectionApi.md#o_bpv4_0_0_create_my_api_collection) | **POST** /obp/v5.0.0/my/api-collections | Create My Api Collection
[**o_bpv4_0_0_create_my_api_collection_endpoint**](ApiCollectionApi.md#o_bpv4_0_0_create_my_api_collection_endpoint) | **POST** /obp/v5.0.0/my/api-collections/API_COLLECTION_NAME/api-collection-endpoints | Create My Api Collection Endpoint
[**o_bpv4_0_0_create_my_api_collection_endpoint_by_id**](ApiCollectionApi.md#o_bpv4_0_0_create_my_api_collection_endpoint_by_id) | **POST** /obp/v5.0.0/my/api-collection-ids/API_COLLECTION_ID/api-collection-endpoints | Create My Api Collection Endpoint By Id
[**o_bpv4_0_0_delete_my_api_collection**](ApiCollectionApi.md#o_bpv4_0_0_delete_my_api_collection) | **DELETE** /obp/v5.0.0/my/api-collections/API_COLLECTION_ID | Delete My Api Collection
[**o_bpv4_0_0_delete_my_api_collection_endpoint**](ApiCollectionApi.md#o_bpv4_0_0_delete_my_api_collection_endpoint) | **DELETE** /obp/v5.0.0/my/api-collections/API_COLLECTION_NAME/api-collection-endpoints/OPERATION_ID | Delete My Api Collection Endpoint
[**o_bpv4_0_0_delete_my_api_collection_endpoint_by_id**](ApiCollectionApi.md#o_bpv4_0_0_delete_my_api_collection_endpoint_by_id) | **DELETE** /obp/v5.0.0/my/api-collection-ids/API_COLLECTION_ID/api-collection-endpoint-ids/API_COLLECTION_ENDPOINT_ID | Delete My Api Collection Endpoint By Id
[**o_bpv4_0_0_delete_my_api_collection_endpoint_by_operation_id**](ApiCollectionApi.md#o_bpv4_0_0_delete_my_api_collection_endpoint_by_operation_id) | **DELETE** /obp/v5.0.0/my/api-collection-ids/API_COLLECTION_ID/api-collection-endpoints/OPERATION_ID | Delete My Api Collection Endpoint By Id
[**o_bpv4_0_0_get_api_collection_endpoints**](ApiCollectionApi.md#o_bpv4_0_0_get_api_collection_endpoints) | **GET** /obp/v5.0.0/api-collections/API_COLLECTION_ID/api-collection-endpoints | Get Api Collection Endpoints
[**o_bpv4_0_0_get_api_collections_for_user**](ApiCollectionApi.md#o_bpv4_0_0_get_api_collections_for_user) | **GET** /obp/v5.0.0/users/{USER_ID}/api-collections | Get Api Collections for User
[**o_bpv4_0_0_get_featured_api_collections**](ApiCollectionApi.md#o_bpv4_0_0_get_featured_api_collections) | **GET** /obp/v5.0.0/api-collections/featured | Get Featured Api Collections
[**o_bpv4_0_0_get_my_api_collection_by_id**](ApiCollectionApi.md#o_bpv4_0_0_get_my_api_collection_by_id) | **GET** /obp/v5.0.0/my/api-collections/API_COLLECTION_ID | Get My Api Collection By Id
[**o_bpv4_0_0_get_my_api_collection_by_name**](ApiCollectionApi.md#o_bpv4_0_0_get_my_api_collection_by_name) | **GET** /obp/v5.0.0/my/api-collections/name/API_COLLECTION_NAME | Get My Api Collection By Name
[**o_bpv4_0_0_get_my_api_collection_endpoint**](ApiCollectionApi.md#o_bpv4_0_0_get_my_api_collection_endpoint) | **GET** /obp/v5.0.0/my/api-collections/API_COLLECTION_NAME/api-collection-endpoints/OPERATION_ID | Get My Api Collection Endpoint
[**o_bpv4_0_0_get_my_api_collection_endpoints**](ApiCollectionApi.md#o_bpv4_0_0_get_my_api_collection_endpoints) | **GET** /obp/v5.0.0/my/api-collections/API_COLLECTION_NAME/api-collection-endpoints | Get My Api Collection Endpoints
[**o_bpv4_0_0_get_my_api_collection_endpoints_by_id**](ApiCollectionApi.md#o_bpv4_0_0_get_my_api_collection_endpoints_by_id) | **GET** /obp/v5.0.0/my/api-collection-ids/API_COLLECTION_ID/api-collection-endpoints | Get My Api Collection Endpoints By Id
[**o_bpv4_0_0_get_my_api_collections**](ApiCollectionApi.md#o_bpv4_0_0_get_my_api_collections) | **GET** /obp/v5.0.0/my/api-collections | Get My Api Collections
[**o_bpv4_0_0_get_sharable_api_collection_by_id**](ApiCollectionApi.md#o_bpv4_0_0_get_sharable_api_collection_by_id) | **GET** /obp/v5.0.0/api-collections/sharable/API_COLLECTION_ID | Get Sharable Api Collection By Id


# **o_bpv4_0_0_create_my_api_collection**
> ApiCollectionJson400 o_bpv4_0_0_create_my_api_collection(body)

Create My Api Collection

<p>Create Api Collection for logged in user.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))
body = obp_python.PostApiCollectionJson400() # PostApiCollectionJson400 | PostApiCollectionJson400 object that needs to be added.

try:
    # Create My Api Collection
    api_response = api_instance.o_bpv4_0_0_create_my_api_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_create_my_api_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostApiCollectionJson400**](PostApiCollectionJson400.md)| PostApiCollectionJson400 object that needs to be added. | 

### Return type

[**ApiCollectionJson400**](ApiCollectionJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_my_api_collection_endpoint**
> ApiCollectionEndpointJson400 o_bpv4_0_0_create_my_api_collection_endpoint(body)

Create My Api Collection Endpoint

<p>Create Api Collection Endpoint.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))
body = obp_python.PostApiCollectionEndpointJson400() # PostApiCollectionEndpointJson400 | PostApiCollectionEndpointJson400 object that needs to be added.

try:
    # Create My Api Collection Endpoint
    api_response = api_instance.o_bpv4_0_0_create_my_api_collection_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_create_my_api_collection_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostApiCollectionEndpointJson400**](PostApiCollectionEndpointJson400.md)| PostApiCollectionEndpointJson400 object that needs to be added. | 

### Return type

[**ApiCollectionEndpointJson400**](ApiCollectionEndpointJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_my_api_collection_endpoint_by_id**
> ApiCollectionEndpointJson400 o_bpv4_0_0_create_my_api_collection_endpoint_by_id(body)

Create My Api Collection Endpoint By Id

<p>Create Api Collection Endpoint By Id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))
body = obp_python.PostApiCollectionEndpointJson400() # PostApiCollectionEndpointJson400 | PostApiCollectionEndpointJson400 object that needs to be added.

try:
    # Create My Api Collection Endpoint By Id
    api_response = api_instance.o_bpv4_0_0_create_my_api_collection_endpoint_by_id(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_create_my_api_collection_endpoint_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostApiCollectionEndpointJson400**](PostApiCollectionEndpointJson400.md)| PostApiCollectionEndpointJson400 object that needs to be added. | 

### Return type

[**ApiCollectionEndpointJson400**](ApiCollectionEndpointJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_api_collection**
> Full o_bpv4_0_0_delete_my_api_collection()

Delete My Api Collection

<p>Delete Api Collection By API_COLLECTION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Delete My Api Collection
    api_response = api_instance.o_bpv4_0_0_delete_my_api_collection()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_delete_my_api_collection: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_api_collection_endpoint**
> Full o_bpv4_0_0_delete_my_api_collection_endpoint()

Delete My Api Collection Endpoint

<p>Delete Api Collection Endpoint By OPERATION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Delete My Api Collection Endpoint
    api_response = api_instance.o_bpv4_0_0_delete_my_api_collection_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_delete_my_api_collection_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_api_collection_endpoint_by_id**
> Full o_bpv4_0_0_delete_my_api_collection_endpoint_by_id()

Delete My Api Collection Endpoint By Id

<p>Delete Api Collection Endpoint<br />Delete Api Collection Endpoint By Id</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Delete My Api Collection Endpoint By Id
    api_response = api_instance.o_bpv4_0_0_delete_my_api_collection_endpoint_by_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_delete_my_api_collection_endpoint_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_api_collection_endpoint_by_operation_id**
> Full o_bpv4_0_0_delete_my_api_collection_endpoint_by_operation_id()

Delete My Api Collection Endpoint By Id

<p>Delete Api Collection Endpoint By OPERATION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Delete My Api Collection Endpoint By Id
    api_response = api_instance.o_bpv4_0_0_delete_my_api_collection_endpoint_by_operation_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_delete_my_api_collection_endpoint_by_operation_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_api_collection_endpoints**
> ApiCollectionEndpointsJson400 o_bpv4_0_0_get_api_collection_endpoints()

Get Api Collection Endpoints

<p>Get Api Collection Endpoints By API_COLLECTION_ID.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get Api Collection Endpoints
    api_response = api_instance.o_bpv4_0_0_get_api_collection_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_api_collection_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionEndpointsJson400**](ApiCollectionEndpointsJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_api_collections_for_user**
> ApiCollectionsJson400 o_bpv4_0_0_get_api_collections_for_user(user_id)

Get Api Collections for User

<p>Get Api Collections for User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id

try:
    # Get Api Collections for User
    api_response = api_instance.o_bpv4_0_0_get_api_collections_for_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_api_collections_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 

### Return type

[**ApiCollectionsJson400**](ApiCollectionsJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_featured_api_collections**
> ApiCollectionsJson400 o_bpv4_0_0_get_featured_api_collections()

Get Featured Api Collections

<p>Get Featured Api Collections.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get Featured Api Collections
    api_response = api_instance.o_bpv4_0_0_get_featured_api_collections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_featured_api_collections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionsJson400**](ApiCollectionsJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_api_collection_by_id**
> ApiCollectionJson400 o_bpv4_0_0_get_my_api_collection_by_id()

Get My Api Collection By Id

<p>Get Api Collection By API_COLLECTION_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get My Api Collection By Id
    api_response = api_instance.o_bpv4_0_0_get_my_api_collection_by_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_my_api_collection_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionJson400**](ApiCollectionJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_api_collection_by_name**
> ApiCollectionJson400 o_bpv4_0_0_get_my_api_collection_by_name()

Get My Api Collection By Name

<p>Get Api Collection By API_COLLECTION_NAME.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get My Api Collection By Name
    api_response = api_instance.o_bpv4_0_0_get_my_api_collection_by_name()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_my_api_collection_by_name: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionJson400**](ApiCollectionJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_api_collection_endpoint**
> ApiCollectionEndpointJson400 o_bpv4_0_0_get_my_api_collection_endpoint()

Get My Api Collection Endpoint

<p>Get Api Collection Endpoint By API_COLLECTION_NAME and OPERATION_ID.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get My Api Collection Endpoint
    api_response = api_instance.o_bpv4_0_0_get_my_api_collection_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_my_api_collection_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionEndpointJson400**](ApiCollectionEndpointJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_api_collection_endpoints**
> ApiCollectionEndpointsJson400 o_bpv4_0_0_get_my_api_collection_endpoints()

Get My Api Collection Endpoints

<p>Get Api Collection Endpoints By API_COLLECTION_NAME.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get My Api Collection Endpoints
    api_response = api_instance.o_bpv4_0_0_get_my_api_collection_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_my_api_collection_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionEndpointsJson400**](ApiCollectionEndpointsJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_api_collection_endpoints_by_id**
> ApiCollectionEndpointsJson400 o_bpv4_0_0_get_my_api_collection_endpoints_by_id()

Get My Api Collection Endpoints By Id

<p>Get Api Collection Endpoints By API_COLLECTION_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get My Api Collection Endpoints By Id
    api_response = api_instance.o_bpv4_0_0_get_my_api_collection_endpoints_by_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_my_api_collection_endpoints_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionEndpointsJson400**](ApiCollectionEndpointsJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_api_collections**
> ApiCollectionsJson400 o_bpv4_0_0_get_my_api_collections()

Get My Api Collections

<p>Get all the apiCollections for logged in user.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get My Api Collections
    api_response = api_instance.o_bpv4_0_0_get_my_api_collections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_my_api_collections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionsJson400**](ApiCollectionsJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_sharable_api_collection_by_id**
> ApiCollectionJson400 o_bpv4_0_0_get_sharable_api_collection_by_id()

Get Sharable Api Collection By Id

<p>Get Sharable Api Collection By Id.<br />Authentication is Optional</p>

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
api_instance = obp_python.ApiCollectionApi(obp_python.ApiClient(configuration))

try:
    # Get Sharable Api Collection By Id
    api_response = api_instance.o_bpv4_0_0_get_sharable_api_collection_by_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiCollectionApi->o_bpv4_0_0_get_sharable_api_collection_by_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiCollectionJson400**](ApiCollectionJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

