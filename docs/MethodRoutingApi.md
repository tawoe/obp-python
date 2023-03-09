# obp_python.MethodRoutingApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_method_routing**](MethodRoutingApi.md#o_bpv3_1_0_create_method_routing) | **POST** /obp/v5.0.0/management/method_routings | Create MethodRouting
[**o_bpv3_1_0_delete_method_routing**](MethodRoutingApi.md#o_bpv3_1_0_delete_method_routing) | **DELETE** /obp/v5.0.0/management/method_routings/{METHOD_ROUTING_ID} | Delete MethodRouting
[**o_bpv3_1_0_get_method_routings**](MethodRoutingApi.md#o_bpv3_1_0_get_method_routings) | **GET** /obp/v5.0.0/management/method_routings | Get MethodRoutings
[**o_bpv3_1_0_update_method_routing**](MethodRoutingApi.md#o_bpv3_1_0_update_method_routing) | **PUT** /obp/v5.0.0/management/method_routings/{METHOD_ROUTING_ID} | Update MethodRouting


# **o_bpv3_1_0_create_method_routing**
> MethodRoutingCommons o_bpv3_1_0_create_method_routing(body)

Create MethodRouting

<p>Create a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explanation of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some parameters for this method</li></ul><p>note and CAVEAT!:</p><ul><li>bank_id_pattern has to be empty for methods that do not take bank_id as a function parameter, otherwise might get empty result</li><li>methods that aggregate bank objects (e.g. getBankAccountsForUser) have to take any  existing method routings for these objects into consideration</li><li>so if you create e.g. a bank specific method routing for getting an account, make sure that it is also served by endpoints getting ALL accounts for ALL banks</li><li>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</li></ul><p>If the connector name starts with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

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
api_instance = obp_python.MethodRoutingApi(obp_python.ApiClient(configuration))
body = obp_python.MethodRoutingCommons() # MethodRoutingCommons | MethodRoutingCommons object that needs to be added.

try:
    # Create MethodRouting
    api_response = api_instance.o_bpv3_1_0_create_method_routing(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MethodRoutingApi->o_bpv3_1_0_create_method_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MethodRoutingCommons**](MethodRoutingCommons.md)| MethodRoutingCommons object that needs to be added. | 

### Return type

[**MethodRoutingCommons**](MethodRoutingCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_method_routing**
> o_bpv3_1_0_delete_method_routing(method_routing_id)

Delete MethodRouting

<p>Delete a MethodRouting specified by METHOD_ROUTING_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MethodRoutingApi(obp_python.ApiClient(configuration))
method_routing_id = 'method_routing_id_example' # str | the method routing id 

try:
    # Delete MethodRouting
    api_instance.o_bpv3_1_0_delete_method_routing(method_routing_id)
except ApiException as e:
    print("Exception when calling MethodRoutingApi->o_bpv3_1_0_delete_method_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_routing_id** | **str**| the method routing id  | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_method_routings**
> InlineResponse20010 o_bpv3_1_0_get_method_routings()

Get MethodRoutings

<p>Get the all MethodRoutings.</p><p>Query url parameters:</p><ul><li>method_name: filter with method_name</li><li>active: if active = true, it will show all the webui_ props. Even if they are set yet, we will return all the default webui_ props</li></ul><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.MethodRoutingApi(obp_python.ApiClient(configuration))

try:
    # Get MethodRoutings
    api_response = api_instance.o_bpv3_1_0_get_method_routings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MethodRoutingApi->o_bpv3_1_0_get_method_routings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_method_routing**
> MethodRoutingCommons o_bpv3_1_0_update_method_routing(body, method_routing_id)

Update MethodRouting

<p>Update a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some paremeters for this method<br />note:</li><li><p>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</p></li></ul><p>If connector name start with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, to convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

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
api_instance = obp_python.MethodRoutingApi(obp_python.ApiClient(configuration))
body = obp_python.MethodRoutingCommons() # MethodRoutingCommons | MethodRoutingCommons object that needs to be added.
method_routing_id = 'method_routing_id_example' # str | the method routing id 

try:
    # Update MethodRouting
    api_response = api_instance.o_bpv3_1_0_update_method_routing(body, method_routing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MethodRoutingApi->o_bpv3_1_0_update_method_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MethodRoutingCommons**](MethodRoutingCommons.md)| MethodRoutingCommons object that needs to be added. | 
 **method_routing_id** | **str**| the method routing id  | 

### Return type

[**MethodRoutingCommons**](MethodRoutingCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

