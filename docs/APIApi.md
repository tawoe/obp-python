# obp_python.APIApi

All URIs are relative to *http://test.openbankproject.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp**](APIApi.md#o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp) | **GET** /obp/v5.0.0/banks/{BANK_ID}/resource-docs/{API_VERSION}/obp | Get Bank Level Dynamic Resource Docs.
[**o_bpv1_4_0_get_resource_docs_obp**](APIApi.md#o_bpv1_4_0_get_resource_docs_obp) | **GET** /obp/v5.0.0/resource-docs/{API_VERSION}/obp | Get Resource Docs.
[**o_bpv1_4_0_get_resource_docs_swagger**](APIApi.md#o_bpv1_4_0_get_resource_docs_swagger) | **GET** /obp/v5.0.0/resource-docs/{API_VERSION}/swagger | Get Swagger documentation
[**o_bpv2_0_0_elastic_search_metrics**](APIApi.md#o_bpv2_0_0_elastic_search_metrics) | **GET** /obp/v5.0.0/search/metrics | Search API Metrics via Elasticsearch
[**o_bpv2_1_0_get_metrics**](APIApi.md#o_bpv2_1_0_get_metrics) | **GET** /obp/v5.0.0/management/metrics | Get Metrics
[**o_bpv2_2_0_get_connector_metrics**](APIApi.md#o_bpv2_2_0_get_connector_metrics) | **GET** /obp/v5.0.0/management/connector/metrics | Get Connector Metrics
[**o_bpv2_2_0_get_message_docs**](APIApi.md#o_bpv2_2_0_get_message_docs) | **GET** /obp/v5.0.0/message-docs/CONNECTOR | Get Message Docs
[**o_bpv3_0_0_get_adapter_info_for_bank**](APIApi.md#o_bpv3_0_0_get_adapter_info_for_bank) | **GET** /obp/v5.0.0/banks/{BANK_ID}/adapter | Get Adapter Info for a bank
[**o_bpv3_1_0_config**](APIApi.md#o_bpv3_1_0_config) | **GET** /obp/v5.0.0/config | Get API Configuration
[**o_bpv3_1_0_create_method_routing**](APIApi.md#o_bpv3_1_0_create_method_routing) | **POST** /obp/v5.0.0/management/method_routings | Create MethodRouting
[**o_bpv3_1_0_delete_method_routing**](APIApi.md#o_bpv3_1_0_delete_method_routing) | **DELETE** /obp/v5.0.0/management/method_routings/{METHOD_ROUTING_ID} | Delete MethodRouting
[**o_bpv3_1_0_get_message_docs_swagger**](APIApi.md#o_bpv3_1_0_get_message_docs_swagger) | **GET** /obp/v5.0.0/message-docs/CONNECTOR/swagger2.0 | Get Message Docs Swagger
[**o_bpv3_1_0_get_method_routings**](APIApi.md#o_bpv3_1_0_get_method_routings) | **GET** /obp/v5.0.0/management/method_routings | Get MethodRoutings
[**o_bpv3_1_0_get_o_auth2_server_jwks_uris**](APIApi.md#o_bpv3_1_0_get_o_auth2_server_jwks_uris) | **GET** /obp/v5.0.0/jwks-uris | Get JSON Web Key (JWK) URIs
[**o_bpv3_1_0_get_obp_connector_loopback**](APIApi.md#o_bpv3_1_0_get_obp_connector_loopback) | **GET** /obp/v5.0.0/connector/loopback | Get Connector Status (Loopback)
[**o_bpv3_1_0_get_rate_limiting_info**](APIApi.md#o_bpv3_1_0_get_rate_limiting_info) | **GET** /obp/v5.0.0/rate-limiting | Get Rate Limiting Info
[**o_bpv3_1_0_get_server_jwk**](APIApi.md#o_bpv3_1_0_get_server_jwk) | **GET** /obp/v5.0.0/certs | Get JSON Web Key (JWK)
[**o_bpv3_1_0_update_method_routing**](APIApi.md#o_bpv3_1_0_update_method_routing) | **PUT** /obp/v5.0.0/management/method_routings/{METHOD_ROUTING_ID} | Update MethodRouting
[**o_bpv4_0_0_create_bank_level_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_create_bank_level_dynamic_endpoint) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints | Create Bank Level Dynamic Endpoint
[**o_bpv4_0_0_create_bank_level_dynamic_entity**](APIApi.md#o_bpv4_0_0_create_bank_level_dynamic_entity) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities | Create Bank Level Dynamic Entity
[**o_bpv4_0_0_create_bank_level_endpoint_tag**](APIApi.md#o_bpv4_0_0_create_bank_level_endpoint_tag) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags | Create Bank Level Endpoint Tag
[**o_bpv4_0_0_create_bank_level_endpoint_tag_0**](APIApi.md#o_bpv4_0_0_create_bank_level_endpoint_tag_0) | **POST** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags | Create Bank Level Endpoint Tag
[**o_bpv4_0_0_create_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_create_dynamic_endpoint) | **POST** /obp/v5.0.0/management/dynamic-endpoints | Create Dynamic Endpoint
[**o_bpv4_0_0_create_system_dynamic_entity**](APIApi.md#o_bpv4_0_0_create_system_dynamic_entity) | **POST** /obp/v5.0.0/management/system-dynamic-entities | Create System Level Dynamic Entity
[**o_bpv4_0_0_create_system_level_endpoint_tag**](APIApi.md#o_bpv4_0_0_create_system_level_endpoint_tag) | **POST** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags | Create System Level Endpoint Tag
[**o_bpv4_0_0_create_system_level_endpoint_tag_0**](APIApi.md#o_bpv4_0_0_create_system_level_endpoint_tag_0) | **POST** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags | Create System Level Endpoint Tag
[**o_bpv4_0_0_delete_bank_level_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_delete_bank_level_dynamic_endpoint) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints/DYNAMIC_ENDPOINT_ID |  Delete Bank Level Dynamic Endpoint
[**o_bpv4_0_0_delete_bank_level_dynamic_entity**](APIApi.md#o_bpv4_0_0_delete_bank_level_dynamic_entity) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities/{DYNAMIC_ENTITY_ID} | Delete Bank Level Dynamic Entity
[**o_bpv4_0_0_delete_bank_level_endpoint_tag**](APIApi.md#o_bpv4_0_0_delete_bank_level_endpoint_tag) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Delete Bank Level Endpoint Tag
[**o_bpv4_0_0_delete_bank_level_endpoint_tag_0**](APIApi.md#o_bpv4_0_0_delete_bank_level_endpoint_tag_0) | **DELETE** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Delete Bank Level Endpoint Tag
[**o_bpv4_0_0_delete_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_delete_dynamic_endpoint) | **DELETE** /obp/v5.0.0/management/dynamic-endpoints/DYNAMIC_ENDPOINT_ID |  Delete Dynamic Endpoint
[**o_bpv4_0_0_delete_my_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_delete_my_dynamic_endpoint) | **DELETE** /obp/v5.0.0/my/dynamic-endpoints/DYNAMIC_ENDPOINT_ID | Delete My Dynamic Endpoint
[**o_bpv4_0_0_delete_my_dynamic_entity**](APIApi.md#o_bpv4_0_0_delete_my_dynamic_entity) | **DELETE** /obp/v5.0.0/my/dynamic-entities/{DYNAMIC_ENTITY_ID} | Delete My Dynamic Entity
[**o_bpv4_0_0_delete_system_dynamic_entity**](APIApi.md#o_bpv4_0_0_delete_system_dynamic_entity) | **DELETE** /obp/v5.0.0/management/system-dynamic-entities/{DYNAMIC_ENTITY_ID} | Delete System Level Dynamic Entity
[**o_bpv4_0_0_delete_system_level_endpoint_tag**](APIApi.md#o_bpv4_0_0_delete_system_level_endpoint_tag) | **DELETE** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Delete System Level Endpoint Tag
[**o_bpv4_0_0_delete_system_level_endpoint_tag_0**](APIApi.md#o_bpv4_0_0_delete_system_level_endpoint_tag_0) | **DELETE** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Delete System Level Endpoint Tag
[**o_bpv4_0_0_get_bank_level_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_get_bank_level_dynamic_endpoint) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints/DYNAMIC_ENDPOINT_ID |  Get Bank Level Dynamic Endpoint
[**o_bpv4_0_0_get_bank_level_dynamic_endpoints**](APIApi.md#o_bpv4_0_0_get_bank_level_dynamic_endpoints) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints | Get Bank Level Dynamic Endpoints
[**o_bpv4_0_0_get_bank_level_dynamic_entities**](APIApi.md#o_bpv4_0_0_get_bank_level_dynamic_entities) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities | Get Bank Level Dynamic Entities
[**o_bpv4_0_0_get_bank_level_endpoint_tags**](APIApi.md#o_bpv4_0_0_get_bank_level_endpoint_tags) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags | Get Bank Level Endpoint Tags
[**o_bpv4_0_0_get_bank_level_endpoint_tags_0**](APIApi.md#o_bpv4_0_0_get_bank_level_endpoint_tags_0) | **GET** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags | Get Bank Level Endpoint Tags
[**o_bpv4_0_0_get_call_context**](APIApi.md#o_bpv4_0_0_get_call_context) | **GET** /obp/v5.0.0/development/call_context | Get the Call Context of a current call
[**o_bpv4_0_0_get_dynamic_endpoint**](APIApi.md#o_bpv4_0_0_get_dynamic_endpoint) | **GET** /obp/v5.0.0/management/dynamic-endpoints/DYNAMIC_ENDPOINT_ID | Get Dynamic Endpoint
[**o_bpv4_0_0_get_dynamic_endpoints**](APIApi.md#o_bpv4_0_0_get_dynamic_endpoints) | **GET** /obp/v5.0.0/management/dynamic-endpoints |  Get Dynamic Endpoints
[**o_bpv4_0_0_get_mapper_database_info**](APIApi.md#o_bpv4_0_0_get_mapper_database_info) | **GET** /obp/v5.0.0/database/info | Get Mapper Database Info
[**o_bpv4_0_0_get_my_dynamic_endpoints**](APIApi.md#o_bpv4_0_0_get_my_dynamic_endpoints) | **GET** /obp/v5.0.0/my/dynamic-endpoints | Get My Dynamic Endpoints
[**o_bpv4_0_0_get_my_dynamic_entities**](APIApi.md#o_bpv4_0_0_get_my_dynamic_entities) | **GET** /obp/v5.0.0/my/dynamic-entities | Get My Dynamic Entities
[**o_bpv4_0_0_get_scanned_api_versions**](APIApi.md#o_bpv4_0_0_get_scanned_api_versions) | **GET** /obp/v5.0.0/api/versions | Get scanned API Versions
[**o_bpv4_0_0_get_system_dynamic_entities**](APIApi.md#o_bpv4_0_0_get_system_dynamic_entities) | **GET** /obp/v5.0.0/management/system-dynamic-entities | Get System Dynamic Entities
[**o_bpv4_0_0_get_system_level_endpoint_tags**](APIApi.md#o_bpv4_0_0_get_system_level_endpoint_tags) | **GET** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags | Get System Level Endpoint Tags
[**o_bpv4_0_0_get_system_level_endpoint_tags_0**](APIApi.md#o_bpv4_0_0_get_system_level_endpoint_tags_0) | **GET** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags | Get System Level Endpoint Tags
[**o_bpv4_0_0_root**](APIApi.md#o_bpv4_0_0_root) | **GET** /obp/v5.0.0/root | Get API Info (root)
[**o_bpv4_0_0_update_bank_level_dynamic_endpoint_host**](APIApi.md#o_bpv4_0_0_update_bank_level_dynamic_endpoint_host) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-endpoints/DYNAMIC_ENDPOINT_ID/host |  Update Bank Level Dynamic Endpoint Host
[**o_bpv4_0_0_update_bank_level_dynamic_entity**](APIApi.md#o_bpv4_0_0_update_bank_level_dynamic_entity) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/dynamic-entities/{DYNAMIC_ENTITY_ID} | Update Bank Level Dynamic Entity
[**o_bpv4_0_0_update_bank_level_endpoint_tag**](APIApi.md#o_bpv4_0_0_update_bank_level_endpoint_tag) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Update Bank Level Endpoint Tag
[**o_bpv4_0_0_update_bank_level_endpoint_tag_0**](APIApi.md#o_bpv4_0_0_update_bank_level_endpoint_tag_0) | **PUT** /obp/v5.0.0/management/banks/{BANK_ID}/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Update Bank Level Endpoint Tag
[**o_bpv4_0_0_update_dynamic_endpoint_host**](APIApi.md#o_bpv4_0_0_update_dynamic_endpoint_host) | **PUT** /obp/v5.0.0/management/dynamic-endpoints/DYNAMIC_ENDPOINT_ID/host |  Update Dynamic Endpoint Host
[**o_bpv4_0_0_update_my_dynamic_entity**](APIApi.md#o_bpv4_0_0_update_my_dynamic_entity) | **PUT** /obp/v5.0.0/my/dynamic-entities/{DYNAMIC_ENTITY_ID} | Update My Dynamic Entity
[**o_bpv4_0_0_update_system_dynamic_entity**](APIApi.md#o_bpv4_0_0_update_system_dynamic_entity) | **PUT** /obp/v5.0.0/management/system-dynamic-entities/{DYNAMIC_ENTITY_ID} | Update System Level Dynamic Entity
[**o_bpv4_0_0_update_system_level_endpoint_tag**](APIApi.md#o_bpv4_0_0_update_system_level_endpoint_tag) | **PUT** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Update System Level Endpoint Tag
[**o_bpv4_0_0_update_system_level_endpoint_tag_0**](APIApi.md#o_bpv4_0_0_update_system_level_endpoint_tag_0) | **PUT** /obp/v5.0.0/management/endpoints/OPERATION_ID/tags/ENDPOINT_TAG_ID | Update System Level Endpoint Tag
[**o_bpv4_0_0_verify_request_sign_response**](APIApi.md#o_bpv4_0_0_verify_request_sign_response) | **GET** /obp/v5.0.0/development/echo/jws-verified-request-jws-signed-response | Verify Request and Sign Response of a current call
[**o_bpv5_0_0_get_adapter_info**](APIApi.md#o_bpv5_0_0_get_adapter_info) | **GET** /obp/v5.0.0/adapter | Get Adapter Info
[**o_bpv5_0_0_get_metrics_at_bank**](APIApi.md#o_bpv5_0_0_get_metrics_at_bank) | **GET** /obp/v5.0.0/management/metrics/banks/{BANK_ID} | Get Metrics at Bank


# **o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp**
> ResourceDocsJson o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp(body, api_version, bank_id)

Get Bank Level Dynamic Resource Docs.

<p>Get documentation about the RESTful resources on this server including example bodies for POST and PUT requests.</p><p>This is the native data format used to document OBP endpoints. Each endpoint has a Resource Doc (a Scala case class) defined in the source code.</p><p>This endpoint is used by OBP API Explorer to display and work with the API documentation.</p><p>Most (but not all) fields are also available in swagger format. (The Swagger endpoint is built from Resource Docs.)</p><p>API_VERSION is the version you want documentation about e.g. v3.0.0</p><p>You may filter this endpoint with tags parameter e.g. ?tags=Account,Bank</p><p>You may filter this endpoint with functions parameter e.g. ?functions=enableDisableConsumers,getConnectorMetrics</p><p>For possible function values, see implemented_by.function in the JSON returned by this endpoint or the OBP source code or the footer of the API Explorer which produces a comma separated list of functions that reflect the server or filtering by API Explorer based on tags etc.</p><p>You may filter this endpoint using the 'content' url parameter, e.g. ?content=dynamic<br />if set content=dynamic, only show dynamic endpoints, if content=static, only show the static endpoints. if omit this parameter, we will show all the endpoints.</p><p>You may need some other language resource docs, now we support en and zh , e.g. ?language=zh</p><p>You can filter with api-collection-id, but api-collection-id can not be used with others together. If api-collection-id is used in URL, it will ignore all other parameters.</p><p>You can easily pass the cache, use different value for cache-modifier, eg: ?cache-modifier= 123</p><p>See the Resource Doc endpoint for more information.</p><p>Following are more examples:<br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?tags=Account,Bank\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?tags=Account,Bank</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?functions=getBanks,bankById\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?functions=getBanks,bankById</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?language=zh\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?language=zh</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?content=static,dynamic,all\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?content=static,dynamic,all</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?api-collection-id=4e866c86-60c3-4268-a221-cb0bbf1ad221\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?api-collection-id=4e866c86-60c3-4268-a221-cb0bbf1ad221</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?cache-modifier=3141592653\">https://test.openbankproject.com/obp/v4.0.0/banks/BANK_ID/resource-docs/v4.0.0/obp?cache-modifier=3141592653</a></p><ul><li> operation_id is concatenation of \"v\", version and function and should be unique (used for DOM element IDs etc. maybe used to link to source code) </li><li> version references the version that the API call is defined in.</li><li> function is the (scala) partial function that implements this endpoint. It is unique per version of the API.</li><li> request_url is empty for the root call, else the path. It contains the standard prefix (e.g. /obp) and the implemented version (the version where this endpoint was defined) e.g. /obp/v1.2.0/resource</li><li> specified_url (recommended to use) is empty for the root call, else the path. It contains the standard prefix (e.g. /obp) and the version specified in the call e.g. /obp/v3.1.0/resource. In OBP, endpoints are first made available at the request_url, but the same resource (function call) is often made available under later versions (specified_url). To access the latest version of all endpoints use the latest version available on your OBP instance e.g. /obp/v3.1.0 - To get the original version use the request_url. We recommend to use the specified_url since non semantic improvements are more likely to be applied to later implementations of the call.</li><li> summary is a short description inline with the swagger terminology. </li><li> description may contain html markup (generated from markdown on the server).</li></ul><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
api_version = 'api_version_example' # str | eg:v2.2.0, v3.0.0
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Resource Docs.
    api_response = api_instance.o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp(body, api_version, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv1_4_0_get_bank_level_dynamic_resource_docs_obp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **api_version** | **str**| eg:v2.2.0, v3.0.0 | 
 **bank_id** | **str**| The bank id | 

### Return type

[**ResourceDocsJson**](ResourceDocsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_4_0_get_resource_docs_obp**
> ResourceDocsJson o_bpv1_4_0_get_resource_docs_obp(body, api_version)

Get Resource Docs.

<p>Get documentation about the RESTful resources on this server including example bodies for POST and PUT requests.</p><p>This is the native data format used to document OBP endpoints. Each endpoint has a Resource Doc (a Scala case class) defined in the source code.</p><p>This endpoint is used by OBP API Explorer to display and work with the API documentation.</p><p>Most (but not all) fields are also available in swagger format. (The Swagger endpoint is built from Resource Docs.)</p><p>API_VERSION is the version you want documentation about e.g. v3.0.0</p><p>You may filter this endpoint with tags parameter e.g. ?tags=Account,Bank</p><p>You may filter this endpoint with functions parameter e.g. ?functions=enableDisableConsumers,getConnectorMetrics</p><p>For possible function values, see implemented_by.function in the JSON returned by this endpoint or the OBP source code or the footer of the API Explorer which produces a comma separated list of functions that reflect the server or filtering by API Explorer based on tags etc.</p><p>You may filter this endpoint using the 'content' url parameter, e.g. ?content=dynamic<br />if set content=dynamic, only show dynamic endpoints, if content=static, only show the static endpoints. if omit this parameter, we will show all the endpoints.</p><p>You may need some other language resource docs, now we support en and zh , e.g. ?language=zh</p><p>You can filter with api-collection-id, but api-collection-id can not be used with others together. If api-collection-id is used in URL, it will ignore all other parameters.</p><p>You can easily pass the cache, use different value for cache-modifier, eg: ?cache-modifier= 123</p><p>See the Resource Doc endpoint for more information.</p><p>Following are more examples:<br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?tags=Account,Bank\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?tags=Account,Bank</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?functions=getBanks,bankById\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?functions=getBanks,bankById</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?language=zh\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?language=zh</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?content=static,dynamic,all\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?content=static,dynamic,all</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?api-collection-id=4e866c86-60c3-4268-a221-cb0bbf1ad221\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?api-collection-id=4e866c86-60c3-4268-a221-cb0bbf1ad221</a><br /><a href=\"https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?cache-modifier=3141592653\">https://test.openbankproject.com/obp/v4.0.0/resource-docs/v4.0.0/obp?cache-modifier=3141592653</a></p><ul><li> operation_id is concatenation of \"v\", version and function and should be unique (used for DOM element IDs etc. maybe used to link to source code) </li><li> version references the version that the API call is defined in.</li><li> function is the (scala) partial function that implements this endpoint. It is unique per version of the API.</li><li> request_url is empty for the root call, else the path. It contains the standard prefix (e.g. /obp) and the implemented version (the version where this endpoint was defined) e.g. /obp/v1.2.0/resource</li><li> specified_url (recommended to use) is empty for the root call, else the path. It contains the standard prefix (e.g. /obp) and the version specified in the call e.g. /obp/v3.1.0/resource. In OBP, endpoints are first made available at the request_url, but the same resource (function call) is often made available under later versions (specified_url). To access the latest version of all endpoints use the latest version available on your OBP instance e.g. /obp/v3.1.0 - To get the original version use the request_url. We recommend to use the specified_url since non semantic improvements are more likely to be applied to later implementations of the call.</li><li> summary is a short description inline with the swagger terminology. </li><li> description may contain html markup (generated from markdown on the server).</li></ul><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
api_version = 'api_version_example' # str | eg:v2.2.0, v3.0.0

try:
    # Get Resource Docs.
    api_response = api_instance.o_bpv1_4_0_get_resource_docs_obp(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv1_4_0_get_resource_docs_obp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **api_version** | **str**| eg:v2.2.0, v3.0.0 | 

### Return type

[**ResourceDocsJson**](ResourceDocsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv1_4_0_get_resource_docs_swagger**
> EmptyClassJson o_bpv1_4_0_get_resource_docs_swagger(body, api_version)

Get Swagger documentation

<p>Returns documentation about the RESTful resources on this server in Swagger format.</p><p>API_VERSION is the version you want documentation about e.g. v3.0.0</p><p>You may filter this endpoint using the 'tags' url parameter e.g. ?tags=Account,Bank</p><p>(All endpoints are given one or more tags which for used in grouping)</p><p>You may filter this endpoint using the 'functions' url parameter e.g. ?functions=getBanks,bankById</p><p>(Each endpoint is implemented in the OBP Scala code by a 'function')</p><p>See the Resource Doc endpoint for more information.</p><p>Following are more examples:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger\">https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger?tags=Account,Bank\">https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger?tags=Account,Bank</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger?functions=getBanks,bankById\">https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger?functions=getBanks,bankById</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger?tags=Account,Bank,PSD2&amp;functions=getBanks,bankById\">https://test.openbankproject.com/obp/v3.1.0/resource-docs/v3.1.0/swagger?tags=Account,Bank,PSD2&amp;functions=getBanks,bankById</a></p><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.
api_version = 'api_version_example' # str | eg:v2.2.0, v3.0.0

try:
    # Get Swagger documentation
    api_response = api_instance.o_bpv1_4_0_get_resource_docs_swagger(body, api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv1_4_0_get_resource_docs_swagger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 
 **api_version** | **str**| eg:v2.2.0, v3.0.0 | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_0_0_elastic_search_metrics**
> EmptyClassJson o_bpv2_0_0_elastic_search_metrics(body)

Search API Metrics via Elasticsearch

<p>Search the API calls made to this API instance via Elastic Search.</p><p>Login is required.</p><p>CanSearchMetrics entitlement is required to search metrics data.</p><p>parameters:</p><p>esType  - elasticsearch type</p><p>simple query:</p><p>q       - plain_text_query</p><p>df      - default field to search</p><p>sort    - field to sort on</p><p>size    - number of hits returned, default 10</p><p>from    - show hits starting from</p><p>json query:</p><p>source  - JSON_query_(URL-escaped)</p><p>example usage:</p><p>/search/metrics/q=findThis</p><p>or:</p><p>/search/metrics/source={&quot;query&quot;:{&quot;query_string&quot;:{&quot;query&quot;:&quot;findThis&quot;}}}</p><p>Note!!</p><p>The whole JSON query string MUST be URL-encoded:</p><ul><li>For {  use %7B</li><li>For }  use %7D</li><li>For : use %3A</li><li>For &quot; use %22</li></ul><p>etc..</p><p>Only q, source and esType are passed to Elastic</p><p>Elastic simple query: <a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/search-uri-request.html\">https://www.elastic.co/guide/en/elasticsearch/reference/current/search-uri-request.html</a></p><p>Elastic JSON query: <a href=\"https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html\">https://www.elastic.co/guide/en/elasticsearch/reference/current/query-filter-context.html</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Search API Metrics via Elasticsearch
    api_response = api_instance.o_bpv2_0_0_elastic_search_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv2_0_0_elastic_search_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**EmptyClassJson**](EmptyClassJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_1_0_get_metrics**
> MetricsJson o_bpv2_1_0_get_metrics(body)

Get Metrics

<p>Get the all metrics</p><p>require CanReadMetrics role</p><p>Filters Part 1.<em>filtering</em> (no wilde cards etc.) parameters to GET /management/metrics</p><p>Should be able to filter on the following metrics fields</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=50&amp;offset=2</p><p>1 from_date (defaults to one week before current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 limit (for pagination: defaults to 50)  eg:limit=200</p><p>4 offset (for pagination: zero index, defaults to 0) eg: offset=10</p><p>5 sort_by (defaults to date field) eg: sort_by=date<br />possible values:<br />&quot;url&quot;,<br />&quot;date&quot;,<br />&quot;user_name&quot;,<br />&quot;app_name&quot;,<br />&quot;developer_email&quot;,<br />&quot;implemented_by_partial_function&quot;,<br />&quot;implemented_in_version&quot;,<br />&quot;consumer_id&quot;,<br />&quot;verb&quot;</p><p>6 direction (defaults to date desc) eg: direction=desc</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:<a href=\"&#109;&#97;&#x69;&#108;&#x74;&#x6f;&#x3a;&#48;&#49;.&#48;&#48;&#x30;&#90;&#38;&#108;&#105;m&#x69;&#x74;&#x3d;&#x31;&#48;&#x30;&#x30;&#x30;&#38;o&#x66;&#102;&#x73;&#101;&#116;&#61;0&amp;a&#110;&#111;&#x6e;=&#x66;&#97;l&#115;&#x65;&amp;ap&#112;&#95;&#110;&#97;m&#x65;&#61;&#84;&#101;a&#116;A&#x70;&#112;&#38;&#105;&#x6d;&#x70;l&#101;&#x6d;e&#110;&#116;e&#x64;&#x5f;&#x69;&#x6e;&#x5f;v&#x65;&#114;s&#x69;&#x6f;&#x6e;&#x3d;&#118;2.&#49;.&#x30;&#x26;&#x76;&#101;&#x72;&#98;&#x3d;&#80;O&#x53;&#84;&#38;&#117;&#115;e&#114;_i&#x64;&#x3d;&#x63;&#x37;&#x62;6c&#x62;&#x34;7-&#99;&#98;&#57;&#x36;&#45;&#x34;&#52;&#52;&#x31;-8&#56;&#48;1&#x2d;&#x33;5&#x62;&#53;&#55;45&#x36;&#x37;&#x35;&#x33;&#x61;&#x26;&#117;&#115;&#x65;r&#95;n&#97;me&#61;s&#117;&#115;&#97;&#110;&#46;&#117;&#107;&#x2e;&#50;&#x39;@&#x65;&#120;&#97;&#109;&#112;l&#101;&#x2e;&#99;o&#109;\">&#x30;1.0&#x30;&#48;Z&#x26;&#x6c;i&#x6d;&#x69;&#116;&#61;&#x31;&#48;&#x30;0&#x30;&#38;&#x6f;&#x66;&#x66;&#x73;&#x65;&#116;&#x3d;&#x30;&#x26;&#x61;&#x6e;&#x6f;&#110;&#x3d;f&#x61;&#x6c;&#x73;e&amp;&#x61;&#x70;p&#x5f;n&#97;&#x6d;e&#61;&#84;&#101;&#97;&#x74;&#65;&#x70;&#x70;&#38;&#x69;&#x6d;&#112;&#x6c;&#x65;&#x6d;&#101;&#110;&#x74;ed&#x5f;&#105;&#x6e;&#x5f;v&#x65;&#x72;&#x73;&#x69;&#x6f;&#x6e;&#61;&#x76;2&#x2e;&#x31;&#x2e;&#x30;&#38;&#118;er&#x62;=&#80;&#79;S&#x54;&#38;&#117;&#115;&#101;&#114;&#x5f;i&#x64;&#x3d;&#x63;&#x37;&#x62;&#54;c&#98;&#x34;7&#x2d;&#99;&#x62;&#57;&#54;&#45;4&#52;&#x34;&#49;&#x2d;&#x38;&#x38;&#x30;&#49;&#45;&#x33;&#x35;&#x62;&#x35;7&#52;&#x35;67&#53;&#51;a&#x26;&#117;&#115;&#101;&#x72;_&#110;&#97;&#x6d;&#101;&#x3d;&#x73;&#x75;s&#x61;&#x6e;&#x2e;&#117;&#107;&#46;29&#64;&#101;&#120;&#97;&#109;&#112;&#x6c;&#101;&#46;&#99;o&#109;</a>&amp;consumer_id=78</p><p>Other filters:</p><p>7 consumer_id  (if null ignore)</p><p>8 user_id (if null ignore)</p><p>9 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>10 url (if null ignore), note: can not contain '&amp;'.</p><p>11 app_name (if null ignore)</p><p>12 implemented_by_partial_function (if null ignore),</p><p>13 implemented_in_version (if null ignore)</p><p>14 verb (if null ignore)</p><p>15 correlation_id (if null ignore)</p><p>16 duration (if null ignore) non digit chars will be silently omitted</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Metrics
    api_response = api_instance.o_bpv2_1_0_get_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv2_1_0_get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**MetricsJson**](MetricsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_2_0_get_connector_metrics**
> ConnectorMetricsJson o_bpv2_2_0_get_connector_metrics(body)

Get Connector Metrics

<p>Get the all metrics</p><p>require CanGetConnectorMetrics role</p><p>Filters Part 1.<em>filtering</em> (no wilde cards etc.) parameters to GET /management/connector/metrics</p><p>Should be able to filter on the following metrics fields</p><p>eg: /management/connector/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=50&amp;offset=2</p><p>1 from_date (defaults to one week before current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 limit (for pagination: defaults to 1000)  eg:limit=2000</p><p>4 offset (for pagination: zero index, defaults to 0) eg: offset=10</p><p>eg: /management/connector/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=100&amp;offset=300</p><p>Other filters:</p><p>5 connector_name  (if null ignore)</p><p>6 function_name (if null ignore)</p><p>7 correlation_id (if null ignore)</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Connector Metrics
    api_response = api_instance.o_bpv2_2_0_get_connector_metrics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv2_2_0_get_connector_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**ConnectorMetricsJson**](ConnectorMetricsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv2_2_0_get_message_docs**
> MessageDocsJson o_bpv2_2_0_get_message_docs(body)

Get Message Docs

<p>These message docs provide example messages sent by OBP to the (Kafka) message queue for processing by the Core Banking / Payment system Adapter - together with an example expected response and possible error codes.<br />Integrators can use these messages to build Adapters that provide core banking services to OBP.</p><p>Note: API Explorer provides a Message Docs page where these messages are displayed.</p><p><code>CONNECTOR</code>: kafka_vSept2018, stored_procedure_vDec2019 ...</p><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EmptyClassJson() # EmptyClassJson | EmptyClassJson object that needs to be added.

try:
    # Get Message Docs
    api_response = api_instance.o_bpv2_2_0_get_message_docs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv2_2_0_get_message_docs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmptyClassJson**](EmptyClassJson.md)| EmptyClassJson object that needs to be added. | 

### Return type

[**MessageDocsJson**](MessageDocsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_0_0_get_adapter_info_for_bank**
> AdapterInfoJsonV300 o_bpv3_0_0_get_adapter_info_for_bank(bank_id)

Get Adapter Info for a bank

<p>Get basic information about the Adapter listening on behalf of this bank.</p><p>Authentication is Optional</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Adapter Info for a bank
    api_response = api_instance.o_bpv3_0_0_get_adapter_info_for_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_0_0_get_adapter_info_for_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**AdapterInfoJsonV300**](AdapterInfoJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_config**
> ConfigurationJSON o_bpv3_1_0_config()

Get API Configuration

<p>Returns information about:</p><ul><li>The default bank_id</li><li>Akka configuration</li><li>Elastic Search configuration</li><li>Cached functions</li></ul><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get API Configuration
    api_response = api_instance.o_bpv3_1_0_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigurationJSON**](ConfigurationJSON.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_create_method_routing**
> MethodRoutingCommons o_bpv3_1_0_create_method_routing(body)

Create MethodRouting

<p>Create a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explanation of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some parameters for this method</li></ul><p>note and CAVEAT!:</p><ul><li>bank_id_pattern has to be empty for methods that do not take bank_id as a function parameter, otherwise might get empty result</li><li>methods that aggregate bank objects (e.g. getBankAccountsForUser) have to take any  existing method routings for these objects into consideration</li><li>so if you create e.g. a bank specific method routing for getting an account, make sure that it is also served by endpoints getting ALL accounts for ALL banks</li><li>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</li></ul><p>If the connector name starts with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.MethodRoutingCommons() # MethodRoutingCommons | MethodRoutingCommons object that needs to be added.

try:
    # Create MethodRouting
    api_response = api_instance.o_bpv3_1_0_create_method_routing(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_create_method_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MethodRoutingCommons**](MethodRoutingCommons.md)| MethodRoutingCommons object that needs to be added. | 

### Return type

[**MethodRoutingCommons**](MethodRoutingCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_delete_method_routing**
> o_bpv3_1_0_delete_method_routing(method_routing_id)

Delete MethodRouting

<p>Delete a MethodRouting specified by METHOD_ROUTING_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
method_routing_id = 'method_routing_id_example' # str | the method routing id 

try:
    # Delete MethodRouting
    api_instance.o_bpv3_1_0_delete_method_routing(method_routing_id)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_delete_method_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **method_routing_id** | **str**| the method routing id  | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_message_docs_swagger**
> MessageDocsJson o_bpv3_1_0_get_message_docs_swagger()

Get Message Docs Swagger

<p>This endpoint provides example message docs in swagger format.<br />It is only relavent for REST Connectors.</p><p>This endpoint can be used by the developer building a REST Adapter that connects to the Core Banking System (CBS).<br />That is, the Adapter developer can use the Swagger surfaced here to build the REST APIs that the OBP REST connector will call to consume CBS services.</p><p>i.e.:</p><p>OBP API (Core OBP API code) -&gt; OBP REST Connector (OBP REST Connector code) -&gt; OBP REST Adapter (Adapter developer code) -&gt; CBS (Main Frame)</p><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get Message Docs Swagger
    api_response = api_instance.o_bpv3_1_0_get_message_docs_swagger()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_get_message_docs_swagger: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MessageDocsJson**](MessageDocsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_method_routings**
> InlineResponse20010 o_bpv3_1_0_get_method_routings()

Get MethodRoutings

<p>Get the all MethodRoutings.</p><p>Query url parameters:</p><ul><li>method_name: filter with method_name</li><li>active: if active = true, it will show all the webui_ props. Even if they are set yet, we will return all the default webui_ props</li></ul><p>eg:<br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?active=true</a><br /><a href=\"https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank\">https://test.openbankproject.com/obp/v3.1.0/management/method_routings?method_name=getBank</a></p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get MethodRoutings
    api_response = api_instance.o_bpv3_1_0_get_method_routings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_get_method_routings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_o_auth2_server_jwks_uris**
> OAuth2ServerJwksUrisJson o_bpv3_1_0_get_o_auth2_server_jwks_uris()

Get JSON Web Key (JWK) URIs

<p>Get the OAuth2 server's public JSON Web Key (JWK) URIs.<br />It is required by client applications to validate ID tokens, self-contained access tokens and other issued objects.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get JSON Web Key (JWK) URIs
    api_response = api_instance.o_bpv3_1_0_get_o_auth2_server_jwks_uris()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_get_o_auth2_server_jwks_uris: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OAuth2ServerJwksUrisJson**](OAuth2ServerJwksUrisJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_obp_connector_loopback**
> ObpApiLoopbackJson o_bpv3_1_0_get_obp_connector_loopback()

Get Connector Status (Loopback)

<p>This endpoint makes a call to the Connector to check the backend transport (e.g. Kafka) is reachable.</p><p>Currently this is only implemented for Kafka based connectors.</p><p>For Kafka based connectors, this endpoint writes a message to Kafka and reads it again.</p><p>In the future, this endpoint may also return information about database connections etc.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get Connector Status (Loopback)
    api_response = api_instance.o_bpv3_1_0_get_obp_connector_loopback()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_get_obp_connector_loopback: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ObpApiLoopbackJson**](ObpApiLoopbackJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_rate_limiting_info**
> RateLimitingInfoV310 o_bpv3_1_0_get_rate_limiting_info()

Get Rate Limiting Info

<p>Get information about the Rate Limiting setup on this OBP Instance such as:</p><p>Is rate limiting enabled and active?<br />What backend is used to keep track of the API calls (e.g. REDIS).</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get Rate Limiting Info
    api_response = api_instance.o_bpv3_1_0_get_rate_limiting_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_get_rate_limiting_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RateLimitingInfoV310**](RateLimitingInfoV310.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_get_server_jwk**
> SeverJWK o_bpv3_1_0_get_server_jwk()

Get JSON Web Key (JWK)

<p>Get the server's public JSON Web Key (JWK) set and certificate chain.<br />It is required by client applications to validate ID tokens, self-contained access tokens and other issued objects.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get JSON Web Key (JWK)
    api_response = api_instance.o_bpv3_1_0_get_server_jwk()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_get_server_jwk: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SeverJWK**](SeverJWK.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv3_1_0_update_method_routing**
> MethodRoutingCommons o_bpv3_1_0_update_method_routing(body, method_routing_id)

Update MethodRouting

<p>Update a MethodRouting.</p><p>Authentication is Mandatory</p><p>Explaination of Fields:</p><ul><li>method_name is required String value, current supported value: [mapped | internal | rest_vMar2019]</li><li>connector_name is required String value</li><li>is_bank_id_exact_match is required boolean value, if bank_id_pattern is exact bank_id value, this value is true; if bank_id_pattern is null or a regex, this value is false</li><li>bank_id_pattern is optional String value, it can be null, a exact bank_id or a regex</li><li>parameters is optional array of key value pairs. You can set some paremeters for this method<br />note:</li><li><p>if bank_id_pattern is regex, special characters need to do escape, for example: bank_id_pattern = &quot;some-id_pattern_\\d+&quot;</p></li></ul><p>If connector name start with rest, parameters can contain &quot;outBoundMapping&quot; and &quot;inBoundMapping&quot;, to convert OutBound and InBound json structure.<br />for example:<br />outBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248007-33332e00-580e-11ea-8d2a-d1856035fa24.png\" alt=\"Snipaste_outBoundMapping\" /><br />Build OutBound json value rules:<br />1 set cId value with: outboundAdapterCallContext.correlationId value<br />2 set bankId value with: concat bankId.value value with  string helloworld<br />3 set originalJson value with: whole source json, note: the field value expression is $root</p><p>inBoundMapping example, convert json from source to target:<br /><img src=\"https://user-images.githubusercontent.com/2577334/75248199-a9d02b80-580e-11ea-9238-e073264e9170.png\" alt=\"inBoundMapping\" /><br />Build InBound json value rules:<br />1 and 2 set inboundAdapterCallContext and status value: because field name ends with &quot;$default&quot;, remove &quot;$default&quot; from field name, not change the value<br />3 set fullName value with: concat string full: with result.name value<br />4 set bankRoutingScheme value: because source value is Array, but target value is not Array, the mapping field name must ends with [0].</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.MethodRoutingCommons() # MethodRoutingCommons | MethodRoutingCommons object that needs to be added.
method_routing_id = 'method_routing_id_example' # str | the method routing id 

try:
    # Update MethodRouting
    api_response = api_instance.o_bpv3_1_0_update_method_routing(body, method_routing_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv3_1_0_update_method_routing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MethodRoutingCommons**](MethodRoutingCommons.md)| MethodRoutingCommons object that needs to be added. | 
 **method_routing_id** | **str**| the method routing id  | 

### Return type

[**MethodRoutingCommons**](MethodRoutingCommons.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_bank_level_dynamic_endpoint**
> InlineResponse201 o_bpv4_0_0_create_bank_level_dynamic_endpoint(body, bank_id)

Create Bank Level Dynamic Endpoint

<p>Create dynamic endpoints.</p><p>Create dynamic endpoints with one json format swagger content.</p><p>If the host of swagger is <code>dynamic_entity</code>, then you need link the swagger fields to the dynamic entity fields,<br />please check <code>Endpoint Mapping</code> endpoints.</p><p>If the host of swagger is <code>obp_mock</code>, every dynamic endpoint will return example response of swagger,</p><p>when create MethodRouting for given dynamic endpoint, it will be routed to given url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.Body() # Body | JObject object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_create_bank_level_dynamic_endpoint(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_bank_level_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)| JObject object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_bank_level_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_create_bank_level_dynamic_entity(body, bank_id)

Create Bank Level Dynamic Entity

<p>Create a Bank Level DynamicEntity.</p><p>Authentication is Mandatory</p><p>Create a DynamicEntity. If creation is successful, the corresponding POST, GET, PUT and DELETE (Create, Read, Update, Delete or CRUD for short) endpoints will be generated automatically</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>The DATE_WITH_DAY format is: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;260e3831-4bdf-49a2-a807-1d7781fde395&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;branchId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;atmId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;accountId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;productCode=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;cardId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;accountId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&amp;transactionId=19f67d44-5abb-464d-a8a4-86892a7d24ae&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=260e3831-4bdf-49a2-a807-1d7781fde395&amp;accountId=8735b3b6-9b7f-425d-9041-f5932a9df7d8&amp;counterpartyId=19f67d44-5abb-464d-a8a4-86892a7d24ae&quot;}</code></pre><p>Note: if you set <code>hasPersonalEntity</code> = false, then OBP will not generate the CRUD my FooBar endpoints.</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_create_bank_level_dynamic_entity(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_bank_level_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_bank_level_endpoint_tag**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_create_bank_level_endpoint_tag(body, bank_id)

Create Bank Level Endpoint Tag

<p>Create Bank Level Endpoint Tag</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_create_bank_level_endpoint_tag(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_bank_level_endpoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_bank_level_endpoint_tag_0**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_create_bank_level_endpoint_tag_0(body, bank_id)

Create Bank Level Endpoint Tag

<p>Create Bank Level Endpoint Tag</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Create Bank Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_create_bank_level_endpoint_tag_0(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_bank_level_endpoint_tag_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_dynamic_endpoint**
> InlineResponse2011 o_bpv4_0_0_create_dynamic_endpoint(body)

Create Dynamic Endpoint

<p>Create dynamic endpoints.</p><p>Create dynamic endpoints with one json format swagger content.</p><p>If the host of swagger is <code>dynamic_entity</code>, then you need link the swagger fields to the dynamic entity fields,<br />please check <code>Endpoint Mapping</code> endpoints.</p><p>If the host of swagger is <code>obp_mock</code>, every dynamic endpoint will return example response of swagger,</p><p>when create MethodRouting for given dynamic endpoint, it will be routed to given url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.Body3() # Body3 | JObject object that needs to be added.

try:
    # Create Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_create_dynamic_endpoint(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| JObject object that needs to be added. | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_system_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_create_system_dynamic_entity(body)

Create System Level Dynamic Entity

<p>Create a system level Dynamic Entity.</p><p>Authentication is Mandatory</p><p>Create a DynamicEntity. If creation is successful, the corresponding POST, GET, PUT and DELETE (Create, Read, Update, Delete or CRUD for short) endpoints will be generated automatically</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>The DATE_WITH_DAY format is: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />See the following list of currently available reference types and examples of how to construct key values correctly. Note: As more Dynamic Entities are created on this instance, this list will grow:</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;branchId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;atmId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;accountId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;productCode=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;cardId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;accountId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&amp;transactionId=45a74569-c3a2-4b82-8111-3f68a32e5d95&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=2494121b-1bcc-4793-8d9e-6eb5f49f1b2c&amp;accountId=8ab76ee8-0303-4fd3-a71c-c5c6f467cb78&amp;counterpartyId=45a74569-c3a2-4b82-8111-3f68a32e5d95&quot;}</code></pre><p>Note: if you set <code>hasPersonalEntity</code> = false, then OBP will not generate the CRUD my FooBar endpoints.</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.

try:
    # Create System Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_create_system_dynamic_entity(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_system_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_system_level_endpoint_tag**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_create_system_level_endpoint_tag(body)

Create System Level Endpoint Tag

<p>Create System Level Endpoint Tag</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.

try:
    # Create System Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_create_system_level_endpoint_tag(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_system_level_endpoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_create_system_level_endpoint_tag_0**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_create_system_level_endpoint_tag_0(body)

Create System Level Endpoint Tag

<p>Create System Level Endpoint Tag</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.

try:
    # Create System Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_create_system_level_endpoint_tag_0(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_create_system_level_endpoint_tag_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_dynamic_endpoint**
> o_bpv4_0_0_delete_bank_level_dynamic_endpoint(bank_id)

 Delete Bank Level Dynamic Endpoint

<p>Delete a Bank Level DynamicEndpoint specified by DYNAMIC_ENDPOINT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    #  Delete Bank Level Dynamic Endpoint
    api_instance.o_bpv4_0_0_delete_bank_level_dynamic_endpoint(bank_id)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_bank_level_dynamic_endpoint: %s\n" % e)
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

# **o_bpv4_0_0_delete_bank_level_dynamic_entity**
> o_bpv4_0_0_delete_bank_level_dynamic_entity(dynamic_entity_id, bank_id)

Delete Bank Level Dynamic Entity

<p>Delete a Bank Level DynamicEntity specified by DYNAMIC_ENTITY_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Dynamic Entity
    api_instance.o_bpv4_0_0_delete_bank_level_dynamic_entity(dynamic_entity_id, bank_id)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_bank_level_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_entity_id** | **str**| the dynamic entity id  | 
 **bank_id** | **str**| The bank id | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_endpoint_tag**
> Full o_bpv4_0_0_delete_bank_level_endpoint_tag(bank_id)

Delete Bank Level Endpoint Tag

<p>Delete Bank Level Endpoint Tag.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_delete_bank_level_endpoint_tag(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_bank_level_endpoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_bank_level_endpoint_tag_0**
> Full o_bpv4_0_0_delete_bank_level_endpoint_tag_0(bank_id)

Delete Bank Level Endpoint Tag

<p>Delete Bank Level Endpoint Tag.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Delete Bank Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_delete_bank_level_endpoint_tag_0(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_bank_level_endpoint_tag_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_dynamic_endpoint**
> o_bpv4_0_0_delete_dynamic_endpoint()

 Delete Dynamic Endpoint

<p>Delete a DynamicEndpoint specified by DYNAMIC_ENDPOINT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    #  Delete Dynamic Endpoint
    api_instance.o_bpv4_0_0_delete_dynamic_endpoint()
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_dynamic_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_dynamic_endpoint**
> o_bpv4_0_0_delete_my_dynamic_endpoint()

Delete My Dynamic Endpoint

<p>Delete a DynamicEndpoint specified by DYNAMIC_ENDPOINT_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Delete My Dynamic Endpoint
    api_instance.o_bpv4_0_0_delete_my_dynamic_endpoint()
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_my_dynamic_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_my_dynamic_entity**
> o_bpv4_0_0_delete_my_dynamic_entity(dynamic_entity_id)

Delete My Dynamic Entity

<p>Delete my DynamicEntity specified by DYNAMIC_ENTITY_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Delete My Dynamic Entity
    api_instance.o_bpv4_0_0_delete_my_dynamic_entity(dynamic_entity_id)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_my_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_system_dynamic_entity**
> o_bpv4_0_0_delete_system_dynamic_entity(dynamic_entity_id)

Delete System Level Dynamic Entity

<p>Delete a DynamicEntity specified by DYNAMIC_ENTITY_ID.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Delete System Level Dynamic Entity
    api_instance.o_bpv4_0_0_delete_system_dynamic_entity(dynamic_entity_id)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_system_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_system_level_endpoint_tag**
> Full o_bpv4_0_0_delete_system_level_endpoint_tag()

Delete System Level Endpoint Tag

<p>Delete System Level Endpoint Tag.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Delete System Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_delete_system_level_endpoint_tag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_system_level_endpoint_tag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_delete_system_level_endpoint_tag_0**
> Full o_bpv4_0_0_delete_system_level_endpoint_tag_0()

Delete System Level Endpoint Tag

<p>Delete System Level Endpoint Tag.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Delete System Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_delete_system_level_endpoint_tag_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_delete_system_level_endpoint_tag_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Full**](Full.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_endpoint**
> InlineResponse201 o_bpv4_0_0_get_bank_level_dynamic_endpoint(bank_id)

 Get Bank Level Dynamic Endpoint

<p>Get a Bank Level Dynamic Endpoint.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    #  Get Bank Level Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_endpoint(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_bank_level_dynamic_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_endpoints**
> InlineResponse2003 o_bpv4_0_0_get_bank_level_dynamic_endpoints(bank_id)

Get Bank Level Dynamic Endpoints

<p>Get Bank Level Dynamic Endpoints.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Endpoints
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_endpoints(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_bank_level_dynamic_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_dynamic_entities**
> InlineResponse2004 o_bpv4_0_0_get_bank_level_dynamic_entities(bank_id)

Get Bank Level Dynamic Entities

<p>Get all the bank level Dynamic Entities for one bank.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Dynamic Entities
    api_response = api_instance.o_bpv4_0_0_get_bank_level_dynamic_entities(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_bank_level_dynamic_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_endpoint_tags**
> Coloncolon o_bpv4_0_0_get_bank_level_endpoint_tags(bank_id)

Get Bank Level Endpoint Tags

<p>Get Bank Level Endpoint Tags.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Endpoint Tags
    api_response = api_instance.o_bpv4_0_0_get_bank_level_endpoint_tags(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_bank_level_endpoint_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**Coloncolon**](Coloncolon.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_bank_level_endpoint_tags_0**
> Coloncolon o_bpv4_0_0_get_bank_level_endpoint_tags_0(bank_id)

Get Bank Level Endpoint Tags

<p>Get Bank Level Endpoint Tags.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Bank Level Endpoint Tags
    api_response = api_instance.o_bpv4_0_0_get_bank_level_endpoint_tags_0(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_bank_level_endpoint_tags_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**Coloncolon**](Coloncolon.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_call_context**
> o_bpv4_0_0_get_call_context()

Get the Call Context of a current call

<p>Get the Call Context of the current call.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get the Call Context of a current call
    api_instance.o_bpv4_0_0_get_call_context()
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_call_context: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_dynamic_endpoint**
> InlineResponse2011 o_bpv4_0_0_get_dynamic_endpoint()

Get Dynamic Endpoint

<p>Get a Dynamic Endpoint.</p><p>Get one DynamicEndpoint,</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get Dynamic Endpoint
    api_response = api_instance.o_bpv4_0_0_get_dynamic_endpoint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_dynamic_endpoint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_dynamic_endpoints**
> InlineResponse2009 o_bpv4_0_0_get_dynamic_endpoints()

 Get Dynamic Endpoints

<p>Get Dynamic Endpoints.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    #  Get Dynamic Endpoints
    api_response = api_instance.o_bpv4_0_0_get_dynamic_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_dynamic_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_mapper_database_info**
> AdapterInfoJsonV300 o_bpv4_0_0_get_mapper_database_info()

Get Mapper Database Info

<p>Get basic information about the Mapper Database.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get Mapper Database Info
    api_response = api_instance.o_bpv4_0_0_get_mapper_database_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_mapper_database_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdapterInfoJsonV300**](AdapterInfoJsonV300.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_dynamic_endpoints**
> InlineResponse20012 o_bpv4_0_0_get_my_dynamic_endpoints()

Get My Dynamic Endpoints

<p>Get My Dynamic Endpoints.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get My Dynamic Endpoints
    api_response = api_instance.o_bpv4_0_0_get_my_dynamic_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_my_dynamic_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_my_dynamic_entities**
> InlineResponse2004 o_bpv4_0_0_get_my_dynamic_entities()

Get My Dynamic Entities

<p>Get all my Dynamic Entities.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get My Dynamic Entities
    api_response = api_instance.o_bpv4_0_0_get_my_dynamic_entities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_my_dynamic_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_scanned_api_versions**
> InlineResponse200 o_bpv4_0_0_get_scanned_api_versions()

Get scanned API Versions

<p>Get all the scanned API Versions.</p><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get scanned API Versions
    api_response = api_instance.o_bpv4_0_0_get_scanned_api_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_scanned_api_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_system_dynamic_entities**
> InlineResponse2004 o_bpv4_0_0_get_system_dynamic_entities()

Get System Dynamic Entities

<p>Get all System Dynamic Entities</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get System Dynamic Entities
    api_response = api_instance.o_bpv4_0_0_get_system_dynamic_entities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_system_dynamic_entities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_system_level_endpoint_tags**
> Coloncolon o_bpv4_0_0_get_system_level_endpoint_tags()

Get System Level Endpoint Tags

<p>Get System Level Endpoint Tags.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get System Level Endpoint Tags
    api_response = api_instance.o_bpv4_0_0_get_system_level_endpoint_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_system_level_endpoint_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Coloncolon**](Coloncolon.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_get_system_level_endpoint_tags_0**
> Coloncolon o_bpv4_0_0_get_system_level_endpoint_tags_0()

Get System Level Endpoint Tags

<p>Get System Level Endpoint Tags.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get System Level Endpoint Tags
    api_response = api_instance.o_bpv4_0_0_get_system_level_endpoint_tags_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_get_system_level_endpoint_tags_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Coloncolon**](Coloncolon.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_root**
> APIInfoJson400 o_bpv4_0_0_root()

Get API Info (root)

<p>Returns information about:</p><ul><li>API version</li><li>Hosted by information</li><li>Hosted at information</li><li>Energy source information</li><li>Git Commit</li></ul><p>Authentication is Optional</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get API Info (root)
    api_response = api_instance.o_bpv4_0_0_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIInfoJson400**](APIInfoJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_dynamic_endpoint_host**
> DynamicEndpointHostJson400 o_bpv4_0_0_update_bank_level_dynamic_endpoint_host(body, bank_id)

 Update Bank Level Dynamic Endpoint Host

<p>Update Bank Level  dynamic endpoint Host.<br />The value can be obp_mock, dynamic_entity, or some service url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEndpointHostJson400() # DynamicEndpointHostJson400 | DynamicEndpointHostJson400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    #  Update Bank Level Dynamic Endpoint Host
    api_response = api_instance.o_bpv4_0_0_update_bank_level_dynamic_endpoint_host(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_bank_level_dynamic_endpoint_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)| DynamicEndpointHostJson400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_update_bank_level_dynamic_entity(body, dynamic_entity_id, bank_id)

Update Bank Level Dynamic Entity

<p>Update a Bank Level DynamicEntity.</p><p>Authentication is Mandatory</p><p>Update one DynamicEntity, after update finished, the corresponding CRUD endpoints will be changed.</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>DATE_WITH_DAY format: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;56ea676b-9e92-4b47-b3cb-9ec259372581&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;branchId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;atmId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;accountId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;productCode=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;cardId=6b433d26-692d-47d9-8433-bf8c8b249a4b&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;accountId=6b433d26-692d-47d9-8433-bf8c8b249a4b&amp;transactionId=d69c95e9-6d71-4219-9d8a-d0dbe4014817&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=56ea676b-9e92-4b47-b3cb-9ec259372581&amp;accountId=6b433d26-692d-47d9-8433-bf8c8b249a4b&amp;counterpartyId=d69c95e9-6d71-4219-9d8a-d0dbe4014817&quot;}</code></pre>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_update_bank_level_dynamic_entity(body, dynamic_entity_id, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_bank_level_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **dynamic_entity_id** | **str**| the dynamic entity id  | 
 **bank_id** | **str**| The bank id | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_endpoint_tag**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_update_bank_level_endpoint_tag(body, bank_id)

Update Bank Level Endpoint Tag

<p>Update Endpoint Tag, you can only update the tag_name here, operation_id can not be updated.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_update_bank_level_endpoint_tag(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_bank_level_endpoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_bank_level_endpoint_tag_0**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_update_bank_level_endpoint_tag_0(body, bank_id)

Update Bank Level Endpoint Tag

<p>Update Endpoint Tag, you can only update the tag_name here, operation_id can not be updated.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.
bank_id = 'bank_id_example' # str | The bank id

try:
    # Update Bank Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_update_bank_level_endpoint_tag_0(body, bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_bank_level_endpoint_tag_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 
 **bank_id** | **str**| The bank id | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_dynamic_endpoint_host**
> DynamicEndpointHostJson400 o_bpv4_0_0_update_dynamic_endpoint_host(body)

 Update Dynamic Endpoint Host

<p>Update dynamic endpoint Host.<br />The value can be obp_mock, dynamic_entity, or some service url.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEndpointHostJson400() # DynamicEndpointHostJson400 | DynamicEndpointHostJson400 object that needs to be added.

try:
    #  Update Dynamic Endpoint Host
    api_response = api_instance.o_bpv4_0_0_update_dynamic_endpoint_host(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_dynamic_endpoint_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)| DynamicEndpointHostJson400 object that needs to be added. | 

### Return type

[**DynamicEndpointHostJson400**](DynamicEndpointHostJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_my_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_update_my_dynamic_entity(body, dynamic_entity_id)

Update My Dynamic Entity

<p>Update my DynamicEntity.</p><p>Authentication is Mandatory</p><p>Update one of my DynamicEntity, after update finished, the corresponding CRUD endpoints will be changed.</p><p>Current support filed types as follow:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>DATE_WITH_DAY format: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;eebb4aa3-8b94-4c5c-aeee-e7849443f93f&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;branchId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;atmId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;accountId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;productCode=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;cardId=26617f71-1ba3-4ecb-94d1-e784071c7e24&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;accountId=26617f71-1ba3-4ecb-94d1-e784071c7e24&amp;transactionId=e0c520f5-8a29-4554-9a8b-8321b15bf478&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=eebb4aa3-8b94-4c5c-aeee-e7849443f93f&amp;accountId=26617f71-1ba3-4ecb-94d1-e784071c7e24&amp;counterpartyId=e0c520f5-8a29-4554-9a8b-8321b15bf478&quot;}</code></pre>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Update My Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_update_my_dynamic_entity(body, dynamic_entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_my_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_system_dynamic_entity**
> DynamicEntityFooBar o_bpv4_0_0_update_system_dynamic_entity(body, dynamic_entity_id)

Update System Level Dynamic Entity

<p>Update a System Level Dynamic Entity.</p><p>Authentication is Mandatory</p><p>Update one DynamicEntity, after update finished, the corresponding CRUD endpoints will be changed.</p><p>The following field types are as supported:<br />[number, integer, boolean, string, DATE_WITH_DAY, reference]</p><p>DATE_WITH_DAY format: yyyy-MM-dd</p><p>Reference types are like foreign keys and composite foreign keys are supported. The value you need to supply as the (composite) foreign key is a UUID (or several UUIDs in the case of a composite key) that match value in another Entity..<br />The following list shows all the possible reference types in the system with corresponding examples values so you can see how to construct each reference type value.</p><pre><code>&quot;someField0&quot;: {    &quot;type&quot;: &quot;reference:Bank&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField1&quot;: {    &quot;type&quot;: &quot;reference:Consumer&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField2&quot;: {    &quot;type&quot;: &quot;reference:Customer&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField3&quot;: {    &quot;type&quot;: &quot;reference:MethodRouting&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField4&quot;: {    &quot;type&quot;: &quot;reference:DynamicEntity&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField5&quot;: {    &quot;type&quot;: &quot;reference:TransactionRequest&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField6&quot;: {    &quot;type&quot;: &quot;reference:ProductAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField7&quot;: {    &quot;type&quot;: &quot;reference:AccountAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField8&quot;: {    &quot;type&quot;: &quot;reference:TransactionAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField9&quot;: {    &quot;type&quot;: &quot;reference:CustomerAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField10&quot;: {    &quot;type&quot;: &quot;reference:AccountApplication&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField11&quot;: {    &quot;type&quot;: &quot;reference:CardAttribute&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField12&quot;: {    &quot;type&quot;: &quot;reference:Counterparty&quot;,    &quot;example&quot;: &quot;3c2723b2-a420-4c92-ad85-64e94bfe0168&quot;}&quot;someField13&quot;: {    &quot;type&quot;: &quot;reference:Branch:bankId&amp;branchId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;branchId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField14&quot;: {    &quot;type&quot;: &quot;reference:Atm:bankId&amp;atmId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;atmId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField15&quot;: {    &quot;type&quot;: &quot;reference:BankAccount:bankId&amp;accountId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;accountId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField16&quot;: {    &quot;type&quot;: &quot;reference:Product:bankId&amp;productCode&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;productCode=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField17&quot;: {    &quot;type&quot;: &quot;reference:PhysicalCard:bankId&amp;cardId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;cardId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&quot;}&quot;someField18&quot;: {    &quot;type&quot;: &quot;reference:Transaction:bankId&amp;accountId&amp;transactionId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;accountId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&amp;transactionId=cad30b93-7ba0-4287-9942-6e9c81925f8d&quot;}&quot;someField19&quot;: {    &quot;type&quot;: &quot;reference:Counterparty:bankId&amp;accountId&amp;counterpartyId&quot;,    &quot;example&quot;: &quot;bankId=3c2723b2-a420-4c92-ad85-64e94bfe0168&amp;accountId=4c8fbdd6-5397-4ab8-a7b2-9f127589a458&amp;counterpartyId=cad30b93-7ba0-4287-9942-6e9c81925f8d&quot;}</code></pre>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.DynamicEntityFooBar() # DynamicEntityFooBar | DynamicEntityFooBar object that needs to be added.
dynamic_entity_id = 'dynamic_entity_id_example' # str | the dynamic entity id 

try:
    # Update System Level Dynamic Entity
    api_response = api_instance.o_bpv4_0_0_update_system_dynamic_entity(body, dynamic_entity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_system_dynamic_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DynamicEntityFooBar**](DynamicEntityFooBar.md)| DynamicEntityFooBar object that needs to be added. | 
 **dynamic_entity_id** | **str**| the dynamic entity id  | 

### Return type

[**DynamicEntityFooBar**](DynamicEntityFooBar.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_system_level_endpoint_tag**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_update_system_level_endpoint_tag(body)

Update System Level Endpoint Tag

<p>Update System Level Endpoint Tag, you can only update the tag_name here, operation_id can not be updated.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.

try:
    # Update System Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_update_system_level_endpoint_tag(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_system_level_endpoint_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_update_system_level_endpoint_tag_0**
> BankLevelEndpointTagResponseJson400 o_bpv4_0_0_update_system_level_endpoint_tag_0(body)

Update System Level Endpoint Tag

<p>Update System Level Endpoint Tag, you can only update the tag_name here, operation_id can not be updated.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
body = obp_python.EndpointTagJson400() # EndpointTagJson400 | EndpointTagJson400 object that needs to be added.

try:
    # Update System Level Endpoint Tag
    api_response = api_instance.o_bpv4_0_0_update_system_level_endpoint_tag_0(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_update_system_level_endpoint_tag_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointTagJson400**](EndpointTagJson400.md)| EndpointTagJson400 object that needs to be added. | 

### Return type

[**BankLevelEndpointTagResponseJson400**](BankLevelEndpointTagResponseJson400.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv4_0_0_verify_request_sign_response**
> o_bpv4_0_0_verify_request_sign_response()

Verify Request and Sign Response of a current call

<p>Verify Request and Sign Response of a current call.</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Verify Request and Sign Response of a current call
    api_instance.o_bpv4_0_0_verify_request_sign_response()
except ApiException as e:
    print("Exception when calling APIApi->o_bpv4_0_0_verify_request_sign_response: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_adapter_info**
> AdapterInfoJsonV500 o_bpv5_0_0_get_adapter_info()

Get Adapter Info

<p>Get basic information about the Adapter.</p><p>Authentication is Optional</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))

try:
    # Get Adapter Info
    api_response = api_instance.o_bpv5_0_0_get_adapter_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv5_0_0_get_adapter_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdapterInfoJsonV500**](AdapterInfoJsonV500.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_bpv5_0_0_get_metrics_at_bank**
> MetricsJson o_bpv5_0_0_get_metrics_at_bank(bank_id)

Get Metrics at Bank

<p>Get the all metrics at the Bank specified by BANK_ID</p><p>require CanReadMetrics role</p><p>Filters Part 1.<em>filtering</em> (no wilde cards etc.) parameters to GET /management/metrics</p><p>Should be able to filter on the following metrics fields</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z&amp;limit=50&amp;offset=2</p><p>1 from_date (defaults to one week before current date): eg:from_date=1100-01-01T01:01:01.000Z</p><p>2 to_date (defaults to current date) eg:to_date=1100-01-01T01:01:01.000Z</p><p>3 limit (for pagination: defaults to 50)  eg:limit=200</p><p>4 offset (for pagination: zero index, defaults to 0) eg: offset=10</p><p>5 sort_by (defaults to date field) eg: sort_by=date<br />possible values:<br />&quot;url&quot;,<br />&quot;date&quot;,<br />&quot;user_name&quot;,<br />&quot;app_name&quot;,<br />&quot;developer_email&quot;,<br />&quot;implemented_by_partial_function&quot;,<br />&quot;implemented_in_version&quot;,<br />&quot;consumer_id&quot;,<br />&quot;verb&quot;</p><p>6 direction (defaults to date desc) eg: direction=desc</p><p>eg: /management/metrics?from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:<a href=\"&#109;&#97;&#105;&#x6c;&#x74;&#x6f;&#58;&#x30;&#49;&#x2e;&#48;&#48;&#x30;&#x5a;&amp;&#108;&#x69;&#x6d;&#x69;&#x74;&#61;&#49;&#48;&#x30;&#x30;&#48;&#38;&#111;&#x66;&#102;&#x73;&#101;t&#x3d;&#48;&#x26;&#x61;no&#110;&#61;&#x66;&#97;&#x6c;&#115;&#x65;&#38;&#97;&#112;&#x70;&#x5f;&#110;&#x61;&#109;&#x65;&#x3d;&#84;&#101;&#97;&#x74;&#x41;p&#112;&amp;&#105;&#109;&#112;l&#x65;&#x6d;&#101;&#x6e;&#116;&#101;&#100;_&#105;n&#95;v&#101;&#114;&#115;&#x69;&#111;n&#x3d;&#x76;&#x32;&#x2e;&#49;&#x2e;&#48;&#38;&#118;&#101;&#114;&#98;&#x3d;&#80;&#79;&#83;T&amp;&#117;&#x73;&#x65;&#x72;&#x5f;&#105;d=&#x63;&#x37;&#x62;&#x36;&#x63;&#98;&#52;&#x37;&#45;c&#x62;&#57;&#54;&#x2d;&#52;&#52;&#x34;1&#x2d;88&#48;&#x31;&#45;&#51;5&#x62;5&#x37;4&#x35;&#54;&#55;&#53;&#x33;&#97;&#x26;&#117;&#115;&#x65;&#x72;_&#x6e;&#97;&#x6d;&#101;&#61;s&#117;&#x73;a&#x6e;&#x2e;&#117;&#x6b;&#46;&#x32;&#x39;&#x40;e&#120;a&#x6d;p&#x6c;&#x65;&#x2e;&#x63;&#x6f;m\">&#48;&#x31;&#46;&#48;&#48;&#x30;&#90;&#38;&#108;&#105;&#x6d;i&#x74;=1&#x30;&#x30;0&#48;&#x26;&#111;&#102;&#102;&#x73;&#101;&#116;&#x3d;&#x30;&#x26;a&#110;&#111;n&#61;f&#x61;l&#x73;&#101;&#x26;&#97;&#x70;p&#95;n&#x61;&#109;e&#x3d;&#x54;&#x65;&#97;&#x74;&#65;p&#112;&#38;&#105;&#109;p&#x6c;&#101;&#109;e&#110;&#x74;&#x65;&#x64;&#95;&#x69;&#110;&#95;&#118;er&#115;&#x69;o&#x6e;&#61;&#118;2&#46;1&#x2e;&#48;&#38;&#118;&#x65;r&#x62;&#61;&#80;OS&#x54;&#x26;&#117;&#115;&#101;r&#x5f;&#105;d&#x3d;&#99;&#55;&#98;&#54;cb&#52;7&#x2d;&#99;&#x62;9&#54;&#x2d;&#x34;&#52;&#52;&#x31;&#45;8&#56;&#48;&#49;&#45;&#x33;5&#98;&#x35;&#x37;&#52;56&#x37;5&#51;a&amp;&#117;&#x73;&#x65;&#114;&#x5f;&#110;a&#x6d;&#x65;&#x3d;&#x73;&#x75;&#115;&#97;&#x6e;.&#x75;&#x6b;.29&#64;&#101;&#120;&#97;&#x6d;&#x70;l&#101;&#46;&#x63;&#x6f;&#109;</a>&amp;consumer_id=78</p><p>Other filters:</p><p>7 consumer_id  (if null ignore)</p><p>8 user_id (if null ignore)</p><p>9 anon (if null ignore) only support two value : true (return where user_id is null.) or false (return where user_id is not null.)</p><p>10 url (if null ignore), note: can not contain '&amp;'.</p><p>11 app_name (if null ignore)</p><p>12 implemented_by_partial_function (if null ignore),</p><p>13 implemented_in_version (if null ignore)</p><p>14 verb (if null ignore)</p><p>15 correlation_id (if null ignore)</p><p>16 duration (if null ignore) non digit chars will be silently omitted</p><p>Authentication is Mandatory</p>

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
api_instance = obp_python.APIApi(obp_python.ApiClient(configuration))
bank_id = 'bank_id_example' # str | The bank id

try:
    # Get Metrics at Bank
    api_response = api_instance.o_bpv5_0_0_get_metrics_at_bank(bank_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIApi->o_bpv5_0_0_get_metrics_at_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| The bank id | 

### Return type

[**MetricsJson**](MetricsJson.md)

### Authorization

[directLogin](../README.md#directLogin), [gatewayLogin](../README.md#gatewayLogin)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

