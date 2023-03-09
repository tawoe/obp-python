# obp_python.KYCApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv2_0_0_add_kyc_check**](KYCApi.md#o_bpv2_0_0_add_kyc_check) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_check/{KYC_CHECK_ID} | Add KYC Check
[**o_bpv2_0_0_add_kyc_document**](KYCApi.md#o_bpv2_0_0_add_kyc_document) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_documents/{KYC_DOCUMENT_ID} | Add KYC Document
[**o_bpv2_0_0_add_kyc_media**](KYCApi.md#o_bpv2_0_0_add_kyc_media) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_media/{KYC_MEDIA_ID} | Add KYC Media
[**o_bpv2_0_0_add_kyc_status**](KYCApi.md#o_bpv2_0_0_add_kyc_status) | **PUT** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/kyc_statuses | Add KYC Status
[**o_bpv2_0_0_get_kyc_checks**](KYCApi.md#o_bpv2_0_0_get_kyc_checks) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_checks | Get Customer KYC Checks
[**o_bpv2_0_0_get_kyc_documents**](KYCApi.md#o_bpv2_0_0_get_kyc_documents) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_documents | Get Customer KYC Documents
[**o_bpv2_0_0_get_kyc_media**](KYCApi.md#o_bpv2_0_0_get_kyc_media) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_media | Get KYC Media for a customer
[**o_bpv2_0_0_get_kyc_statuses**](KYCApi.md#o_bpv2_0_0_get_kyc_statuses) | **GET** /obp/v5.0.0/customers/{CUSTOMER_ID}/kyc_statuses | Get Customer KYC statuses
[**o_bpv3_1_0_create_tax_residence**](KYCApi.md#o_bpv3_1_0_create_tax_residence) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/tax-residence | Create Tax Residence
[**o_bpv3_1_0_delete_customer_address**](KYCApi.md#o_bpv3_1_0_delete_customer_address) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/addresses/{CUSTOMER_ADDRESS_ID} | Delete Customer Address
[**o_bpv3_1_0_delete_tax_residence**](KYCApi.md#o_bpv3_1_0_delete_tax_residence) | **DELETE** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/tax_residencies/{TAX_RESIDENCE_ID} | Delete Tax Residence
[**o_bpv3_1_0_get_customer_addresses**](KYCApi.md#o_bpv3_1_0_get_customer_addresses) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/addresses | Get Customer Addresses
[**o_bpv3_1_0_get_customer_by_customer_number**](KYCApi.md#o_bpv3_1_0_get_customer_by_customer_number) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/customer-number | Get Customer by CUSTOMER_NUMBER
[**o_bpv3_1_0_get_tax_residence**](KYCApi.md#o_bpv3_1_0_get_tax_residence) | **GET** /obp/v5.0.0/banks/{BANK_ID}/customers/{CUSTOMER_ID}/tax-residences | Get Tax Residences of Customer
[**o_bpv4_0_0_create_user_invitation**](KYCApi.md#o_bpv4_0_0_create_user_invitation) | **POST** /obp/v5.0.0/banks/{BANK_ID}/user-invitation | Create User Invitation
[**o_bpv4_0_0_get_customers_by_customer_phone_number**](KYCApi.md#o_bpv4_0_0_get_customers_by_customer_phone_number) | **POST** /obp/v5.0.0/banks/{BANK_ID}/search/customers/mobile-phone-number | Get Customers by MOBILE_PHONE_NUMBER
[**o_bpv4_0_0_get_user_invitation_anonymous**](KYCApi.md#o_bpv4_0_0_get_user_invitation_anonymous) | **POST** /obp/v5.0.0/banks/{BANK_ID}/user-invitations | Get User Invitation Information
[**o_bpv5_0_0_get_customer_overview**](KYCApi.md#o_bpv5_0_0_get_customer_overview) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/customer-number-query/overview | Get Customer Overview
[**o_bpv5_0_0_get_customer_overview_flat**](KYCApi.md#o_bpv5_0_0_get_customer_overview_flat) | **POST** /obp/v5.0.0/banks/{BANK_ID}/customers/customer-number-query/overview-flat | Get Customer Overview Flat


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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycCheckJSON() # PostKycCheckJSON | PostKycCheckJSON object that needs to be added.
kyc_check_id = 'kyc_check_id_example' # str | The kyc check id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Check
    api_response = api_instance.o_bpv2_0_0_add_kyc_check(body, kyc_check_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_add_kyc_check: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycDocumentJSON() # PostKycDocumentJSON | PostKycDocumentJSON object that needs to be added.
kyc_document_id = 'kyc_document_id_example' # str | The kyc document id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Document
    api_response = api_instance.o_bpv2_0_0_add_kyc_document(body, kyc_document_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_add_kyc_document: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycMediaJSON() # PostKycMediaJSON | PostKycMediaJSON object that needs to be added.
kyc_media_id = 'kyc_media_id_example' # str | The kyc media id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Media
    api_response = api_instance.o_bpv2_0_0_add_kyc_media(body, kyc_media_id, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_add_kyc_media: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostKycStatusJSON() # PostKycStatusJSON | PostKycStatusJSON object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Add KYC Status
    api_response = api_instance.o_bpv2_0_0_add_kyc_status(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_add_kyc_status: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Customer KYC Checks
    api_response = api_instance.o_bpv2_0_0_get_kyc_checks(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_get_kyc_checks: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Customer KYC Documents
    api_response = api_instance.o_bpv2_0_0_get_kyc_documents(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_get_kyc_documents: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get KYC Media for a customer
    api_response = api_instance.o_bpv2_0_0_get_kyc_media(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_get_kyc_media: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id

try:
    # Get Customer KYC statuses
    api_response = api_instance.o_bpv2_0_0_get_kyc_statuses(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv2_0_0_get_kyc_statuses: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostTaxResidenceJsonV310() # PostTaxResidenceJsonV310 | PostTaxResidenceJsonV310 object that needs to be added.
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Tax Residence
    api_response = api_instance.o_bpv3_1_0_create_tax_residence(body, customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv3_1_0_create_tax_residence: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
customer_address_id = 'customer_address_id_example' # str | the customer address id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Customer Address
    api_instance.o_bpv3_1_0_delete_customer_address(customer_address_id, customer_id, bank_id)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv3_1_0_delete_customer_address: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
tax_residence_id = 'tax_residence_id_example' # str | the tax residence id
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Tax Residence
    api_instance.o_bpv3_1_0_delete_tax_residence(tax_residence_id, customer_id, bank_id)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv3_1_0_delete_tax_residence: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Addresses
    api_response = api_instance.o_bpv3_1_0_get_customer_addresses(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv3_1_0_get_customer_addresses: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerNumberJsonV310() # PostCustomerNumberJsonV310 | PostCustomerNumberJsonV310 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer by CUSTOMER_NUMBER
    api_response = api_instance.o_bpv3_1_0_get_customer_by_customer_number(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv3_1_0_get_customer_by_customer_number: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The customer id
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Tax Residences of Customer
    api_response = api_instance.o_bpv3_1_0_get_tax_residence(customer_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv3_1_0_get_tax_residence: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserInvitationJsonV400() # PostUserInvitationJsonV400 | PostUserInvitationJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create User Invitation
    api_response = api_instance.o_bpv4_0_0_create_user_invitation(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv4_0_0_create_user_invitation: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerPhoneNumberJsonV400() # PostCustomerPhoneNumberJsonV400 | PostCustomerPhoneNumberJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customers by MOBILE_PHONE_NUMBER
    api_response = api_instance.o_bpv4_0_0_get_customers_by_customer_phone_number(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv4_0_0_get_customers_by_customer_phone_number: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostUserInvitationAnonymousJsonV400() # PostUserInvitationAnonymousJsonV400 | PostUserInvitationAnonymousJsonV400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get User Invitation Information
    api_response = api_instance.o_bpv4_0_0_get_user_invitation_anonymous(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv4_0_0_get_user_invitation_anonymous: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerOverviewJsonV500() # PostCustomerOverviewJsonV500 | PostCustomerOverviewJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Overview
    api_response = api_instance.o_bpv5_0_0_get_customer_overview(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv5_0_0_get_customer_overview: %s\n" % e)
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
api_instance = obp_python.KYCApi(obp_python.ApiClient(configuration))
body = obp_python.PostCustomerOverviewJsonV500() # PostCustomerOverviewJsonV500 | PostCustomerOverviewJsonV500 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Customer Overview Flat
    api_response = api_instance.o_bpv5_0_0_get_customer_overview_flat(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCApi->o_bpv5_0_0_get_customer_overview_flat: %s\n" % e)
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

