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


class ShortCustomField(object):
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
        'field_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'field_type': 'field_type'
    }

    def __init__(self, id=None, name=None, field_type=None):
        """
        ShortCustomField - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._field_type = None

        self.id = id
        self.name = name
        self.field_type = field_type

    @property
    def id(self):
        """
        Gets the id of this ShortCustomField.
        Custom field id

        :return: The id of this ShortCustomField.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ShortCustomField.
        Custom field id

        :param id: The id of this ShortCustomField.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ShortCustomField.
        Custom field name

        :return: The name of this ShortCustomField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ShortCustomField.
        Custom field name

        :param name: The name of this ShortCustomField.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def field_type(self):
        """
        Gets the field_type of this ShortCustomField.
        Custom field type

        :return: The field_type of this ShortCustomField.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """
        Sets the field_type of this ShortCustomField.
        Custom field type

        :param field_type: The field_type of this ShortCustomField.
        :type: str
        """
        if field_type is None:
            raise ValueError("Invalid value for `field_type`, must not be `None`")
        allowed_values = ["text", "textarea", "dropdown", "url", "email", "date", "dropdown_large_list"]
        if field_type not in allowed_values:
            raise ValueError(
                "Invalid value for `field_type` ({0}), must be one of {1}"
                .format(field_type, allowed_values)
            )

        self._field_type = field_type

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
        if not isinstance(other, ShortCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other