
import unittest

import src.template.awa.markdown.iam as iam


class TestTemplateIam(unittest.TestCase):
    def test_role_markdown(self):
        data = {"schema_version": 0,
                "attributes_arn": "test_arn",
                "attributes_assume_role_policy": "test_attributes_assume_role_policy",
                "attributes_description": "test_attributes_description",
                "attributes_tags": {
                    "test_tag1": "t1",
                    "test_tag2": "t2"
                },
                "dependencies": ["dependencies1",
                                 "dependencies2"]
                }
        service = iam.MarkdownTemplateAWSIam()
        dst = service.role_template(data=data, name="test_role_test")
        self.assertTrue("test_arn" in dst)
        self.assertTrue("test_role_test" in dst)
        self.assertFalse("test_attributes_assume_role_policyb" in dst)
        # print(dst)
