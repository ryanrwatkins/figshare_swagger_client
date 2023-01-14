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


class ProjectCreate(object):
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
        'funding': 'str',
        'funding_list': 'list[FundingCreate]',
        'group_id': 'int',
        'custom_fields': 'object',
        'custom_fields_list': 'list[CustomArticleFieldAdd]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'funding': 'funding',
        'funding_list': 'funding_list',
        'group_id': 'group_id',
        'custom_fields': 'custom_fields',
        'custom_fields_list': 'custom_fields_list'
    }

    def __init__(self, title=None, description=None, funding=None, funding_list=None, group_id=None, custom_fields=None, custom_fields_list=None):
        """
        ProjectCreate - a model defined in Swagger
        """

        self._title = None
        self._description = None
        self._funding = None
        self._funding_list = None
        self._group_id = None
        self._custom_fields = None
        self._custom_fields_list = None

        self.title = title
        if description is not None:
          self.description = description
        if funding is not None:
          self.funding = funding
        if funding_list is not None:
          self.funding_list = funding_list
        if group_id is not None:
          self.group_id = group_id
        if custom_fields is not None:
          self.custom_fields = custom_fields
        if custom_fields_list is not None:
          self.custom_fields_list = custom_fields_list

    @property
    def title(self):
        """
        Gets the title of this ProjectCreate.
        The title for this project - mandatory. 3 - 1000 characters.

        :return: The title of this ProjectCreate.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ProjectCreate.
        The title for this project - mandatory. 3 - 1000 characters.

        :param title: The title of this ProjectCreate.
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
        Gets the description of this ProjectCreate.
        Project description

        :return: The description of this ProjectCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProjectCreate.
        Project description

        :param description: The description of this ProjectCreate.
        :type: str
        """
        if description is not None and len(description) > 10000:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")

        self._description = description

    @property
    def funding(self):
        """
        Gets the funding of this ProjectCreate.
        Grant number or organization(s) that funded this project. Up to 2000 characters permitted.

        :return: The funding of this ProjectCreate.
        :rtype: str
        """
        return self._funding

    @funding.setter
    def funding(self, funding):
        """
        Sets the funding of this ProjectCreate.
        Grant number or organization(s) that funded this project. Up to 2000 characters permitted.

        :param funding: The funding of this ProjectCreate.
        :type: str
        """

        self._funding = funding

    @property
    def funding_list(self):
        """
        Gets the funding_list of this ProjectCreate.
        Funding creation / update items

        :return: The funding_list of this ProjectCreate.
        :rtype: list[FundingCreate]
        """
        return self._funding_list

    @funding_list.setter
    def funding_list(self, funding_list):
        """
        Sets the funding_list of this ProjectCreate.
        Funding creation / update items

        :param funding_list: The funding_list of this ProjectCreate.
        :type: list[FundingCreate]
        """

        self._funding_list = funding_list

    @property
    def group_id(self):
        """
        Gets the group_id of this ProjectCreate.
        Only if project type is group.

        :return: The group_id of this ProjectCreate.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this ProjectCreate.
        Only if project type is group.

        :param group_id: The group_id of this ProjectCreate.
        :type: int
        """

        self._group_id = group_id

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this ProjectCreate.
        List of key, values pairs to be associated with the project

        :return: The custom_fields of this ProjectCreate.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this ProjectCreate.
        List of key, values pairs to be associated with the project

        :param custom_fields: The custom_fields of this ProjectCreate.
        :type: object
        """

        self._custom_fields = custom_fields

    @property
    def custom_fields_list(self):
        """
        Gets the custom_fields_list of this ProjectCreate.
        List of custom fields values, supersedes custom_fields parameter

        :return: The custom_fields_list of this ProjectCreate.
        :rtype: list[CustomArticleFieldAdd]
        """
        return self._custom_fields_list

    @custom_fields_list.setter
    def custom_fields_list(self, custom_fields_list):
        """
        Sets the custom_fields_list of this ProjectCreate.
        List of custom fields values, supersedes custom_fields parameter

        :param custom_fields_list: The custom_fields_list of this ProjectCreate.
        :type: list[CustomArticleFieldAdd]
        """

        self._custom_fields_list = custom_fields_list

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
        if not isinstance(other, ProjectCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other