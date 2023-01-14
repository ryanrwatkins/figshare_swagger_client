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


class PrivateFile(object):
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
        'id': 'int',
        'name': 'str',
        'size': 'int',
        'is_link_only': 'bool',
        'download_url': 'str',
        'supplied_md5': 'str',
        'computed_md5': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'size': 'size',
        'is_link_only': 'is_link_only',
        'download_url': 'download_url',
        'supplied_md5': 'supplied_md5',
        'computed_md5': 'computed_md5'
    }

    def __init__(self, id=None, name=None, size=None, is_link_only=None, download_url=None, supplied_md5=None, computed_md5=None):
        """
        PrivateFile - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._size = None
        self._is_link_only = None
        self._download_url = None
        self._supplied_md5 = None
        self._computed_md5 = None

        self.id = id
        self.name = name
        self.size = size
        self.is_link_only = is_link_only
        self.download_url = download_url
        self.supplied_md5 = supplied_md5
        self.computed_md5 = computed_md5

    @property
    def id(self):
        """
        Gets the id of this PrivateFile.
        File id

        :return: The id of this PrivateFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateFile.
        File id

        :param id: The id of this PrivateFile.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PrivateFile.
        File name

        :return: The name of this PrivateFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PrivateFile.
        File name

        :param name: The name of this PrivateFile.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def size(self):
        """
        Gets the size of this PrivateFile.
        File size

        :return: The size of this PrivateFile.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this PrivateFile.
        File size

        :param size: The size of this PrivateFile.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size

    @property
    def is_link_only(self):
        """
        Gets the is_link_only of this PrivateFile.
        True if file is hosted somewhere else

        :return: The is_link_only of this PrivateFile.
        :rtype: bool
        """
        return self._is_link_only

    @is_link_only.setter
    def is_link_only(self, is_link_only):
        """
        Sets the is_link_only of this PrivateFile.
        True if file is hosted somewhere else

        :param is_link_only: The is_link_only of this PrivateFile.
        :type: bool
        """
        if is_link_only is None:
            raise ValueError("Invalid value for `is_link_only`, must not be `None`")

        self._is_link_only = is_link_only

    @property
    def download_url(self):
        """
        Gets the download_url of this PrivateFile.
        Url for file download

        :return: The download_url of this PrivateFile.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this PrivateFile.
        Url for file download

        :param download_url: The download_url of this PrivateFile.
        :type: str
        """
        if download_url is None:
            raise ValueError("Invalid value for `download_url`, must not be `None`")

        self._download_url = download_url

    @property
    def supplied_md5(self):
        """
        Gets the supplied_md5 of this PrivateFile.
        File supplied md5

        :return: The supplied_md5 of this PrivateFile.
        :rtype: str
        """
        return self._supplied_md5

    @supplied_md5.setter
    def supplied_md5(self, supplied_md5):
        """
        Sets the supplied_md5 of this PrivateFile.
        File supplied md5

        :param supplied_md5: The supplied_md5 of this PrivateFile.
        :type: str
        """
        if supplied_md5 is None:
            raise ValueError("Invalid value for `supplied_md5`, must not be `None`")

        self._supplied_md5 = supplied_md5

    @property
    def computed_md5(self):
        """
        Gets the computed_md5 of this PrivateFile.
        File computed md5

        :return: The computed_md5 of this PrivateFile.
        :rtype: str
        """
        return self._computed_md5

    @computed_md5.setter
    def computed_md5(self, computed_md5):
        """
        Sets the computed_md5 of this PrivateFile.
        File computed md5

        :param computed_md5: The computed_md5 of this PrivateFile.
        :type: str
        """
        if computed_md5 is None:
            raise ValueError("Invalid value for `computed_md5`, must not be `None`")

        self._computed_md5 = computed_md5

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
        if not isinstance(other, PrivateFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other