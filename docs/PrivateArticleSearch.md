# PrivateArticleSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_for** | **str** | Search term | [optional] 
**page** | **int** | Page number. Used for pagination with page_size | [optional] 
**page_size** | **int** | The number of results included on a page. Used for pagination with page | [optional] [default to 10]
**limit** | **int** | Number of results included on a page. Used for pagination with query | [optional] 
**offset** | **int** | Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
**order_direction** | **str** | Direction of ordering | [optional] [default to 'desc']
**institution** | **int** | only return collections from this institution | [optional] 
**published_since** | **str** | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
**modified_since** | **str** | Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] 
**group** | **int** | only return collections from this group | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


