# obp_python.ConsentApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv3_1_0_answer_consent_challenge**](ConsentApi.md#o_bpv3_1_0_answer_consent_challenge) | **POST** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID}/challenge | Answer Consent Challenge
[**o_bpv3_1_0_create_consent_email**](ConsentApi.md#o_bpv3_1_0_create_consent_email) | **POST** /obp/v5.0.0/banks/{BANK_ID}/my/consents/EMAIL | Create Consent (EMAIL)
[**o_bpv3_1_0_create_consent_sms**](ConsentApi.md#o_bpv3_1_0_create_consent_sms) | **POST** /obp/v5.0.0/banks/{BANK_ID}/my/consents/SMS | Create Consent (SMS)
[**o_bpv3_1_0_revoke_consent**](ConsentApi.md#o_bpv3_1_0_revoke_consent) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consents/{CONSENT_ID}/revoke | Revoke Consent
[**o_bpv4_0_0_add_consent_user**](ConsentApi.md#o_bpv4_0_0_add_consent_user) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID}/user-update-request | Add User to a Consent
[**o_bpv4_0_0_get_consent_infos**](ConsentApi.md#o_bpv4_0_0_get_consent_infos) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consent-infos | Get Consents Info
[**o_bpv4_0_0_get_consents**](ConsentApi.md#o_bpv4_0_0_get_consents) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/consents | Get Consents
[**o_bpv4_0_0_update_consent_status**](ConsentApi.md#o_bpv4_0_0_update_consent_status) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/consents/{CONSENT_ID} | Update Consent Status
[**o_bpv5_0_0_create_consent_by_consent_request_id_email**](ConsentApi.md#o_bpv5_0_0_create_consent_by_consent_request_id_email) | **POST** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/EMAIL/consents | Create Consent By CONSENT_REQUEST_ID (EMAIL)
[**o_bpv5_0_0_create_consent_by_consent_request_id_sms**](ConsentApi.md#o_bpv5_0_0_create_consent_by_consent_request_id_sms) | **POST** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/SMS/consents | Create Consent By CONSENT_REQUEST_ID (SMS)
[**o_bpv5_0_0_create_consent_request**](ConsentApi.md#o_bpv5_0_0_create_consent_request) | **POST** /obp/v5.0.0/consumer/consent-requests | Create Consent Request
[**o_bpv5_0_0_get_consent_by_consent_request_id**](ConsentApi.md#o_bpv5_0_0_get_consent_by_consent_request_id) | **GET** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID/consents | Get Consent By Consent Request Id
[**o_bpv5_0_0_get_consent_request**](ConsentApi.md#o_bpv5_0_0_get_consent_request) | **GET** /obp/v5.0.0/consumer/consent-requests/CONSENT_REQUEST_ID | Get Consent Request


# **o_bpv3_1_0_answer_consent_challenge**
> ConsentChallengeJsonV310 o_bpv3_1_0_answer_consent_challenge(body, consent_id, bank_id)

Answer Consent Challenge

<p>An OBP Consent allows the holder of the Consent to call one or more endpoints.</p><p>Consents must be created and authorisied using SCA (Strong Customer Authentication).</p><p>That is, Consents can be created by an authorised User via the OBP REST API but they must be confirmed via an out of band (OOB) mechanism such as a code sent to a mobile phone.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Each Consent is bound to a consumer i.e. you need to identify yourself over request header value Consumer-Key.<br />For example:<br />GET /obp/v4.0.0/users/current HTTP/1.1<br />Host: 127.0.0.1:8080<br />Consent-JWT: eyJhbGciOiJIUzI1NiJ9.eyJlbnRpdGxlbWVudHMiOlt7InJvbGVfbmFtZSI6IkNhbkdldEFueVVzZXIiLCJiYW5rX2lkIjoiIn<br />1dLCJjcmVhdGVkQnlVc2VySWQiOiJhYjY1MzlhOS1iMTA1LTQ0ODktYTg4My0wYWQ4ZDZjNjE2NTciLCJzdWIiOiIzNDc1MDEzZi03YmY5LTQyNj<br />EtOWUxYy0xZTdlNWZjZTJlN2UiLCJhdWQiOiI4MTVhMGVmMS00YjZhLTQyMDUtYjExMi1lNDVmZDZmNGQzYWQiLCJuYmYiOjE1ODA3NDE2NjcsIml<br />zcyI6Imh0dHA6XC9cLzEyNy4wLjAuMTo4MDgwIiwiZXhwIjoxNTgwNzQ1MjY3LCJpYXQiOjE1ODA3NDE2NjcsImp0aSI6ImJkYzVjZTk5LTE2ZTY<br />tNDM4Yi1hNjllLTU3MTAzN2RhMTg3OCIsInZpZXdzIjpbXX0.L3fEEEhdCVr3qnmyRKBBUaIQ7dk1VjiFaEBW8hUNjfg</p><p>Consumer-Key: ejznk505d132ryomnhbx1qmtohurbsbb0kijajsk<br />cache-control: no-cache</p><p>Maximum time to live of the token is specified over props value consents.max_time_to_live. In case isn't defined default value is 3600 seconds.</p><p>Example of POST JSON:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;&#x6c;&#x74;o&#x3a;&#101;&#118;&#101;&#x6c;&#x69;&#x6e;&#x65;&#x40;&#x65;&#120;&#x61;&#109;pl&#101;&#x2e;&#99;&#111;m\">&#101;&#118;&#x65;&#108;i&#110;&#x65;&#x40;&#101;&#120;a&#109;&#x70;&#108;&#101;&#x2e;c&#x6f;&#109;</a>&quot;,<br />&quot;valid_from&quot;: &quot;2020-02-07T08:43:34Z&quot;,<br />&quot;time_to_live&quot;: 3600<br />}<br />Please note that only optional fields are: consumer_id, valid_from and time_to_live.<br />In case you omit they the default values are used:<br />consumer_id = consumer of current user<br />valid_from = current time<br />time_to_live = consents.max_time_to_live</p><p>This endpoint is used to confirm a Consent previously created.</p><p>The User must supply a code that was sent out of band (OOB) for example via an SMS.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentChallengeJsonV310() # PostConsentChallengeJsonV310 | PostConsentChallengeJsonV310 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Answer Consent Challenge
    api_response = api_instance.o_bpv3_1_0_answer_consent_challenge(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv3_1_0_answer_consent_challenge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentChallengeJsonV310**](PostConsentChallengeJsonV310.md)| PostConsentChallengeJsonV310 object that needs to be added. | 
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentChallengeJsonV310**](ConsentChallengeJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_consent_email**
> ConsentJsonV310 o_bpv3_1_0_create_consent_email(body, bank_id)

Create Consent (EMAIL)

<p>This endpoint starts the process of creating a Consent.</p><p>The Consent is created in an INITIATED state.</p><p>A One Time Password (OTP) (AKA security challenge) is sent Out of band (OOB) to the User via the transport defined in SCA_METHOD<br />SCA_METHOD is typically &quot;SMS&quot; or &quot;EMAIL&quot;. &quot;EMAIL&quot; is used for testing purposes.</p><p>When the Consent is created, OBP (or a backend system) stores the challenge so it can be checked later against the value supplied by the User with the Answer Consent Challenge endpoint.</p><p>An OBP Consent allows the holder of the Consent to call one or more endpoints.</p><p>Consents must be created and authorisied using SCA (Strong Customer Authentication).</p><p>That is, Consents can be created by an authorised User via the OBP REST API but they must be confirmed via an out of band (OOB) mechanism such as a code sent to a mobile phone.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Each Consent is bound to a consumer i.e. you need to identify yourself over request header value Consumer-Key.<br />For example:<br />GET /obp/v4.0.0/users/current HTTP/1.1<br />Host: 127.0.0.1:8080<br />Consent-JWT: eyJhbGciOiJIUzI1NiJ9.eyJlbnRpdGxlbWVudHMiOlt7InJvbGVfbmFtZSI6IkNhbkdldEFueVVzZXIiLCJiYW5rX2lkIjoiIn<br />1dLCJjcmVhdGVkQnlVc2VySWQiOiJhYjY1MzlhOS1iMTA1LTQ0ODktYTg4My0wYWQ4ZDZjNjE2NTciLCJzdWIiOiIzNDc1MDEzZi03YmY5LTQyNj<br />EtOWUxYy0xZTdlNWZjZTJlN2UiLCJhdWQiOiI4MTVhMGVmMS00YjZhLTQyMDUtYjExMi1lNDVmZDZmNGQzYWQiLCJuYmYiOjE1ODA3NDE2NjcsIml<br />zcyI6Imh0dHA6XC9cLzEyNy4wLjAuMTo4MDgwIiwiZXhwIjoxNTgwNzQ1MjY3LCJpYXQiOjE1ODA3NDE2NjcsImp0aSI6ImJkYzVjZTk5LTE2ZTY<br />tNDM4Yi1hNjllLTU3MTAzN2RhMTg3OCIsInZpZXdzIjpbXX0.L3fEEEhdCVr3qnmyRKBBUaIQ7dk1VjiFaEBW8hUNjfg</p><p>Consumer-Key: ejznk505d132ryomnhbx1qmtohurbsbb0kijajsk<br />cache-control: no-cache</p><p>Maximum time to live of the token is specified over props value consents.max_time_to_live. In case isn't defined default value is 3600 seconds.</p><p>Example of POST JSON:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#x61;i&#108;&#x74;&#x6f;&#58;e&#x76;&#101;&#108;&#105;&#110;&#101;&#x40;&#x65;&#x78;&#x61;&#109;&#112;&#108;e&#x2e;&#x63;&#x6f;&#109;\">&#x65;&#118;&#x65;li&#x6e;&#101;&#64;&#x65;&#120;&#x61;&#x6d;&#112;&#108;&#101;&#x2e;&#x63;o&#109;</a>&quot;,<br />&quot;valid_from&quot;: &quot;2020-02-07T08:43:34Z&quot;,<br />&quot;time_to_live&quot;: 3600<br />}<br />Please note that only optional fields are: consumer_id, valid_from and time_to_live.<br />In case you omit they the default values are used:<br />consumer_id = consumer of current user<br />valid_from = current time<br />time_to_live = consents.max_time_to_live</p><p>Authentication is Mandatory</p><p>Example 1:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;l&#x74;&#111;&#x3a;e&#118;&#101;&#x6c;&#x69;&#110;&#x65;&#x40;&#x65;&#x78;&#x61;&#x6d;p&#x6c;&#x65;&#x2e;&#x63;&#x6f;&#109;\">&#101;v&#101;&#108;&#105;&#110;&#101;@&#101;&#x78;&#97;&#109;&#x70;&#x6c;&#101;.&#x63;&#x6f;&#x6d;</a>&quot;<br />}</p><p>Please note that consumer_id is optional field<br />Example 2:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;lto&#x3a;&#x65;&#118;e&#x6c;&#x69;n&#x65;&#x40;&#x65;&#120;&#97;&#x6d;p&#108;&#x65;&#x2e;&#x63;&#x6f;&#x6d;\">&#x65;&#x76;&#101;&#108;&#x69;&#110;&#101;&#64;&#x65;x&#x61;&#x6d;&#112;&#x6c;&#101;&#x2e;&#x63;&#111;&#109;</a>&quot;<br />}</p><p>Please note if everything=false you need to explicitly specify views and entitlements<br />Example 3:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#x61;&#105;&#108;&#116;&#x6f;&#x3a;&#x65;&#x76;&#101;&#x6c;&#x69;&#x6e;&#x65;&#64;&#101;&#x78;&#97;&#x6d;p&#x6c;&#x65;&#46;&#99;&#111;&#109;\">&#x65;&#x76;&#101;&#x6c;&#105;&#110;&#101;&#x40;&#x65;&#x78;&#97;&#x6d;&#x70;&#x6c;&#101;&#x2e;&#99;&#x6f;&#109;</a>&quot;<br />}</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentEmailJsonV310() # PostConsentEmailJsonV310 | PostConsentEmailJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Consent (EMAIL)
    api_response = api_instance.o_bpv3_1_0_create_consent_email(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv3_1_0_create_consent_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentEmailJsonV310**](PostConsentEmailJsonV310.md)| PostConsentEmailJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentJsonV310**](ConsentJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_consent_sms**
> ConsentJsonV310 o_bpv3_1_0_create_consent_sms(body, bank_id)

Create Consent (SMS)

<p>This endpoint starts the process of creating a Consent.</p><p>The Consent is created in an INITIATED state.</p><p>A One Time Password (OTP) (AKA security challenge) is sent Out of Band (OOB) to the User via the transport defined in SCA_METHOD<br />SCA_METHOD is typically &quot;SMS&quot; or &quot;EMAIL&quot;. &quot;EMAIL&quot; is used for testing purposes.</p><p>When the Consent is created, OBP (or a backend system) stores the challenge so it can be checked later against the value supplied by the User with the Answer Consent Challenge endpoint.</p><p>An OBP Consent allows the holder of the Consent to call one or more endpoints.</p><p>Consents must be created and authorisied using SCA (Strong Customer Authentication).</p><p>That is, Consents can be created by an authorised User via the OBP REST API but they must be confirmed via an out of band (OOB) mechanism such as a code sent to a mobile phone.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Each Consent is bound to a consumer i.e. you need to identify yourself over request header value Consumer-Key.<br />For example:<br />GET /obp/v4.0.0/users/current HTTP/1.1<br />Host: 127.0.0.1:8080<br />Consent-JWT: eyJhbGciOiJIUzI1NiJ9.eyJlbnRpdGxlbWVudHMiOlt7InJvbGVfbmFtZSI6IkNhbkdldEFueVVzZXIiLCJiYW5rX2lkIjoiIn<br />1dLCJjcmVhdGVkQnlVc2VySWQiOiJhYjY1MzlhOS1iMTA1LTQ0ODktYTg4My0wYWQ4ZDZjNjE2NTciLCJzdWIiOiIzNDc1MDEzZi03YmY5LTQyNj<br />EtOWUxYy0xZTdlNWZjZTJlN2UiLCJhdWQiOiI4MTVhMGVmMS00YjZhLTQyMDUtYjExMi1lNDVmZDZmNGQzYWQiLCJuYmYiOjE1ODA3NDE2NjcsIml<br />zcyI6Imh0dHA6XC9cLzEyNy4wLjAuMTo4MDgwIiwiZXhwIjoxNTgwNzQ1MjY3LCJpYXQiOjE1ODA3NDE2NjcsImp0aSI6ImJkYzVjZTk5LTE2ZTY<br />tNDM4Yi1hNjllLTU3MTAzN2RhMTg3OCIsInZpZXdzIjpbXX0.L3fEEEhdCVr3qnmyRKBBUaIQ7dk1VjiFaEBW8hUNjfg</p><p>Consumer-Key: ejznk505d132ryomnhbx1qmtohurbsbb0kijajsk<br />cache-control: no-cache</p><p>Maximum time to live of the token is specified over props value consents.max_time_to_live. In case isn't defined default value is 3600 seconds.</p><p>Example of POST JSON:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"ma&#105;&#108;&#x74;&#111;:&#x65;&#x76;e&#x6c;i&#x6e;&#101;&#64;&#x65;&#x78;&#97;&#x6d;&#x70;&#108;e&#46;c&#111;&#109;\">&#x65;&#x76;&#101;&#x6c;&#105;&#110;&#101;&#64;e&#120;&#x61;&#109;p&#108;&#101;&#x2e;&#x63;o&#109;</a>&quot;,<br />&quot;valid_from&quot;: &quot;2020-02-07T08:43:34Z&quot;,<br />&quot;time_to_live&quot;: 3600<br />}<br />Please note that only optional fields are: consumer_id, valid_from and time_to_live.<br />In case you omit they the default values are used:<br />consumer_id = consumer of current user<br />valid_from = current time<br />time_to_live = consents.max_time_to_live</p><p>Authentication is Mandatory</p><p>Example 1:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"m&#x61;&#x69;&#108;&#116;o&#x3a;e&#118;&#x65;&#108;&#x69;&#110;&#101;&#x40;ex&#x61;&#x6d;&#112;&#x6c;&#101;&#46;&#x63;&#111;&#x6d;\">&#x65;&#118;el&#x69;&#110;&#101;&#64;&#101;x&#97;&#x6d;&#x70;le&#46;&#99;&#111;&#x6d;</a>&quot;<br />}</p><p>Please note that consumer_id is optional field<br />Example 2:<br />{<br />&quot;everything&quot;: true,<br />&quot;views&quot;: [],<br />&quot;entitlements&quot;: [],<br />&quot;email&quot;: &quot;<a href=\"m&#97;&#x69;&#108;&#116;o:&#101;&#x76;&#x65;&#x6c;i&#x6e;&#101;&#64;&#101;&#120;&#x61;&#109;&#x70;l&#101;&#46;&#x63;&#111;&#109;\">ev&#101;&#x6c;&#x69;&#110;&#x65;&#64;&#101;&#x78;&#x61;&#109;p&#x6c;&#x65;.c&#111;&#x6d;</a>&quot;<br />}</p><p>Please note if everything=false you need to explicitly specify views and entitlements<br />Example 3:<br />{<br />&quot;everything&quot;: false,<br />&quot;views&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;account_id&quot;: &quot;8ca8a7e4-6d02-40e3-a129-0b2bf89de9f0&quot;,<br />&quot;view_id&quot;: &quot;owner&quot;<br />}<br />],<br />&quot;entitlements&quot;: [<br />{<br />&quot;bank_id&quot;: &quot;GENODEM1GLS&quot;,<br />&quot;role_name&quot;: &quot;CanGetCustomer&quot;<br />}<br />],<br />&quot;consumer_id&quot;: &quot;7uy8a7e4-6d02-40e3-a129-0b2bf89de8uh&quot;,<br />&quot;email&quot;: &quot;<a href=\"&#109;&#97;&#105;lto&#58;&#101;&#x76;&#x65;&#x6c;i&#x6e;&#101;&#64;&#101;&#x78;&#x61;&#x6d;pl&#101;&#x2e;&#x63;&#111;&#109;\">e&#x76;&#101;&#108;&#x69;&#x6e;&#x65;&#64;e&#120;a&#x6d;&#112;&#108;&#x65;.c&#x6f;&#x6d;</a>&quot;<br />}</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentPhoneJsonV310() # PostConsentPhoneJsonV310 | PostConsentPhoneJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Consent (SMS)
    api_response = api_instance.o_bpv3_1_0_create_consent_sms(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv3_1_0_create_consent_sms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentPhoneJsonV310**](PostConsentPhoneJsonV310.md)| PostConsentPhoneJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentJsonV310**](ConsentJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_revoke_consent**
> ConsentJsonV310 o_bpv3_1_0_revoke_consent(consent_id, bank_id)

Revoke Consent

<p>Revoke Consent for current user specified by CONSENT_ID</p><p>There are a few reasons you might need to revoke an application’s access to a user’s account:<br />- The user explicitly wishes to revoke the application’s access<br />- You as the service provider have determined an application is compromised or malicious, and want to disable it<br />- etc.</p><p>Please note that this endpoint only supports the case:: &quot;The user explicitly wishes to revoke the application’s access&quot;</p><p>OBP as a resource server stores access tokens in a database, then it is relatively easy to revoke some token that belongs to a particular user.<br />The status of the token is changed to &quot;REVOKED&quot; so the next time the revoked client makes a request, their token will fail to validate.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Revoke Consent
    api_response = api_instance.o_bpv3_1_0_revoke_consent(consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv3_1_0_revoke_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentJsonV310**](ConsentJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_add_consent_user**
> ConsentChallengeJsonV310 o_bpv4_0_0_add_consent_user(body, consent_id, bank_id)

Add User to a Consent

<p>This endpoint is used to add the User of Consent.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
body = obp_python.PutConsentUserJsonV400() # PutConsentUserJsonV400 | PutConsentUserJsonV400 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add User to a Consent
    api_response = api_instance.o_bpv4_0_0_add_consent_user(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv4_0_0_add_consent_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutConsentUserJsonV400**](PutConsentUserJsonV400.md)| PutConsentUserJsonV400 object that needs to be added. | 
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentChallengeJsonV310**](ConsentChallengeJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_consent_infos**
> ConsentInfosJsonV400 o_bpv4_0_0_get_consent_infos(bank_id)

Get Consents Info

<p>This endpoint gets the Consents that the current User created.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Consents Info
    api_response = api_instance.o_bpv4_0_0_get_consent_infos(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv4_0_0_get_consent_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentInfosJsonV400**](ConsentInfosJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_consents**
> ConsentsJsonV400 o_bpv4_0_0_get_consents(bank_id)

Get Consents

<p>This endpoint gets the Consents that the current User created.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Consents
    api_response = api_instance.o_bpv4_0_0_get_consents(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv4_0_0_get_consents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentsJsonV400**](ConsentsJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_consent_status**
> ConsentChallengeJsonV310 o_bpv4_0_0_update_consent_status(body, consent_id, bank_id)

Update Consent Status

<p>This endpoint is used to update the Status of Consent.</p><p>Each Consent has one of the following states: INITIATED, ACCEPTED, REJECTED, REVOKED, RECEIVED, VALID, REVOKEDBYPSU, EXPIRED, TERMINATEDBYTPP, AUTHORISED, AWAITINGAUTHORISATION.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
body = obp_python.PutConsentStatusJsonV400() # PutConsentStatusJsonV400 | PutConsentStatusJsonV400 object that needs to be added.
consent_id = 'consent_id_example' # str | the consent id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Consent Status
    api_response = api_instance.o_bpv4_0_0_update_consent_status(body, consent_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv4_0_0_update_consent_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutConsentStatusJsonV400**](PutConsentStatusJsonV400.md)| PutConsentStatusJsonV400 object that needs to be added. | 
 **consent_id** | **str**| the consent id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ConsentChallengeJsonV310**](ConsentChallengeJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_consent_by_consent_request_id_email**
> ConsentJsonV500 o_bpv5_0_0_create_consent_by_consent_request_id_email()

Create Consent By CONSENT_REQUEST_ID (EMAIL)

<p>This endpoint continues the process of creating a Consent. It starts the SCA flow which changes the status of the consent from INITIATED to ACCEPTED or REJECTED.<br />Please note that the Consent cannot elevate the privileges logged in user already have.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))

try:
    # Create Consent By CONSENT_REQUEST_ID (EMAIL)
    api_response = api_instance.o_bpv5_0_0_create_consent_by_consent_request_id_email()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv5_0_0_create_consent_by_consent_request_id_email: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentJsonV500**](ConsentJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_consent_by_consent_request_id_sms**
> ConsentJsonV500 o_bpv5_0_0_create_consent_by_consent_request_id_sms()

Create Consent By CONSENT_REQUEST_ID (SMS)

<p>This endpoint continues the process of creating a Consent. It starts the SCA flow which changes the status of the consent from INITIATED to ACCEPTED or REJECTED.<br />Please note that the Consent cannot elevate the privileges logged in user already have.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))

try:
    # Create Consent By CONSENT_REQUEST_ID (SMS)
    api_response = api_instance.o_bpv5_0_0_create_consent_by_consent_request_id_sms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv5_0_0_create_consent_by_consent_request_id_sms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentJsonV500**](ConsentJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_create_consent_request**
> ConsentRequestResponseJson o_bpv5_0_0_create_consent_request(body)

Create Consent Request

<p>Client Authentication (mandatory)</p><p>It is used when applications request an access token to access their own resources, not on behalf of a user.</p><p>The client needs to authenticate themselves for this request.<br />In case of public client we use client_id and private kew to obtain access token, otherwise we use client_id and client_secret.<br />The obtained access token is used in the HTTP Bearer auth header of our request.</p><p>Example:<br />Authorization: Bearer eXtneO-THbQtn3zvK_kQtXXfvOZyZFdBCItlPDbR2Bk.dOWqtXCtFX-tqGTVR0YrIjvAolPIVg7GZ-jz83y6nA0</p><p>Authentication is Optional</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))
body = obp_python.PostConsentRequestJsonV500() # PostConsentRequestJsonV500 | PostConsentRequestJsonV500 object that needs to be added.

try:
    # Create Consent Request
    api_response = api_instance.o_bpv5_0_0_create_consent_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv5_0_0_create_consent_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostConsentRequestJsonV500**](PostConsentRequestJsonV500.md)| PostConsentRequestJsonV500 object that needs to be added. | 

### Return type

[**ConsentRequestResponseJson**](ConsentRequestResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_consent_by_consent_request_id**
> ConsentJsonV500 o_bpv5_0_0_get_consent_by_consent_request_id()

Get Consent By Consent Request Id

<p>This endpoint gets the Consent By consent request id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))

try:
    # Get Consent By Consent Request Id
    api_response = api_instance.o_bpv5_0_0_get_consent_by_consent_request_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv5_0_0_get_consent_by_consent_request_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentJsonV500**](ConsentJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_consent_request**
> ConsentRequestResponseJson o_bpv5_0_0_get_consent_request()

Get Consent Request

<p>Authentication is Optional</p>

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
api_instance = obp_python.ConsentApi(obp_python.ApiClient(configuration))

try:
    # Get Consent Request
    api_response = api_instance.o_bpv5_0_0_get_consent_request()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsentApi->o_bpv5_0_0_get_consent_request: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConsentRequestResponseJson**](ConsentRequestResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

