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


class CollectionDOI(object):
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
        'doi': 'str'
    }

    attribute_map = {
        'doi': 'doi'
    }

    def __init__(self, doi=None):
        """
        CollectionDOI - a model defined in Swagger
        """

        self._doi = None

        self.doi = doi

    @property
    def doi(self):
        """
        Gets the doi of this CollectionDOI.
        Reserved DOI

        :return: The doi of this CollectionDOI.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """
        Sets the doi of this CollectionDOI.
        Reserved DOI

        :param doi: The doi of this CollectionDOI.
        :type: str
        """
        if doi is None:
            raise ValueError("Invalid value for `doi`, must not be `None`")

        self._doi = doi

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
        if not isinstance(other, CollectionDOI):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
