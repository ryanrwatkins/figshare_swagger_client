# CollectionUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding** | **str** | Grant number or funding authority | [optional] [default to '']
**funding_list** | [**list[FundingCreate]**](FundingCreate.md) | Funding creation / update items | [optional] 
**title** | **str** | Title of collection | [optional] 
**description** | **str** | The collection description. In a publisher case, usually this is the remote collection description | [optional] [default to '']
**articles** | **list[int]** | List of articles to be associated with the collection | [optional] 
**authors** | **list[object]** | List of authors to be associated with the collection. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint. | [optional] 
**categories** | **list[int]** | List of category ids to be associated with the collection (e.g [1, 23, 33, 66]) | [optional] 
**categories_by_source_id** | **list[str]** | List of category source ids to be associated with the article, supersedes the categories property | [optional] 
**tags** | **list[str]** | List of tags to be associated with the collection. Keywords can be used instead | [optional] 
**keywords** | **list[str]** | List of tags to be associated with the collection. Tags can be used instead | [optional] 
**references** | **list[str]** | List of links to be associated with the collection (e.g [\&quot;http://link1\&quot;, \&quot;http://link2\&quot;, \&quot;http://link3\&quot;]) | [optional] 
**custom_fields** | **object** | List of key, values pairs to be associated with the collection | [optional] 
**custom_fields_list** | [**list[CustomArticleFieldAdd]**](CustomArticleFieldAdd.md) | List of custom fields values, supersedes custom_fields parameter | [optional] 
**doi** | **str** | Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system. | [optional] [default to '']
**handle** | **str** | Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system. | [optional] [default to '']
**resource_id** | **str** | Not applicable to regular users. In a publisher case, this is the publisher article id | [optional] 
**resource_doi** | **str** | Not applicable to regular users. In a publisher case, this is the publisher article DOI. | [optional] [default to '']
**resource_link** | **str** | Not applicable to regular users. In a publisher case, this is the publisher article link | [optional] 
**resource_title** | **str** | Not applicable to regular users. In a publisher case, this is the publisher article title. | [optional] [default to '']
**resource_version** | **int** | Not applicable to regular users. In a publisher case, this is the publisher article version | [optional] 
**group_id** | **int** | Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups | [optional] 
**timeline** | [**TimelineUpdate**](TimelineUpdate.md) | Various timeline dates | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


