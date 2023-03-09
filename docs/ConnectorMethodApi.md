# obp_python.ConnectorMethodApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_connector_method**](ConnectorMethodApi.md#o_bpv4_0_0_create_connector_method) | **POST** /obp/v5.0.0/management/connector-methods | Create Connector Method
[**o_bpv4_0_0_get_all_connector_methods**](ConnectorMethodApi.md#o_bpv4_0_0_get_all_connector_methods) | **GET** /obp/v5.0.0/management/connector-methods | Get all Connector Methods
[**o_bpv4_0_0_get_connector_method**](ConnectorMethodApi.md#o_bpv4_0_0_get_connector_method) | **GET** /obp/v5.0.0/management/connector-methods/CONNECTOR_METHOD_ID | Get Connector Method by Id
[**o_bpv4_0_0_update_connector_method**](ConnectorMethodApi.md#o_bpv4_0_0_update_connector_method) | **PUT** /obp/v5.0.0/management/connector-methods/CONNECTOR_METHOD_ID | Update Connector Method


# **o_bpv4_0_0_create_connector_method**
> JsonConnectorMethod o_bpv4_0_0_create_connector_method(body)

Create Connector Method

<p>Create an internal connector.</p><p>The method_body is URL-encoded format String</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConnectorMethodApi(obp_python.ApiClient(configuration))
body = obp_python.JsonConnectorMethod() # JsonConnectorMethod | JsonConnectorMethod object that needs to be added.

try:
    # Create Connector Method
    api_response = api_instance.o_bpv4_0_0_create_connector_method(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorMethodApi->o_bpv4_0_0_create_connector_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonConnectorMethod**](JsonConnectorMethod.md)| JsonConnectorMethod object that needs to be added. | 

### Return type

[**JsonConnectorMethod**](JsonConnectorMethod.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_all_connector_methods**
> InlineResponse2008 o_bpv4_0_0_get_all_connector_methods()

Get all Connector Methods

<p>Get all Connector Methods.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConnectorMethodApi(obp_python.ApiClient(configuration))

try:
    # Get all Connector Methods
    api_response = api_instance.o_bpv4_0_0_get_all_connector_methods()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorMethodApi->o_bpv4_0_0_get_all_connector_methods: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_connector_method**
> JsonConnectorMethod o_bpv4_0_0_get_connector_method()

Get Connector Method by Id

<p>Get an internal connector by CONNECTOR_METHOD_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConnectorMethodApi(obp_python.ApiClient(configuration))

try:
    # Get Connector Method by Id
    api_response = api_instance.o_bpv4_0_0_get_connector_method()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorMethodApi->o_bpv4_0_0_get_connector_method: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonConnectorMethod**](JsonConnectorMethod.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_connector_method**
> JsonConnectorMethod o_bpv4_0_0_update_connector_method(body)

Update Connector Method

<p>Update an internal connector.</p><p>The method_body is URL-encoded format String</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConnectorMethodApi(obp_python.ApiClient(configuration))
body = obp_python.JsonConnectorMethodMethodBody() # JsonConnectorMethodMethodBody | JsonConnectorMethodMethodBody object that needs to be added.

try:
    # Update Connector Method
    api_response = api_instance.o_bpv4_0_0_update_connector_method(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorMethodApi->o_bpv4_0_0_update_connector_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonConnectorMethodMethodBody**](JsonConnectorMethodMethodBody.md)| JsonConnectorMethodMethodBody object that needs to be added. | 

### Return type

[**JsonConnectorMethod**](JsonConnectorMethod.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

