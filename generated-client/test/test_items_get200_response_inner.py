# coding: utf-8

"""
    Sample API

    A sample API for testing OpenAPI specifications

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.items_get200_response_inner import ItemsGet200ResponseInner

class TestItemsGet200ResponseInner(unittest.TestCase):
    """ItemsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemsGet200ResponseInner:
        """Test ItemsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemsGet200ResponseInner`
        """
        model = ItemsGet200ResponseInner()
        if include_optional:
            return ItemsGet200ResponseInner(
                id = 56,
                name = ''
            )
        else:
            return ItemsGet200ResponseInner(
        )
        """

    def testItemsGet200ResponseInner(self):
        """Test ItemsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
