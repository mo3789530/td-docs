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
        ### {{rds_type}} {{name}}
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
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name, rds_type=rds_type)
        return str(dst)

    # aws_rds_cluster_parameter_group
    def rds_cluster_parameter_group_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        ### {{rds_type}} {{name}}
        | Items       | values               |
        | ----------- | -------------------- |
        | arn         | {{data.arn}}         |
        | tags        | {{data.tags}}        |
        | tags_all    | {{data.tags_all}}    |
        | name        | {{data.name}}        |
        | family      | {{data.family}}      |
        | parameter   | {{data.parameter}}   |
        | description | {{data.description}} |
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name, rds_type=rds_type)
        return str(dst)

    # aws_db_instance
    def db_instance_template(self, data: dict, name: str, rds_type: str) -> str:
        format = '''
        ### {{rds_type}} {{name}}
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
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name, rds_type=rds_type)
        return str(dst)

    def unknown_template(self, data: dict, name: str, rds_type: str) -> str:
        self.logger.warning(f"unknown_template: {rds_type} {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, rds_type: str) -> str:
        switcher = {
            "aws_rds_cluster": self.rds_cluster_template,
            "aws_rds_cluster_parameter_group": self.rds_cluster_parameter_group_template,
            "aws_db_instance": self.db_instance_template,
        }

        return switcher.get(rds_type, self.unknown_template)(data=data, name=name, rds_type=rds_type)
