# obp_python.SandboxApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_1_0_sandbox_data_import**](SandboxApi.md#o_bpv2_1_0_sandbox_data_import) | **POST** /obp/v5.0.0/sandbox/data-import | Create sandbox


# **o_bpv2_1_0_sandbox_data_import**
> SuccessMessage o_bpv2_1_0_sandbox_data_import(body)

Create sandbox

<p>Import bulk data into the sandbox (Authenticated access).</p><p>This call can be used to create banks, users, accounts and transactions which are stored in the local RDBMS.</p><p>The user needs to have CanCreateSandbox entitlement.</p><p>Note: This is a monolithic call. You could also use a combination of endpoints including create bank, create user, create account and create transaction request to create similar data.</p><p>An example of an import set of data (json) can be found <a href=\"https://raw.githubusercontent.com/OpenBankProject/OBP-API/develop/obp-api/src/main/scala/code/api/sandbox/example_data/2016-04-28/example_import.json\">here</a><br />Authentication is Mandatory</p>

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
api_instance = obp_python.SandboxApi(obp_python.ApiClient(configuration))
body = obp_python.SandboxDataImport() # SandboxDataImport | SandboxDataImport object that needs to be added.

try:
    # Create sandbox
    api_response = api_instance.o_bpv2_1_0_sandbox_data_import(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SandboxApi->o_bpv2_1_0_sandbox_data_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SandboxDataImport**](SandboxDataImport.md)| SandboxDataImport object that needs to be added. | 

### Return type

[**SuccessMessage**](SuccessMessage.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

