# swagger_client.ArticlesApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_article_report**](ArticlesApi.md#account_article_report) | **GET** /account/articles/export | Account Article Report
[**account_article_report_generate**](ArticlesApi.md#account_article_report_generate) | **POST** /account/articles/export | Initiate a new Report
[**article_details**](ArticlesApi.md#article_details) | **GET** /articles/{article_id} | View article details
[**article_file_details**](ArticlesApi.md#article_file_details) | **GET** /articles/{article_id}/files/{file_id} | Article file details
[**article_files**](ArticlesApi.md#article_files) | **GET** /articles/{article_id}/files | List article files
[**article_version_confidentiality**](ArticlesApi.md#article_version_confidentiality) | **GET** /articles/{article_id}/versions/{v_number}/confidentiality | Public Article Confidentiality for article version
[**article_version_details**](ArticlesApi.md#article_version_details) | **GET** /articles/{article_id}/versions/{v_number} | Article details for version
[**article_version_embargo**](ArticlesApi.md#article_version_embargo) | **GET** /articles/{article_id}/versions/{v_number}/embargo | Public Article Embargo for article version
[**article_version_update**](ArticlesApi.md#article_version_update) | **PUT** /account/articles/{article_id}/versions/{version_id}/ | Update article version
[**article_version_update_thumb**](ArticlesApi.md#article_version_update_thumb) | **PUT** /account/articles/{article_id}/versions/{version_id}/update_thumb | Update article version thumbnail
[**article_versions**](ArticlesApi.md#article_versions) | **GET** /articles/{article_id}/versions | List article versions
[**articles_list**](ArticlesApi.md#articles_list) | **GET** /articles | Public Articles
[**articles_search**](ArticlesApi.md#articles_search) | **POST** /articles/search | Public Articles Search
[**private_article_author_delete**](ArticlesApi.md#private_article_author_delete) | **DELETE** /account/articles/{article_id}/authors/{author_id} | Delete article author
[**private_article_authors_add**](ArticlesApi.md#private_article_authors_add) | **POST** /account/articles/{article_id}/authors | Add article authors
[**private_article_authors_list**](ArticlesApi.md#private_article_authors_list) | **GET** /account/articles/{article_id}/authors | List article authors
[**private_article_authors_replace**](ArticlesApi.md#private_article_authors_replace) | **PUT** /account/articles/{article_id}/authors | Replace article authors
[**private_article_categories_add**](ArticlesApi.md#private_article_categories_add) | **POST** /account/articles/{article_id}/categories | Add article categories
[**private_article_categories_list**](ArticlesApi.md#private_article_categories_list) | **GET** /account/articles/{article_id}/categories | List article categories
[**private_article_categories_replace**](ArticlesApi.md#private_article_categories_replace) | **PUT** /account/articles/{article_id}/categories | Replace article categories
[**private_article_category_delete**](ArticlesApi.md#private_article_category_delete) | **DELETE** /account/articles/{article_id}/categories/{category_id} | Delete article category
[**private_article_confidentiality_delete**](ArticlesApi.md#private_article_confidentiality_delete) | **DELETE** /account/articles/{article_id}/confidentiality | Delete article confidentiality
[**private_article_confidentiality_details**](ArticlesApi.md#private_article_confidentiality_details) | **GET** /account/articles/{article_id}/confidentiality | Article confidentiality details
[**private_article_confidentiality_update**](ArticlesApi.md#private_article_confidentiality_update) | **PUT** /account/articles/{article_id}/confidentiality | Update article confidentiality
[**private_article_create**](ArticlesApi.md#private_article_create) | **POST** /account/articles | Create new Article
[**private_article_delete**](ArticlesApi.md#private_article_delete) | **DELETE** /account/articles/{article_id} | Delete article
[**private_article_details**](ArticlesApi.md#private_article_details) | **GET** /account/articles/{article_id} | Article details
[**private_article_embargo_delete**](ArticlesApi.md#private_article_embargo_delete) | **DELETE** /account/articles/{article_id}/embargo | Delete Article Embargo
[**private_article_embargo_details**](ArticlesApi.md#private_article_embargo_details) | **GET** /account/articles/{article_id}/embargo | Article Embargo Details
[**private_article_embargo_update**](ArticlesApi.md#private_article_embargo_update) | **PUT** /account/articles/{article_id}/embargo | Update Article Embargo
[**private_article_file**](ArticlesApi.md#private_article_file) | **GET** /account/articles/{article_id}/files/{file_id} | Single File
[**private_article_file_delete**](ArticlesApi.md#private_article_file_delete) | **DELETE** /account/articles/{article_id}/files/{file_id} | File Delete
[**private_article_files_list**](ArticlesApi.md#private_article_files_list) | **GET** /account/articles/{article_id}/files | List article files
[**private_article_private_link**](ArticlesApi.md#private_article_private_link) | **GET** /account/articles/{article_id}/private_links | List private links
[**private_article_private_link_create**](ArticlesApi.md#private_article_private_link_create) | **POST** /account/articles/{article_id}/private_links | Create private link
[**private_article_private_link_delete**](ArticlesApi.md#private_article_private_link_delete) | **DELETE** /account/articles/{article_id}/private_links/{link_id} | Disable private link
[**private_article_private_link_update**](ArticlesApi.md#private_article_private_link_update) | **PUT** /account/articles/{article_id}/private_links/{link_id} | Update private link
[**private_article_publish**](ArticlesApi.md#private_article_publish) | **POST** /account/articles/{article_id}/publish | Private Article Publish
[**private_article_reserve_doi**](ArticlesApi.md#private_article_reserve_doi) | **POST** /account/articles/{article_id}/reserve_doi | Private Article Reserve DOI
[**private_article_reserve_handle**](ArticlesApi.md#private_article_reserve_handle) | **POST** /account/articles/{article_id}/reserve_handle | Private Article Reserve Handle
[**private_article_resource**](ArticlesApi.md#private_article_resource) | **POST** /account/articles/{article_id}/resource | Private Article Resource
[**private_article_update**](ArticlesApi.md#private_article_update) | **PUT** /account/articles/{article_id} | Update article
[**private_article_upload_complete**](ArticlesApi.md#private_article_upload_complete) | **POST** /account/articles/{article_id}/files/{file_id} | Complete Upload
[**private_article_upload_initiate**](ArticlesApi.md#private_article_upload_initiate) | **POST** /account/articles/{article_id}/files | Initiate Upload
[**private_articles_list**](ArticlesApi.md#private_articles_list) | **GET** /account/articles | Private Articles
[**private_articles_search**](ArticlesApi.md#private_articles_search) | **POST** /account/articles/search | Private Articles search


# **account_article_report**
> list[AccountReport] account_article_report(group_id=group_id)

Account Article Report

Return status on all reports generated for the account from the oauth credentials

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
api_instance = swagger_client.ArticlesApi()
group_id = 789 # int | A group ID to filter by (optional)

try: 
    # Account Article Report
    api_response = api_instance.account_article_report(group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->account_article_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| A group ID to filter by | [optional] 

### Return type

[**list[AccountReport]**](AccountReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_article_report_generate**
> AccountReport account_article_report_generate()

Initiate a new Report

Initiate a new Article Report for this Account. There is a limit of 1 report per day.

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
api_instance = swagger_client.ArticlesApi()

try: 
    # Initiate a new Report
    api_response = api_instance.account_article_report_generate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->account_article_report_generate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountReport**](AccountReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_details**
> ArticleComplete article_details(article_id)

View article details

View an article

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier

try: 
    # View article details
    api_response = api_instance.article_details(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 

### Return type

[**ArticleComplete**](ArticleComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_file_details**
> PublicFile article_file_details(article_id, file_id)

Article file details

File by id

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier
file_id = 789 # int | File Unique identifier

try: 
    # Article file details
    api_response = api_instance.article_file_details(article_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_file_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 
 **file_id** | **int**| File Unique identifier | 

### Return type

[**PublicFile**](PublicFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_files**
> list[PublicFile] article_files(article_id)

List article files

Files list for article

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier

try: 
    # List article files
    api_response = api_instance.article_files(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 

### Return type

[**list[PublicFile]**](PublicFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_version_confidentiality**
> ArticleConfidentiality article_version_confidentiality(article_id, v_number)

Public Article Confidentiality for article version

Confidentiality for article version. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier
v_number = 789 # int | Version Number

try: 
    # Public Article Confidentiality for article version
    api_response = api_instance.article_version_confidentiality(article_id, v_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_version_confidentiality: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 
 **v_number** | **int**| Version Number | 

### Return type

[**ArticleConfidentiality**](ArticleConfidentiality.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_version_details**
> ArticleComplete article_version_details(article_id, v_number)

Article details for version

Article with specified version

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier
v_number = 789 # int | Article Version Number

try: 
    # Article details for version
    api_response = api_instance.article_version_details(article_id, v_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_version_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 
 **v_number** | **int**| Article Version Number | 

### Return type

[**ArticleComplete**](ArticleComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_version_embargo**
> ArticleEmbargo article_version_embargo(article_id, v_number)

Public Article Embargo for article version

Embargo for article version

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier
v_number = 789 # int | Version Number

try: 
    # Public Article Embargo for article version
    api_response = api_instance.article_version_embargo(article_id, v_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_version_embargo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 
 **v_number** | **int**| Version Number | 

### Return type

[**ArticleEmbargo**](ArticleEmbargo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_version_update**
> LocationWarningsUpdate article_version_update(article_id, version_id, article)

Update article version

Updating an article version by passing body parameters; request can also be made with the PATCH method.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
version_id = 789 # int | Article version identifier
article = swagger_client.ArticleUpdate() # ArticleUpdate | Article description

try: 
    # Update article version
    api_response = api_instance.article_version_update(article_id, version_id, article)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_version_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **version_id** | **int**| Article version identifier | 
 **article** | [**ArticleUpdate**](ArticleUpdate.md)| Article description | 

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_version_update_thumb**
> article_version_update_thumb(article_id, version_id, file_id)

Update article version thumbnail

For a given public article version update the article thumbnail by choosing one of the associated files

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
version_id = 789 # int | Article version identifier
file_id = swagger_client.FileId() # FileId | File ID

try: 
    # Update article version thumbnail
    api_instance.article_version_update_thumb(article_id, version_id, file_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_version_update_thumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **version_id** | **int**| Article version identifier | 
 **file_id** | [**FileId**](FileId.md)| File ID | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **article_versions**
> list[ArticleVersions] article_versions(article_id)

List article versions

List public article versions

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article Unique identifier

try: 
    # List article versions
    api_response = api_instance.article_versions(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->article_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article Unique identifier | 

### Return type

[**list[ArticleVersions]**](ArticleVersions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **articles_list**
> list[Article] articles_list(x_cursor=x_cursor, page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, institution=institution, published_since=published_since, modified_since=modified_since, group=group, resource_doi=resource_doi, item_type=item_type, doi=doi, handle=handle)

Public Articles

Returns a list of public articles

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
x_cursor = 'x_cursor_example' # str | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. (optional)
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
order = 'published_date' # str | The field by which to order. Default varies by endpoint/resource. (optional) (default to published_date)
order_direction = 'desc' # str |  (optional) (default to desc)
institution = 789 # int | only return articles from this institution (optional)
published_since = 'published_since_example' # str | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD (optional)
modified_since = 'modified_since_example' # str | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD (optional)
group = 789 # int | only return articles from this group (optional)
resource_doi = 'resource_doi_example' # str | only return articles with this resource_doi (optional)
item_type = 789 # int | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model (optional)
doi = 'doi_example' # str | only return articles with this doi (optional)
handle = 'handle_example' # str | only return articles with this handle (optional)

try: 
    # Public Articles
    api_response = api_instance.articles_list(x_cursor=x_cursor, page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, institution=institution, published_since=published_since, modified_since=modified_since, group=group, resource_doi=resource_doi, item_type=item_type, doi=doi, handle=handle)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->articles_list: %s\n" % e)
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
 **institution** | **int**| only return articles from this institution | [optional] 
 **published_since** | **str**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **modified_since** | **str**| Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **group** | **int**| only return articles from this group | [optional] 
 **resource_doi** | **str**| only return articles with this resource_doi | [optional] 
 **item_type** | **int**| Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] 
 **doi** | **str**| only return articles with this doi | [optional] 
 **handle** | **str**| only return articles with this handle | [optional] 

### Return type

[**list[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **articles_search**
> list[ArticleWithProject] articles_search(x_cursor=x_cursor, search=search)

Public Articles Search

Returns a list of public articles, filtered by the search parameters

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArticlesApi()
x_cursor = 'x_cursor_example' # str | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. (optional)
search = swagger_client.ArticleSearch() # ArticleSearch | Search Parameters (optional)

try: 
    # Public Articles Search
    api_response = api_instance.articles_search(x_cursor=x_cursor, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->articles_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_cursor** | **str**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **search** | [**ArticleSearch**](ArticleSearch.md)| Search Parameters | [optional] 

### Return type

[**list[ArticleWithProject]**](ArticleWithProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_author_delete**
> private_article_author_delete(article_id, author_id)

Delete article author

De-associate author from article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
author_id = 789 # int | Article Author unique identifier

try: 
    # Delete article author
    api_instance.private_article_author_delete(article_id, author_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_author_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **author_id** | **int**| Article Author unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_authors_add**
> private_article_authors_add(article_id, authors)

Add article authors

Associate new authors with the article. This will add new authors to the list of already associated authors

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
authors = swagger_client.AuthorsCreator() # AuthorsCreator | Authors description

try: 
    # Add article authors
    api_instance.private_article_authors_add(article_id, authors)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_authors_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **authors** | [**AuthorsCreator**](AuthorsCreator.md)| Authors description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_authors_list**
> list[Author] private_article_authors_list(article_id)

List article authors

List article authors

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # List article authors
    api_response = api_instance.private_article_authors_list(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_authors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**list[Author]**](Author.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_authors_replace**
> private_article_authors_replace(article_id, authors)

Replace article authors

Associate new authors with the article. This will remove all already associated authors and add these new ones

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
authors = swagger_client.AuthorsCreator() # AuthorsCreator | Authors description

try: 
    # Replace article authors
    api_instance.private_article_authors_replace(article_id, authors)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_authors_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **authors** | [**AuthorsCreator**](AuthorsCreator.md)| Authors description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_categories_add**
> private_article_categories_add(article_id, categories)

Add article categories

Associate new categories with the article. This will add new categories to the list of already associated categories

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
categories = swagger_client.CategoriesCreator() # CategoriesCreator | 

try: 
    # Add article categories
    api_instance.private_article_categories_add(article_id, categories)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_categories_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **categories** | [**CategoriesCreator**](CategoriesCreator.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_categories_list**
> list[Category] private_article_categories_list(article_id)

List article categories

List article categories

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # List article categories
    api_response = api_instance.private_article_categories_list(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_categories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**list[Category]**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_categories_replace**
> private_article_categories_replace(article_id, categories)

Replace article categories

Associate new categories with the article. This will remove all already associated categories and add these new ones

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
categories = swagger_client.CategoriesCreator() # CategoriesCreator | 

try: 
    # Replace article categories
    api_instance.private_article_categories_replace(article_id, categories)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_categories_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **categories** | [**CategoriesCreator**](CategoriesCreator.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_category_delete**
> private_article_category_delete(article_id, category_id)

Delete article category

De-associate category from article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
category_id = 789 # int | Category unique identifier

try: 
    # Delete article category
    api_instance.private_article_category_delete(article_id, category_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_category_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **category_id** | **int**| Category unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_confidentiality_delete**
> private_article_confidentiality_delete(article_id)

Delete article confidentiality

Delete confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Delete article confidentiality
    api_instance.private_article_confidentiality_delete(article_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_confidentiality_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_confidentiality_details**
> ArticleConfidentiality private_article_confidentiality_details(article_id)

Article confidentiality details

View confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Article confidentiality details
    api_response = api_instance.private_article_confidentiality_details(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_confidentiality_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**ArticleConfidentiality**](ArticleConfidentiality.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_confidentiality_update**
> private_article_confidentiality_update(article_id, reason)

Update article confidentiality

Update confidentiality settings. The confidentiality feature is now deprecated. This has been replaced by the new extended embargo functionality and all items that used to be confidential have now been migrated to items with a permanent embargo on files. All API endpoints related to this functionality will remain for backwards compatibility, but will now be attached to the new extended embargo workflows.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
reason = swagger_client.ConfidentialityCreator() # ConfidentialityCreator | 

try: 
    # Update article confidentiality
    api_instance.private_article_confidentiality_update(article_id, reason)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_confidentiality_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **reason** | [**ConfidentialityCreator**](ConfidentialityCreator.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_create**
> LocationWarnings private_article_create(article)

Create new Article

Create a new Article by sending article information

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
api_instance = swagger_client.ArticlesApi()
article = swagger_client.ArticleCreate() # ArticleCreate | Article description

try: 
    # Create new Article
    api_response = api_instance.private_article_create(article)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article** | [**ArticleCreate**](ArticleCreate.md)| Article description | 

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_delete**
> private_article_delete(article_id)

Delete article

Delete an article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Delete article
    api_instance.private_article_delete(article_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_details**
> ArticleCompletePrivate private_article_details(article_id)

Article details

View a private article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Article details
    api_response = api_instance.private_article_details(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**ArticleCompletePrivate**](ArticleCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_embargo_delete**
> private_article_embargo_delete(article_id)

Delete Article Embargo

Will lift the embargo for the specified article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Delete Article Embargo
    api_instance.private_article_embargo_delete(article_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_embargo_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_embargo_details**
> ArticleEmbargo private_article_embargo_details(article_id)

Article Embargo Details

View a private article embargo details

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Article Embargo Details
    api_response = api_instance.private_article_embargo_details(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_embargo_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**ArticleEmbargo**](ArticleEmbargo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_embargo_update**
> private_article_embargo_update(article_id, embargo)

Update Article Embargo

Note: setting an article under whole embargo does not imply that the article will be published when the embargo will expire. You must explicitly call the publish endpoint to enable this functionality.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
embargo = swagger_client.ArticleEmbargoUpdater() # ArticleEmbargoUpdater | Embargo description

try: 
    # Update Article Embargo
    api_instance.private_article_embargo_update(article_id, embargo)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_embargo_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **embargo** | [**ArticleEmbargoUpdater**](ArticleEmbargoUpdater.md)| Embargo description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_file**
> PrivateFile private_article_file(article_id, file_id)

Single File

View details of file for specified article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
file_id = 789 # int | File unique identifier

try: 
    # Single File
    api_response = api_instance.private_article_file(article_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **file_id** | **int**| File unique identifier | 

### Return type

[**PrivateFile**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_file_delete**
> private_article_file_delete(article_id, file_id)

File Delete

Complete file upload

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
file_id = 789 # int | File unique identifier

try: 
    # File Delete
    api_instance.private_article_file_delete(article_id, file_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_file_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **file_id** | **int**| File unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_files_list**
> list[PrivateFile] private_article_files_list(article_id)

List article files

List private files

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # List article files
    api_response = api_instance.private_article_files_list(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**list[PrivateFile]**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_private_link**
> list[PrivateLink] private_article_private_link(article_id)

List private links

List private links

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # List private links
    api_response = api_instance.private_article_private_link(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_private_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**list[PrivateLink]**](PrivateLink.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_private_link_create**
> PrivateLinkResponse private_article_private_link_create(article_id, private_link=private_link)

Create private link

Create new private link for this article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
private_link = swagger_client.PrivateLinkCreator() # PrivateLinkCreator |  (optional)

try: 
    # Create private link
    api_response = api_instance.private_article_private_link_create(article_id, private_link=private_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_private_link_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **private_link** | [**PrivateLinkCreator**](PrivateLinkCreator.md)|  | [optional] 

### Return type

[**PrivateLinkResponse**](PrivateLinkResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_private_link_delete**
> private_article_private_link_delete(article_id, link_id)

Disable private link

Disable/delete private link for this article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
link_id = 'link_id_example' # str | Private link token

try: 
    # Disable private link
    api_instance.private_article_private_link_delete(article_id, link_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_private_link_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **link_id** | **str**| Private link token | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_private_link_update**
> private_article_private_link_update(article_id, link_id, private_link=private_link)

Update private link

Update existing private link for this article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
link_id = 'link_id_example' # str | Private link token
private_link = swagger_client.PrivateLinkCreator() # PrivateLinkCreator |  (optional)

try: 
    # Update private link
    api_instance.private_article_private_link_update(article_id, link_id, private_link=private_link)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_private_link_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **link_id** | **str**| Private link token | 
 **private_link** | [**PrivateLinkCreator**](PrivateLinkCreator.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_publish**
> Location private_article_publish(article_id)

Private Article Publish

- If the whole article is under embargo, it will not be published immediately, but when the embargo expires or is lifted. - When an article is published, a new public version will be generated. Any further updates to the article will affect the private article data. In order to make these changes publicly visible, an explicit publish operation is needed.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Private Article Publish
    api_response = api_instance.private_article_publish(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_reserve_doi**
> ArticleDOI private_article_reserve_doi(article_id)

Private Article Reserve DOI

Reserve DOI for article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Private Article Reserve DOI
    api_response = api_instance.private_article_reserve_doi(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_reserve_doi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**ArticleDOI**](ArticleDOI.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_reserve_handle**
> ArticleHandle private_article_reserve_handle(article_id)

Private Article Reserve Handle

Reserve Handle for article

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier

try: 
    # Private Article Reserve Handle
    api_response = api_instance.private_article_reserve_handle(article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_reserve_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 

### Return type

[**ArticleHandle**](ArticleHandle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_resource**
> Location private_article_resource(article_id, resource)

Private Article Resource

Edit article resource data.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
resource = swagger_client.Resource() # Resource | Resource data

try: 
    # Private Article Resource
    api_response = api_instance.private_article_resource(article_id, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **resource** | [**Resource**](Resource.md)| Resource data | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_update**
> LocationWarningsUpdate private_article_update(article_id, article)

Update article

Updating an article by passing body parameters; request can also be made with the PATCH method.

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
article = swagger_client.ArticleUpdate() # ArticleUpdate | Article description

try: 
    # Update article
    api_response = api_instance.private_article_update(article_id, article)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **article** | [**ArticleUpdate**](ArticleUpdate.md)| Article description | 

### Return type

[**LocationWarningsUpdate**](LocationWarningsUpdate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_upload_complete**
> private_article_upload_complete(article_id, file_id)

Complete Upload

Complete file upload

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
file_id = 789 # int | File unique identifier

try: 
    # Complete Upload
    api_instance.private_article_upload_complete(article_id, file_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_upload_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **file_id** | **int**| File unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_article_upload_initiate**
> Location private_article_upload_initiate(article_id, file)

Initiate Upload

Initiate a new file upload within the article. Either use the link property to point to an existing file that resides elsewhere and will not be uploaded to Figshare or use the other 3 parameters (md5, name, size).

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
api_instance = swagger_client.ArticlesApi()
article_id = 789 # int | Article unique identifier
file = swagger_client.FileCreator() # FileCreator | 

try: 
    # Initiate Upload
    api_response = api_instance.private_article_upload_initiate(article_id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_article_upload_initiate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **article_id** | **int**| Article unique identifier | 
 **file** | [**FileCreator**](FileCreator.md)|  | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_articles_list**
> list[Article] private_articles_list(page=page, page_size=page_size, limit=limit, offset=offset)

Private Articles

Get Own Articles

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
api_instance = swagger_client.ArticlesApi()
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # Private Articles
    api_response = api_instance.private_articles_list(page=page, page_size=page_size, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_articles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **private_articles_search**
> list[ArticleWithProject] private_articles_search(search)

Private Articles search

Returns a list of private articles filtered by the search parameters

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
api_instance = swagger_client.ArticlesApi()
search = swagger_client.PrivateArticleSearch() # PrivateArticleSearch | Search Parameters

try: 
    # Private Articles search
    api_response = api_instance.private_articles_search(search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArticlesApi->private_articles_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**PrivateArticleSearch**](PrivateArticleSearch.md)| Search Parameters | 

### Return type

[**list[ArticleWithProject]**](ArticleWithProject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

