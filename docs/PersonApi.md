# obp_python.PersonApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_4_0_create_customer_message**](PersonApi.md#o_bpv1_4_0_create_customer_message) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customer/{CUSTOMER_ID}/messages | Create Customer Message
[**o_bpv4_0_0_create_customer_message**](PersonApi.md#o_bpv4_0_0_create_customer_message) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/messages | Create Customer Message
[**o_bpv5_0_0_create_customer**](PersonApi.md#o_bpv5_0_0_create_customer) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers | Create Customer


# **o_bpv1_4_0_create_customer_message**
> SuccessMessage o_bpv1_4_0_create_customer_message(body, customer_id, bank_id)

Create Customer Message

<p>Create a message for the customer specified by CUSTOMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PersonApi(obp_python.ApiClient(configuration))
body = obp_python.AddCustomerMessageJson() # AddCustomerMessageJson | AddCustomerMessageJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Message
    api_response = api_instance.o_bpv1_4_0_create_customer_message(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->o_bpv1_4_0_create_customer_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddCustomerMessageJson**](AddCustomerMessageJson.md)| AddCustomerMessageJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_customer_message**
> SuccessMessage o_bpv4_0_0_create_customer_message(body, customer_id, bank_id)

Create Customer Message

<p>Create a message for the customer specified by CUSTOMER_ID<br />Authentication is Mandatory</p>

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
api_instance = obp_python.PersonApi(obp_python.ApiClient(configuration))
body = obp_python.CreateMessageJsonV400() # CreateMessageJsonV400 | CreateMessageJsonV400 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Message
    api_response = api_instance.o_bpv4_0_0_create_customer_message(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->o_bpv4_0_0_create_customer_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMessageJsonV400**](CreateMessageJsonV400.md)| CreateMessageJsonV400 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_customer**
> CustomerJsonV310 o_bpv5_0_0_create_customer(body, bank_id)

Create Customer

<p>The Customer resource stores the customer number (which is set by the backend), legal name, email, phone number, their date of birth, relationship status, education attained, a url for a profile image, KYC status etc.<br />Dates need to be in the format 2013-01-21T23:08:00Z</p><p>Note: If you need to set a specific customer number, use the Update Customer Number endpoint after this call.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.PersonApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerJsonV500() # PostCustomerJsonV500 | PostCustomerJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer
    api_response = api_instance.o_bpv5_0_0_create_customer(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonApi->o_bpv5_0_0_create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerJsonV500**](PostCustomerJsonV500.md)| PostCustomerJsonV500 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

