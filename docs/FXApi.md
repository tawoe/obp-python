# obp_python.FXApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_2_0_create_fx**](FXApi.md#o_bpv2_2_0_create_fx) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/fx | Create Fx
[**o_bpv2_2_0_get_current_fx_rate**](FXApi.md#o_bpv2_2_0_get_current_fx_rate) | **GET** /obp/v5.0.0/banks/{BANK_ID}/fx/{FROM_CURRENCY_CODE}/{TO_CURRENCY_CODE} | Get Current FxRate


# **o_bpv2_2_0_create_fx**
> FXRateJsonV220 o_bpv2_2_0_create_fx(body, bank_id)

Create Fx

<p>Create or Update Fx for the Bank.</p><p>Example:</p><p>“from_currency_code”:“EUR”,<br />“to_currency_code”:“USD”,<br />“conversion_value”: 1.136305,<br />“inverse_conversion_value”: 1 / 1.136305 = 0.8800454103431737,</p><p>Thus 1 Euro = 1.136305 US Dollar<br />and<br />1 US Dollar = 0.8800 Euro</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.FXApi(obp_python.ApiClient(configuration))
body = obp_python.FXRateJsonV220() # FXRateJsonV220 | FXRateJsonV220 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Fx
    api_response = api_instance.o_bpv2_2_0_create_fx(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FXApi->o_bpv2_2_0_create_fx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FXRateJsonV220**](FXRateJsonV220.md)| FXRateJsonV220 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**FXRateJsonV220**](FXRateJsonV220.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_2_0_get_current_fx_rate**
> FXRateJsonV220 o_bpv2_2_0_get_current_fx_rate(body, to_currency_code, from_currency_code, bank_id)

Get Current FxRate

<p>Get the latest FX rate specified by BANK_ID, FROM_CURRENCY_CODE and TO_CURRENCY_CODE</p><p>OBP may try different sources of FX rate information depending on the Connector in operation.</p><p>For example we want to convert EUR =&gt; USD:</p><p>OBP will:<br />1st try - Connector (database, core banking system or external FX service)<br />2nd try part 1 - fallbackexchangerates/eur.json<br />2nd try part 2 - fallbackexchangerates/usd.json (the inverse rate is used)<br />3rd try - Hardcoded map of FX rates.</p><p><img src=\"https://user-images.githubusercontent.com/485218/60005085-1eded600-966e-11e9-96fb-798b102d9ad0.png\" alt=\"FX Flow\" /></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.FXApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
to_currency_code = 'to_currency_code_example' # str | The to currency code
from_currency_code = 'from_currency_code_example' # str | The from currency code
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Current FxRate
    api_response = api_instance.o_bpv2_2_0_get_current_fx_rate(body, to_currency_code, from_currency_code, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FXApi->o_bpv2_2_0_get_current_fx_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **to_currency_code** | **str**| The to currency code | 
 **from_currency_code** | **str**| The from currency code | 
 **bank_id** | **str**| The bank id | 

### Return type

[**FXRateJsonV220**](FXRateJsonV220.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

