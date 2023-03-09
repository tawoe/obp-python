# obp_python.WebUiPropsApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_web_ui_props**](WebUiPropsApi.md#o_bpv3_1_0_create_web_ui_props) | **POST** /obp/v5.0.0/management/webui_props | Create WebUiProps
[**o_bpv3_1_0_delete_web_ui_props**](WebUiPropsApi.md#o_bpv3_1_0_delete_web_ui_props) | **DELETE** /obp/v5.0.0/management/webui_props/{WEB_UI_PROPS_ID} | Delete WebUiProps
[**o_bpv3_1_0_get_web_ui_props**](WebUiPropsApi.md#o_bpv3_1_0_get_web_ui_props) | **GET** /obp/v5.0.0/management/webui_props | Get WebUiProps


# **o_bpv3_1_0_create_web_ui_props**
> WebUiPropsCommons o_bpv3_1_0_create_web_ui_props(body)

Create WebUiProps

<p>Create a WebUiProps.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>name is required String value</li><li>value is required String value</li></ul><p>The line break and double quotations should do escape, example:</p><pre><code>{&quot;name&quot;: &quot;webui_some&quot;, &quot;value&quot;: &quot;this valuehave &quot;line break&quot; and double quotations.&quot;}</code></pre><p>should do escape like this:</p><pre><code>{&quot;name&quot;: &quot;webui_some&quot;, &quot;value&quot;: &quot;this value\\nhave \\&quot;line break\\&quot; and double quotations.&quot;}</code></pre><p>Insert image examples:</p><pre><code>// set width=100 and height=50{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;100&quot; height=&quot;50&quot; /&gt;&quot;}// only set height=50{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;&quot; height=&quot;50&quot; /&gt;&quot;}// only width=20%{&quot;name&quot;: &quot;webui_some_pic&quot;, &quot;value&quot;: &quot;here is a picture &lt;img alt=&quot;hello&quot; src=&quot;http://somedomain.com/images/pic.png&quot; width=&quot;20%&quot; height=&quot;&quot; /&gt;&quot;}</code></pre>

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
api_instance = obp_python.WebUiPropsApi(obp_python.ApiClient(configuration))
body = obp_python.WebUiPropsCommons() # WebUiPropsCommons | WebUiPropsCommons object that needs to be added.

try:
    # Create WebUiProps
    api_response = api_instance.o_bpv3_1_0_create_web_ui_props(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebUiPropsApi->o_bpv3_1_0_create_web_ui_props: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebUiPropsCommons**](WebUiPropsCommons.md)| WebUiPropsCommons object that needs to be added. | 

### Return type

[**WebUiPropsCommons**](WebUiPropsCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_web_ui_props**
> o_bpv3_1_0_delete_web_ui_props(web_ui_props_id)

Delete WebUiProps

<p>Delete a WebUiProps specified by WEB_UI_PROPS_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.WebUiPropsApi(obp_python.ApiClient(configuration))
web_ui_props_id = 'web_ui_props_id_example' # str | the web ui props id

try:
    # Delete WebUiProps
    api_instance.o_bpv3_1_0_delete_web_ui_props(web_ui_props_id)
except ApiException as e:
    print("Exception when calling WebUiPropsApi->o_bpv3_1_0_delete_web_ui_props: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_ui_props_id** | **str**| the web ui props id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_web_ui_props**
> InlineResponse20011 o_bpv3_1_0_get_web_ui_props()

Get WebUiProps

<p>Get the all WebUiProps key values, those props key with &quot;webui_&quot; can be stored in DB, this endpoint get all from DB.</p><p>url query parameter:<br />active: It must be a boolean string. and If active = true, it will show<br />combination of explicit (inserted) + implicit (default)  method_routings.</p><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/webui_props\">https://test.openbankproject.com/obp/v3.1.0/management/webui_props</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/webui_props?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/webui_props?active=true</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.WebUiPropsApi(obp_python.ApiClient(configuration))

try:
    # Get WebUiProps
    api_response = api_instance.o_bpv3_1_0_get_web_ui_props()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebUiPropsApi->o_bpv3_1_0_get_web_ui_props: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

