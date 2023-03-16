import json
import unittest

import src.provider.terraform.state as state


class TestState(unittest.TestCase):

    json = '''
    {
        "format_version": "1.0",
        "terraform_version": "1.3.9",
        "values": {
            "root_module": {
                "resources": [
                    {}
                ]
            }
        }
    }
    '''

    def test_parse(self):
        # print(self.json)
        parser = state.State()
        dic = parser.parse(json.loads(self.json))
        print(dic)
        self.assertEqual(dic["version"], '1.0')


if __name__ == "__main__":
    unittest.main()
