import json
import unittest

import src.provider.aws.vpc


class TestAwsVpc(unittest.TestCase):
    def test_vpc_parser(self):
        json_str = """
        {
            "schema_version": 1,
            "attributes": {
                "arn": "arn:aws:ec2:us-east-1:862989290375:vpc/vpc-062aad044e883696e",
                "assign_generated_ipv6_cidr_block": false,
                "cidr_block": "10.200.0.0/16",
                "default_network_acl_id": "acl-08282e1c04805bd13",
                "default_route_table_id": "rtb-08a8be1f89cb27e37",
                "default_security_group_id": "sg-01ec034c7a7cd9113",
                "dhcp_options_id": "dopt-7f2a4e05",
                "enable_classiclink": false,
                "enable_classiclink_dns_support": false,
                "enable_dns_hostnames": false,
                "enable_dns_support": true,
                "id": "vpc-062aad044e883696e",
                "instance_tenancy": "default",
                "ipv6_association_id": "",
                "ipv6_cidr_block": "",
                "main_route_table_id": "rtb-08a8be1f89cb27e37",
                "owner_id": "862989290375",
                "tags": {
                    "Deployment_Method": "terraform",
                    "name": "Aleidy-us-east-1-dev-vpc"
                }
            },
            "private": "eyJzY2hlbWFfdmVyc2lvbiI6IjEifQ==",
            "create_before_destroy": true
        }
        """

        data = json.loads(json_str)
        vpc = src.provider.aws.vpc.Vpc()
        res = vpc.aws_vpc_parse(json=data, vpc_type="")
        self.assertEqual(
            res.get("arn"), "arn:aws:ec2:us-east-1:862989290375:vpc/vpc-062aad044e883696e")
