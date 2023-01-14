# UploadFilePart

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_no** | **int** | File part id | [optional] 
**start_offset** | **int** | Indexes on byte range. zero-based and inclusive | [optional] 
**end_offset** | **int** | Indexes on byte range. zero-based and inclusive | [optional] 
**status** | **str** | part status | [optional] 
**locked** | **bool** | When a part is being uploaded it is being locked, by setting the locked flag to true. No changes/uploads can happen on this part from other requests. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


