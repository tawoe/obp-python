# obp_python.CustomerApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_4_0_create_customer_message**](CustomerApi.md#o_bpv1_4_0_create_customer_message) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customer/{CUSTOMER_ID}/messages | Create Customer Message
[**o_bpv1_4_0_get_crm_events**](CustomerApi.md#o_bpv1_4_0_get_crm_events) | **GET** /obp/v5.0.0/banks/{BANK_ID}/crm-events | Get CRM Events
[**o_bpv1_4_0_get_customer_messages**](CustomerApi.md#o_bpv1_4_0_get_customer_messages) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customer/messages | Get Customer Messages for a Customer
[**o_bpv2_0_0_add_kyc_check**](CustomerApi.md#o_bpv2_0_0_add_kyc_check) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_check/{KYC_CHECK_ID} | Add KYC Check
[**o_bpv2_0_0_add_kyc_document**](CustomerApi.md#o_bpv2_0_0_add_kyc_document) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_documents/{KYC_DOCUMENT_ID} | Add KYC Document
[**o_bpv2_0_0_add_kyc_media**](CustomerApi.md#o_bpv2_0_0_add_kyc_media) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_media/{KYC_MEDIA_ID} | Add KYC Media
[**o_bpv2_0_0_add_kyc_status**](CustomerApi.md#o_bpv2_0_0_add_kyc_status) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_statuses | Add KYC Status
[**o_bpv2_0_0_add_social_media_handle**](CustomerApi.md#o_bpv2_0_0_add_social_media_handle) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/social_media_handles | Add Social Media Handle
[**o_bpv2_0_0_get_kyc_checks**](CustomerApi.md#o_bpv2_0_0_get_kyc_checks) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_checks | Get Customer KYC Checks
[**o_bpv2_0_0_get_kyc_documents**](CustomerApi.md#o_bpv2_0_0_get_kyc_documents) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_documents | Get Customer KYC Documents
[**o_bpv2_0_0_get_kyc_media**](CustomerApi.md#o_bpv2_0_0_get_kyc_media) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_media | Get KYC Media for a customer
[**o_bpv2_0_0_get_kyc_statuses**](CustomerApi.md#o_bpv2_0_0_get_kyc_statuses) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_statuses | Get Customer KYC statuses
[**o_bpv2_0_0_get_social_media_handles**](CustomerApi.md#o_bpv2_0_0_get_social_media_handles) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/social_media_handles | Get Customer Social Media Handles
[**o_bpv3_0_0_get_customers_for_user**](CustomerApi.md#o_bpv3_0_0_get_customers_for_user) | **GET** /obp/v5.0.0/users/current/customers | Get Customers for Current User
[**o_bpv3_1_0_create_credit_limit_request**](CustomerApi.md#o_bpv3_1_0_create_credit_limit_request) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/credit_limit/requests | Create Credit Limit Order Request
[**o_bpv3_1_0_create_customer_address**](CustomerApi.md#o_bpv3_1_0_create_customer_address) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/address | Create Address
[**o_bpv3_1_0_create_meeting**](CustomerApi.md#o_bpv3_1_0_create_meeting) | **POST** /obp/v5.0.0/banks/{BANK_ID}/meetings | Create Meeting (video conference/call)
[**o_bpv3_1_0_create_tax_residence**](CustomerApi.md#o_bpv3_1_0_create_tax_residence) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/tax-residence | Create Tax Residence
[**o_bpv3_1_0_delete_customer_address**](CustomerApi.md#o_bpv3_1_0_delete_customer_address) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/addresses/{CUSTOMER_ADDRESS_ID} | Delete Customer Address
[**o_bpv3_1_0_delete_tax_residence**](CustomerApi.md#o_bpv3_1_0_delete_tax_residence) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/tax_residencies/{TAX_RESIDENCE_ID} | Delete Tax Residence
[**o_bpv3_1_0_get_credit_limit_request_by_request_id**](CustomerApi.md#o_bpv3_1_0_get_credit_limit_request_by_request_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/credit_limit/requests/{REQUEST_ID} | Get Credit Limit Order Request By Request Id
[**o_bpv3_1_0_get_credit_limit_requests**](CustomerApi.md#o_bpv3_1_0_get_credit_limit_requests) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/credit_limit/requests | Get Credit Limit Order Requests 
[**o_bpv3_1_0_get_customer_addresses**](CustomerApi.md#o_bpv3_1_0_get_customer_addresses) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/addresses | Get Customer Addresses
[**o_bpv3_1_0_get_customer_by_customer_id**](CustomerApi.md#o_bpv3_1_0_get_customer_by_customer_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID} | Get Customer by CUSTOMER_ID
[**o_bpv3_1_0_get_customer_by_customer_number**](CustomerApi.md#o_bpv3_1_0_get_customer_by_customer_number) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/customer-number | Get Customer by CUSTOMER_NUMBER
[**o_bpv3_1_0_get_firehose_customers**](CustomerApi.md#o_bpv3_1_0_get_firehose_customers) | **GET** /obp/v5.0.0/banks/{BANK_ID}/firehose/customers | Get Firehose Customers
[**o_bpv3_1_0_get_meeting**](CustomerApi.md#o_bpv3_1_0_get_meeting) | **GET** /obp/v5.0.0/banks/{BANK_ID}/meetings/{MEETING_ID} | Get Meeting
[**o_bpv3_1_0_get_meetings**](CustomerApi.md#o_bpv3_1_0_get_meetings) | **GET** /obp/v5.0.0/banks/{BANK_ID}/meetings | Get Meetings
[**o_bpv3_1_0_get_tax_residence**](CustomerApi.md#o_bpv3_1_0_get_tax_residence) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/tax-residences | Get Tax Residences of Customer
[**o_bpv3_1_0_update_customer_address**](CustomerApi.md#o_bpv3_1_0_update_customer_address) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/addresses/{CUSTOMER_ADDRESS_ID} | Update the Address of a Customer
[**o_bpv3_1_0_update_customer_branch**](CustomerApi.md#o_bpv3_1_0_update_customer_branch) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/branch | Update the Branch of a Customer
[**o_bpv3_1_0_update_customer_credit_limit**](CustomerApi.md#o_bpv3_1_0_update_customer_credit_limit) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/credit-limit | Update the credit limit of a Customer
[**o_bpv3_1_0_update_customer_credit_rating_and_source**](CustomerApi.md#o_bpv3_1_0_update_customer_credit_rating_and_source) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/credit-rating-and-source | Update the credit rating and source of a Customer
[**o_bpv3_1_0_update_customer_data**](CustomerApi.md#o_bpv3_1_0_update_customer_data) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/data | Update the other data of a Customer
[**o_bpv3_1_0_update_customer_email**](CustomerApi.md#o_bpv3_1_0_update_customer_email) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/email | Update the email of a Customer
[**o_bpv3_1_0_update_customer_identity**](CustomerApi.md#o_bpv3_1_0_update_customer_identity) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/identity | Update the identity data of a Customer
[**o_bpv3_1_0_update_customer_mobile_number**](CustomerApi.md#o_bpv3_1_0_update_customer_mobile_number) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/mobile-number | Update the mobile number of a Customer
[**o_bpv3_1_0_update_customer_number**](CustomerApi.md#o_bpv3_1_0_update_customer_number) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/number | Update the number of a Customer
[**o_bpv4_0_0_create_customer_attribute**](CustomerApi.md#o_bpv4_0_0_create_customer_attribute) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/attribute | Create Customer Attribute
[**o_bpv4_0_0_create_customer_message**](CustomerApi.md#o_bpv4_0_0_create_customer_message) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/messages | Create Customer Message
[**o_bpv4_0_0_create_or_update_customer_attribute_attribute_definition**](CustomerApi.md#o_bpv4_0_0_create_or_update_customer_attribute_attribute_definition) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/customer | Create or Update Customer Attribute Definition
[**o_bpv4_0_0_create_user_customer_links**](CustomerApi.md#o_bpv4_0_0_create_user_customer_links) | **POST** /obp/v5.0.0/banks/{BANK_ID}/user_customer_links | Create User Customer Link
[**o_bpv4_0_0_delete_customer_attribute**](CustomerApi.md#o_bpv4_0_0_delete_customer_attribute) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/{CUSTOMER_ID}/attributes/CUSTOMER_ATTRIBUTE_ID | Delete Customer Attribute
[**o_bpv4_0_0_delete_customer_attribute_definition**](CustomerApi.md#o_bpv4_0_0_delete_customer_attribute_definition) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/ATTRIBUTE_DEFINITION_ID/customer | Delete Customer Attribute Definition
[**o_bpv4_0_0_delete_customer_cascade**](CustomerApi.md#o_bpv4_0_0_delete_customer_cascade) | **DELETE** /obp/v5.0.0/management/cascading/banks/{BANK_ID}/customers/{CUSTOMER_ID} | Delete Customer Cascade
[**o_bpv4_0_0_delete_user_customer_link**](CustomerApi.md#o_bpv4_0_0_delete_user_customer_link) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/user_customer_links/USER_CUSTOMER_LINK_ID | Delete User Customer Link
[**o_bpv4_0_0_get_correlated_users_info_by_customer_id**](CustomerApi.md#o_bpv4_0_0_get_correlated_users_info_by_customer_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/correlated-users | Get Correlated User Info by Customer
[**o_bpv4_0_0_get_customer_attribute_by_id**](CustomerApi.md#o_bpv4_0_0_get_customer_attribute_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/attributes/ATTRIBUTE_ID | Get Customer Attribute By Id
[**o_bpv4_0_0_get_customer_attribute_definition**](CustomerApi.md#o_bpv4_0_0_get_customer_attribute_definition) | **GET** /obp/v5.0.0/banks/{BANK_ID}/attribute-definitions/customer | Get Customer Attribute Definition
[**o_bpv4_0_0_get_customer_attributes**](CustomerApi.md#o_bpv4_0_0_get_customer_attributes) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/attributes | Get Customer Attributes
[**o_bpv4_0_0_get_customer_messages**](CustomerApi.md#o_bpv4_0_0_get_customer_messages) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/messages | Get Customer Messages for a Customer
[**o_bpv4_0_0_get_customers_at_any_bank**](CustomerApi.md#o_bpv4_0_0_get_customers_at_any_bank) | **GET** /obp/v5.0.0/customers | Get Customers at Any Bank
[**o_bpv4_0_0_get_customers_by_customer_phone_number**](CustomerApi.md#o_bpv4_0_0_get_customers_by_customer_phone_number) | **POST** /obp/v5.0.0/banks/{BANK_ID}/search/customers/mobile-phone-number | Get Customers by MOBILE_PHONE_NUMBER
[**o_bpv4_0_0_get_customers_minimal_at_any_bank**](CustomerApi.md#o_bpv4_0_0_get_customers_minimal_at_any_bank) | **GET** /obp/v5.0.0/customers-minimal | Get Customers Minimal at Any Bank
[**o_bpv4_0_0_get_my_correlated_entities**](CustomerApi.md#o_bpv4_0_0_get_my_correlated_entities) | **GET** /obp/v5.0.0/my/correlated-entities | Get Correlated Entities for the current User
[**o_bpv4_0_0_get_user_customer_links_by_customer_id**](CustomerApi.md#o_bpv4_0_0_get_user_customer_links_by_customer_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/user_customer_links/customers/{CUSTOMER_ID} | Get User Customer Links by Customer
[**o_bpv4_0_0_get_user_customer_links_by_user_id**](CustomerApi.md#o_bpv4_0_0_get_user_customer_links_by_user_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/user_customer_links/users/{USER_ID} | Get User Customer Links by User
[**o_bpv4_0_0_update_customer_attribute**](CustomerApi.md#o_bpv4_0_0_update_customer_attribute) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/attributes/CUSTOMER_ATTRIBUTE_ID | Update Customer Attribute
[**o_bpv5_0_0_create_customer**](CustomerApi.md#o_bpv5_0_0_create_customer) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers | Create Customer
[**o_bpv5_0_0_create_customer_account_link**](CustomerApi.md#o_bpv5_0_0_create_customer_account_link) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customer-account-links | Create Customer Account Link
[**o_bpv5_0_0_delete_customer_account_link_by_id**](CustomerApi.md#o_bpv5_0_0_delete_customer_account_link_by_id) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/customer-account-links/CUSTOMER_ACCOUNT_LINK_ID | Delete Customer Account Link
[**o_bpv5_0_0_get_customer_account_link_by_id**](CustomerApi.md#o_bpv5_0_0_get_customer_account_link_by_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customer-account-links/CUSTOMER_ACCOUNT_LINK_ID | Get Customer Account Link by Id
[**o_bpv5_0_0_get_customer_account_links_by_bank_id_account_id**](CustomerApi.md#o_bpv5_0_0_get_customer_account_links_by_bank_id_account_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/accounts/{ACCOUNT_ID}/customer-account-links | Get Customer Account Links by ACCOUNT_ID
[**o_bpv5_0_0_get_customer_account_links_by_customer_id**](CustomerApi.md#o_bpv5_0_0_get_customer_account_links_by_customer_id) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/customer-account-links | Get Customer Account Links by CUSTOMER_ID
[**o_bpv5_0_0_get_customer_overview**](CustomerApi.md#o_bpv5_0_0_get_customer_overview) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/customer-number-query/overview | Get Customer Overview
[**o_bpv5_0_0_get_customer_overview_flat**](CustomerApi.md#o_bpv5_0_0_get_customer_overview_flat) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/customer-number-query/overview-flat | Get Customer Overview Flat
[**o_bpv5_0_0_get_customers_at_one_bank**](CustomerApi.md#o_bpv5_0_0_get_customers_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers | Get Customers at Bank
[**o_bpv5_0_0_get_customers_minimal_at_one_bank**](CustomerApi.md#o_bpv5_0_0_get_customers_minimal_at_one_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers-minimal | Get Customers Minimal at Bank
[**o_bpv5_0_0_get_my_customers_at_any_bank**](CustomerApi.md#o_bpv5_0_0_get_my_customers_at_any_bank) | **GET** /obp/v5.0.0/my/customers | Get My Customers
[**o_bpv5_0_0_get_my_customers_at_bank**](CustomerApi.md#o_bpv5_0_0_get_my_customers_at_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/my/customers | Get My Customers at Bank
[**o_bpv5_0_0_update_customer_account_link_by_id**](CustomerApi.md#o_bpv5_0_0_update_customer_account_link_by_id) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customer-account-links/CUSTOMER_ACCOUNT_LINK_ID | Update Customer Account Link by Id


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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.AddCustomerMessageJson() # AddCustomerMessageJson | AddCustomerMessageJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Message
    api_response = api_instance.o_bpv1_4_0_create_customer_message(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv1_4_0_create_customer_message: %s\n" % e)
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

# **o_bpv1_4_0_get_crm_events**
> CrmEventsJson o_bpv1_4_0_get_crm_events(body, bank_id)

Get CRM Events

<p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get CRM Events
    api_response = api_instance.o_bpv1_4_0_get_crm_events(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv1_4_0_get_crm_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CrmEventsJson**](CrmEventsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_4_0_get_customer_messages**
> CustomerMessagesJson o_bpv1_4_0_get_customer_messages(body, bank_id)

Get Customer Messages for a Customer

<p>Get messages for the logged in customer<br />Messages sent to the currently authenticated user.</p><p>Authentication via OAuth is required.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Messages for a Customer
    api_response = api_instance.o_bpv1_4_0_get_customer_messages(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv1_4_0_get_customer_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerMessagesJson**](CustomerMessagesJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_add_kyc_check**
> KycCheckJSON o_bpv2_0_0_add_kyc_check(body, kyc_check_id, customer_id, bank_id)

Add KYC Check

<p>Add a KYC check for the customer specified by CUSTOMER_ID. KYC Checks store details of checks on a customer made by the KYC team, their comments and a satisfied status</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycCheckJSON() # PostKycCheckJSON | PostKycCheckJSON object that needs to be added.
kyc_check_id = 'kyc_check_id_example' # str | The kyc check id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Check
    api_response = api_instance.o_bpv2_0_0_add_kyc_check(body, kyc_check_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_add_kyc_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostKycCheckJSON**](PostKycCheckJSON.md)| PostKycCheckJSON object that needs to be added. | 
 **kyc_check_id** | **str**| The kyc check id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**KycCheckJSON**](KycCheckJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_add_kyc_document**
> KycDocumentJSON o_bpv2_0_0_add_kyc_document(body, kyc_document_id, customer_id, bank_id)

Add KYC Document

<p>Add a KYC document for the customer specified by CUSTOMER_ID. KYC Documents contain the document type (e.g. passport), place of issue, expiry etc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycDocumentJSON() # PostKycDocumentJSON | PostKycDocumentJSON object that needs to be added.
kyc_document_id = 'kyc_document_id_example' # str | The kyc document id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Document
    api_response = api_instance.o_bpv2_0_0_add_kyc_document(body, kyc_document_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_add_kyc_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostKycDocumentJSON**](PostKycDocumentJSON.md)| PostKycDocumentJSON object that needs to be added. | 
 **kyc_document_id** | **str**| The kyc document id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**KycDocumentJSON**](KycDocumentJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_add_kyc_media**
> KycMediaJSON o_bpv2_0_0_add_kyc_media(body, kyc_media_id, customer_id, bank_id)

Add KYC Media

<p>Add some KYC media for the customer specified by CUSTOMER_ID. KYC Media resources relate to KYC Documents and KYC Checks and contain media urls for scans of passports, utility bills etc</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycMediaJSON() # PostKycMediaJSON | PostKycMediaJSON object that needs to be added.
kyc_media_id = 'kyc_media_id_example' # str | The kyc media id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Media
    api_response = api_instance.o_bpv2_0_0_add_kyc_media(body, kyc_media_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_add_kyc_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostKycMediaJSON**](PostKycMediaJSON.md)| PostKycMediaJSON object that needs to be added. | 
 **kyc_media_id** | **str**| The kyc media id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**KycMediaJSON**](KycMediaJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_add_kyc_status**
> KycStatusJSON o_bpv2_0_0_add_kyc_status(body, customer_id, bank_id)

Add KYC Status

<p>Add a kyc_status for the customer specified by CUSTOMER_ID. KYC Status is a timeline of the KYC status of the customer</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycStatusJSON() # PostKycStatusJSON | PostKycStatusJSON object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Status
    api_response = api_instance.o_bpv2_0_0_add_kyc_status(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_add_kyc_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostKycStatusJSON**](PostKycStatusJSON.md)| PostKycStatusJSON object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**KycStatusJSON**](KycStatusJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_add_social_media_handle**
> SuccessMessage o_bpv2_0_0_add_social_media_handle(body, customer_id, bank_id)

Add Social Media Handle

<p>Add a social media handle for the customer specified by CUSTOMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.SocialMediaJSON() # SocialMediaJSON | SocialMediaJSON object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add Social Media Handle
    api_response = api_instance.o_bpv2_0_0_add_social_media_handle(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_add_social_media_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SocialMediaJSON**](SocialMediaJSON.md)| SocialMediaJSON object that needs to be added. | 
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

# **o_bpv2_0_0_get_kyc_checks**
> KycChecksJSON o_bpv2_0_0_get_kyc_checks(body, customer_id)

Get Customer KYC Checks

<p>Get KYC checks for the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Customer KYC Checks
    api_response = api_instance.o_bpv2_0_0_get_kyc_checks(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_get_kyc_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 

### Return type

[**KycChecksJSON**](KycChecksJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_get_kyc_documents**
> KycDocumentsJSON o_bpv2_0_0_get_kyc_documents(body, customer_id)

Get Customer KYC Documents

<p>Get KYC (know your customer) documents for a customer specified by CUSTOMER_ID<br />Get a list of documents that affirm the identity of the customer<br />Passport, driving licence etc.<br />Authentication is Optional</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Customer KYC Documents
    api_response = api_instance.o_bpv2_0_0_get_kyc_documents(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_get_kyc_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 

### Return type

[**KycDocumentsJSON**](KycDocumentsJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_get_kyc_media**
> KycMediasJSON o_bpv2_0_0_get_kyc_media(body, customer_id)

Get KYC Media for a customer

<p>Get KYC media (scans, pictures, videos) that affirms the identity of the customer.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get KYC Media for a customer
    api_response = api_instance.o_bpv2_0_0_get_kyc_media(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_get_kyc_media: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 

### Return type

[**KycMediasJSON**](KycMediasJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_get_kyc_statuses**
> KycStatusesJSON o_bpv2_0_0_get_kyc_statuses(body, customer_id)

Get Customer KYC statuses

<p>Get the KYC statuses for a customer specified by CUSTOMER_ID over time.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Customer KYC statuses
    api_response = api_instance.o_bpv2_0_0_get_kyc_statuses(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_get_kyc_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 

### Return type

[**KycStatusesJSON**](KycStatusesJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_get_social_media_handles**
> SocialMediasJSON o_bpv2_0_0_get_social_media_handles(body, customer_id, bank_id)

Get Customer Social Media Handles

<p>Get social media handles for a customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Social Media Handles
    api_response = api_instance.o_bpv2_0_0_get_social_media_handles(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv2_0_0_get_social_media_handles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**SocialMediasJSON**](SocialMediasJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_customers_for_user**
> CustomersWithAttributesJsonV300 o_bpv3_0_0_get_customers_for_user()

Get Customers for Current User

<p>Gets all Customers that are linked to a User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))

try:
    # Get Customers for Current User
    api_response = api_instance.o_bpv3_0_0_get_customers_for_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_0_0_get_customers_for_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomersWithAttributesJsonV300**](CustomersWithAttributesJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_credit_limit_request**
> CreditLimitOrderResponseJson o_bpv3_1_0_create_credit_limit_request(body, customer_id, bank_id)

Create Credit Limit Order Request

<p><strong>NOTE: This endpoint currently only returns example data.</strong></p><p>Create credit limit order request</p><p>Authentication is Optional</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CreditLimitRequestJson() # CreditLimitRequestJson | CreditLimitRequestJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Credit Limit Order Request
    api_response = api_instance.o_bpv3_1_0_create_credit_limit_request(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_create_credit_limit_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreditLimitRequestJson**](CreditLimitRequestJson.md)| CreditLimitRequestJson object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CreditLimitOrderResponseJson**](CreditLimitOrderResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_customer_address**
> CustomerAddressJsonV310 o_bpv3_1_0_create_customer_address(body, customer_id, bank_id)

Create Address

<p>Create an Address for a Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerAddressJsonV310() # PostCustomerAddressJsonV310 | PostCustomerAddressJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Address
    api_response = api_instance.o_bpv3_1_0_create_customer_address(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_create_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerAddressJsonV310**](PostCustomerAddressJsonV310.md)| PostCustomerAddressJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAddressJsonV310**](CustomerAddressJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CreateMeetingJsonV310() # CreateMeetingJsonV310 | CreateMeetingJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Meeting (video conference/call)
    api_response = api_instance.o_bpv3_1_0_create_meeting(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_create_meeting: %s\n" % e)
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

# **o_bpv3_1_0_create_tax_residence**
> TaxResidenceV310 o_bpv3_1_0_create_tax_residence(body, customer_id, bank_id)

Create Tax Residence

<p>Create a Tax Residence for a Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostTaxResidenceJsonV310() # PostTaxResidenceJsonV310 | PostTaxResidenceJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Tax Residence
    api_response = api_instance.o_bpv3_1_0_create_tax_residence(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_create_tax_residence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostTaxResidenceJsonV310**](PostTaxResidenceJsonV310.md)| PostTaxResidenceJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TaxResidenceV310**](TaxResidenceV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_customer_address**
> o_bpv3_1_0_delete_customer_address(customer_address_id, customer_id, bank_id)

Delete Customer Address

<p>Delete an Address of the Customer specified by CUSTOMER_ADDRESS_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_address_id = 'customer_address_id_example' # str | the customer address id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Customer Address
    api_instance.o_bpv3_1_0_delete_customer_address(customer_address_id, customer_id, bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_delete_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_address_id** | **str**| the customer address id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_tax_residence**
> o_bpv3_1_0_delete_tax_residence(tax_residence_id, customer_id, bank_id)

Delete Tax Residence

<p>Delete a Tax Residence of the Customer specified by TAX_RESIDENCE_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
tax_residence_id = 'tax_residence_id_example' # str | the tax residence id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Tax Residence
    api_instance.o_bpv3_1_0_delete_tax_residence(tax_residence_id, customer_id, bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_delete_tax_residence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_residence_id** | **str**| the tax residence id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_credit_limit_request_by_request_id**
> CreditLimitOrderJson o_bpv3_1_0_get_credit_limit_request_by_request_id(request_id, customer_id, bank_id)

Get Credit Limit Order Request By Request Id

<p><strong>NOTE: This endpoint currently only returns example data.</strong></p><pre><code>    Get Credit Limit Order Request By Request Id</code></pre><p>Authentication is Optional</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
request_id = 'request_id_example' # str | the request id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Credit Limit Order Request By Request Id
    api_response = api_instance.o_bpv3_1_0_get_credit_limit_request_by_request_id(request_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_credit_limit_request_by_request_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| the request id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CreditLimitOrderJson**](CreditLimitOrderJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_credit_limit_requests**
> CreditLimitOrderJson o_bpv3_1_0_get_credit_limit_requests(customer_id, bank_id)

Get Credit Limit Order Requests 

<p><strong>NOTE: This endpoint currently only returns example data.</strong></p><p>Get Credit Limit Order Requests</p><p>Authentication is Optional</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Credit Limit Order Requests 
    api_response = api_instance.o_bpv3_1_0_get_credit_limit_requests(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_credit_limit_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CreditLimitOrderJson**](CreditLimitOrderJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_customer_addresses**
> CustomerAddressesJsonV310 o_bpv3_1_0_get_customer_addresses(customer_id, bank_id)

Get Customer Addresses

<p>Get the Addresses of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Addresses
    api_response = api_instance.o_bpv3_1_0_get_customer_addresses(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_customer_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAddressesJsonV310**](CustomerAddressesJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_customer_by_customer_id**
> CustomerWithAttributesJsonV310 o_bpv3_1_0_get_customer_by_customer_id(customer_id, bank_id)

Get Customer by CUSTOMER_ID

<p>Gets the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer by CUSTOMER_ID
    api_response = api_instance.o_bpv3_1_0_get_customer_by_customer_id(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_customer_by_customer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerWithAttributesJsonV310**](CustomerWithAttributesJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_customer_by_customer_number**
> CustomerWithAttributesJsonV310 o_bpv3_1_0_get_customer_by_customer_number(body, bank_id)

Get Customer by CUSTOMER_NUMBER

<p>Gets the Customer specified by CUSTOMER_NUMBER.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerNumberJsonV310() # PostCustomerNumberJsonV310 | PostCustomerNumberJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer by CUSTOMER_NUMBER
    api_response = api_instance.o_bpv3_1_0_get_customer_by_customer_number(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_customer_by_customer_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerNumberJsonV310**](PostCustomerNumberJsonV310.md)| PostCustomerNumberJsonV310 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerWithAttributesJsonV310**](CustomerWithAttributesJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_firehose_customers**
> CustomerJSONs o_bpv3_1_0_get_firehose_customers(bank_id)

Get Firehose Customers

<p>Get Customers that has a firehose View.</p><p>Allows bulk access to customers.<br />User must have the CanUseFirehoseAtAnyBank Role</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>from_date=DATE =&gt; example value: 1970-01-01T00:00:00.000Z. NOTE! The default value is one year ago (1970-01-01T00:00:00.000Z).</li><li>to_date=DATE =&gt; example value: 2023-02-16T16:23:47.689Z. NOTE! The default value is now (2023-02-16T16:23:47.689Z).</li></ul><p>Date format parameter: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'(1100-01-01T01:01:01.000Z) ==&gt; time zone is UTC.</p><p>eg3:?sort_direction=ASC&amp;limit=100&amp;offset=0&amp;from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Firehose Customers
    api_response = api_instance.o_bpv3_1_0_get_firehose_customers(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_firehose_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJSONs**](CustomerJSONs.md)

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
meeting_id = 'meeting_id_example' # str | the meeting id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Meeting
    api_response = api_instance.o_bpv3_1_0_get_meeting(meeting_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_meeting: %s\n" % e)
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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Meetings
    api_response = api_instance.o_bpv3_1_0_get_meetings(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_meetings: %s\n" % e)
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

# **o_bpv3_1_0_get_tax_residence**
> TaxResidenceJsonV310 o_bpv3_1_0_get_tax_residence(customer_id, bank_id)

Get Tax Residences of Customer

<p>Get the Tax Residences of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Tax Residences of Customer
    api_response = api_instance.o_bpv3_1_0_get_tax_residence(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_get_tax_residence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**TaxResidenceJsonV310**](TaxResidenceJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_address**
> CustomerAddressJsonV310 o_bpv3_1_0_update_customer_address(body, customer_address_id, customer_id, bank_id)

Update the Address of a Customer

<p>Update an Address of the Customer specified by CUSTOMER_ADDRESS_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerAddressJsonV310() # PostCustomerAddressJsonV310 | PostCustomerAddressJsonV310 object that needs to be added.
customer_address_id = 'customer_address_id_example' # str | the customer address id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the Address of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_address(body, customer_address_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerAddressJsonV310**](PostCustomerAddressJsonV310.md)| PostCustomerAddressJsonV310 object that needs to be added. | 
 **customer_address_id** | **str**| the customer address id | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAddressJsonV310**](CustomerAddressJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_branch**
> CustomerJsonV310 o_bpv3_1_0_update_customer_branch(body, customer_id, bank_id)

Update the Branch of a Customer

<p>Update the Branch of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerBranchJsonV310() # PutUpdateCustomerBranchJsonV310 | PutUpdateCustomerBranchJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the Branch of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_branch(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_branch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerBranchJsonV310**](PutUpdateCustomerBranchJsonV310.md)| PutUpdateCustomerBranchJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_credit_limit**
> CustomerJsonV310 o_bpv3_1_0_update_customer_credit_limit(body, customer_id, bank_id)

Update the credit limit of a Customer

<p>Update the credit limit of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerCreditLimitJsonV310() # PutUpdateCustomerCreditLimitJsonV310 | PutUpdateCustomerCreditLimitJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the credit limit of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_credit_limit(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_credit_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerCreditLimitJsonV310**](PutUpdateCustomerCreditLimitJsonV310.md)| PutUpdateCustomerCreditLimitJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_credit_rating_and_source**
> CustomerJsonV310 o_bpv3_1_0_update_customer_credit_rating_and_source(body, customer_id, bank_id)

Update the credit rating and source of a Customer

<p>Update the credit rating and source of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerCreditRatingAndSourceJsonV310() # PutUpdateCustomerCreditRatingAndSourceJsonV310 | PutUpdateCustomerCreditRatingAndSourceJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the credit rating and source of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_credit_rating_and_source(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_credit_rating_and_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerCreditRatingAndSourceJsonV310**](PutUpdateCustomerCreditRatingAndSourceJsonV310.md)| PutUpdateCustomerCreditRatingAndSourceJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_data**
> CustomerJsonV310 o_bpv3_1_0_update_customer_data(body, customer_id, bank_id)

Update the other data of a Customer

<p>Update the other data of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerDataJsonV310() # PutUpdateCustomerDataJsonV310 | PutUpdateCustomerDataJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the other data of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_data(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerDataJsonV310**](PutUpdateCustomerDataJsonV310.md)| PutUpdateCustomerDataJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_email**
> CustomerJsonV310 o_bpv3_1_0_update_customer_email(body, customer_id, bank_id)

Update the email of a Customer

<p>Update an email of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerEmailJsonV310() # PutUpdateCustomerEmailJsonV310 | PutUpdateCustomerEmailJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the email of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_email(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerEmailJsonV310**](PutUpdateCustomerEmailJsonV310.md)| PutUpdateCustomerEmailJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_identity**
> CustomerJsonV310 o_bpv3_1_0_update_customer_identity(body, customer_id, bank_id)

Update the identity data of a Customer

<p>Update the identity data of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerIdentityJsonV310() # PutUpdateCustomerIdentityJsonV310 | PutUpdateCustomerIdentityJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the identity data of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_identity(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerIdentityJsonV310**](PutUpdateCustomerIdentityJsonV310.md)| PutUpdateCustomerIdentityJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_mobile_number**
> CustomerJsonV310 o_bpv3_1_0_update_customer_mobile_number(body, customer_id, bank_id)

Update the mobile number of a Customer

<p>Update the mobile number of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerMobilePhoneNumberJsonV310() # PutUpdateCustomerMobilePhoneNumberJsonV310 | PutUpdateCustomerMobilePhoneNumberJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the mobile number of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_mobile_number(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_mobile_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerMobilePhoneNumberJsonV310**](PutUpdateCustomerMobilePhoneNumberJsonV310.md)| PutUpdateCustomerMobilePhoneNumberJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_customer_number**
> CustomerJsonV310 o_bpv3_1_0_update_customer_number(body, customer_id, bank_id)

Update the number of a Customer

<p>Update the number of the Customer specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PutUpdateCustomerNumberJsonV310() # PutUpdateCustomerNumberJsonV310 | PutUpdateCustomerNumberJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update the number of a Customer
    api_response = api_instance.o_bpv3_1_0_update_customer_number(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv3_1_0_update_customer_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutUpdateCustomerNumberJsonV310**](PutUpdateCustomerNumberJsonV310.md)| PutUpdateCustomerNumberJsonV310 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_customer_attribute**
> CustomerAttributeResponseJsonV300 o_bpv4_0_0_create_customer_attribute(body, customer_id, bank_id)

Create Customer Attribute

<p>Create Customer Attribute</p><p>The type field must be one of &quot;STRING&quot;, &quot;INTEGER&quot;, &quot;DOUBLE&quot; or DATE_WITH_DAY&quot;</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CustomerAttributeJsonV400() # CustomerAttributeJsonV400 | CustomerAttributeJsonV400 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Attribute
    api_response = api_instance.o_bpv4_0_0_create_customer_attribute(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_create_customer_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerAttributeJsonV400**](CustomerAttributeJsonV400.md)| CustomerAttributeJsonV400 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAttributeResponseJsonV300**](CustomerAttributeResponseJsonV300.md)

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CreateMessageJsonV400() # CreateMessageJsonV400 | CreateMessageJsonV400 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Message
    api_response = api_instance.o_bpv4_0_0_create_customer_message(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_create_customer_message: %s\n" % e)
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

# **o_bpv4_0_0_create_or_update_customer_attribute_attribute_definition**
> AttributeDefinitionResponseJsonV400 o_bpv4_0_0_create_or_update_customer_attribute_attribute_definition(body, bank_id)

Create or Update Customer Attribute Definition

<p>Create or Update Customer Attribute Definition</p><p>The category field must be one of: Customer</p><p>The type field must be one of; DOUBLE, STRING, INTEGER and DATE_WITH_DAY</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.AttributeDefinitionJsonV400() # AttributeDefinitionJsonV400 | AttributeDefinitionJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create or Update Customer Attribute Definition
    api_response = api_instance.o_bpv4_0_0_create_or_update_customer_attribute_attribute_definition(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_create_or_update_customer_attribute_attribute_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributeDefinitionJsonV400**](AttributeDefinitionJsonV400.md)| AttributeDefinitionJsonV400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**AttributeDefinitionResponseJsonV400**](AttributeDefinitionResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_user_customer_links**
> UserCustomerLinkJson o_bpv4_0_0_create_user_customer_links(body, bank_id)

Create User Customer Link

<p>Link a User to a Customer</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CreateUserCustomerLinkJson() # CreateUserCustomerLinkJson | CreateUserCustomerLinkJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create User Customer Link
    api_response = api_instance.o_bpv4_0_0_create_user_customer_links(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_create_user_customer_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserCustomerLinkJson**](CreateUserCustomerLinkJson.md)| CreateUserCustomerLinkJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserCustomerLinkJson**](UserCustomerLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_customer_attribute**
> o_bpv4_0_0_delete_customer_attribute(customer_id, bank_id)

Delete Customer Attribute

<p>Delete Customer Attribute</p><p>CustomerAttributes are used to enhance the OBP Customer object with Bank specific entities.</p><p>Delete a Customer Attribute by its id.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Customer Attribute
    api_instance.o_bpv4_0_0_delete_customer_attribute(customer_id, bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_delete_customer_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_customer_attribute_definition**
> o_bpv4_0_0_delete_customer_attribute_definition(bank_id)

Delete Customer Attribute Definition

<p>Delete Customer Attribute Definition by ATTRIBUTE_DEFINITION_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Customer Attribute Definition
    api_instance.o_bpv4_0_0_delete_customer_attribute_definition(bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_delete_customer_attribute_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_customer_cascade**
> o_bpv4_0_0_delete_customer_cascade(customer_id, bank_id)

Delete Customer Cascade

<p>Delete a Customer Cascade specified by CUSTOMER_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Customer Cascade
    api_instance.o_bpv4_0_0_delete_customer_cascade(customer_id, bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_delete_customer_cascade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_user_customer_link**
> o_bpv4_0_0_delete_user_customer_link(bank_id)

Delete User Customer Link

<p>Delete User Customer Link by USER_CUSTOMER_LINK_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete User Customer Link
    api_instance.o_bpv4_0_0_delete_user_customer_link(bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_delete_user_customer_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_correlated_users_info_by_customer_id**
> CustomerAndUsersWithAttributesResponseJson o_bpv4_0_0_get_correlated_users_info_by_customer_id(customer_id, bank_id)

Get Correlated User Info by Customer

<p>Get Correlated User Info by CUSTOMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Correlated User Info by Customer
    api_response = api_instance.o_bpv4_0_0_get_correlated_users_info_by_customer_id(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_correlated_users_info_by_customer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAndUsersWithAttributesResponseJson**](CustomerAndUsersWithAttributesResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customer_attribute_by_id**
> CustomerAttributeResponseJsonV300 o_bpv4_0_0_get_customer_attribute_by_id(customer_id, bank_id)

Get Customer Attribute By Id

<p>Get Customer Attribute By Id</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Attribute By Id
    api_response = api_instance.o_bpv4_0_0_get_customer_attribute_by_id(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customer_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAttributeResponseJsonV300**](CustomerAttributeResponseJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customer_attribute_definition**
> AttributeDefinitionsResponseJsonV400 o_bpv4_0_0_get_customer_attribute_definition(bank_id)

Get Customer Attribute Definition

<p>Get Customer Attribute Definition</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Attribute Definition
    api_response = api_instance.o_bpv4_0_0_get_customer_attribute_definition(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customer_attribute_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AttributeDefinitionsResponseJsonV400**](AttributeDefinitionsResponseJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customer_attributes**
> CustomerAttributesResponseJson o_bpv4_0_0_get_customer_attributes(customer_id, bank_id)

Get Customer Attributes

<p>Get Customer Attributes</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Attributes
    api_response = api_instance.o_bpv4_0_0_get_customer_attributes(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customer_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAttributesResponseJson**](CustomerAttributesResponseJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customer_messages**
> CustomerMessagesJsonV400 o_bpv4_0_0_get_customer_messages(customer_id, bank_id)

Get Customer Messages for a Customer

<p>Get messages for the customer specified by CUSTOMER_ID<br />Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Messages for a Customer
    api_response = api_instance.o_bpv4_0_0_get_customer_messages(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customer_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerMessagesJsonV400**](CustomerMessagesJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customers_at_any_bank**
> CustomerJSONsV300 o_bpv4_0_0_get_customers_at_any_bank()

Get Customers at Any Bank

<p>Get Customers at Any Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))

try:
    # Get Customers at Any Bank
    api_response = api_instance.o_bpv4_0_0_get_customers_at_any_bank()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customers_at_any_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerJSONsV300**](CustomerJSONsV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customers_by_customer_phone_number**
> CustomerJsonV310 o_bpv4_0_0_get_customers_by_customer_phone_number(body, bank_id)

Get Customers by MOBILE_PHONE_NUMBER

<p>Gets the Customers specified by MOBILE_PHONE_NUMBER.</p><p>There are two wildcards often used in conjunction with the LIKE operator:<br />% - The percent sign represents zero, one, or multiple characters<br />_ - The underscore represents a single character<br />For example {&quot;customer_phone_number&quot;:&quot;%381%&quot;} lists all numbers which contain 381 sequence</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerPhoneNumberJsonV400() # PostCustomerPhoneNumberJsonV400 | PostCustomerPhoneNumberJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customers by MOBILE_PHONE_NUMBER
    api_response = api_instance.o_bpv4_0_0_get_customers_by_customer_phone_number(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customers_by_customer_phone_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerPhoneNumberJsonV400**](PostCustomerPhoneNumberJsonV400.md)| PostCustomerPhoneNumberJsonV400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJsonV310**](CustomerJsonV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_customers_minimal_at_any_bank**
> CustomersMinimalJsonV400 o_bpv4_0_0_get_customers_minimal_at_any_bank()

Get Customers Minimal at Any Bank

<p>Get Customers Minimal at Any Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))

try:
    # Get Customers Minimal at Any Bank
    api_response = api_instance.o_bpv4_0_0_get_customers_minimal_at_any_bank()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_customers_minimal_at_any_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomersMinimalJsonV400**](CustomersMinimalJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_correlated_entities**
> CorrelatedEntities o_bpv4_0_0_get_my_correlated_entities()

Get Correlated Entities for the current User

<p>Correlated Entities are users and customers linked to the currently authenticated user via User-Customer-Links</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))

try:
    # Get Correlated Entities for the current User
    api_response = api_instance.o_bpv4_0_0_get_my_correlated_entities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_my_correlated_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CorrelatedEntities**](CorrelatedEntities.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_customer_links_by_customer_id**
> UserCustomerLinksJson o_bpv4_0_0_get_user_customer_links_by_customer_id(customer_id, bank_id)

Get User Customer Links by Customer

<p>Get User Customer Links by CUSTOMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get User Customer Links by Customer
    api_response = api_instance.o_bpv4_0_0_get_user_customer_links_by_customer_id(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_user_customer_links_by_customer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserCustomerLinksJson**](UserCustomerLinksJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_user_customer_links_by_user_id**
> UserCustomerLinksJson o_bpv4_0_0_get_user_customer_links_by_user_id(user_id, bank_id)

Get User Customer Links by User

<p>Get User Customer Links by USER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
user_id = 'user_id_example' # str | The user id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get User Customer Links by User
    api_response = api_instance.o_bpv4_0_0_get_user_customer_links_by_user_id(user_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_get_user_customer_links_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**UserCustomerLinksJson**](UserCustomerLinksJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_customer_attribute**
> CustomerAttributeResponseJsonV300 o_bpv4_0_0_update_customer_attribute(body, customer_id, bank_id)

Update Customer Attribute

<p>Update Customer Attribute</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CustomerAttributeJsonV400() # CustomerAttributeJsonV400 | CustomerAttributeJsonV400 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Customer Attribute
    api_response = api_instance.o_bpv4_0_0_update_customer_attribute(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv4_0_0_update_customer_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerAttributeJsonV400**](CustomerAttributeJsonV400.md)| CustomerAttributeJsonV400 object that needs to be added. | 
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAttributeResponseJsonV300**](CustomerAttributeResponseJsonV300.md)

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerJsonV500() # PostCustomerJsonV500 | PostCustomerJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer
    api_response = api_instance.o_bpv5_0_0_create_customer(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_create_customer: %s\n" % e)
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

# **o_bpv5_0_0_create_customer_account_link**
> CustomerAccountLinkJson o_bpv5_0_0_create_customer_account_link(body, bank_id)

Create Customer Account Link

<p>Link a Customer to a Account</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.CreateCustomerAccountLinkJson() # CreateCustomerAccountLinkJson | CreateCustomerAccountLinkJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Customer Account Link
    api_response = api_instance.o_bpv5_0_0_create_customer_account_link(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_create_customer_account_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerAccountLinkJson**](CreateCustomerAccountLinkJson.md)| CreateCustomerAccountLinkJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAccountLinkJson**](CustomerAccountLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_delete_customer_account_link_by_id**
> o_bpv5_0_0_delete_customer_account_link_by_id(bank_id)

Delete Customer Account Link

<p>Delete Customer Account Link by CUSTOMER_ACCOUNT_LINK_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Customer Account Link
    api_instance.o_bpv5_0_0_delete_customer_account_link_by_id(bank_id)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_delete_customer_account_link_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customer_account_link_by_id**
> CustomerAccountLinkJson o_bpv5_0_0_get_customer_account_link_by_id(bank_id)

Get Customer Account Link by Id

<p>Get Customer Account Link by CUSTOMER_ACCOUNT_LINK_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Account Link by Id
    api_response = api_instance.o_bpv5_0_0_get_customer_account_link_by_id(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customer_account_link_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAccountLinkJson**](CustomerAccountLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customer_account_links_by_bank_id_account_id**
> CustomerAccountLinksJson o_bpv5_0_0_get_customer_account_links_by_bank_id_account_id(account_id, bank_id)

Get Customer Account Links by ACCOUNT_ID

<p>Get Customer Account Links by ACCOUNT_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
account_id = 'account_id_example' # str | The account id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Account Links by ACCOUNT_ID
    api_response = api_instance.o_bpv5_0_0_get_customer_account_links_by_bank_id_account_id(account_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customer_account_links_by_bank_id_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The account id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAccountLinksJson**](CustomerAccountLinksJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customer_account_links_by_customer_id**
> CustomerAccountLinksJson o_bpv5_0_0_get_customer_account_links_by_customer_id(customer_id, bank_id)

Get Customer Account Links by CUSTOMER_ID

<p>Get Customer Account Links by CUSTOMER_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Account Links by CUSTOMER_ID
    api_response = api_instance.o_bpv5_0_0_get_customer_account_links_by_customer_id(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customer_account_links_by_customer_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The customer id | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAccountLinksJson**](CustomerAccountLinksJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customer_overview**
> CustomerOverviewJsonV500 o_bpv5_0_0_get_customer_overview(body, bank_id)

Get Customer Overview

<p>Gets the Customer Overview specified by customer_number and bank_code.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerOverviewJsonV500() # PostCustomerOverviewJsonV500 | PostCustomerOverviewJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Overview
    api_response = api_instance.o_bpv5_0_0_get_customer_overview(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customer_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerOverviewJsonV500**](PostCustomerOverviewJsonV500.md)| PostCustomerOverviewJsonV500 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerOverviewJsonV500**](CustomerOverviewJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customer_overview_flat**
> CustomerOverviewFlatJsonV500 o_bpv5_0_0_get_customer_overview_flat(body, bank_id)

Get Customer Overview Flat

<p>Gets the Customer Overview Flat specified by customer_number and bank_code.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerOverviewJsonV500() # PostCustomerOverviewJsonV500 | PostCustomerOverviewJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Overview Flat
    api_response = api_instance.o_bpv5_0_0_get_customer_overview_flat(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customer_overview_flat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostCustomerOverviewJsonV500**](PostCustomerOverviewJsonV500.md)| PostCustomerOverviewJsonV500 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerOverviewFlatJsonV500**](CustomerOverviewFlatJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customers_at_one_bank**
> CustomerJSONsV300 o_bpv5_0_0_get_customers_at_one_bank(bank_id)

Get Customers at Bank

<p>Get Customers at Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customers at Bank
    api_response = api_instance.o_bpv5_0_0_get_customers_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customers_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJSONsV300**](CustomerJSONsV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_customers_minimal_at_one_bank**
> CustomersMinimalJsonV400 o_bpv5_0_0_get_customers_minimal_at_one_bank(bank_id)

Get Customers Minimal at Bank

<p>Get Customers Minimal at Bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customers Minimal at Bank
    api_response = api_instance.o_bpv5_0_0_get_customers_minimal_at_one_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_customers_minimal_at_one_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomersMinimalJsonV400**](CustomersMinimalJsonV400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_my_customers_at_any_bank**
> CustomerJsonV210 o_bpv5_0_0_get_my_customers_at_any_bank()

Get My Customers

<p>Gets all Customers that are linked to me.</p><p>Authentication via OAuth is required.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))

try:
    # Get My Customers
    api_response = api_instance.o_bpv5_0_0_get_my_customers_at_any_bank()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_my_customers_at_any_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerJsonV210**](CustomerJsonV210.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_my_customers_at_bank**
> CustomerJSONs o_bpv5_0_0_get_my_customers_at_bank(bank_id)

Get My Customers at Bank

<p>Returns a list of Customers at the Bank that are linked to the currently authenticated User.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get My Customers at Bank
    api_response = api_instance.o_bpv5_0_0_get_my_customers_at_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_get_my_customers_at_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerJSONs**](CustomerJSONs.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_update_customer_account_link_by_id**
> CustomerAccountLinkJson o_bpv5_0_0_update_customer_account_link_by_id(body, bank_id)

Update Customer Account Link by Id

<p>Update Customer Account Link by CUSTOMER_ACCOUNT_LINK_ID</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.CustomerApi(obp_python.ApiClient(configuration))
body = obp_python.UpdateCustomerAccountLinkJson() # UpdateCustomerAccountLinkJson | UpdateCustomerAccountLinkJson object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Customer Account Link by Id
    api_response = api_instance.o_bpv5_0_0_update_customer_account_link_by_id(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->o_bpv5_0_0_update_customer_account_link_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCustomerAccountLinkJson**](UpdateCustomerAccountLinkJson.md)| UpdateCustomerAccountLinkJson object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**CustomerAccountLinkJson**](CustomerAccountLinkJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

