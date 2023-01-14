# swagger_client.CollectionsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_articles**](CollectionsApi.md#collection_articles) | **GET** /collections/{collection_id}/articles | Public Collection Articles
[**collection_details**](CollectionsApi.md#collection_details) | **GET** /collections/{collection_id} | Collection details
[**collection_version_details**](CollectionsApi.md#collection_version_details) | **GET** /collections/{collection_id}/versions/{version_id} | Collection Version details
[**collection_versions**](CollectionsApi.md#collection_versions) | **GET** /collections/{collection_id}/versions | Collection Versions list
[**collections_list**](CollectionsApi.md#collections_list) | **GET** /collections | Public Collections
[**collections_search**](CollectionsApi.md#collections_search) | **POST** /collections/search | Public Collections Search
[**private_collection_article_delete**](CollectionsApi.md#private_collection_article_delete) | **DELETE** /account/collections/{collection_id}/articles/{article_id} | Delete collection article
[**private_collection_articles_add**](CollectionsApi.md#private_collection_articles_add) | **POST** /account/collections/{collection_id}/articles | Add collection articles
[**private_collection_articles_list**](CollectionsApi.md#private_collection_articles_list) | **GET** /account/collections/{collection_id}/articles | List collection articles
[**private_collection_articles_replace**](CollectionsApi.md#private_collection_articles_replace) | **PUT** /account/collections/{collection_id}/articles | Replace collection articles
[**private_collection_author_delete**](CollectionsApi.md#private_collection_author_delete) | **DELETE** /account/collections/{collection_id}/authors/{author_id} | Delete collection author
[**private_collection_authors_add**](CollectionsApi.md#private_collection_authors_add) | **POST** /account/collections/{collection_id}/authors | Add collection authors
[**private_collection_authors_list**](CollectionsApi.md#private_collection_authors_list) | **GET** /account/collections/{collection_id}/authors | List collection authors
[**private_collection_authors_replace**](CollectionsApi.md#private_collection_authors_replace) | **PUT** /account/collections/{collection_id}/authors | Replace collection authors
[**private_collection_categories_add**](CollectionsApi.md#private_collection_categories_add) | **POST** /account/collections/{collection_id}/categories | Add collection categories
[**private_collection_categories_list**](CollectionsApi.md#private_collection_categories_list) | **GET** /account/collections/{collection_id}/categories | List collection categories
[**private_collection_categories_replace**](CollectionsApi.md#private_collection_categories_replace) | **PUT** /account/collections/{collection_id}/categories | Replace collection categories
[**private_collection_category_delete**](CollectionsApi.md#private_collection_category_delete) | **DELETE** /account/collections/{collection_id}/categories/{category_id} | Delete collection category
[**private_collection_create**](CollectionsApi.md#private_collection_create) | **POST** /account/collections | Create collection
[**private_collection_delete**](CollectionsApi.md#private_collection_delete) | **DELETE** /account/collections/{collection_id} | Delete collection
[**private_collection_details**](CollectionsApi.md#private_collection_details) | **GET** /account/collections/{collection_id} | Collection details
[**private_collection_private_link_create**](CollectionsApi.md#private_collection_private_link_create) | **POST** /account/collections/{collection_id}/private_links | Create collection private link
[**private_collection_private_link_delete**](CollectionsApi.md#private_collection_private_link_delete) | **DELETE** /account/collections/{collection_id}/private_links/{link_id} | Disable private link
[**private_collection_private_link_update**](CollectionsApi.md#private_collection_private_link_update) | **PUT** /account/collections/{collection_id}/private_links/{link_id} | Update collection private link
[**private_collection_private_links_list**](CollectionsApi.md#private_collection_private_links_list) | **GET** /account/collections/{collection_id}/private_links | List collection private links
[**private_collection_publish**](CollectionsApi.md#private_collection_publish) | **POST** /account/collections/{collection_id}/publish | Private Collection Publish
[**private_collection_reserve_doi**](CollectionsApi.md#private_collection_reserve_doi) | **POST** /account/collections/{collection_id}/reserve_doi | Private Collection Reserve DOI
[**private_collection_reserve_handle**](CollectionsApi.md#private_collection_reserve_handle) | **POST** /account/collections/{collection_id}/reserve_handle | Private Collection Reserve Handle
[**private_collection_resource**](CollectionsApi.md#private_collection_resource) | **POST** /account/collections/{collection_id}/resource | Private Collection Resource
[**private_collection_update**](CollectionsApi.md#private_collection_update) | **PUT** /account/collections/{collection_id} | Update collection
[**private_collections_list**](CollectionsApi.md#private_collections_list) | **GET** /account/collections | Private Collections List
[**private_collections_search**](CollectionsApi.md#private_collections_search) | **POST** /account/collections/search | Private Collections Search


# **collection_articles**
> list[Article] collection_articles(collection_id, page=page, page_size=page_size, limit=limit, offset=offset)

Public Collection Articles

Returns a list of public collection articles

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # Public Collection Articles
    api_response = api_instance.collection_articles(collection_id, page=page, page_size=page_size, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collection_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**list[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_details**
> CollectionComplete collection_details(collection_id)

Collection details

View a collection

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Collection details
    api_response = api_instance.collection_details(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collection_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

[**CollectionComplete**](CollectionComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_version_details**
> CollectionComplete collection_version_details(collection_id, version_id)

Collection Version details

View details for a certain version of a collection

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier
version_id = 789 # int | Version Number

try: 
    # Collection Version details
    api_response = api_instance.collection_version_details(collection_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collection_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 
 **version_id** | **int**| Version Number | 

### Return type

[**CollectionComplete**](CollectionComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collection_versions**
> list[CollectionVersions] collection_versions(collection_id)

Collection Versions list

Returns a list of public collection Versions

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Collection Versions list
    api_response = api_instance.collection_versions(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collection_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

[**list[CollectionVersions]**](CollectionVersions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_list**
> list[Collection] collections_list(x_cursor=x_cursor, page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, institution=institution, published_since=published_since, modified_since=modified_since, group=group, resource_doi=resource_doi, doi=doi, handle=handle)

Public Collections

Returns a list of public collections

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
x_cursor = 'x_cursor_example' # str | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. (optional)
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
order = 'published_date' # str | The field by which to order. Default varies by endpoint/resource. (optional) (default to published_date)
order_direction = 'desc' # str |  (optional) (default to desc)
institution = 789 # int | only return collections from this institution (optional)
published_since = 'published_since_example' # str | Filter by collection publishing date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD (optional)
modified_since = 'modified_since_example' # str | Filter by collection modified date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD (optional)
group = 789 # int | only return collections from this group (optional)
resource_doi = 'resource_doi_example' # str | only return collections with this resource_doi (optional)
doi = 'doi_example' # str | only return collections with this doi (optional)
handle = 'handle_example' # str | only return collections with this handle (optional)

try: 
    # Public Collections
    api_response = api_instance.collections_list(x_cursor=x_cursor, page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, institution=institution, published_since=published_since, modified_since=modified_since, group=group, resource_doi=resource_doi, doi=doi, handle=handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_cursor** | **str**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **str**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to published_date]
 **order_direction** | **str**|  | [optional] [default to desc]
 **institution** | **int**| only return collections from this institution | [optional] 
 **published_since** | **str**| Filter by collection publishing date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **modified_since** | **str**| Filter by collection modified date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **group** | **int**| only return collections from this group | [optional] 
 **resource_doi** | **str**| only return collections with this resource_doi | [optional] 
 **doi** | **str**| only return collections with this doi | [optional] 
 **handle** | **str**| only return collections with this handle | [optional] 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_search**
> list[Collection] collections_search(x_cursor=x_cursor, search=search)

Public Collections Search

Returns a list of public collections

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
x_cursor = 'x_cursor_example' # str | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. (optional)
search = swagger_client.CollectionSearch() # CollectionSearch | Search Parameters (optional)

try: 
    # Public Collections Search
    api_response = api_instance.collections_search(x_cursor=x_cursor, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_cursor** | **str**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **search** | [**CollectionSearch**](CollectionSearch.md)| Search Parameters | [optional] 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_article_delete**
> private_collection_article_delete(collection_id, article_id)

Delete collection article

De-associate article from collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
article_id = 789 # int | Collection article unique identifier

try: 
    # Delete collection article
    api_instance.private_collection_article_delete(collection_id, article_id)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_article_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **article_id** | **int**| Collection article unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_articles_add**
> Location private_collection_articles_add(collection_id, articles)

Add collection articles

Associate new articles with the collection. This will add new articles to the list of already associated articles

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
articles = swagger_client.ArticlesCreator() # ArticlesCreator | Articles list

try: 
    # Add collection articles
    api_response = api_instance.private_collection_articles_add(collection_id, articles)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_articles_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **articles** | [**ArticlesCreator**](ArticlesCreator.md)| Articles list | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_articles_list**
> list[Article] private_collection_articles_list(collection_id, page=page, page_size=page_size, limit=limit, offset=offset)

List collection articles

List collection articles

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # List collection articles
    api_response = api_instance.private_collection_articles_list(collection_id, page=page, page_size=page_size, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_articles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**list[Article]**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_articles_replace**
> private_collection_articles_replace(collection_id, articles)

Replace collection articles

Associate new articles with the collection. This will remove all already associated articles and add these new ones

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
articles = swagger_client.ArticlesCreator() # ArticlesCreator | Articles List

try: 
    # Replace collection articles
    api_instance.private_collection_articles_replace(collection_id, articles)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_articles_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **articles** | [**ArticlesCreator**](ArticlesCreator.md)| Articles List | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_author_delete**
> private_collection_author_delete(collection_id, author_id)

Delete collection author

Delete collection author

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
author_id = 789 # int | Collection Author unique identifier

try: 
    # Delete collection author
    api_instance.private_collection_author_delete(collection_id, author_id)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_author_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **author_id** | **int**| Collection Author unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_authors_add**
> Location private_collection_authors_add(collection_id, authors)

Add collection authors

Associate new authors with the collection. This will add new authors to the list of already associated authors

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
authors = swagger_client.AuthorsCreator() # AuthorsCreator | List of authors

try: 
    # Add collection authors
    api_response = api_instance.private_collection_authors_add(collection_id, authors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_authors_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **authors** | [**AuthorsCreator**](AuthorsCreator.md)| List of authors | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_authors_list**
> list[Author] private_collection_authors_list(collection_id)

List collection authors

List collection authors

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier

try: 
    # List collection authors
    api_response = api_instance.private_collection_authors_list(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_authors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 

### Return type

[**list[Author]**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_authors_replace**
> private_collection_authors_replace(collection_id, authors)

Replace collection authors

Associate new authors with the collection. This will remove all already associated authors and add these new ones

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
authors = swagger_client.AuthorsCreator() # AuthorsCreator | List of authors

try: 
    # Replace collection authors
    api_instance.private_collection_authors_replace(collection_id, authors)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_authors_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **authors** | [**AuthorsCreator**](AuthorsCreator.md)| List of authors | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_categories_add**
> Location private_collection_categories_add(collection_id, categories)

Add collection categories

Associate new categories with the collection. This will add new categories to the list of already associated categories

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
categories = swagger_client.CategoriesCreator() # CategoriesCreator | Categories list

try: 
    # Add collection categories
    api_response = api_instance.private_collection_categories_add(collection_id, categories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_categories_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **categories** | [**CategoriesCreator**](CategoriesCreator.md)| Categories list | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_categories_list**
> list[Category] private_collection_categories_list(collection_id)

List collection categories

List collection categories

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier

try: 
    # List collection categories
    api_response = api_instance.private_collection_categories_list(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_categories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 

### Return type

[**list[Category]**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_categories_replace**
> private_collection_categories_replace(collection_id, categories)

Replace collection categories

Associate new categories with the collection. This will remove all already associated categories and add these new ones

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
categories = swagger_client.CategoriesCreator() # CategoriesCreator | Categories list

try: 
    # Replace collection categories
    api_instance.private_collection_categories_replace(collection_id, categories)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_categories_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **categories** | [**CategoriesCreator**](CategoriesCreator.md)| Categories list | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_category_delete**
> private_collection_category_delete(collection_id, category_id)

Delete collection category

De-associate category from collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
category_id = 789 # int | Collection category unique identifier

try: 
    # Delete collection category
    api_instance.private_collection_category_delete(collection_id, category_id)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_category_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **category_id** | **int**| Collection category unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_create**
> LocationWarnings private_collection_create(collection)

Create collection

Create a new Collection by sending collection information

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
api_instance = swagger_client.CollectionsApi()
collection = swagger_client.CollectionCreate() # CollectionCreate | Collection description

try: 
    # Create collection
    api_response = api_instance.private_collection_create(collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | [**CollectionCreate**](CollectionCreate.md)| Collection description | 

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_delete**
> private_collection_delete(collection_id)

Delete collection

Delete n collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Delete collection
    api_instance.private_collection_delete(collection_id)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_details**
> CollectionCompletePrivate private_collection_details(collection_id)

Collection details

View a collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Collection details
    api_response = api_instance.private_collection_details(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

[**CollectionCompletePrivate**](CollectionCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_private_link_create**
> PrivateLinkResponse private_collection_private_link_create(collection_id, private_link=private_link)

Create collection private link

Create new private link

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
private_link = swagger_client.CollectionPrivateLinkCreator() # CollectionPrivateLinkCreator |  (optional)

try: 
    # Create collection private link
    api_response = api_instance.private_collection_private_link_create(collection_id, private_link=private_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_private_link_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **private_link** | [**CollectionPrivateLinkCreator**](CollectionPrivateLinkCreator.md)|  | [optional] 

### Return type

[**PrivateLinkResponse**](PrivateLinkResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_private_link_delete**
> private_collection_private_link_delete(collection_id, link_id)

Disable private link

Disable/delete private link for this collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
link_id = 'link_id_example' # str | Private link token

try: 
    # Disable private link
    api_instance.private_collection_private_link_delete(collection_id, link_id)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_private_link_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **link_id** | **str**| Private link token | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_private_link_update**
> private_collection_private_link_update(collection_id, link_id, private_link=private_link)

Update collection private link

Update existing private link for this collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
link_id = 'link_id_example' # str | Private link token
private_link = swagger_client.CollectionPrivateLinkCreator() # CollectionPrivateLinkCreator |  (optional)

try: 
    # Update collection private link
    api_instance.private_collection_private_link_update(collection_id, link_id, private_link=private_link)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_private_link_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **link_id** | **str**| Private link token | 
 **private_link** | [**CollectionPrivateLinkCreator**](CollectionPrivateLinkCreator.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_private_links_list**
> list[PrivateLink] private_collection_private_links_list(collection_id)

List collection private links

List article private links

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier

try: 
    # List collection private links
    api_response = api_instance.private_collection_private_links_list(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_private_links_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 

### Return type

[**list[PrivateLink]**](PrivateLink.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_publish**
> Location private_collection_publish(collection_id)

Private Collection Publish

When a collection is published, a new public version will be generated. Any further updates to the collection will affect the private collection data. In order to make these changes publicly visible, an explicit publish operation is needed.

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Private Collection Publish
    api_response = api_instance.private_collection_publish(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_reserve_doi**
> CollectionDOI private_collection_reserve_doi(collection_id)

Private Collection Reserve DOI

Reserve DOI for collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Private Collection Reserve DOI
    api_response = api_instance.private_collection_reserve_doi(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_reserve_doi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

[**CollectionDOI**](CollectionDOI.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_reserve_handle**
> CollectionHandle private_collection_reserve_handle(collection_id)

Private Collection Reserve Handle

Reserve Handle for collection

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier

try: 
    # Private Collection Reserve Handle
    api_response = api_instance.private_collection_reserve_handle(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_reserve_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 

### Return type

[**CollectionHandle**](CollectionHandle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_resource**
> Location private_collection_resource(collection_id, resource)

Private Collection Resource

Edit collection resource data.

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection unique identifier
resource = swagger_client.Resource() # Resource | Resource data

try: 
    # Private Collection Resource
    api_response = api_instance.private_collection_resource(collection_id, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection unique identifier | 
 **resource** | [**Resource**](Resource.md)| Resource data | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collection_update**
> LocationWarningsUpdate private_collection_update(collection_id, collection)

Update collection

Update collection details; request can also be made with the PATCH method.

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
api_instance = swagger_client.CollectionsApi()
collection_id = 789 # int | Collection Unique identifier
collection = swagger_client.CollectionUpdate() # CollectionUpdate | Collection description

try: 
    # Update collection
    api_response = api_instance.private_collection_update(collection_id, collection)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collection_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **int**| Collection Unique identifier | 
 **collection** | [**CollectionUpdate**](CollectionUpdate.md)| Collection description | 

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collections_list**
> list[Collection] private_collections_list(page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction)

Private Collections List

List private collections

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
api_instance = swagger_client.CollectionsApi()
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
order = 'published_date' # str | The field by which to order. Default varies by endpoint/resource. (optional) (default to published_date)
order_direction = 'desc' # str |  (optional) (default to desc)

try: 
    # Private Collections List
    api_response = api_instance.private_collections_list(page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collections_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **str**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to published_date]
 **order_direction** | **str**|  | [optional] [default to desc]

### Return type

[**list[Collection]**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_collections_search**
> list[Collection] private_collections_search(search)

Private Collections Search

Returns a list of private Collections

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
api_instance = swagger_client.CollectionsApi()
search = swagger_client.PrivateCollectionSearch() # PrivateCollectionSearch | Search Parameters

try: 
    # Private Collections Search
    api_response = api_instance.private_collections_search(search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->private_collections_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**PrivateCollectionSearch**](PrivateCollectionSearch.md)| Search Parameters | 

### Return type

[**list[Collection]**](Collection.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

