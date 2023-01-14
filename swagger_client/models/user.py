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


class User(object):
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
        'first_name': 'str',
        'last_name': 'str',
        'name': 'str',
        'is_active': 'bool',
        'url_name': 'str',
        'is_public': 'bool',
        'job_title': 'str',
        'orcid_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'name': 'name',
        'is_active': 'is_active',
        'url_name': 'url_name',
        'is_public': 'is_public',
        'job_title': 'job_title',
        'orcid_id': 'orcid_id'
    }

    def __init__(self, id=None, first_name=None, last_name=None, name=None, is_active=None, url_name=None, is_public=None, job_title=None, orcid_id=None):
        """
        User - a model defined in Swagger
        """

        self._id = None
        self._first_name = None
        self._last_name = None
        self._name = None
        self._is_active = None
        self._url_name = None
        self._is_public = None
        self._job_title = None
        self._orcid_id = None

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.name = name
        self.is_active = is_active
        self.url_name = url_name
        self.is_public = is_public
        self.job_title = job_title
        self.orcid_id = orcid_id

    @property
    def id(self):
        """
        Gets the id of this User.
        User id

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        User id

        :param id: The id of this User.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def first_name(self):
        """
        Gets the first_name of this User.
        First Name

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.
        First Name

        :param first_name: The first_name of this User.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this User.
        Last Name

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.
        Last Name

        :param last_name: The last_name of this User.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def name(self):
        """
        Gets the name of this User.
        Full Name

        :return: The name of this User.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this User.
        Full Name

        :param name: The name of this User.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def is_active(self):
        """
        Gets the is_active of this User.
        Account activity status

        :return: The is_active of this User.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this User.
        Account activity status

        :param is_active: The is_active of this User.
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")

        self._is_active = is_active

    @property
    def url_name(self):
        """
        Gets the url_name of this User.
        Name that appears in website url

        :return: The url_name of this User.
        :rtype: str
        """
        return self._url_name

    @url_name.setter
    def url_name(self, url_name):
        """
        Sets the url_name of this User.
        Name that appears in website url

        :param url_name: The url_name of this User.
        :type: str
        """
        if url_name is None:
            raise ValueError("Invalid value for `url_name`, must not be `None`")

        self._url_name = url_name

    @property
    def is_public(self):
        """
        Gets the is_public of this User.
        Account public status

        :return: The is_public of this User.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this User.
        Account public status

        :param is_public: The is_public of this User.
        :type: bool
        """
        if is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")

        self._is_public = is_public

    @property
    def job_title(self):
        """
        Gets the job_title of this User.
        User Job title

        :return: The job_title of this User.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this User.
        User Job title

        :param job_title: The job_title of this User.
        :type: str
        """
        if job_title is None:
            raise ValueError("Invalid value for `job_title`, must not be `None`")

        self._job_title = job_title

    @property
    def orcid_id(self):
        """
        Gets the orcid_id of this User.
        Orcid associated to this User

        :return: The orcid_id of this User.
        :rtype: str
        """
        return self._orcid_id

    @orcid_id.setter
    def orcid_id(self, orcid_id):
        """
        Sets the orcid_id of this User.
        Orcid associated to this User

        :param orcid_id: The orcid_id of this User.
        :type: str
        """
        if orcid_id is None:
            raise ValueError("Invalid value for `orcid_id`, must not be `None`")

        self._orcid_id = orcid_id

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
