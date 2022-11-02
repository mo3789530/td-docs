import json
import unittest

import src.provider.terraform.resource as resource


class TestResource(unittest.TestCase):
    json = '''
    {
        "resources": [
            {
                "mode": "data",
                "type": "aws_availability_zones",
                "name": "available",
                "provider": "provider[registry.terraform.io/hashicorp/aws]",
                "instances": [
                    {
                        "schema_version": 0,
                        "attributes": {}
                    }
                ]
            }
        ]
    }
    '''

    def test_parse_array(self):
        data = json.loads(self.json)
        parser = resource.Resources()
        list = parser.resource_parse(data)
        self.assertEqual(data["resources"][0]["type"], list[0]["type"])

    def test_parse(self):
        data = json.loads(self.json)
        parser = resource.Resources()
        dic = parser.parse(data["resources"][0])
        self.assertEqual(dic["type"], data["resources"][0]["type"])
        self.assertEqual(dic["provider"], "AWS")
