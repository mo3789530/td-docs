import unittest
import json
import src.provider.aws.iam


class TestAwsIam(unittest.TestCase):
    json = '''
        {"type": aws_iam_instance_profile}
    '''

    def test_parse(self):
        json_str = """
        {"type": aws_iam_instance_profile, "attributes": {}}
        """

        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_instance_profile")
        self.assertEqual(res.get("type"), "aws_iam_instance_profile")
