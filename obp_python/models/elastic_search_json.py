# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2023. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from obp_python.configuration import Configuration


class ElasticSearchJSON(object):
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
        'metrics': 'list[MetricsJSON]',
        'warehouse': 'list[WarehouseJSON]'
    }

    attribute_map = {
        'metrics': 'metrics',
        'warehouse': 'warehouse'
    }

    def __init__(self, metrics=None, warehouse=None, _configuration=None):  # noqa: E501
        """ElasticSearchJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metrics = None
        self._warehouse = None
        self.discriminator = None

        self.metrics = metrics
        self.warehouse = warehouse

    @property
    def metrics(self):
        """Gets the metrics of this ElasticSearchJSON.  # noqa: E501


        :return: The metrics of this ElasticSearchJSON.  # noqa: E501
        :rtype: list[MetricsJSON]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ElasticSearchJSON.


        :param metrics: The metrics of this ElasticSearchJSON.  # noqa: E501
        :type: list[MetricsJSON]
        """
        if self._configuration.client_side_validation and metrics is None:
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def warehouse(self):
        """Gets the warehouse of this ElasticSearchJSON.  # noqa: E501


        :return: The warehouse of this ElasticSearchJSON.  # noqa: E501
        :rtype: list[WarehouseJSON]
        """
        return self._warehouse

    @warehouse.setter
    def warehouse(self, warehouse):
        """Sets the warehouse of this ElasticSearchJSON.


        :param warehouse: The warehouse of this ElasticSearchJSON.  # noqa: E501
        :type: list[WarehouseJSON]
        """
        if self._configuration.client_side_validation and warehouse is None:
            raise ValueError("Invalid value for `warehouse`, must not be `None`")  # noqa: E501

        self._warehouse = warehouse

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
        if issubclass(ElasticSearchJSON, dict):
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
        if not isinstance(other, ElasticSearchJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElasticSearchJSON):
            return True

        return self.to_dict() != other.to_dict()