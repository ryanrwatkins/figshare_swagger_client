# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ArticleProjectCreate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'keywords': 'list[str]',
        'references': 'list[str]',
        'categories': 'list[int]',
        'categories_by_source_id': 'list[str]',
        'authors': 'list[object]',
        'custom_fields': 'object',
        'custom_fields_list': 'list[CustomArticleFieldAdd]',
        'defined_type': 'str',
        'funding': 'str',
        'funding_list': 'list[FundingCreate]',
        'license': 'int',
        'doi': 'str',
        'handle': 'str',
        'resource_doi': 'str',
        'resource_title': 'str',
        'timeline': 'TimelineUpdate'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'tags': 'tags',
        'keywords': 'keywords',
        'references': 'references',
        'categories': 'categories',
        'categories_by_source_id': 'categories_by_source_id',
        'authors': 'authors',
        'custom_fields': 'custom_fields',
        'custom_fields_list': 'custom_fields_list',
        'defined_type': 'defined_type',
        'funding': 'funding',
        'funding_list': 'funding_list',
        'license': 'license',
        'doi': 'doi',
        'handle': 'handle',
        'resource_doi': 'resource_doi',
        'resource_title': 'resource_title',
        'timeline': 'timeline'
    }

    def __init__(self, title=None, description='', tags=None, keywords=None, references=None, categories=None, categories_by_source_id=None, authors=None, custom_fields=None, custom_fields_list=None, defined_type=None, funding='', funding_list=None, license=0, doi='', handle='', resource_doi='', resource_title='', timeline=None):
        """
        ArticleProjectCreate - a model defined in Swagger
        """

        self._title = None
        self._description = None
        self._tags = None
        self._keywords = None
        self._references = None
        self._categories = None
        self._categories_by_source_id = None
        self._authors = None
        self._custom_fields = None
        self._custom_fields_list = None
        self._defined_type = None
        self._funding = None
        self._funding_list = None
        self._license = None
        self._doi = None
        self._handle = None
        self._resource_doi = None
        self._resource_title = None
        self._timeline = None

        self.title = title
        if description is not None:
          self.description = description
        if tags is not None:
          self.tags = tags
        if keywords is not None:
          self.keywords = keywords
        if references is not None:
          self.references = references
        if categories is not None:
          self.categories = categories
        if categories_by_source_id is not None:
          self.categories_by_source_id = categories_by_source_id
        if authors is not None:
          self.authors = authors
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if custom_fields_list is not None:
          self.custom_fields_list = custom_fields_list
        if defined_type is not None:
          self.defined_type = defined_type
        if funding is not None:
          self.funding = funding
        if funding_list is not None:
          self.funding_list = funding_list
        if license is not None:
          self.license = license
        if doi is not None:
          self.doi = doi
        if handle is not None:
          self.handle = handle
        if resource_doi is not None:
          self.resource_doi = resource_doi
        if resource_title is not None:
          self.resource_title = resource_title
        if timeline is not None:
          self.timeline = timeline

    @property
    def title(self):
        """
        Gets the title of this ArticleProjectCreate.
        Title of article

        :return: The title of this ArticleProjectCreate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ArticleProjectCreate.
        Title of article

        :param title: The title of this ArticleProjectCreate.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if title is not None and len(title) > 1000:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `1000`")
        if title is not None and len(title) < 3:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `3`")

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this ArticleProjectCreate.
        The article description. In a publisher case, usually this is the remote article description

        :return: The description of this ArticleProjectCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ArticleProjectCreate.
        The article description. In a publisher case, usually this is the remote article description

        :param description: The description of this ArticleProjectCreate.
        :type: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")

        self._description = description

    @property
    def tags(self):
        """
        Gets the tags of this ArticleProjectCreate.
        List of tags to be associated with the article. Keywords can be used instead

        :return: The tags of this ArticleProjectCreate.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ArticleProjectCreate.
        List of tags to be associated with the article. Keywords can be used instead

        :param tags: The tags of this ArticleProjectCreate.
        :type: list[str]
        """

        self._tags = tags

    @property
    def keywords(self):
        """
        Gets the keywords of this ArticleProjectCreate.
        List of tags to be associated with the article. Tags can be used instead

        :return: The keywords of this ArticleProjectCreate.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this ArticleProjectCreate.
        List of tags to be associated with the article. Tags can be used instead

        :param keywords: The keywords of this ArticleProjectCreate.
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def references(self):
        """
        Gets the references of this ArticleProjectCreate.
        List of links to be associated with the article (e.g [\"http://link1\", \"http://link2\", \"http://link3\"])

        :return: The references of this ArticleProjectCreate.
        :rtype: list[str]
        """
        return self._references

    @references.setter
    def references(self, references):
        """
        Sets the references of this ArticleProjectCreate.
        List of links to be associated with the article (e.g [\"http://link1\", \"http://link2\", \"http://link3\"])

        :param references: The references of this ArticleProjectCreate.
        :type: list[str]
        """

        self._references = references

    @property
    def categories(self):
        """
        Gets the categories of this ArticleProjectCreate.
        List of category ids to be associated with the article(e.g [1, 23, 33, 66])

        :return: The categories of this ArticleProjectCreate.
        :rtype: list[int]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this ArticleProjectCreate.
        List of category ids to be associated with the article(e.g [1, 23, 33, 66])

        :param categories: The categories of this ArticleProjectCreate.
        :type: list[int]
        """

        self._categories = categories

    @property
    def categories_by_source_id(self):
        """
        Gets the categories_by_source_id of this ArticleProjectCreate.
        List of category source ids to be associated with the article, supersedes the categories property

        :return: The categories_by_source_id of this ArticleProjectCreate.
        :rtype: list[str]
        """
        return self._categories_by_source_id

    @categories_by_source_id.setter
    def categories_by_source_id(self, categories_by_source_id):
        """
        Sets the categories_by_source_id of this ArticleProjectCreate.
        List of category source ids to be associated with the article, supersedes the categories property

        :param categories_by_source_id: The categories_by_source_id of this ArticleProjectCreate.
        :type: list[str]
        """

        self._categories_by_source_id = categories_by_source_id

    @property
    def authors(self):
        """
        Gets the authors of this ArticleProjectCreate.
        List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.

        :return: The authors of this ArticleProjectCreate.
        :rtype: list[object]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """
        Sets the authors of this ArticleProjectCreate.
        List of authors to be associated with the article. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.

        :param authors: The authors of this ArticleProjectCreate.
        :type: list[object]
        """

        self._authors = authors

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this ArticleProjectCreate.
        List of key, values pairs to be associated with the article

        :return: The custom_fields of this ArticleProjectCreate.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this ArticleProjectCreate.
        List of key, values pairs to be associated with the article

        :param custom_fields: The custom_fields of this ArticleProjectCreate.
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def custom_fields_list(self):
        """
        Gets the custom_fields_list of this ArticleProjectCreate.
        List of custom fields values, supersedes custom_fields parameter

        :return: The custom_fields_list of this ArticleProjectCreate.
        :rtype: list[CustomArticleFieldAdd]
        """
        return self._custom_fields_list

    @custom_fields_list.setter
    def custom_fields_list(self, custom_fields_list):
        """
        Sets the custom_fields_list of this ArticleProjectCreate.
        List of custom fields values, supersedes custom_fields parameter

        :param custom_fields_list: The custom_fields_list of this ArticleProjectCreate.
        :type: list[CustomArticleFieldAdd]
        """

        self._custom_fields_list = custom_fields_list

    @property
    def defined_type(self):
        """
        Gets the defined_type of this ArticleProjectCreate.
        <b>One of:</b> <code>figure</code> <code>online resource</code> <code>preprint</code> <code>book</code> <code>conference contribution</code> <code>media</code> <code>dataset</code> <code>poster</code> <code>journal contribution</code> <code>presentation</code> <code>thesis</code> <code>software</code>

        :return: The defined_type of this ArticleProjectCreate.
        :rtype: str
        """
        return self._defined_type

    @defined_type.setter
    def defined_type(self, defined_type):
        """
        Sets the defined_type of this ArticleProjectCreate.
        <b>One of:</b> <code>figure</code> <code>online resource</code> <code>preprint</code> <code>book</code> <code>conference contribution</code> <code>media</code> <code>dataset</code> <code>poster</code> <code>journal contribution</code> <code>presentation</code> <code>thesis</code> <code>software</code>

        :param defined_type: The defined_type of this ArticleProjectCreate.
        :type: str
        """

        self._defined_type = defined_type

    @property
    def funding(self):
        """
        Gets the funding of this ArticleProjectCreate.
        Grant number or funding authority

        :return: The funding of this ArticleProjectCreate.
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """
        Sets the funding of this ArticleProjectCreate.
        Grant number or funding authority

        :param funding: The funding of this ArticleProjectCreate.
        :type: str
        """

        self._funding = funding

    @property
    def funding_list(self):
        """
        Gets the funding_list of this ArticleProjectCreate.
        Funding creation / update items

        :return: The funding_list of this ArticleProjectCreate.
        :rtype: list[FundingCreate]
        """
        return self._funding_list

    @funding_list.setter
    def funding_list(self, funding_list):
        """
        Sets the funding_list of this ArticleProjectCreate.
        Funding creation / update items

        :param funding_list: The funding_list of this ArticleProjectCreate.
        :type: list[FundingCreate]
        """

        self._funding_list = funding_list

    @property
    def license(self):
        """
        Gets the license of this ArticleProjectCreate.
        License id for this article.

        :return: The license of this ArticleProjectCreate.
        :rtype: int
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this ArticleProjectCreate.
        License id for this article.

        :param license: The license of this ArticleProjectCreate.
        :type: int
        """

        self._license = license

    @property
    def doi(self):
        """
        Gets the doi of this ArticleProjectCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :return: The doi of this ArticleProjectCreate.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """
        Sets the doi of this ArticleProjectCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :param doi: The doi of this ArticleProjectCreate.
        :type: str
        """

        self._doi = doi

    @property
    def handle(self):
        """
        Gets the handle of this ArticleProjectCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :return: The handle of this ArticleProjectCreate.
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """
        Sets the handle of this ArticleProjectCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :param handle: The handle of this ArticleProjectCreate.
        :type: str
        """

        self._handle = handle

    @property
    def resource_doi(self):
        """
        Gets the resource_doi of this ArticleProjectCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article DOI.

        :return: The resource_doi of this ArticleProjectCreate.
        :rtype: str
        """
        return self._resource_doi

    @resource_doi.setter
    def resource_doi(self, resource_doi):
        """
        Sets the resource_doi of this ArticleProjectCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article DOI.

        :param resource_doi: The resource_doi of this ArticleProjectCreate.
        :type: str
        """

        self._resource_doi = resource_doi

    @property
    def resource_title(self):
        """
        Gets the resource_title of this ArticleProjectCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article title.

        :return: The resource_title of this ArticleProjectCreate.
        :rtype: str
        """
        return self._resource_title

    @resource_title.setter
    def resource_title(self, resource_title):
        """
        Sets the resource_title of this ArticleProjectCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article title.

        :param resource_title: The resource_title of this ArticleProjectCreate.
        :type: str
        """

        self._resource_title = resource_title

    @property
    def timeline(self):
        """
        Gets the timeline of this ArticleProjectCreate.
        Various timeline dates

        :return: The timeline of this ArticleProjectCreate.
        :rtype: TimelineUpdate
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """
        Sets the timeline of this ArticleProjectCreate.
        Various timeline dates

        :param timeline: The timeline of this ArticleProjectCreate.
        :type: TimelineUpdate
        """

        self._timeline = timeline

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ArticleProjectCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
