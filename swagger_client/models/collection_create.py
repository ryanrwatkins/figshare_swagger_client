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


class CollectionCreate(object):
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
        'funding': 'str',
        'funding_list': 'list[FundingCreate]',
        'title': 'str',
        'description': 'str',
        'articles': 'list[int]',
        'authors': 'list[object]',
        'categories': 'list[int]',
        'categories_by_source_id': 'list[str]',
        'tags': 'list[str]',
        'keywords': 'list[str]',
        'references': 'list[str]',
        'custom_fields': 'object',
        'custom_fields_list': 'list[CustomArticleFieldAdd]',
        'doi': 'str',
        'handle': 'str',
        'resource_id': 'str',
        'resource_doi': 'str',
        'resource_link': 'str',
        'resource_title': 'str',
        'resource_version': 'int',
        'group_id': 'int',
        'timeline': 'TimelineUpdate'
    }

    attribute_map = {
        'funding': 'funding',
        'funding_list': 'funding_list',
        'title': 'title',
        'description': 'description',
        'articles': 'articles',
        'authors': 'authors',
        'categories': 'categories',
        'categories_by_source_id': 'categories_by_source_id',
        'tags': 'tags',
        'keywords': 'keywords',
        'references': 'references',
        'custom_fields': 'custom_fields',
        'custom_fields_list': 'custom_fields_list',
        'doi': 'doi',
        'handle': 'handle',
        'resource_id': 'resource_id',
        'resource_doi': 'resource_doi',
        'resource_link': 'resource_link',
        'resource_title': 'resource_title',
        'resource_version': 'resource_version',
        'group_id': 'group_id',
        'timeline': 'timeline'
    }

    def __init__(self, funding='', funding_list=None, title=None, description='', articles=None, authors=None, categories=None, categories_by_source_id=None, tags=None, keywords=None, references=None, custom_fields=None, custom_fields_list=None, doi='', handle='', resource_id=None, resource_doi='', resource_link=None, resource_title='', resource_version=None, group_id=None, timeline=None):
        """
        CollectionCreate - a model defined in Swagger
        """

        self._funding = None
        self._funding_list = None
        self._title = None
        self._description = None
        self._articles = None
        self._authors = None
        self._categories = None
        self._categories_by_source_id = None
        self._tags = None
        self._keywords = None
        self._references = None
        self._custom_fields = None
        self._custom_fields_list = None
        self._doi = None
        self._handle = None
        self._resource_id = None
        self._resource_doi = None
        self._resource_link = None
        self._resource_title = None
        self._resource_version = None
        self._group_id = None
        self._timeline = None

        if funding is not None:
          self.funding = funding
        if funding_list is not None:
          self.funding_list = funding_list
        self.title = title
        if description is not None:
          self.description = description
        if articles is not None:
          self.articles = articles
        if authors is not None:
          self.authors = authors
        if categories is not None:
          self.categories = categories
        if categories_by_source_id is not None:
          self.categories_by_source_id = categories_by_source_id
        if tags is not None:
          self.tags = tags
        if keywords is not None:
          self.keywords = keywords
        if references is not None:
          self.references = references
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if custom_fields_list is not None:
          self.custom_fields_list = custom_fields_list
        if doi is not None:
          self.doi = doi
        if handle is not None:
          self.handle = handle
        if resource_id is not None:
          self.resource_id = resource_id
        if resource_doi is not None:
          self.resource_doi = resource_doi
        if resource_link is not None:
          self.resource_link = resource_link
        if resource_title is not None:
          self.resource_title = resource_title
        if resource_version is not None:
          self.resource_version = resource_version
        if group_id is not None:
          self.group_id = group_id
        if timeline is not None:
          self.timeline = timeline

    @property
    def funding(self):
        """
        Gets the funding of this CollectionCreate.
        Grant number or funding authority

        :return: The funding of this CollectionCreate.
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """
        Sets the funding of this CollectionCreate.
        Grant number or funding authority

        :param funding: The funding of this CollectionCreate.
        :type: str
        """

        self._funding = funding

    @property
    def funding_list(self):
        """
        Gets the funding_list of this CollectionCreate.
        Funding creation / update items

        :return: The funding_list of this CollectionCreate.
        :rtype: list[FundingCreate]
        """
        return self._funding_list

    @funding_list.setter
    def funding_list(self, funding_list):
        """
        Sets the funding_list of this CollectionCreate.
        Funding creation / update items

        :param funding_list: The funding_list of this CollectionCreate.
        :type: list[FundingCreate]
        """

        self._funding_list = funding_list

    @property
    def title(self):
        """
        Gets the title of this CollectionCreate.
        Title of collection

        :return: The title of this CollectionCreate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CollectionCreate.
        Title of collection

        :param title: The title of this CollectionCreate.
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
        Gets the description of this CollectionCreate.
        The collection description. In a publisher case, usually this is the remote collection description

        :return: The description of this CollectionCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CollectionCreate.
        The collection description. In a publisher case, usually this is the remote collection description

        :param description: The description of this CollectionCreate.
        :type: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")

        self._description = description

    @property
    def articles(self):
        """
        Gets the articles of this CollectionCreate.
        List of articles to be associated with the collection

        :return: The articles of this CollectionCreate.
        :rtype: list[int]
        """
        return self._articles

    @articles.setter
    def articles(self, articles):
        """
        Sets the articles of this CollectionCreate.
        List of articles to be associated with the collection

        :param articles: The articles of this CollectionCreate.
        :type: list[int]
        """

        self._articles = articles

    @property
    def authors(self):
        """
        Gets the authors of this CollectionCreate.
        List of authors to be associated with the collection. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.

        :return: The authors of this CollectionCreate.
        :rtype: list[object]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """
        Sets the authors of this CollectionCreate.
        List of authors to be associated with the collection. The list can contain the following fields: id, name, first_name, last_name, email, orcid_id. If an id is supplied, it will take priority and everything else will be ignored. No more than 10 authors. For adding more authors use the specific authors endpoint.

        :param authors: The authors of this CollectionCreate.
        :type: list[object]
        """

        self._authors = authors

    @property
    def categories(self):
        """
        Gets the categories of this CollectionCreate.
        List of category ids to be associated with the collection(e.g [1, 23, 33, 66])

        :return: The categories of this CollectionCreate.
        :rtype: list[int]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this CollectionCreate.
        List of category ids to be associated with the collection(e.g [1, 23, 33, 66])

        :param categories: The categories of this CollectionCreate.
        :type: list[int]
        """

        self._categories = categories

    @property
    def categories_by_source_id(self):
        """
        Gets the categories_by_source_id of this CollectionCreate.
        List of category source ids to be associated with the collection, supersedes the categories property

        :return: The categories_by_source_id of this CollectionCreate.
        :rtype: list[str]
        """
        return self._categories_by_source_id

    @categories_by_source_id.setter
    def categories_by_source_id(self, categories_by_source_id):
        """
        Sets the categories_by_source_id of this CollectionCreate.
        List of category source ids to be associated with the collection, supersedes the categories property

        :param categories_by_source_id: The categories_by_source_id of this CollectionCreate.
        :type: list[str]
        """

        self._categories_by_source_id = categories_by_source_id

    @property
    def tags(self):
        """
        Gets the tags of this CollectionCreate.
        List of tags to be associated with the collection. Keywords can be used instead

        :return: The tags of this CollectionCreate.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CollectionCreate.
        List of tags to be associated with the collection. Keywords can be used instead

        :param tags: The tags of this CollectionCreate.
        :type: list[str]
        """

        self._tags = tags

    @property
    def keywords(self):
        """
        Gets the keywords of this CollectionCreate.
        List of tags to be associated with the collection. Tags can be used instead

        :return: The keywords of this CollectionCreate.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this CollectionCreate.
        List of tags to be associated with the collection. Tags can be used instead

        :param keywords: The keywords of this CollectionCreate.
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def references(self):
        """
        Gets the references of this CollectionCreate.
        List of links to be associated with the collection (e.g [\"http://link1\", \"http://link2\", \"http://link3\"])

        :return: The references of this CollectionCreate.
        :rtype: list[str]
        """
        return self._references

    @references.setter
    def references(self, references):
        """
        Sets the references of this CollectionCreate.
        List of links to be associated with the collection (e.g [\"http://link1\", \"http://link2\", \"http://link3\"])

        :param references: The references of this CollectionCreate.
        :type: list[str]
        """

        self._references = references

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this CollectionCreate.
        List of key, values pairs to be associated with the collection

        :return: The custom_fields of this CollectionCreate.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this CollectionCreate.
        List of key, values pairs to be associated with the collection

        :param custom_fields: The custom_fields of this CollectionCreate.
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def custom_fields_list(self):
        """
        Gets the custom_fields_list of this CollectionCreate.
        List of custom fields values, supersedes custom_fields parameter

        :return: The custom_fields_list of this CollectionCreate.
        :rtype: list[CustomArticleFieldAdd]
        """
        return self._custom_fields_list

    @custom_fields_list.setter
    def custom_fields_list(self, custom_fields_list):
        """
        Sets the custom_fields_list of this CollectionCreate.
        List of custom fields values, supersedes custom_fields parameter

        :param custom_fields_list: The custom_fields_list of this CollectionCreate.
        :type: list[CustomArticleFieldAdd]
        """

        self._custom_fields_list = custom_fields_list

    @property
    def doi(self):
        """
        Gets the doi of this CollectionCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :return: The doi of this CollectionCreate.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """
        Sets the doi of this CollectionCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting DOIs. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :param doi: The doi of this CollectionCreate.
        :type: str
        """

        self._doi = doi

    @property
    def handle(self):
        """
        Gets the handle of this CollectionCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :return: The handle of this CollectionCreate.
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """
        Sets the handle of this CollectionCreate.
        Not applicable for regular users. In an institutional case, make sure your group supports setting Handles. This setting is applied by figshare via opening a ticket through our support/helpdesk system.

        :param handle: The handle of this CollectionCreate.
        :type: str
        """

        self._handle = handle

    @property
    def resource_id(self):
        """
        Gets the resource_id of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article id

        :return: The resource_id of this CollectionCreate.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article id

        :param resource_id: The resource_id of this CollectionCreate.
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_doi(self):
        """
        Gets the resource_doi of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article DOI.

        :return: The resource_doi of this CollectionCreate.
        :rtype: str
        """
        return self._resource_doi

    @resource_doi.setter
    def resource_doi(self, resource_doi):
        """
        Sets the resource_doi of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article DOI.

        :param resource_doi: The resource_doi of this CollectionCreate.
        :type: str
        """

        self._resource_doi = resource_doi

    @property
    def resource_link(self):
        """
        Gets the resource_link of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article link

        :return: The resource_link of this CollectionCreate.
        :rtype: str
        """
        return self._resource_link

    @resource_link.setter
    def resource_link(self, resource_link):
        """
        Sets the resource_link of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article link

        :param resource_link: The resource_link of this CollectionCreate.
        :type: str
        """

        self._resource_link = resource_link

    @property
    def resource_title(self):
        """
        Gets the resource_title of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article title.

        :return: The resource_title of this CollectionCreate.
        :rtype: str
        """
        return self._resource_title

    @resource_title.setter
    def resource_title(self, resource_title):
        """
        Sets the resource_title of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article title.

        :param resource_title: The resource_title of this CollectionCreate.
        :type: str
        """

        self._resource_title = resource_title

    @property
    def resource_version(self):
        """
        Gets the resource_version of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article version

        :return: The resource_version of this CollectionCreate.
        :rtype: int
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """
        Sets the resource_version of this CollectionCreate.
        Not applicable to regular users. In a publisher case, this is the publisher article version

        :param resource_version: The resource_version of this CollectionCreate.
        :type: int
        """

        self._resource_version = resource_version

    @property
    def group_id(self):
        """
        Gets the group_id of this CollectionCreate.
        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups

        :return: The group_id of this CollectionCreate.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this CollectionCreate.
        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups

        :param group_id: The group_id of this CollectionCreate.
        :type: int
        """

        self._group_id = group_id

    @property
    def timeline(self):
        """
        Gets the timeline of this CollectionCreate.
        Various timeline dates

        :return: The timeline of this CollectionCreate.
        :rtype: TimelineUpdate
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """
        Sets the timeline of this CollectionCreate.
        Various timeline dates

        :param timeline: The timeline of this CollectionCreate.
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
        if not isinstance(other, CollectionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
