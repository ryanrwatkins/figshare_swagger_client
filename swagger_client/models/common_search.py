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


class CommonSearch(object):
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
        'search_for': 'str',
        'page': 'int',
        'page_size': 'int',
        'limit': 'int',
        'offset': 'int',
        'order_direction': 'str',
        'institution': 'int',
        'published_since': 'str',
        'modified_since': 'str',
        'group': 'int'
    }

    attribute_map = {
        'search_for': 'search_for',
        'page': 'page',
        'page_size': 'page_size',
        'limit': 'limit',
        'offset': 'offset',
        'order_direction': 'order_direction',
        'institution': 'institution',
        'published_since': 'published_since',
        'modified_since': 'modified_since',
        'group': 'group'
    }

    def __init__(self, search_for=None, page=None, page_size=10, limit=None, offset=None, order_direction='desc', institution=None, published_since=None, modified_since=None, group=None):
        """
        CommonSearch - a model defined in Swagger
        """

        self._search_for = None
        self._page = None
        self._page_size = None
        self._limit = None
        self._offset = None
        self._order_direction = None
        self._institution = None
        self._published_since = None
        self._modified_since = None
        self._group = None

        if search_for is not None:
          self.search_for = search_for
        if page is not None:
          self.page = page
        if page_size is not None:
          self.page_size = page_size
        if limit is not None:
          self.limit = limit
        if offset is not None:
          self.offset = offset
        if order_direction is not None:
          self.order_direction = order_direction
        if institution is not None:
          self.institution = institution
        if published_since is not None:
          self.published_since = published_since
        if modified_since is not None:
          self.modified_since = modified_since
        if group is not None:
          self.group = group

    @property
    def search_for(self):
        """
        Gets the search_for of this CommonSearch.
        Search term

        :return: The search_for of this CommonSearch.
        :rtype: str
        """
        return self._search_for

    @search_for.setter
    def search_for(self, search_for):
        """
        Sets the search_for of this CommonSearch.
        Search term

        :param search_for: The search_for of this CommonSearch.
        :type: str
        """

        self._search_for = search_for

    @property
    def page(self):
        """
        Gets the page of this CommonSearch.
        Page number. Used for pagination with page_size

        :return: The page of this CommonSearch.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this CommonSearch.
        Page number. Used for pagination with page_size

        :param page: The page of this CommonSearch.
        :type: int
        """
        if page is not None and page > 5000:
            raise ValueError("Invalid value for `page`, must be a value less than or equal to `5000`")
        if page is not None and page < 1:
            raise ValueError("Invalid value for `page`, must be a value greater than or equal to `1`")

        self._page = page

    @property
    def page_size(self):
        """
        Gets the page_size of this CommonSearch.
        The number of results included on a page. Used for pagination with page

        :return: The page_size of this CommonSearch.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this CommonSearch.
        The number of results included on a page. Used for pagination with page

        :param page_size: The page_size of this CommonSearch.
        :type: int
        """
        if page_size is not None and page_size > 1000:
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `1000`")
        if page_size is not None and page_size < 1:
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `1`")

        self._page_size = page_size

    @property
    def limit(self):
        """
        Gets the limit of this CommonSearch.
        Number of results included on a page. Used for pagination with query

        :return: The limit of this CommonSearch.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CommonSearch.
        Number of results included on a page. Used for pagination with query

        :param limit: The limit of this CommonSearch.
        :type: int
        """
        if limit is not None and limit > 1000:
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `1000`")
        if limit is not None and limit < 1:
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `1`")

        self._limit = limit

    @property
    def offset(self):
        """
        Gets the offset of this CommonSearch.
        Where to start the listing(the offset of the first result). Used for pagination with limit

        :return: The offset of this CommonSearch.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this CommonSearch.
        Where to start the listing(the offset of the first result). Used for pagination with limit

        :param offset: The offset of this CommonSearch.
        :type: int
        """
        if offset is not None and offset > 5000:
            raise ValueError("Invalid value for `offset`, must be a value less than or equal to `5000`")
        if offset is not None and offset < 0:
            raise ValueError("Invalid value for `offset`, must be a value greater than or equal to `0`")

        self._offset = offset

    @property
    def order_direction(self):
        """
        Gets the order_direction of this CommonSearch.
        Direction of ordering

        :return: The order_direction of this CommonSearch.
        :rtype: str
        """
        return self._order_direction

    @order_direction.setter
    def order_direction(self, order_direction):
        """
        Sets the order_direction of this CommonSearch.
        Direction of ordering

        :param order_direction: The order_direction of this CommonSearch.
        :type: str
        """
        allowed_values = ["asc", "desc"]
        if order_direction not in allowed_values:
            raise ValueError(
                "Invalid value for `order_direction` ({0}), must be one of {1}"
                .format(order_direction, allowed_values)
            )

        self._order_direction = order_direction

    @property
    def institution(self):
        """
        Gets the institution of this CommonSearch.
        only return collections from this institution

        :return: The institution of this CommonSearch.
        :rtype: int
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """
        Sets the institution of this CommonSearch.
        only return collections from this institution

        :param institution: The institution of this CommonSearch.
        :type: int
        """

        self._institution = institution

    @property
    def published_since(self):
        """
        Gets the published_since of this CommonSearch.
        Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :return: The published_since of this CommonSearch.
        :rtype: str
        """
        return self._published_since

    @published_since.setter
    def published_since(self, published_since):
        """
        Sets the published_since of this CommonSearch.
        Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :param published_since: The published_since of this CommonSearch.
        :type: str
        """

        self._published_since = published_since

    @property
    def modified_since(self):
        """
        Gets the modified_since of this CommonSearch.
        Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :return: The modified_since of this CommonSearch.
        :rtype: str
        """
        return self._modified_since

    @modified_since.setter
    def modified_since(self, modified_since):
        """
        Sets the modified_since of this CommonSearch.
        Filter by article modified date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD

        :param modified_since: The modified_since of this CommonSearch.
        :type: str
        """

        self._modified_since = modified_since

    @property
    def group(self):
        """
        Gets the group of this CommonSearch.
        only return collections from this group

        :return: The group of this CommonSearch.
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this CommonSearch.
        only return collections from this group

        :param group: The group of this CommonSearch.
        :type: int
        """

        self._group = group

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
        if not isinstance(other, CommonSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other