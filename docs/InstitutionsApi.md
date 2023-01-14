# swagger_client.InstitutionsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_institution_curation**](InstitutionsApi.md#account_institution_curation) | **GET** /account/institution/review/{curation_id} | Institution Curation Review
[**account_institution_curation_comments**](InstitutionsApi.md#account_institution_curation_comments) | **GET** /account/institution/review/{curation_id}/comments | Institution Curation Review Comments
[**account_institution_curation_comments_0**](InstitutionsApi.md#account_institution_curation_comments_0) | **POST** /account/institution/review/{curation_id}/comments | POST Institution Curation Review Comment
[**account_institution_curations**](InstitutionsApi.md#account_institution_curations) | **GET** /account/institution/reviews | Institution Curation Reviews
[**custom_fields_list**](InstitutionsApi.md#custom_fields_list) | **GET** /account/institution/custom_fields | Private account institution group custom fields
[**custom_fields_upload**](InstitutionsApi.md#custom_fields_upload) | **POST** /account/institution/custom_fields/{custom_field_id}/items/upload | Custom fields values files upload
[**institution_articles**](InstitutionsApi.md#institution_articles) | **GET** /institutions/{institution_string_id}/articles/filter-by | Public Licenses
[**institution_hrfeed_upload**](InstitutionsApi.md#institution_hrfeed_upload) | **POST** /institution/hrfeed/upload | Private Institution HRfeed Upload
[**private_account_institution_user**](InstitutionsApi.md#private_account_institution_user) | **GET** /account/institution/users/{account_id} | Private Account Institution User
[**private_categories_list**](InstitutionsApi.md#private_categories_list) | **GET** /account/categories | Private Account Categories
[**private_group_embargo_options_details**](InstitutionsApi.md#private_group_embargo_options_details) | **GET** /account/institution/groups/{group_id}/embargo_options | Private Account Institution Group Embargo Options
[**private_institution_account_group_role_delete**](InstitutionsApi.md#private_institution_account_group_role_delete) | **DELETE** /account/institution/roles/{account_id}/{group_id}/{role_id} | Delete Institution Account Group Role
[**private_institution_account_group_roles**](InstitutionsApi.md#private_institution_account_group_roles) | **GET** /account/institution/roles/{account_id} | List Institution Account Group Roles
[**private_institution_account_group_roles_create**](InstitutionsApi.md#private_institution_account_group_roles_create) | **POST** /account/institution/roles/{account_id} | Add Institution Account Group Roles
[**private_institution_accounts_create**](InstitutionsApi.md#private_institution_accounts_create) | **POST** /account/institution/accounts | Create new Institution Account
[**private_institution_accounts_list**](InstitutionsApi.md#private_institution_accounts_list) | **GET** /account/institution/accounts | Private Account Institution Accounts
[**private_institution_accounts_search**](InstitutionsApi.md#private_institution_accounts_search) | **POST** /account/institution/accounts/search | Private Account Institution Accounts Search
[**private_institution_accounts_update**](InstitutionsApi.md#private_institution_accounts_update) | **PUT** /account/institution/accounts/{account_id} | Update Institution Account
[**private_institution_articles**](InstitutionsApi.md#private_institution_articles) | **GET** /account/institution/articles | Private Institution Articles
[**private_institution_details**](InstitutionsApi.md#private_institution_details) | **GET** /account/institution | Private Account Institutions
[**private_institution_embargo_options_details**](InstitutionsApi.md#private_institution_embargo_options_details) | **GET** /account/institution/embargo_options | Private Account Institution embargo options
[**private_institution_groups_list**](InstitutionsApi.md#private_institution_groups_list) | **GET** /account/institution/groups | Private Account Institution Groups
[**private_institution_roles_list**](InstitutionsApi.md#private_institution_roles_list) | **GET** /account/institution/roles | Private Account Institution Roles


# **account_institution_curation**
> CurationDetail account_institution_curation(curation_id)

Institution Curation Review

Retrieve a certain curation review by its ID

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
api_instance = swagger_client.InstitutionsApi()
curation_id = 789 # int | ID of the curation

try: 
    # Institution Curation Review
    api_response = api_instance.account_institution_curation(curation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->account_institution_curation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curation_id** | **int**| ID of the curation | 

### Return type

[**CurationDetail**](CurationDetail.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_institution_curation_comments**
> CurationComment account_institution_curation_comments(curation_id, limit=limit, offset=offset)

Institution Curation Review Comments

Retrieve a certain curation review's comments.

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
api_instance = swagger_client.InstitutionsApi()
curation_id = 789 # int | ID of the curation
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # Institution Curation Review Comments
    api_response = api_instance.account_institution_curation_comments(curation_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->account_institution_curation_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curation_id** | **int**| ID of the curation | 
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**CurationComment**](CurationComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_institution_curation_comments_0**
> account_institution_curation_comments_0(curation_id, curation_comment)

POST Institution Curation Review Comment

Add a new comment to the review.

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
api_instance = swagger_client.InstitutionsApi()
curation_id = 789 # int | ID of the curation
curation_comment = swagger_client.CurationCommentCreate() # CurationCommentCreate | The content/value of the comment.

try: 
    # POST Institution Curation Review Comment
    api_instance.account_institution_curation_comments_0(curation_id, curation_comment)
except ApiException as e:
    print("Exception when calling InstitutionsApi->account_institution_curation_comments_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **curation_id** | **int**| ID of the curation | 
 **curation_comment** | [**CurationCommentCreate**](CurationCommentCreate.md)| The content/value of the comment. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_institution_curations**
> Curation account_institution_curations(group_id=group_id, article_id=article_id, status=status, limit=limit, offset=offset)

Institution Curation Reviews

Retrieve a list of curation reviews for this institution

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
api_instance = swagger_client.InstitutionsApi()
group_id = 789 # int | Filter by the group ID (optional)
article_id = 789 # int | Retrieve the reviews for this article (optional)
status = 'status_example' # str | Filter by the status of the review (optional)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # Institution Curation Reviews
    api_response = api_instance.account_institution_curations(group_id=group_id, article_id=article_id, status=status, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->account_institution_curations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Filter by the group ID | [optional] 
 **article_id** | **int**| Retrieve the reviews for this article | [optional] 
 **status** | **str**| Filter by the status of the review | [optional] 
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**Curation**](Curation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_list**
> list[ShortCustomField] custom_fields_list(group_id=group_id)

Private account institution group custom fields

Returns the custom fields in the group the user belongs to, or the ones in the group specified, if the user has access.

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
api_instance = swagger_client.InstitutionsApi()
group_id = 789 # int | Group_id (optional)

try: 
    # Private account institution group custom fields
    api_response = api_instance.custom_fields_list(group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->custom_fields_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group_id | [optional] 

### Return type

[**list[ShortCustomField]**](ShortCustomField.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_fields_upload**
> object custom_fields_upload(custom_field_id, external_file=external_file)

Custom fields values files upload

Uploads a CSV containing values for a specific custom field of type <b>dropdown_large_list</b>. More details in the <a href=\"#custom_fields\">Custom Fields section</a>

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
api_instance = swagger_client.InstitutionsApi()
custom_field_id = 789 # int | Custom field identifier
external_file = '/path/to/file.txt' # file | CSV file to be uploaded (optional)

try: 
    # Custom fields values files upload
    api_response = api_instance.custom_fields_upload(custom_field_id, external_file=external_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->custom_fields_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_id** | **int**| Custom field identifier | 
 **external_file** | **file**| CSV file to be uploaded | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institution_articles**
> list[Article] institution_articles(institution_string_id, resource_id, filename)

Public Licenses

Returns a list of articles belonging to the institution

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstitutionsApi()
institution_string_id = 'institution_string_id_example' # str | 
resource_id = 'resource_id_example' # str | 
filename = 'filename_example' # str | 

try: 
    # Public Licenses
    api_response = api_instance.institution_articles(institution_string_id, resource_id, filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->institution_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_string_id** | **str**|  | 
 **resource_id** | **str**|  | 
 **filename** | **str**|  | 

### Return type

[**list[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institution_hrfeed_upload**
> ResponseMessage institution_hrfeed_upload(hrfeed=hrfeed)

Private Institution HRfeed Upload

More info in the <a href=\"#hr_feed\">HR Feed section</a>

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
api_instance = swagger_client.InstitutionsApi()
hrfeed = '/path/to/file.txt' # file | You can find an example in the Hr Feed section (optional)

try: 
    # Private Institution HRfeed Upload
    api_response = api_instance.institution_hrfeed_upload(hrfeed=hrfeed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->institution_hrfeed_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hrfeed** | **file**| You can find an example in the Hr Feed section | [optional] 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_account_institution_user**
> User private_account_institution_user(account_id)

Private Account Institution User

Retrieve institution user information using the account_id

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
api_instance = swagger_client.InstitutionsApi()
account_id = 789 # int | Account identifier the user is associated to

try: 
    # Private Account Institution User
    api_response = api_instance.private_account_institution_user(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_account_institution_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account identifier the user is associated to | 

### Return type

[**User**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_categories_list**
> list[Category] private_categories_list()

Private Account Categories

List institution categories (including parent Categories)

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
api_instance = swagger_client.InstitutionsApi()

try: 
    # Private Account Categories
    api_response = api_instance.private_categories_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_categories_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Category]**](Category.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_group_embargo_options_details**
> list[GroupEmbargoOptions] private_group_embargo_options_details(group_id)

Private Account Institution Group Embargo Options

Account institution group embargo options details

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
api_instance = swagger_client.InstitutionsApi()
group_id = 789 # int | Group identifier

try: 
    # Private Account Institution Group Embargo Options
    api_response = api_instance.private_group_embargo_options_details(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_group_embargo_options_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Group identifier | 

### Return type

[**list[GroupEmbargoOptions]**](GroupEmbargoOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_account_group_role_delete**
> private_institution_account_group_role_delete(account_id, group_id, role_id)

Delete Institution Account Group Role

Delete Institution Account Group Role

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
api_instance = swagger_client.InstitutionsApi()
account_id = 789 # int | Account identifier for which to remove the role
group_id = 789 # int | Group identifier for which to remove the role
role_id = 789 # int | Role identifier

try: 
    # Delete Institution Account Group Role
    api_instance.private_institution_account_group_role_delete(account_id, group_id, role_id)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_account_group_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account identifier for which to remove the role | 
 **group_id** | **int**| Group identifier for which to remove the role | 
 **role_id** | **int**| Role identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_account_group_roles**
> AccountGroupRoles private_institution_account_group_roles(account_id)

List Institution Account Group Roles

List Institution Account Group Roles

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
api_instance = swagger_client.InstitutionsApi()
account_id = 789 # int | Account identifier the user is associated to

try: 
    # List Institution Account Group Roles
    api_response = api_instance.private_institution_account_group_roles(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_account_group_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account identifier the user is associated to | 

### Return type

[**AccountGroupRoles**](AccountGroupRoles.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_account_group_roles_create**
> private_institution_account_group_roles_create(account_id, account)

Add Institution Account Group Roles

Add Institution Account Group Roles

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
api_instance = swagger_client.InstitutionsApi()
account_id = 789 # int | Account identifier the user is associated to
account = swagger_client.AccountGroupRolesCreate() # AccountGroupRolesCreate | Account description

try: 
    # Add Institution Account Group Roles
    api_instance.private_institution_account_group_roles_create(account_id, account)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_account_group_roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account identifier the user is associated to | 
 **account** | [**AccountGroupRolesCreate**](AccountGroupRolesCreate.md)| Account description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_accounts_create**
> private_institution_accounts_create(account)

Create new Institution Account

Create a new Account by sending account information

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
api_instance = swagger_client.InstitutionsApi()
account = swagger_client.AccountCreate() # AccountCreate | Account description

try: 
    # Create new Institution Account
    api_instance.private_institution_accounts_create(account)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_accounts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**AccountCreate**](AccountCreate.md)| Account description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_accounts_list**
> list[ShortAccount] private_institution_accounts_list(page=page, page_size=page_size, limit=limit, offset=offset, is_active=is_active, institution_user_id=institution_user_id, email=email, id_lte=id_lte, id_gte=id_gte)

Private Account Institution Accounts

Returns the accounts for which the account has administrative privileges (assigned and inherited).

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
api_instance = swagger_client.InstitutionsApi()
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
is_active = 789 # int | Filter by active status (optional)
institution_user_id = 'institution_user_id_example' # str | Filter by institution_user_id (optional)
email = 'email_example' # str | Filter by email (optional)
id_lte = 789 # int | Retrieve accounts with an ID lower or equal to the specified value (optional)
id_gte = 789 # int | Retrieve accounts with an ID greater or equal to the specified value (optional)

try: 
    # Private Account Institution Accounts
    api_response = api_instance.private_institution_accounts_list(page=page, page_size=page_size, limit=limit, offset=offset, is_active=is_active, institution_user_id=institution_user_id, email=email, id_lte=id_lte, id_gte=id_gte)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_accounts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **is_active** | **int**| Filter by active status | [optional] 
 **institution_user_id** | **str**| Filter by institution_user_id | [optional] 
 **email** | **str**| Filter by email | [optional] 
 **id_lte** | **int**| Retrieve accounts with an ID lower or equal to the specified value | [optional] 
 **id_gte** | **int**| Retrieve accounts with an ID greater or equal to the specified value | [optional] 

### Return type

[**list[ShortAccount]**](ShortAccount.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_accounts_search**
> list[ShortAccount] private_institution_accounts_search(search)

Private Account Institution Accounts Search

Returns the accounts for which the account has administrative privileges (assigned and inherited).

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
api_instance = swagger_client.InstitutionsApi()
search = swagger_client.InstitutionAccountsSearch() # InstitutionAccountsSearch | Search Parameters

try: 
    # Private Account Institution Accounts Search
    api_response = api_instance.private_institution_accounts_search(search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_accounts_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**InstitutionAccountsSearch**](InstitutionAccountsSearch.md)| Search Parameters | 

### Return type

[**list[ShortAccount]**](ShortAccount.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_accounts_update**
> private_institution_accounts_update(account_id, account)

Update Institution Account

Update Institution Account

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
api_instance = swagger_client.InstitutionsApi()
account_id = 789 # int | Account identifier the user is associated to
account = swagger_client.AccountUpdate() # AccountUpdate | Account description

try: 
    # Update Institution Account
    api_instance.private_institution_accounts_update(account_id, account)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_accounts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account identifier the user is associated to | 
 **account** | [**AccountUpdate**](AccountUpdate.md)| Account description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_articles**
> list[Article] private_institution_articles(page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, published_since=published_since, modified_since=modified_since, status=status, resource_doi=resource_doi, item_type=item_type)

Private Institution Articles

Get Articles from own institution. User must be administrator of the institution

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
api_instance = swagger_client.InstitutionsApi()
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
order = 'published_date' # str | The field by which to order. Default varies by endpoint/resource. (optional) (default to published_date)
order_direction = 'desc' # str |  (optional) (default to desc)
published_since = 'published_since_example' # str | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD (optional)
modified_since = 'modified_since_example' # str | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD (optional)
status = 789 # int | only return collections with this status (optional)
resource_doi = 'resource_doi_example' # str | only return collections with this resource_doi (optional)
item_type = 789 # int | Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model (optional)

try: 
    # Private Institution Articles
    api_response = api_instance.private_institution_articles(page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, published_since=published_since, modified_since=modified_since, status=status, resource_doi=resource_doi, item_type=item_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_articles: %s\n" % e)
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
 **published_since** | **str**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **modified_since** | **str**| Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **status** | **int**| only return collections with this status | [optional] 
 **resource_doi** | **str**| only return collections with this resource_doi | [optional] 
 **item_type** | **int**| Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model | [optional] 

### Return type

[**list[Article]**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_details**
> Institution private_institution_details()

Private Account Institutions

Account institution details

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
api_instance = swagger_client.InstitutionsApi()

try: 
    # Private Account Institutions
    api_response = api_instance.private_institution_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Institution**](Institution.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_embargo_options_details**
> list[GroupEmbargoOptions] private_institution_embargo_options_details()

Private Account Institution embargo options

Account institution embargo options details

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
api_instance = swagger_client.InstitutionsApi()

try: 
    # Private Account Institution embargo options
    api_response = api_instance.private_institution_embargo_options_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_embargo_options_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GroupEmbargoOptions]**](GroupEmbargoOptions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_groups_list**
> list[Group] private_institution_groups_list()

Private Account Institution Groups

Returns the groups for which the account has administrative privileges (assigned and inherited).

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
api_instance = swagger_client.InstitutionsApi()

try: 
    # Private Account Institution Groups
    api_response = api_instance.private_institution_groups_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_groups_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Group]**](Group.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_institution_roles_list**
> list[Role] private_institution_roles_list()

Private Account Institution Roles

Returns the roles available for groups and the institution group.

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
api_instance = swagger_client.InstitutionsApi()

try: 
    # Private Account Institution Roles
    api_response = api_instance.private_institution_roles_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstitutionsApi->private_institution_roles_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Role]**](Role.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

