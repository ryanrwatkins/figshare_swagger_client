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


class AccountUpdate(object):
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
        'group_id': 'int',
        'is_active': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'is_active': 'is_active'
    }

    def __init__(self, group_id=None, is_active=None):
        """
        AccountUpdate - a model defined in Swagger
        """

        self._group_id = None
        self._is_active = None

        self.group_id = group_id
        self.is_active = is_active

    @property
    def group_id(self):
        """
        Gets the group_id of this AccountUpdate.
        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups

        :return: The group_id of this AccountUpdate.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this AccountUpdate.
        Not applicable to regular users. This field is reserved to institutions/publishers with access to assign to specific groups

        :param group_id: The group_id of this AccountUpdate.
        :type: int
        """
        if group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")

        self._group_id = group_id

    @property
    def is_active(self):
        """
        Gets the is_active of this AccountUpdate.
        Is account active

        :return: The is_active of this AccountUpdate.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this AccountUpdate.
        Is account active

        :param is_active: The is_active of this AccountUpdate.
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")

        self._is_active = is_active

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
        if not isinstance(other, AccountUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other