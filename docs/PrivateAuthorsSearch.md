# PrivateAuthorsSearch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_for** | **str** | Search term | [optional] 
**page** | **int** | Page number. Used for pagination with page_size | [optional] 
**page_size** | **int** | The number of results included on a page. Used for pagination with page | [optional] [default to 10]
**limit** | **int** | Number of results included on a page. Used for pagination with query | [optional] 
**offset** | **int** | Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] 
**order** | **str** | The field by which to order. Default varies by endpoint/resource. | [optional] [default to 'published_date']
**order_direction** | **str** | Direction of ordering | [optional] [default to 'desc']
**institution_id** | **int** | Return only authors associated to this institution | [optional] 
**orcid** | **str** | Orcid of author | [optional] 
**group_id** | **int** | Return only authors in this group or subgroups of the group | [optional] 
**is_active** | **bool** | Return only active authors if True | [optional] 
**is_public** | **bool** | Return only authors that have published items if True | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


