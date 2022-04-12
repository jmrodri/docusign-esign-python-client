# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class BillingEntityInformationResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'billing_profile': 'str',
        'entity_name': 'str',
        'external_entity_id': 'str',
        'is_externally_billed': 'str'
    }

    attribute_map = {
        'billing_profile': 'billingProfile',
        'entity_name': 'entityName',
        'external_entity_id': 'externalEntityId',
        'is_externally_billed': 'isExternallyBilled'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """BillingEntityInformationResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._billing_profile = None
        self._entity_name = None
        self._external_entity_id = None
        self._is_externally_billed = None
        self.discriminator = None

        setattr(self, "_{}".format('billing_profile'), kwargs.get('billing_profile', None))
        setattr(self, "_{}".format('entity_name'), kwargs.get('entity_name', None))
        setattr(self, "_{}".format('external_entity_id'), kwargs.get('external_entity_id', None))
        setattr(self, "_{}".format('is_externally_billed'), kwargs.get('is_externally_billed', None))

    @property
    def billing_profile(self):
        """Gets the billing_profile of this BillingEntityInformationResponse.  # noqa: E501

          # noqa: E501

        :return: The billing_profile of this BillingEntityInformationResponse.  # noqa: E501
        :rtype: str
        """
        return self._billing_profile

    @billing_profile.setter
    def billing_profile(self, billing_profile):
        """Sets the billing_profile of this BillingEntityInformationResponse.

          # noqa: E501

        :param billing_profile: The billing_profile of this BillingEntityInformationResponse.  # noqa: E501
        :type: str
        """

        self._billing_profile = billing_profile

    @property
    def entity_name(self):
        """Gets the entity_name of this BillingEntityInformationResponse.  # noqa: E501

          # noqa: E501

        :return: The entity_name of this BillingEntityInformationResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this BillingEntityInformationResponse.

          # noqa: E501

        :param entity_name: The entity_name of this BillingEntityInformationResponse.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def external_entity_id(self):
        """Gets the external_entity_id of this BillingEntityInformationResponse.  # noqa: E501

          # noqa: E501

        :return: The external_entity_id of this BillingEntityInformationResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, external_entity_id):
        """Sets the external_entity_id of this BillingEntityInformationResponse.

          # noqa: E501

        :param external_entity_id: The external_entity_id of this BillingEntityInformationResponse.  # noqa: E501
        :type: str
        """

        self._external_entity_id = external_entity_id

    @property
    def is_externally_billed(self):
        """Gets the is_externally_billed of this BillingEntityInformationResponse.  # noqa: E501

          # noqa: E501

        :return: The is_externally_billed of this BillingEntityInformationResponse.  # noqa: E501
        :rtype: str
        """
        return self._is_externally_billed

    @is_externally_billed.setter
    def is_externally_billed(self, is_externally_billed):
        """Sets the is_externally_billed of this BillingEntityInformationResponse.

          # noqa: E501

        :param is_externally_billed: The is_externally_billed of this BillingEntityInformationResponse.  # noqa: E501
        :type: str
        """

        self._is_externally_billed = is_externally_billed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(BillingEntityInformationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BillingEntityInformationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingEntityInformationResponse):
            return True

        return self.to_dict() != other.to_dict()