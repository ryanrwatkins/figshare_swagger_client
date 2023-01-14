# ArticleProjectCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title of article | 
**description** | **str** | The article description. In a publisher case, usually this is the remote article description | [optional] [default to '']
**tags** | **list[str]** | List of tags to be associated with the article. Keywords can be used instead | [optional] 
**keywords** | **list[str]** | List of tags to be associated with the article. Tags can be used instead | [optional] 
**references** | **list[str]** | List of links to be associated with the article (e.g [\&quot;http://link1\&quot;, \&quot;http://link2\&quot;, \&quot;http://link3\&quot;]) | [optional] 
**categories** | **list[int]** | List of category ids to be associated with the article(e.g [1, 23, 33, 66]) | [optional] 
**categories_by_source_id** | **list[str]** | List of category source ids to be associated with the article, supersedes the categories property | [optional] 
**authors** | **list[object]** | List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint. | [optional] 
**custom_fields** | **object** | List of key, values pairs to be associated with the article | [optional] 
**custom_fields_list** | [**list[CustomArticleFieldAdd]**](CustomArticleFieldAdd.md) | List of custom fields values, supersedes custom_fields parameter | [optional] 
**defined_type** | **str** | &lt;b&gt;One of:&lt;/b&gt; &lt;code&gt;figure&lt;/code&gt; &lt;code&gt;online resource&lt;/code&gt; &lt;code&gt;preprint&lt;/code&gt; &lt;code&gt;book&lt;/code&gt; &lt;code&gt;conference contribution&lt;/code&gt; &lt;code&gt;media&lt;/code&gt; &lt;code&gt;dataset&lt;/code&gt; &lt;code&gt;poster&lt;/code&gt; &lt;code&gt;journal contribution&lt;/code&gt; &lt;code&gt;presentation&lt;/code&gt; &lt;code&gt;thesis&lt;/code&gt; &lt;code&gt;software&lt;/code&gt; | [optional] 
**funding** | **str** | Grant number or funding authority | [optional] [default to '']
**funding_list** | [**list[FundingCreate]**](FundingCreate.md) | Funding creation / update items | [optional] 
**license** | **int** | License id for this article. | [optional] [default to 0]
**doi** | **str** | Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system. | [optional] [default to '']
**handle** | **str** | Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system. | [optional] [default to '']
**resource_doi** | **str** | Not applicable to regular users. In a publisher case, this is the publisher article DOI. | [optional] [default to '']
**resource_title** | **str** | Not applicable to regular users. In a publisher case, this is the publisher article title. | [optional] [default to '']
**timeline** | [**TimelineUpdate**](TimelineUpdate.md) | Various timeline dates | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


