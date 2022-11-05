### aws_db_instance {{name}}
| Items                           | values                                   |
| ------------------------------- | ---------------------------------------- |
| id                              | {{data.id}}                              |
| arn                             | {{data.arn}}                             |
| name                            | {{data.name}}                            |
| port                            | {{data.port}}                            |
| tags                            | {{data.tags}}                            |
| tags_all                        | {{data.tags_all}}                        |
| engine                          | {{data.engine}}                          |
| engine_version                  | {{data.engine_version}}                  |
| address                         | {{data.address}}                         |
| timezone                        | {{data.timezone}}                        |
| endpoint                        | {{data.endpoint}}                        |
| identifier                      | {{data.identifier}}                      |
| instance_class                  | {{data.instance_class}}                  |
| storage_type                    | {{data.storage_type}}                    |
| storage_encrypted               | {{data.storage_encrypted}}               |
| allocated_storage               | {{data.allocated_storage}}               |
| publicly_accessible             | {{data.publicly_accessible}}             |
| security_group_names            | {{data.security_group_names}}            |
| snapshot_identifier             | {{data.snapshot_identifier}}             |
| availability_zone               | {{data.availability_zone}}               |
| backup_retention_period         | {{data.backup_retention_period}}         |
| backup_window                   | {{data.backup_window}}                   |
| delete_automated_backups        | {{data.delete_automated_backups}}        |
| deletion_protection             | {{data.deletion_protection}}             |
| enabled_cloudwatch_logs_exports | {{data.enabled_cloudwatch_logs_exports}} |
| maintenance_window              | {{data.maintenance_window}}              |
| vpc_security_group_ids          | {{data.vpc_security_group_ids}}          |
| allow_major_version_upgrade     | {{data.allow_major_version_upgrade}}     |
| db_subnet_group_name            | {{data.db_subnet_group_name}}            |
| dependencies                    | {{data.dependencies}}                    |

### aws_rds_cluster_instance {{name}}
| Items                           | values                                   |
| ------------------------------- | ---------------------------------------- |
| id                              | {{data.id}}                              |
| arn                             | {{data.arn}}                             |
| name                            | {{data.name}}                            |
| port                            | {{data.port}}                            |
| tags                            | {{data.tags}}                            |
| tags_all                        | {{data.tags_all}}                        |
| engine                          | {{data.engine}}                          |
| engine_version                  | {{data.engine_version}}                  |
| address                         | {{data.address}}                         |
| timezone                        | {{data.timezone}}                        |
| endpoint                        | {{data.endpoint}}                        |
| identifier                      | {{data.identifier}}                      |
| instance_class                  | {{data.instance_class}}                  |
| storage_type                    | {{data.storage_type}}                    |
| storage_encrypted               | {{data.storage_encrypted}}               |
| allocated_storage               | {{data.allocated_storage}}               |
| publicly_accessible             | {{data.publicly_accessible}}             |
| db_parameter_group_name         | {{data.db_parameter_group_name}}         |
| security_group_names            | {{data.security_group_names}}            |
| snapshot_identifier             | {{data.snapshot_identifier}}             |
| availability_zone               | {{data.availability_zone}}               |
| backup_retention_period         | {{data.backup_retention_period}}         |
| backup_window                   | {{data.backup_window}}                   |
| delete_automated_backups        | {{data.delete_automated_backups}}        |
| deletion_protection             | {{data.deletion_protection}}             |
| enabled_cloudwatch_logs_exports | {{data.enabled_cloudwatch_logs_exports}} |
| maintenance_window              | {{data.maintenance_window}}              |
| vpc_security_group_ids          | {{data.vpc_security_group_ids}}          |
| allow_major_version_upgrade     | {{data.allow_major_version_upgrade}}     |
| db_subnet_group_name            | {{data.db_subnet_group_name}}            |
| dependencies                    | {{data.dependencies}}                    |




### aws_rds_cluster {{name}}
| Items                           | values                                   |
| ------------------------------- | ---------------------------------------- |
| arn                             | {{data.arn}}                             |
| port                            | {{data.port}}                            |
| tags                            | {{data.tags}}                            |
| tags_all                        | {{data.tags_all}}                        |
| engine                          | {{data.engine}}                          |
| engine_version                  | {{data.engine_version}}                  |
| endpoint                        | {{data.endpoint}}                        |
| cluster_identifier              | {{data.cluster_identifier}}              |
| availability_zone               | {{data.availability_zone}}               |
| backup_retention_period         | {{data.backup_retention_period}}         |
| backup_window                   | {{data.backup_window}}                   |
| deletion_protection             | {{data.deletion_protection}}             |
| vpc_security_group_ids          | {{data.vpc_security_group_ids}}          |
| copy_tags_to_snapshot           | {{data.copy_tags_to_snapshot}}           |
| database_name                   | {{data.database_name}}                   |
| db_cluster_parameter_group_name | {{data.db_cluster_parameter_group_name}} |
| skip_final_snapshot             | {{data.skip_final_snapshot}}             |
| scaling_configuration           | {{data.scaling_configuration}}           |
| enabled_cloudwatch_logs_exports | {{data.enabled_cloudwatch_logs_exports}} |
| storage_encrypted               | {{data.storage_encrypted}}               |
| db_subnet_group_name            | {{data.db_subnet_group_name}}            |
| global_cluster_identifier       | {{data.global_cluster_identifier}}       |


### aws_rds_cluster_parameter_group {{name}}
| Items       | values               |
| ----------- | -------------------- |
| arn         | {{data.arn}}         |
| tags        | {{data.tags}}        |
| tags_all    | {{data.tags_all}}    |
| name        | {{data.name}}        |
| family      | {{data.family}}      |
| parameter   | {{data.parameter}}   |
| description | {{data.description}} |



### aws_db_subnet_group {{name}}
| Items        | values                |
| ------------ | --------------------- |
| id           | {{data.id}}           |
| arn          | {{data.arn}}          |
| tags         | {{data.tags}}         |
| tags_all     | {{data.tags_all}}     |
| description  | {{data.description}}  |
| name         | {{data.name}}         |
| subnet_ids   | {{data.subnet_ids}}   |
| dependencies | {{data.dependencies}} |



