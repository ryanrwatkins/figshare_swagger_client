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


class Collaborator(object):
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
        'role_name': 'str',
        'user_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'role_name': 'role_name',
        'user_id': 'user_id',
        'name': 'name'
    }

    def __init__(self, role_name=None, user_id=None, name=None):
        """
        Collaborator - a model defined in Swagger
        """

        self._role_name = None
        self._user_id = None
        self._name = None

        self.role_name = role_name
        self.user_id = user_id
        self.name = name

    @property
    def role_name(self):
        """
        Gets the role_name of this Collaborator.
        Collaborator role

        :return: The role_name of this Collaborator.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """
        Sets the role_name of this Collaborator.
        Collaborator role

        :param role_name: The role_name of this Collaborator.
        :type: str
        """
        if role_name is None:
            raise ValueError("Invalid value for `role_name`, must not be `None`")

        self._role_name = role_name

    @property
    def user_id(self):
        """
        Gets the user_id of this Collaborator.
        Collaborator id

        :return: The user_id of this Collaborator.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Collaborator.
        Collaborator id

        :param user_id: The user_id of this Collaborator.
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

    @property
    def name(self):
        """
        Gets the name of this Collaborator.
        Collaborator name

        :return: The name of this Collaborator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Collaborator.
        Collaborator name

        :param name: The name of this Collaborator.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, Collaborator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
