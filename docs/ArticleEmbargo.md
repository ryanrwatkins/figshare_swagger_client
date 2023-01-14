# ArticleEmbargo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_embargoed** | **bool** | True if embargoed | 
**embargo_title** | **str** | Title for embargo | 
**embargo_reason** | **str** | Reason for embargo | 
**embargo_options** | **list[object]** | List of embargo permissions that are associated with the article. If the type is logged_in and the group_ids list is empty, then the whole institution can see the article; if there are multiple group_ids, then only users that are under those groups can see the article. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


