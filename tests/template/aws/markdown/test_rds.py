
import unittest

import src.template.awa.markdown.rds as rds


class TestTemplateIam(unittest.TestCase):
    def test_rds_cluster_markdown(self):
        data = {"engine_version": "test_engine_version"}
        service = rds.MarkdownTemplateAWSRds()
        dst = service.rds_cluster_template(
            data=data, name="test_rds_test", rds_type="aws_rds_cluster")
        self.assertTrue("engine_version" in dst)
        self.assertTrue("aws_rds_cluster" in dst)
        # print(dst)
