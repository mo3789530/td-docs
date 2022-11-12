from logging import getLogger

from jinja2 import Template


class MarkdownTemplateAWSRds:
    project_id = None
    logger = getLogger("src").getChild(__name__)  # type: ignore

    def __init__(self) -> None:
        pass

    # aws_rds_cluster
    def rds_cluster_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        # {{rds_type}} ({{name}})

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
        '''
        template = Template(format)
        dst = template.render(data=data, name=name, rds_type=rds_type)
        return str(dst)

    # aws_rds_cluster_instance
    def rds_cluster_instance_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        # {{rds_type}} ({{name}})

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

        '''
        template = Template(format)
        dst = template.render(data=data, name=name, rds_type=rds_type)
        return str(dst)

    # aws_rds_cluster_parameter_group
    def rds_cluster_parameter_group_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        # {{rds_type}} ({{name}})

        | Items       | values             |
        | ----------- | ------------------ |
        | arn         | {{data.arn         | default("None")}} |
        | tags        | {{data.tags        | default("None")}} |
        | tags_all    | {{data.tags_all    | default("None")}} |
        | name        | {{data.name        | default("None")}} |
        | family      | {{data.family      | default("None")}} |
        | parameter   | {{data.parameter   | default("None")}} |
        | description | {{data.description | default("None")}} |

        '''
        template = Template(format)
        dst = template.render(data=data, name=name, rds_type=rds_type)
        return str(dst)

    # aws_db_instance
    def db_instance_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        # {{rds_type}} ({{name}})

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
        '''
        template = Template(format)
        dst = template.render(data=data, name=name, rds_type=rds_type)
        return str(dst)

    # aws_db_subnet_group
    def db_subnet_group_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        # {{rds_type}} ({{name}})
        
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
        '''
        template = Template(format)
        dst = template.render(data=data, name=name, rds_type=rds_type)
        return str(dst)

    def unknown_template(self, data: dict, name: str, rds_type: str) -> str:
        self.logger.warning(f"unknown_template: {rds_type} {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, rds_type: str) -> str:
        switcher = {
            "aws_rds_cluster": self.rds_cluster_template,
            "aws_rds_cluster_instance": self.rds_cluster_instance_template,
            "aws_rds_cluster_parameter_group": self.rds_cluster_parameter_group_template,
            "aws_db_instance": self.db_instance_template,
            "aws_db_subnet_group": self.db_subnet_group_template
        }

        return switcher.get(rds_type, self.unknown_template)(data=data, name=name, rds_type=rds_type)
