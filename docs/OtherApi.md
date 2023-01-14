# swagger_client.OtherApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_list**](OtherApi.md#categories_list) | **GET** /categories | Public Categories
[**file_download**](OtherApi.md#file_download) | **GET** /file/download/{file_id} | Public File Download
[**item_types_list**](OtherApi.md#item_types_list) | **GET** /item_types | Item Types
[**licenses_list**](OtherApi.md#licenses_list) | **GET** /licenses | Public Licenses
[**private_account**](OtherApi.md#private_account) | **GET** /account | Private Account information
[**private_funding_search**](OtherApi.md#private_funding_search) | **POST** /account/funding/search | Search Funding
[**private_licenses_list**](OtherApi.md#private_licenses_list) | **GET** /account/licenses | Private Account Licenses


# **categories_list**
> list[Category] categories_list()

Public Categories

Returns a list of public categories

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtherApi()

try: 
    # Public Categories
    api_response = api_instance.categories_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtherApi->categories_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Category]**](Category.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_download**
> file_download(file_id)

Public File Download

Starts the download of a file

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtherApi()
file_id = 789 # int | 

try: 
    # Public File Download
    api_instance.file_download(file_id)
except ApiException as e:
    print("Exception when calling OtherApi->file_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/force-download

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_types_list**
> list[ItemType] item_types_list(group_id=group_id)

Item Types

Returns the list of Item Types of the requested group. If no user is authenticated, returns the item types available for Figshare.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OtherApi()
group_id = 0 # int | Identifier of the group for which the item types are requested (optional) (default to 0)

try: 
    # Item Types
    api_response = api_instance.item_types_list(group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtherApi->item_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Identifier of the group for which the item types are requested | [optional] [default to 0]

### Return type

[**list[ItemType]**](ItemType.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_list**
> list[License] licenses_list()

Public Licenses

Returns a list of public licenses

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OtherApi()

try: 
    # Public Licenses
    api_response = api_instance.licenses_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtherApi->licenses_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[License]**](License.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_account**
> Account private_account()

Private Account information

Account information for token/personal token

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OtherApi()

try: 
    # Private Account information
    api_response = api_instance.private_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtherApi->private_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Account**](Account.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_funding_search**
> list[FundingInformation] private_funding_search(search=search)

Search Funding

Search for fundings

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OtherApi()
search = swagger_client.FundingSearch() # FundingSearch | Search Parameters (optional)

try: 
    # Search Funding
    api_response = api_instance.private_funding_search(search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtherApi->private_funding_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**FundingSearch**](FundingSearch.md)| Search Parameters | [optional] 

### Return type

[**list[FundingInformation]**](FundingInformation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_licenses_list**
> list[License] private_licenses_list()

Private Account Licenses

This is a private endpoint that requires OAuth. It will return a list with figshare public licenses AND licenses defined for account's institution.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OtherApi()

try: 
    # Private Account Licenses
    api_response = api_instance.private_licenses_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OtherApi->private_licenses_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[License]**](License.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

