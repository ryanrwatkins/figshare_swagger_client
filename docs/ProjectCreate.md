# ProjectCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title for this project - mandatory. 3 - 1000 characters. | 
**description** | **str** | Project description | [optional] 
**funding** | **str** | Grant number or organization(s) that funded this project. Up to 2000 characters permitted. | [optional] 
**funding_list** | [**list[FundingCreate]**](FundingCreate.md) | Funding creation / update items | [optional] 
**group_id** | **int** | Only if project type is group. | [optional] 
**custom_fields** | **object** | List of key, values pairs to be associated with the project | [optional] 
**custom_fields_list** | [**list[CustomArticleFieldAdd]**](CustomArticleFieldAdd.md) | List of custom fields values, supersedes custom_fields parameter | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


