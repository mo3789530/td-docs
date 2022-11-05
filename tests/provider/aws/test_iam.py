import json
import unittest

import src.provider.aws.iam


class TestAwsIam(unittest.TestCase):

    def test_parse(self):
        json_str = """
        {"attributes": {}}
        """

        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_policy")
        # It should be return "aws_iam_policy"
        self.assertEqual(res.get("type"), "aws_iam_policy")
        # It should be return None when iam type is not defind
        res = iam.parse(json={}, iam_type="test_iam_none")
        self.assertEqual(res.get("type"), None)

    def test_role_parse(self):
        json_str = """
                {
                    "index_key": 0,
                    "schema_version": 0,
                    "attributes": {
                        "arn": "arn:aws:iam::552883280992:role/octopusx-grid-520201111113220197100000002",
                        "assume_role_policy": {"Version":"2012-10-17","Statement":[{"Sid":"EKSClusterAssumeRole","Effect":"Allow","Principal":{"Service":"eks.amazonaws.com"},"Action":"sts:AssumeRole"}]},
                        "create_date": "2020-11-11T11:32:21Z",
                        "description": "",
                        "force_detach_policies": true,
                        "id": "octopusx-grid-520201111113220197100000002",
                        "max_session_duration": 3600,
                        "name": "octopusx-grid-520201111113220197100000002",
                        "name_prefix": "octopusx-grid-5",
                        "path": "/",
                        "permissions_boundary": null,
                        "tags": {
                            "Environment": "sandbox"
                        },
                        "unique_id": "AROAYBOTJLRQKDQ4AOSHJ"
                    },
                    "private": "bnVsbA==",
                    "dependencies": [
                        "module.eks.data.aws_iam_policy_document.cluster_assume_role_policy"
                    ],
                    "create_before_destroy": true
                }
        """
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_role")
        self.assertEqual(res.get(
            "arn"), "arn:aws:iam::552883280992:role/octopusx-grid-520201111113220197100000002")

    def test_policy_parse2(self):
        json_str = """
        {
          "index_key": 0,
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:iam::552883280992:policy/octopusx-grid-5-elb-sl-role-creation20201111113220197000000001",
            "description": "Permissions for EKS to create AWSServiceRoleForElasticLoadBalancing service-linked role",
            "id": "arn:aws:iam::552883280992:policy/octopusx-grid-5-elb-sl-role-creation20201111113220197000000001",
            "name": "octopusx-grid-5-elb-sl-role-creation20201111113220197000000001",
            "name_prefix": "octopusx-grid-5-elb-sl-role-creation",
            "path": "/",
            "policy": {  "Version": "2012-10-17",  "Statement": [    {      "Sid": "",      "Effect": "Allow",      "Action": [        "ec2:DescribeInternetGateways",        "ec2:DescribeAccountAttributes"      ],      "Resource": "*"    }  ]}
          },
          "private": "bnVsbA==",
          "dependencies": [
            "module.eks.data.aws_iam_policy_document.cluster_elb_sl_role_creation"
          ]
        }
        """
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_policy")
        self.assertEqual(res.get("schema_version"), 0)
        self.assertEqual(
            res.get("arn"), "arn:aws:iam::552883280992:policy/octopusx-grid-5-elb-sl-role-creation20201111113220197000000001")
        self.assertEqual(res.get(
            "name"), "octopusx-grid-5-elb-sl-role-creation20201111113220197000000001")
        self.assertEqual(res.get("none"), None)

    def test_plicy_document_parser(self):
        json_str = '''
        {
                    "schema_version": 0,
                    "attributes": {
                        "id": "3778018924",
                        "json": { "Version": "2012-10-17", "Statement": [   {     "Sid": "EKSWorkerAssumeRole",     "Effect": "Allow",     "Action": "sts:AssumeRole",     "Principal": {       "Service": "ec2.amazonaws.com"     }   } ]},
                        "override_json": null,
                        "policy_id": null,
                        "source_json": null,
                        "statement": [
                            {
                                "actions": [
                                    "sts:AssumeRole"
                                ],
                                "condition": [],
                                "effect": "Allow",
                                "not_actions": [],
                                "not_principals": [],
                                "not_resources": [],
                                "principals": [
                                    {
                                        "identifiers": [
                                            "ec2.amazonaws.com"
                                        ],
                                        "type": "Service"
                                    }
                                ],
                                "resources": [],
                                "sid": "EKSWorkerAssumeRole"
                            }
                        ],
                        "version": "2012-10-17"
                    }
        }
        '''
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_policy_document")
        self.assertEqual(res.get("schema_version"), 0)
        self.assertEqual(res.get("statement"), data["attributes"]["statement"])
        self.assertEqual(res.get("none"), None)

    def test_policy_parse(self):
        json_str = """
        {
          "index_key": 0,
          "schema_version": 0,
          "attributes": {
            "arn": "arn:aws:iam::552883280992:policy/octopusx-grid-5-elb-sl-role-creation20201111113220197000000001",
            "description": "Permissions for EKS to create AWSServiceRoleForElasticLoadBalancing service-linked role",
            "id": "arn:aws:iam::552883280992:policy/octopusx-grid-5-elb-sl-role-creation20201111113220197000000001",
            "name": "octopusx-grid-5-elb-sl-role-creation20201111113220197000000001",
            "name_prefix": "octopusx-grid-5-elb-sl-role-creation",
            "path": "/",
            "policy": {  "Version": "2012-10-17",  "Statement": [    {      "Sid": "",      "Effect": "Allow",      "Action": [        "ec2:DescribeInternetGateways",        "ec2:DescribeAccountAttributes"      ],      "Resource": "*"    }  ]}
          },
          "private": "bnVsbA==",
          "dependencies": [
            "module.eks.data.aws_iam_policy_document.cluster_elb_sl_role_creation"
          ]
        }
        """
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_policy")
        self.assertEqual(res.get("schema_version"), 0)
        self.assertEqual(
            res.get("arn"), "arn:aws:iam::552883280992:policy/octopusx-grid-5-elb-sl-role-creation20201111113220197000000001")
        self.assertEqual(res.get(
            "name"), "octopusx-grid-5-elb-sl-role-creation20201111113220197000000001")
        self.assertEqual(res.get("none"), None)

    def test_iam_policy_attachment(self):
        json_str = '''
                        {
                    "schema_version": 0,
                    "attributes": {
                        "groups": [],
                        "id": "Aleidy-us-east-1-dev-iamPolicy",
                        "name": "Aleidy-us-east-1-dev-iamPolicy",
                        "policy_arn": "arn:aws:iam::862989290375:policy/Aleidy-us-east-1-dev-ec2Policy",
                        "roles": [
                            "Aleidy-us-east-1-dev-ec2_role"
                        ],
                        "users": []
                    },
                    "private": "bnVsbA==",
                    "dependencies": [
                        "module.ecs_module.aws_iam_policy.ec2_policy",
                        "module.ecs_module.aws_iam_role.ec2-role"
                    ]
                }
        '''
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_policy_attachment")
        self.assertEqual(res.get("schema_version"), 0)
        self.assertEqual(res.get("id"), "Aleidy-us-east-1-dev-iamPolicy")
        self.assertEqual(res.get("none"), None)

    def test_iam_user_parser(self):
        json_str = '''
                {
                    "index_key": 0,
                    "schema_version": 0,
                    "attributes": {
                        "arn": "arn:aws:iam::932716035065:user/admin-accessall",
                        "force_destroy": false,
                        "id": "admin-accessall",
                        "name": "admin-accessall",
                        "path": "/",
                        "permissions_boundary": null,
                        "tags": {
                            "Stage": "Test"
                        },
                        "unique_id": "AIDA5SKRVHP4UT6QCU64A"
                    },
                    "private": "bnVsbA=="
                }
        '''
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_user")
        self.assertEqual(res.get("schema_version"), 0)
        self.assertEqual(
            res.get("arn"), "arn:aws:iam::932716035065:user/admin-accessall")
        self.assertEqual(res.get("none"), None)

    def test_iam_user_policy_attachment_parser(self):
        json_str = '''
                {
                    "schema_version": 0,
                    "attributes": {
                        "id": "loadbalancer-2020111317225517310000000a",
                        "policy_arn": "arn:aws:iam::526954929923:policy/test2",
                        "user": "loadbalancer"
                    },
                    "private": "bnVsbA==",
                    "dependencies": [
                        "aws_iam_policy.test_ro2",
                        "aws_iam_user.test"
                    ]
                }
        '''
        data = json.loads(json_str)
        iam = src.provider.aws.iam.Iam()

        res = iam.parse(json=data, iam_type="aws_iam_user_policy_attachment")
        self.assertEqual(res.get("schema_version"), 0)
        self.assertEqual(
            res.get("id"), "loadbalancer-2020111317225517310000000a")
        self.assertEqual(res.get("none"), None)
