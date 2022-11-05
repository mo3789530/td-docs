import json
import unittest

import src.provider.aws.rds


class TestAwsRds(unittest.TestCase):

    def test_cluster_instance_parser(self):
        json_str = """
        {
                    "schema_version": 1,
                    "attributes": {
                        "address": "mydb.cp8yktnnyp49.eu-west-3.rds.amazonaws.com",
                        "allocated_storage": 10,
                        "allow_major_version_upgrade": null,
                        "apply_immediately": null,
                        "arn": "arn:aws:rds:eu-west-3:903584233714:db:mydb",
                        "auto_minor_version_upgrade": true,
                        "availability_zone": "eu-west-3b",
                        "backup_retention_period": 0,
                        "backup_window": "11:15-11:45",
                        "ca_cert_identifier": "rds-ca-2019",
                        "character_set_name": null,
                        "copy_tags_to_snapshot": false,
                        "db_subnet_group_name": "terraform-20210518092620686100000002",
                        "delete_automated_backups": true,
                        "deletion_protection": false,
                        "domain": "",
                        "domain_iam_role_name": "",
                        "enabled_cloudwatch_logs_exports": null,
                        "endpoint": "mydb.cp8yktnnyp49.eu-west-3.rds.amazonaws.com:5432",
                        "engine": "postgres",
                        "engine_version": "12.5",
                        "final_snapshot_identifier": null,
                        "hosted_zone_id": "ZMESEXB7ZGGQ3",
                        "iam_database_authentication_enabled": false,
                        "id": "mydb",
                        "identifier": "mydb",
                        "identifier_prefix": null,
                        "instance_class": "db.t2.micro",
                        "iops": 0,
                        "kms_key_id": "",
                        "latest_restorable_time": "0001-01-01T00:00:00Z",
                        "license_model": "postgresql-license",
                        "maintenance_window": "sat:05:54-sat:06:24",
                        "max_allocated_storage": 0,
                        "monitoring_interval": 0,
                        "monitoring_role_arn": "",
                        "multi_az": false,
                        "name": "testdb",
                        "option_group_name": "default:postgres-12",
                        "parameter_group_name": "default.postgres12",
                        "password": "!Jupiter",
                        "performance_insights_enabled": false,
                        "performance_insights_kms_key_id": "",
                        "performance_insights_retention_period": 0,
                        "port": 5432,
                        "publicly_accessible": true,
                        "replicas": [],
                        "replicate_source_db": "",
                        "resource_id": "db-UEPUG2WK2I74DC3R2SAW6UYTZE",
                        "restore_to_point_in_time": [],
                        "s3_import": [],
                        "security_group_names": null,
                        "skip_final_snapshot": true,
                        "snapshot_identifier": null,
                        "status": "available",
                        "storage_encrypted": false,
                        "storage_type": "gp2",
                        "tags": null,
                        "tags_all": {},
                        "timeouts": null,
                        "timezone": "",
                        "username": "root",
                        "vpc_security_group_ids": [
                            "sg-0a2cb79bcd2ae7c9b"
                        ]
                    },
                    "sensitive_attributes": [],
                    "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjoyNDAwMDAwMDAwMDAwLCJkZWxldGUiOjM2MDAwMDAwMDAwMDAsInVwZGF0ZSI6NDgwMDAwMDAwMDAwMH0sInNjaGVtYV92ZXJzaW9uIjoiMSJ9",
                    "dependencies": [
                        "aws_db_subnet_group.subn-groups",
                        "aws_security_group.elb-sg",
                        "aws_security_group.rds-sg",
                        "aws_security_group.web-sg",
                        "aws_subnet.privada1",
                        "aws_subnet.privada2",
                        "aws_vpc.vpc",
                        "data.aws_availability_zones.az"
                    ]
                }
        """

        data = json.loads(json_str)
        rds = src.provider.aws.rds.Rds()
        res = rds.db_instance_parser(json=data, rds_type="")
        self.assertEqual(0, res.get("backup_retention_period", 100))
        self.assertEqual("mydb", res.get("id", ""))
        self.assertEqual(
            "mydb.cp8yktnnyp49.eu-west-3.rds.amazonaws.com", res.get("address", ""))

    def test_db_instance_parser(self):
        json_str = """
        {
                    "schema_version": 1,
                    "attributes": {
                        "address": "mydb.cp8yktnnyp49.eu-west-3.rds.amazonaws.com",
                        "allocated_storage": 10,
                        "allow_major_version_upgrade": null,
                        "apply_immediately": null,
                        "arn": "arn:aws:rds:eu-west-3:903584233714:db:mydb",
                        "auto_minor_version_upgrade": true,
                        "availability_zone": "eu-west-3b",
                        "backup_retention_period": 0,
                        "backup_window": "11:15-11:45",
                        "ca_cert_identifier": "rds-ca-2019",
                        "character_set_name": null,
                        "copy_tags_to_snapshot": false,
                        "db_subnet_group_name": "terraform-20210518092620686100000002",
                        "delete_automated_backups": true,
                        "deletion_protection": false,
                        "domain": "",
                        "domain_iam_role_name": "",
                        "enabled_cloudwatch_logs_exports": null,
                        "endpoint": "mydb.cp8yktnnyp49.eu-west-3.rds.amazonaws.com:5432",
                        "engine": "postgres",
                        "engine_version": "12.5",
                        "final_snapshot_identifier": null,
                        "hosted_zone_id": "ZMESEXB7ZGGQ3",
                        "iam_database_authentication_enabled": false,
                        "id": "mydb",
                        "identifier": "mydb",
                        "identifier_prefix": null,
                        "instance_class": "db.t2.micro",
                        "iops": 0,
                        "kms_key_id": "",
                        "latest_restorable_time": "0001-01-01T00:00:00Z",
                        "license_model": "postgresql-license",
                        "maintenance_window": "sat:05:54-sat:06:24",
                        "max_allocated_storage": 0,
                        "monitoring_interval": 0,
                        "monitoring_role_arn": "",
                        "multi_az": false,
                        "name": "testdb",
                        "option_group_name": "default:postgres-12",
                        "parameter_group_name": "default.postgres12",
                        "password": "!Jupiter",
                        "performance_insights_enabled": false,
                        "performance_insights_kms_key_id": "",
                        "performance_insights_retention_period": 0,
                        "port": 5432,
                        "publicly_accessible": true,
                        "replicas": [],
                        "replicate_source_db": "",
                        "resource_id": "db-UEPUG2WK2I74DC3R2SAW6UYTZE",
                        "restore_to_point_in_time": [],
                        "s3_import": [],
                        "security_group_names": null,
                        "skip_final_snapshot": true,
                        "snapshot_identifier": null,
                        "status": "available",
                        "storage_encrypted": false,
                        "storage_type": "gp2",
                        "tags": null,
                        "tags_all": {},
                        "timeouts": null,
                        "timezone": "",
                        "username": "root",
                        "vpc_security_group_ids": [
                            "sg-0a2cb79bcd2ae7c9b"
                        ]
                    },
                    "sensitive_attributes": [],
                    "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjoyNDAwMDAwMDAwMDAwLCJkZWxldGUiOjM2MDAwMDAwMDAwMDAsInVwZGF0ZSI6NDgwMDAwMDAwMDAwMH0sInNjaGVtYV92ZXJzaW9uIjoiMSJ9",
                    "dependencies": [
                        "aws_db_subnet_group.subn-groups",
                        "aws_security_group.elb-sg",
                        "aws_security_group.rds-sg",
                        "aws_security_group.web-sg",
                        "aws_subnet.privada1",
                        "aws_subnet.privada2",
                        "aws_vpc.vpc",
                        "data.aws_availability_zones.az"
                    ]
                }
        """

        data = json.loads(json_str)
        rds = src.provider.aws.rds.Rds()
        res = rds.db_instance_parser(json=data, rds_type="")
        self.assertEqual(0, res.get("backup_retention_period", 100))
        self.assertEqual("mydb", res.get("id", ""))
        self.assertEqual(
            "mydb.cp8yktnnyp49.eu-west-3.rds.amazonaws.com", res.get("address", ""))

    def test_rds_cluster_parser(self):
        json_str = """
        {
                    "schema_version": 0,
                    "attributes": {
                        "apply_immediately": null,
                        "arn": "arn:aws:rds:us-east-1:616100519737:cluster:sandbox-database-cluster",
                        "availability_zones": [
                            "us-east-1a",
                            "us-east-1c",
                            "us-east-1e"
                        ],
                        "backtrack_window": 0,
                        "backup_retention_period": 7,
                        "cluster_identifier": "sandbox-database-cluster",
                        "cluster_identifier_prefix": null,
                        "cluster_members": [
                            "sandbox-database"
                        ],
                        "cluster_resource_id": "cluster-PSSB3S753RXCVO23RRODDRIBME",
                        "copy_tags_to_snapshot": false,
                        "database_name": "avior",
                        "db_cluster_parameter_group_name": "default.aurora5.6",
                        "db_subnet_group_name": "default",
                        "deletion_protection": false,
                        "enable_http_endpoint": false,
                        "enabled_cloudwatch_logs_exports": [],
                        "endpoint": "sandbox-database-cluster.cluster-c9tifqxuh1z2.us-east-1.rds.amazonaws.com",
                        "engine": "aurora",
                        "engine_mode": "provisioned",
                        "engine_version": "5.6.10a",
                        "final_snapshot_identifier": null,
                        "global_cluster_identifier": "",
                        "hosted_zone_id": "Z2R2ITUGPM61AM",
                        "iam_database_authentication_enabled": false,
                        "iam_roles": [],
                        "id": "sandbox-database-cluster",
                        "kms_key_id": "",
                        "master_password": null,
                        "master_username": "root",
                        "port": 3306,
                        "preferred_backup_window": "04:00-06:00",
                        "preferred_maintenance_window": "sat:00:00-sat:02:00",
                        "reader_endpoint": "sandbox-database-cluster.cluster-ro-c9tifqxuh1z2.us-east-1.rds.amazonaws.com",
                        "replication_source_identifier": "",
                        "s3_import": [],
                        "scaling_configuration": [],
                        "skip_final_snapshot": true,
                        "snapshot_identifier": null,
                        "source_region": null,
                        "storage_encrypted": false,
                        "tags": {},
                        "timeouts": {
                            "create": null,
                            "delete": null,
                            "update": null
                        },
                        "vpc_security_group_ids": [
                            "sg-aa0cffeb"
                        ]
                    },
                    "private": "eyJlMmJmYjczMC1lY2FhLTExZTYtOGY4OC0zNDM2M2JjN2M0YzAiOnsiY3JlYXRlIjo3MjAwMDAwMDAwMDAwLCJkZWxldGUiOjcyMDAwMDAwMDAwMDAsInVwZGF0ZSI6NzIwMDAwMDAwMDAwMH0sInNjaGVtYV92ZXJzaW9uIjoiMCJ9"
                }
        """

        data = json.loads(json_str)
        rds = src.provider.aws.rds.Rds()
        res = rds.rds_cluster_parser(json=data, rds_type="")
        self.assertEqual(7, res.get("backup_retention_period", 100))
        self.assertEqual("avior", res.get("database_name", ""))
