### aws_db_instance {{name| default("None")}}
| Items                           | values                                 |
| ------------------------------- | -------------------------------------- |
| id                              | {{data.id                              | default("None")}} |
| arn                             | {{data.arn                             | default("None")}} |
| name                            | {{data.name                            | default("None")}} |
| port                            | {{data.port                            | default("None")}} |
| tags                            | {{data.tags                            | default("None")}} |
| tags_all                        | {{data.tags_all                        | default("None")}} |
| engine                          | {{data.engine                          | default("None")}} |
| engine_version                  | {{data.engine_version                  | default("None")}} |
| address                         | {{data.address                         | default("None")}} |
| timezone                        | {{data.timezone                        | default("None")}} |
| endpoint                        | {{data.endpoint                        | default("None")}} |
| identifier                      | {{data.identifier                      | default("None")}} |
| instance_class                  | {{data.instance_class                  | default("None")}} |
| storage_type                    | {{data.storage_type                    | default("None")}} |
| storage_encrypted               | {{data.storage_encrypted               | default("None")}} |
| allocated_storage               | {{data.allocated_storage               | default("None")}} |
| publicly_accessible             | {{data.publicly_accessible             | default("None")}} |
| security_group_names            | {{data.security_group_names            | default("None")}} |
| snapshot_identifier             | {{data.snapshot_identifier             | default("None")}} |
| availability_zone               | {{data.availability_zone               | default("None")}} |
| backup_retention_period         | {{data.backup_retention_period         | default("None")}} |
| backup_window                   | {{data.backup_window                   | default("None")}} |
| delete_automated_backups        | {{data.delete_automated_backups        | default("None")}} |
| deletion_protection             | {{data.deletion_protection             | default("None")}} |
| enabled_cloudwatch_logs_exports | {{data.enabled_cloudwatch_logs_exports | default("None")}} |
| maintenance_window              | {{data.maintenance_window              | default("None")}} |
| vpc_security_group_ids          | {{data.vpc_security_group_ids          | default("None")}} |
| allow_major_version_upgrade     | {{data.allow_major_version_upgrade     | default("None")}} |
| db_subnet_group_name            | {{data.db_subnet_group_name            | default("None")}} |
| dependencies                    | {{data.dependencies                    | default("None")}} |

### aws_rds_cluster_instance {{name| default("None")}}
| Items                           | values                                 |
| ------------------------------- | -------------------------------------- |
| id                              | {{data.id                              | default("None")}} |
| arn                             | {{data.arn                             | default("None")}} |
| name                            | {{data.name                            | default("None")}} |
| port                            | {{data.port                            | default("None")}} |
| tags                            | {{data.tags                            | default("None")}} |
| tags_all                        | {{data.tags_all                        | default("None")}} |
| engine                          | {{data.engine                          | default("None")}} |
| engine_version                  | {{data.engine_version                  | default("None")}} |
| address                         | {{data.address                         | default("None")}} |
| timezone                        | {{data.timezone                        | default("None")}} |
| endpoint                        | {{data.endpoint                        | default("None")}} |
| identifier                      | {{data.identifier                      | default("None")}} |
| instance_class                  | {{data.instance_class                  | default("None")}} |
| storage_type                    | {{data.storage_type                    | default("None")}} |
| storage_encrypted               | {{data.storage_encrypted               | default("None")}} |
| allocated_storage               | {{data.allocated_storage               | default("None")}} |
| publicly_accessible             | {{data.publicly_accessible             | default("None")}} |
| db_parameter_group_name         | {{data.db_parameter_group_name         | default("None")}} |
| security_group_names            | {{data.security_group_names            | default("None")}} |
| snapshot_identifier             | {{data.snapshot_identifier             | default("None")}} |
| availability_zone               | {{data.availability_zone               | default("None")}} |
| backup_retention_period         | {{data.backup_retention_period         | default("None")}} |
| backup_window                   | {{data.backup_window                   | default("None")}} |
| delete_automated_backups        | {{data.delete_automated_backups        | default("None")}} |
| deletion_protection             | {{data.deletion_protection             | default("None")}} |
| enabled_cloudwatch_logs_exports | {{data.enabled_cloudwatch_logs_exports | default("None")}} |
| maintenance_window              | {{data.maintenance_window              | default("None")}} |
| vpc_security_group_ids          | {{data.vpc_security_group_ids          | default("None")}} |
| allow_major_version_upgrade     | {{data.allow_major_version_upgrade     | default("None")}} |
| db_subnet_group_name            | {{data.db_subnet_group_name            | default("None")}} |
| dependencies                    | {{data.dependencies                    | default("None")}} |




### aws_rds_cluster {{name| default("None")}}
| Items                           | values                                 |
| ------------------------------- | -------------------------------------- |
| arn                             | {{data.arn                             | default("None")}} |
| port                            | {{data.port                            | default("None")}} |
| tags                            | {{data.tags                            | default("None")}} |
| tags_all                        | {{data.tags_all                        | default("None")}} |
| engine                          | {{data.engine                          | default("None")}} |
| engine_version                  | {{data.engine_version                  | default("None")}} |
| endpoint                        | {{data.endpoint                        | default("None")}} |
| cluster_identifier              | {{data.cluster_identifier              | default("None")}} |
| availability_zone               | {{data.availability_zone               | default("None")}} |
| backup_retention_period         | {{data.backup_retention_period         | default("None")}} |
| backup_window                   | {{data.backup_window                   | default("None")}} |
| deletion_protection             | {{data.deletion_protection             | default("None")}} |
| vpc_security_group_ids          | {{data.vpc_security_group_ids          | default("None")}} |
| copy_tags_to_snapshot           | {{data.copy_tags_to_snapshot           | default("None")}} |
| database_name                   | {{data.database_name                   | default("None")}} |
| db_cluster_parameter_group_name | {{data.db_cluster_parameter_group_name | default("None")}} |
| skip_final_snapshot             | {{data.skip_final_snapshot             | default("None")}} |
| scaling_configuration           | {{data.scaling_configuration           | default("None")}} |
| enabled_cloudwatch_logs_exports | {{data.enabled_cloudwatch_logs_exports | default("None")}} |
| storage_encrypted               | {{data.storage_encrypted               | default("None")}} |
| db_subnet_group_name            | {{data.db_subnet_group_name            | default("None")}} |
| global_cluster_identifier       | {{data.global_cluster_identifier       | default("None")}} |


### aws_rds_cluster_parameter_group {{name| default("None")}}
| Items       | values             |
| ----------- | ------------------ |
| arn         | {{data.arn         | default("None")}} |
| tags        | {{data.tags        | default("None")}} |
| tags_all    | {{data.tags_all    | default("None")}} |
| name        | {{data.name        | default("None")}} |
| family      | {{data.family      | default("None")}} |
| parameter   | {{data.parameter   | default("None")}} |
| description | {{data.description | default("None")}} |



### aws_db_subnet_group {{name| default("None")}}
| Items        | values              |
| ------------ | ------------------- |
| id           | {{data.id           | default("None")}} |
| arn          | {{data.arn          | default("None")}} |
| tags         | {{data.tags         | default("None")}} |
| tags_all     | {{data.tags_all     | default("None")}} |
| description  | {{data.description  | default("None")}} |
| name         | {{data.name         | default("None")}} |
| subnet_ids   | {{data.subnet_ids   | default("None")}} |
| dependencies | {{data.dependencies | default("None")}} |



