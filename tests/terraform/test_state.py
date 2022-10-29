import unittest
import json
import src.provider.terraform.state as state

class TestState(unittest.TestCase):

    json = '''
    {
        "version": 4,
        "terraform_version": "0.13.3",
        "serial": 9,
        "lineage": "4afbb278-c8a6-6e81-4ed6-73a3d56bded2",
        "outputs": {
            "cluster_name": {
            "value": "octopusx-grid-5",
            "type": "string"
            },
            "region": {
            "value": "eu-west-1",
            "type": "string"
            }
        },
        "resources": []
    }
    '''

    def test_parse(self):
        # print(self.json)
        parser = state.State()
        dic = parser.parse(json.loads(self.json))
        self.assertEqual(dic["version"], 4)
        self.assertEqual(dic["region"], "eu-west-1")


if __name__ == "__main__":
    unittest.main()
