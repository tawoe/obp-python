# obp_python.UserInvitationApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv4_0_0_create_user_invitation**](UserInvitationApi.md#o_bpv4_0_0_create_user_invitation) | **POST** /obp/v5.0.0/banks/{BANK_ID}/user-invitation | Create User Invitation
[**o_bpv4_0_0_get_user_invitation**](UserInvitationApi.md#o_bpv4_0_0_get_user_invitation) | **GET** /obp/v5.0.0/banks/{BANK_ID}/user-invitations/SECRET_LINK | Get User Invitation
[**o_bpv4_0_0_get_user_invitation_anonymous**](UserInvitationApi.md#o_bpv4_0_0_get_user_invitation_anonymous) | **POST** /obp/v5.0.0/banks/{BANK_ID}/user-invitations | Get User Invitation Information
[**o_bpv4_0_0_get_user_invitations**](UserInvitationApi.md#o_bpv4_0_0_get_user_invitations) | **GET** /obp/v5.0.0/banks/{BANK_ID}/user-invitations | Get User Invitations


# **o_bpv4_0_0_create_user_invitation**
> UserInvitationJsonV400 o_bpv4_0_0_create_user_invitation(body, bank_id)

Create User Invitation

<p>Create User Invitation.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserInvitationApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserInvitationJsonV400() # PostUserInvitationJsonV400 | PostUserInvitationJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create User Invitation
    api_response = api_instance.o_bpv4_0_0_create_user_invitation(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitationApi->o_bpv4_0_0_create_user_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserInvitationJsonV400**](PostUserInvitationJsonV400.md)| PostUserInvitationJsonV400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserInvitationJsonV400**](UserInvitationJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_invitation**
> UserInvitationJsonV400 o_bpv4_0_0_get_user_invitation(bank_id)

Get User Invitation

<p>Get User Invitation</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserInvitationApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get User Invitation
    api_response = api_instance.o_bpv4_0_0_get_user_invitation(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitationApi->o_bpv4_0_0_get_user_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**UserInvitationJsonV400**](UserInvitationJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_invitation_anonymous**
> UserInvitationJsonV400 o_bpv4_0_0_get_user_invitation_anonymous(body, bank_id)

Get User Invitation Information

<p>Create User Invitation Information.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.UserInvitationApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserInvitationAnonymousJsonV400() # PostUserInvitationAnonymousJsonV400 | PostUserInvitationAnonymousJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get User Invitation Information
    api_response = api_instance.o_bpv4_0_0_get_user_invitation_anonymous(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitationApi->o_bpv4_0_0_get_user_invitation_anonymous: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostUserInvitationAnonymousJsonV400**](PostUserInvitationAnonymousJsonV400.md)| PostUserInvitationAnonymousJsonV400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserInvitationJsonV400**](UserInvitationJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_invitations**
> UserInvitationJsonV400 o_bpv4_0_0_get_user_invitations(bank_id)

Get User Invitations

<p>Get User Invitations</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.UserInvitationApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get User Invitations
    api_response = api_instance.o_bpv4_0_0_get_user_invitations(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserInvitationApi->o_bpv4_0_0_get_user_invitations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**UserInvitationJsonV400**](UserInvitationJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

