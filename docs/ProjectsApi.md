# swagger_client.ProjectsApi

All URIs are relative to *https://api.figshare.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_project_article_delete**](ProjectsApi.md#private_project_article_delete) | **DELETE** /account/projects/{project_id}/articles/{article_id} | Delete project article
[**private_project_article_details**](ProjectsApi.md#private_project_article_details) | **GET** /account/projects/{project_id}/articles/{article_id} | Project article details
[**private_project_article_file**](ProjectsApi.md#private_project_article_file) | **GET** /account/projects/{project_id}/articles/{article_id}/files/{file_id} | Project article file details
[**private_project_article_files**](ProjectsApi.md#private_project_article_files) | **GET** /account/projects/{project_id}/articles/{article_id}/files | Project article list files
[**private_project_articles_create**](ProjectsApi.md#private_project_articles_create) | **POST** /account/projects/{project_id}/articles | Create project article
[**private_project_articles_list**](ProjectsApi.md#private_project_articles_list) | **GET** /account/projects/{project_id}/articles | List project articles
[**private_project_collaborator_delete**](ProjectsApi.md#private_project_collaborator_delete) | **DELETE** /account/projects/{project_id}/collaborators/{user_id} | Remove project collaborator
[**private_project_collaborators_invite**](ProjectsApi.md#private_project_collaborators_invite) | **POST** /account/projects/{project_id}/collaborators | Invite project collaborators
[**private_project_collaborators_list**](ProjectsApi.md#private_project_collaborators_list) | **GET** /account/projects/{project_id}/collaborators | List project collaborators
[**private_project_create**](ProjectsApi.md#private_project_create) | **POST** /account/projects | Create project
[**private_project_delete**](ProjectsApi.md#private_project_delete) | **DELETE** /account/projects/{project_id} | Delete project
[**private_project_details**](ProjectsApi.md#private_project_details) | **GET** /account/projects/{project_id} | View project details
[**private_project_leave**](ProjectsApi.md#private_project_leave) | **POST** /account/projects/{project_id}/leave | Private Project Leave
[**private_project_note**](ProjectsApi.md#private_project_note) | **GET** /account/projects/{project_id}/notes/{note_id} | Project note details
[**private_project_note_delete**](ProjectsApi.md#private_project_note_delete) | **DELETE** /account/projects/{project_id}/notes/{note_id} | Delete project note
[**private_project_note_update**](ProjectsApi.md#private_project_note_update) | **PUT** /account/projects/{project_id}/notes/{note_id} | Update project note
[**private_project_notes_create**](ProjectsApi.md#private_project_notes_create) | **POST** /account/projects/{project_id}/notes | Create project note
[**private_project_notes_list**](ProjectsApi.md#private_project_notes_list) | **GET** /account/projects/{project_id}/notes | List project notes
[**private_project_publish**](ProjectsApi.md#private_project_publish) | **POST** /account/projects/{project_id}/publish | Private Project Publish
[**private_project_update**](ProjectsApi.md#private_project_update) | **PUT** /account/projects/{project_id} | Update project
[**private_projects_list**](ProjectsApi.md#private_projects_list) | **GET** /account/projects | Private Projects
[**private_projects_search**](ProjectsApi.md#private_projects_search) | **POST** /account/projects/search | Private Projects search
[**project_articles**](ProjectsApi.md#project_articles) | **GET** /projects/{project_id}/articles | Public Project Articles
[**project_details**](ProjectsApi.md#project_details) | **GET** /projects/{project_id} | Public Project
[**projects_list**](ProjectsApi.md#projects_list) | **GET** /projects | Public Projects
[**projects_search**](ProjectsApi.md#projects_search) | **POST** /projects/search | Public Projects Search


# **private_project_article_delete**
> private_project_article_delete(project_id, article_id)

Delete project article

Delete project article

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
article_id = 789 # int | Project Article unique identifier

try: 
    # Delete project article
    api_instance.private_project_article_delete(project_id, article_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_article_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **article_id** | **int**| Project Article unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_article_details**
> ProjectArticle private_project_article_details(project_id, article_id)

Project article details

Project article details

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
article_id = 789 # int | Project Article unique identifier

try: 
    # Project article details
    api_response = api_instance.private_project_article_details(project_id, article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_article_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **article_id** | **int**| Project Article unique identifier | 

### Return type

[**ProjectArticle**](ProjectArticle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_article_file**
> PrivateFile private_project_article_file(project_id, article_id, file_id)

Project article file details

Project article file details

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
article_id = 789 # int | Project Article unique identifier
file_id = 789 # int | File unique identifier

try: 
    # Project article file details
    api_response = api_instance.private_project_article_file(project_id, article_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_article_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **article_id** | **int**| Project Article unique identifier | 
 **file_id** | **int**| File unique identifier | 

### Return type

[**PrivateFile**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_article_files**
> list[PrivateFile] private_project_article_files(project_id, article_id)

Project article list files

List article files

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
article_id = 789 # int | Project Article unique identifier

try: 
    # Project article list files
    api_response = api_instance.private_project_article_files(project_id, article_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_article_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **article_id** | **int**| Project Article unique identifier | 

### Return type

[**list[PrivateFile]**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_articles_create**
> LocationWarnings private_project_articles_create(project_id, article, page=page, page_size=page_size, limit=limit, offset=offset)

Create project article

Create a new Article and associate it with this project

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
article = swagger_client.ArticleProjectCreate() # ArticleProjectCreate | Article description
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # Create project article
    api_response = api_instance.private_project_articles_create(project_id, article, page=page, page_size=page_size, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_articles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **article** | [**ArticleProjectCreate**](ArticleProjectCreate.md)| Article description | 
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_articles_list**
> list[Article] private_project_articles_list(project_id, page=page, page_size=page_size, limit=limit, offset=offset)

List project articles

List project articles

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # List project articles
    api_response = api_instance.private_project_articles_list(project_id, page=page, page_size=page_size, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_articles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
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

# **private_project_collaborator_delete**
> private_project_collaborator_delete(project_id, user_id)

Remove project collaborator

Remove project collaborator

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
user_id = 789 # int | User unique identifier

try: 
    # Remove project collaborator
    api_instance.private_project_collaborator_delete(project_id, user_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_collaborator_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **user_id** | **int**| User unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_collaborators_invite**
> ResponseMessage private_project_collaborators_invite(project_id, collaborator)

Invite project collaborators

Invite users to collaborate on project or view the project

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
collaborator = swagger_client.ProjectCollaboratorInvite() # ProjectCollaboratorInvite | viewer or collaborator role. User user_id or email of user

try: 
    # Invite project collaborators
    api_response = api_instance.private_project_collaborators_invite(project_id, collaborator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_collaborators_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **collaborator** | [**ProjectCollaboratorInvite**](ProjectCollaboratorInvite.md)| viewer or collaborator role. User user_id or email of user | 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_collaborators_list**
> list[ProjectCollaborator] private_project_collaborators_list(project_id)

List project collaborators

List Project collaborators and invited users

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier

try: 
    # List project collaborators
    api_response = api_instance.private_project_collaborators_list(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_collaborators_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 

### Return type

[**list[ProjectCollaborator]**](ProjectCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_create**
> CreateProjectResponse private_project_create(project)

Create project

Create a new project

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
api_instance = swagger_client.ProjectsApi()
project = swagger_client.ProjectCreate() # ProjectCreate | Project  description

try: 
    # Create project
    api_response = api_instance.private_project_create(project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectCreate**](ProjectCreate.md)| Project  description | 

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_delete**
> private_project_delete(project_id)

Delete project

A project can be deleted only if: - it is not public - it does not have public articles.  When an individual project is deleted, all the articles are moved to my data of each owner.  When a group project is deleted, all the articles and files are deleted as well. Only project owner, group admin and above can delete a project. 

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier

try: 
    # Delete project
    api_instance.private_project_delete(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_details**
> ProjectCompletePrivate private_project_details(project_id)

View project details

View a private project

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier

try: 
    # View project details
    api_response = api_instance.private_project_details(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 

### Return type

[**ProjectCompletePrivate**](ProjectCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_leave**
> private_project_leave(project_id)

Private Project Leave

Please note: project's owner cannot leave the project.

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier

try: 
    # Private Project Leave
    api_instance.private_project_leave(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_leave: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_note**
> ProjectNotePrivate private_project_note(project_id, note_id)

Project note details

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
note_id = 789 # int | Note unique identifier

try: 
    # Project note details
    api_response = api_instance.private_project_note(project_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **note_id** | **int**| Note unique identifier | 

### Return type

[**ProjectNotePrivate**](ProjectNotePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_note_delete**
> private_project_note_delete(project_id, note_id)

Delete project note

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
note_id = 789 # int | Note unique identifier

try: 
    # Delete project note
    api_instance.private_project_note_delete(project_id, note_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_note_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **note_id** | **int**| Note unique identifier | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_note_update**
> private_project_note_update(project_id, note_id, note)

Update project note

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
note_id = 789 # int | Note unique identifier
note = swagger_client.ProjectNoteCreate() # ProjectNoteCreate | Note message

try: 
    # Update project note
    api_instance.private_project_note_update(project_id, note_id, note)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_note_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **note_id** | **int**| Note unique identifier | 
 **note** | [**ProjectNoteCreate**](ProjectNoteCreate.md)| Note message | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_notes_create**
> Location private_project_notes_create(project_id, note)

Create project note

Create a new project note

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
note = swagger_client.ProjectNoteCreate() # ProjectNoteCreate | Note message

try: 
    # Create project note
    api_response = api_instance.private_project_notes_create(project_id, note)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_notes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **note** | [**ProjectNoteCreate**](ProjectNoteCreate.md)| Note message | 

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_notes_list**
> list[ProjectNote] private_project_notes_list(project_id, page=page, page_size=page_size, limit=limit, offset=offset)

List project notes

List project notes

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)

try: 
    # List project notes
    api_response = api_instance.private_project_notes_list(project_id, page=page, page_size=page_size, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_notes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 

### Return type

[**list[ProjectNote]**](ProjectNote.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_publish**
> ResponseMessage private_project_publish(project_id)

Private Project Publish

Publish a project. Possible after all items inside it are public

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier

try: 
    # Private Project Publish
    api_response = api_instance.private_project_publish(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_project_update**
> private_project_update(project_id, project)

Update project

Updating an project by passing body parameters; request can also be made with the PATCH method.

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
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project unique identifier
project = swagger_client.ProjectUpdate() # ProjectUpdate | Project description

try: 
    # Update project
    api_instance.private_project_update(project_id, project)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_project_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project unique identifier | 
 **project** | [**ProjectUpdate**](ProjectUpdate.md)| Project description | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_projects_list**
> list[ProjectPrivate] private_projects_list(page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, storage=storage, roles=roles)

Private Projects

List private projects

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
api_instance = swagger_client.ProjectsApi()
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
order = 'published_date' # str | The field by which to order. (optional) (default to published_date)
order_direction = 'desc' # str |  (optional) (default to desc)
storage = 'storage_example' # str | only return collections from this institution (optional)
roles = 'roles_example' # str | Any combination of owner, collaborator, viewer separated by comma. Examples: \"owner\" or \"owner,collaborator\". (optional)

try: 
    # Private Projects
    api_response = api_instance.private_projects_list(page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, storage=storage, roles=roles)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_projects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. Used for pagination with page_size | [optional] 
 **page_size** | **int**| The number of results included on a page. Used for pagination with page | [optional] [default to 10]
 **limit** | **int**| Number of results included on a page. Used for pagination with query | [optional] 
 **offset** | **int**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
 **order** | **str**| The field by which to order. | [optional] [default to published_date]
 **order_direction** | **str**|  | [optional] [default to desc]
 **storage** | **str**| only return collections from this institution | [optional] 
 **roles** | **str**| Any combination of owner, collaborator, viewer separated by comma. Examples: \&quot;owner\&quot; or \&quot;owner,collaborator\&quot;. | [optional] 

### Return type

[**list[ProjectPrivate]**](ProjectPrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_projects_search**
> list[ProjectPrivate] private_projects_search(search=search)

Private Projects search

Search inside the private projects

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
search = swagger_client.ProjectsSearch() # ProjectsSearch | Search Parameters (optional)

try: 
    # Private Projects search
    api_response = api_instance.private_projects_search(search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->private_projects_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**ProjectsSearch**](ProjectsSearch.md)| Search Parameters | [optional] 

### Return type

[**list[ProjectPrivate]**](ProjectPrivate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_articles**
> list[Article] project_articles(project_id)

Public Project Articles

List articles in project

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project Unique identifier

try: 
    # Public Project Articles
    api_response = api_instance.project_articles(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->project_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project Unique identifier | 

### Return type

[**list[Article]**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_details**
> ProjectComplete project_details(project_id)

Public Project

View a project

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | Project Unique identifier

try: 
    # Public Project
    api_response = api_instance.project_details(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->project_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project Unique identifier | 

### Return type

[**ProjectComplete**](ProjectComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> list[Project] projects_list(x_cursor=x_cursor, page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, institution=institution, published_since=published_since, group=group)

Public Projects

Returns a list of public projects

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
x_cursor = 'x_cursor_example' # str | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. (optional)
page = 789 # int | Page number. Used for pagination with page_size (optional)
page_size = 10 # int | The number of results included on a page. Used for pagination with page (optional) (default to 10)
limit = 789 # int | Number of results included on a page. Used for pagination with query (optional)
offset = 789 # int | Where to start the listing(the offset of the first result). Used for pagination with limit (optional)
order = 'published_date' # str | The field by which to order. Default varies by endpoint/resource. (optional) (default to published_date)
order_direction = 'desc' # str |  (optional) (default to desc)
institution = 789 # int | only return collections from this institution (optional)
published_since = 'published_since_example' # str | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD (optional)
group = 789 # int | only return collections from this group (optional)

try: 
    # Public Projects
    api_response = api_instance.projects_list(x_cursor=x_cursor, page=page, page_size=page_size, limit=limit, offset=offset, order=order, order_direction=order_direction, institution=institution, published_since=published_since, group=group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_list: %s\n" % e)
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
 **published_since** | **str**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
 **group** | **int**| only return collections from this group | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_search**
> list[Project] projects_search(x_cursor=x_cursor, search=search)

Public Projects Search

Returns a list of public articles

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
x_cursor = 'x_cursor_example' # str | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. (optional)
search = swagger_client.ProjectsSearch() # ProjectsSearch | Search Parameters (optional)

try: 
    # Public Projects Search
    api_response = api_instance.projects_search(x_cursor=x_cursor, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_cursor** | **str**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] 
 **search** | [**ProjectsSearch**](ProjectsSearch.md)| Search Parameters | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

