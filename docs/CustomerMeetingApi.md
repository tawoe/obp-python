# obp_python.CustomerMeetingApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_create_meeting**](CustomerMeetingApi.md#o_bpv3_1_0_create_meeting) | **POST** /obp/v5.0.0/banks/{BANK_ID}/meetings | Create Meeting (video conference/call)
[**o_bpv3_1_0_get_meeting**](CustomerMeetingApi.md#o_bpv3_1_0_get_meeting) | **GET** /obp/v5.0.0/banks/{BANK_ID}/meetings/{MEETING_ID} | Get Meeting
[**o_bpv3_1_0_get_meetings**](CustomerMeetingApi.md#o_bpv3_1_0_get_meetings) | **GET** /obp/v5.0.0/banks/{BANK_ID}/meetings | Get Meetings


# **o_bpv3_1_0_create_meeting**
> MeetingJsonV310 o_bpv3_1_0_create_meeting(body, bank_id)

Create Meeting (video conference/call)

<p>Create Meeting: Initiate a video conference/call with the bank.</p><p>The Meetings resource contains meta data about video/other conference sessions</p><p>provider_id determines the provider of the meeting / video chat service. MUST be url friendly (no spaces).</p><p>purpose_id explains the purpose of the chat. onboarding | mortgage | complaint etc. MUST be url friendly (no spaces).</p><p>Login is required.</p><p>This call is <strong>experimental</strong>. Currently staff_user_id is not set. Further calls will be needed to correctly set this.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerMeetingApi(obp_python.ApiClient(configuration))
body = obp_python.CreateMeetingJsonV310() # CreateMeetingJsonV310 | CreateMeetingJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Meeting (video conference/call)
    api_response = api_instance.o_bpv3_1_0_create_meeting(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerMeetingApi->o_bpv3_1_0_create_meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMeetingJsonV310**](CreateMeetingJsonV310.md)| CreateMeetingJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**MeetingJsonV310**](MeetingJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_meeting**
> MeetingJsonV310 o_bpv3_1_0_get_meeting(meeting_id, bank_id)

Get Meeting

<p>Get Meeting specified by BANK_ID / MEETING_ID<br />Meetings contain meta data about, and are used to facilitate, video conferences / chats etc.</p><p>The actual conference/chats are handled by external services.</p><p>Login is required.</p><p>This call is <strong>experimental</strong> and will require further authorisation in the future.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerMeetingApi(obp_python.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | the meeting id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Meeting
    api_response = api_instance.o_bpv3_1_0_get_meeting(meeting_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerMeetingApi->o_bpv3_1_0_get_meeting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meeting_id** | **str**| the meeting id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**MeetingJsonV310**](MeetingJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_meetings**
> MeetingsJsonV310 o_bpv3_1_0_get_meetings(bank_id)

Get Meetings

<p>Meetings contain meta data about, and are used to facilitate, video conferences / chats etc.</p><p>The actual conference/chats are handled by external services.</p><p>Login is required.</p><p>This call is <strong>experimental</strong> and will require further authorisation in the future.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerMeetingApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Meetings
    api_response = api_instance.o_bpv3_1_0_get_meetings(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerMeetingApi->o_bpv3_1_0_get_meetings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**MeetingsJsonV310**](MeetingsJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

