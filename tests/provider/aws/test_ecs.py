import json
import unittest

import src.provider.aws.ecs


class TestAwsEcs(unittest.TestCase):
    def test_ecs_task_definition_parse(self):
        json_str = """
        {
            "schema_version": 1,
            "attributes": {
                "arn": "arn:aws:ecs:eu-central-1:836906079004:task-definition/stan-aws-terraform-definition:8",
                "cpu": "1024",
                "ephemeral_storage": [],
                "execution_role_arn": "arn:aws:iam::836906079004:role/stan-aws-terraform-execution-task-role",
                "family": "stan-aws-terraform-definition",
                "id": "stan-aws-terraform-definition",
                "inference_accelerator": [],
                "ipc_mode": "",
                "memory": "512",
                "network_mode": "",
                "pid_mode": "",
                "placement_constraints": [],
                "proxy_configuration": [],
                "requires_compatibilities": null,
                "revision": 8,
                "runtime_platform": [],
                "skip_destroy": false,
                "tags": null,
                "tags_all": {},
                "task_role_arn": "arn:aws:iam::836906079004:role/stan-aws-terraform-execution-task-role",
                "volume": []
            },
            "sensitive_attributes": [],
            "private": "eyJzY2hlbWFfdmVyc2lvbiI6IjEifQ==",
            "dependencies": [
                "aws_iam_role.ecsTaskExecutionRole"
            ]
        }
        """
        data = json.loads(json_str)
        ecs = src.provider.aws.ecs.Ecs()
        res = ecs.parse(json=data, ecs_type="aws_ecs_task_definition")
        self.assertEqual(res.get(
            "arn"), "arn:aws:ecs:eu-central-1:836906079004:task-definition/stan-aws-terraform-definition:8")

    def test_ecs_service_parse(self):
        pass

    def test_ecs_cluster_parse(self):
        pass
