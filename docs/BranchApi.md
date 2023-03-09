# obp_python.BranchApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_0_0_create_branch**](BranchApi.md#o_bpv3_0_0_create_branch) | **POST** /obp/v5.0.0/banks/{BANK_ID}/branches | Create Branch
[**o_bpv3_0_0_get_branch**](BranchApi.md#o_bpv3_0_0_get_branch) | **GET** /obp/v5.0.0/banks/{BANK_ID}/branches/{BRANCH_ID} | Get Branch
[**o_bpv3_0_0_get_branches**](BranchApi.md#o_bpv3_0_0_get_branches) | **GET** /obp/v5.0.0/banks/{BANK_ID}/branches | Get Branches for a Bank
[**o_bpv3_1_0_delete_branch**](BranchApi.md#o_bpv3_1_0_delete_branch) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/branches/{BRANCH_ID} | Delete Branch


# **o_bpv3_0_0_create_branch**
> BranchJsonV300 o_bpv3_0_0_create_branch(body, bank_id)

Create Branch

<p>Create Branch for the Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.BranchApi(obp_python.ApiClient(configuration))
body = obp_python.BranchJsonV300() # BranchJsonV300 | BranchJsonV300 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Branch
    api_response = api_instance.o_bpv3_0_0_create_branch(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->o_bpv3_0_0_create_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BranchJsonV300**](BranchJsonV300.md)| BranchJsonV300 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BranchJsonV300**](BranchJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_branch**
> BranchJsonV300 o_bpv3_0_0_get_branch(branch_id, bank_id)

Get Branch

<p>Returns information about a single Branch specified by BANK_ID and BRANCH_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under.</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.BranchApi(obp_python.ApiClient(configuration))
branch_id = 'branch_id_example' # str | The branch id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Branch
    api_response = api_instance.o_bpv3_0_0_get_branch(branch_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->o_bpv3_0_0_get_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| The branch id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BranchJsonV300**](BranchJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_branches**
> BranchesJsonV300 o_bpv3_0_0_get_branches(bank_id)

Get Branches for a Bank

<p>Returns information about branches for a single bank specified by BANK_ID including:</p><ul><li>Name</li><li>Address</li><li>Geo Location</li><li>License the data under this endpoint is released under</li><li>Structured opening hours</li><li>Accessible flag</li><li>Branch Type</li><li>More Info</li></ul><p>Pagination:</p><p>By default, 50 records are returned.</p><p>You can use the url query parameters <em>limit</em> and <em>offset</em> for pagination<br />You can also use the follow url query parameters:</p><ul><li><p>city - string, find Branches those in this city, optional</p></li><li><p>withinMetersOf - number, find Branches within given meters distance, optional</p></li><li>nearLatitude - number, a position of latitude value, cooperate with withMetersOf do query filter, optional</li><li>nearLongitude - number, a position of longitude value, cooperate with withMetersOf do query filter, optional</li></ul><p>note: withinMetersOf, nearLatitude and nearLongitude either all empty or all have value.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.BranchApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Branches for a Bank
    api_response = api_instance.o_bpv3_0_0_get_branches(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BranchApi->o_bpv3_0_0_get_branches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**BranchesJsonV300**](BranchesJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_branch**
> o_bpv3_1_0_delete_branch(branch_id, bank_id)

Delete Branch

<p>Delete Branch from given Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.BranchApi(obp_python.ApiClient(configuration))
branch_id = 'branch_id_example' # str | The branch id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Branch
    api_instance.o_bpv3_1_0_delete_branch(branch_id, bank_id)
except ApiException as e:
    print("Exception when calling BranchApi->o_bpv3_1_0_delete_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| The branch id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

