# swagger_client.AuthorsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_author_details**](AuthorsApi.md#private_author_details) | **GET** /account/authors/{author_id} | Author details
[**private_authors_search**](AuthorsApi.md#private_authors_search) | **POST** /account/authors/search | Search Authors


# **private_author_details**
> AuthorComplete private_author_details(author_id)

Author details

View author details

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
api_instance = swagger_client.AuthorsApi()
author_id = 789 # int | Author unique identifier

try: 
    # Author details
    api_response = api_instance.private_author_details(author_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorsApi->private_author_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **int**| Author unique identifier | 

### Return type

[**AuthorComplete**](AuthorComplete.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_authors_search**
> list[Author] private_authors_search(search=search)

Search Authors

Search for authors

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
api_instance = swagger_client.AuthorsApi()
search = swagger_client.PrivateAuthorsSearch() # PrivateAuthorsSearch | Search Parameters (optional)

try: 
    # Search Authors
    api_response = api_instance.private_authors_search(search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorsApi->private_authors_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**PrivateAuthorsSearch**](PrivateAuthorsSearch.md)| Search Parameters | [optional] 

### Return type

[**list[Author]**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

