from logging import getLogger

logger = getLogger("src").getChild(__name__)


class Rds:
    def __init__(self) -> None:
        pass

    # aws_rds_cluster
    def rds_cluster_parser(self, json: dict, rds_type: str) -> dict:
        attributes = "attributes"
        arn = "arn"
        tags = "tags"
        tags_all = "tags_all"
        availability_zones = "availability_zones"
        backtrack_window = "backtrack_window"
        backup_retention_period = "backup_retention_period"
        cluster_identifier = "cluster_identifier"
        # cluster_resource_id = "cluster_resource_id"
        copy_tags_to_snapshot = "copy_tags_to_snapshot"
        database_name = "database_name"
        db_cluster_parameter_group_name = "db_cluster_parameter_group_name"
        endpoint = "endpoint"
        engine = "engine"
        engine_version = "engine_version"
        port = "port"
        preferred_backup_window = "preferred_backup_window"
        preferred_maintenance_window = "preferred_maintenance_window"
        skip_final_snapshot = "skip_final_snapshot"
        vpc_security_group_ids = "vpc_security_group_ids"
        scaling_configuration = "scaling_configuration"
        availability_zone = "availability_zone"
        enabled_cloudwatch_logs_exports = "enabled_cloudwatch_logs_exports"
        storage_encrypted = "storage_encrypted"
        db_subnet_group_name = "db_subnet_group_name"
        global_cluster_identifier = "global_cluster_identifier"

        attrs = json.get(attributes, {})
        return {
            arn: attrs.get(arn),
            availability_zones:              attrs.get(availability_zones),
            tags:                            attrs.get(tags),
            tags_all:                        attrs.get(tags_all),
            backtrack_window:                attrs.get(backtrack_window),
            backup_retention_period:         attrs.get(backup_retention_period),
            copy_tags_to_snapshot:           attrs.get(copy_tags_to_snapshot),
            database_name:                   attrs.get(database_name),
            cluster_identifier:              attrs.get(cluster_identifier),
            db_cluster_parameter_group_name: attrs.get(db_cluster_parameter_group_name),
            endpoint:                        attrs.get(endpoint),
            engine:                          attrs.get(engine),
            engine_version:                  attrs.get(engine_version),
            port:                            attrs.get(port),
            availability_zone:               attrs.get(availability_zone),
            preferred_backup_window:         attrs.get(preferred_backup_window),
            preferred_maintenance_window:    attrs.get(preferred_maintenance_window),
            skip_final_snapshot:             attrs.get(skip_final_snapshot),
            vpc_security_group_ids:          attrs.get(vpc_security_group_ids),
            enabled_cloudwatch_logs_exports: attrs.get(enabled_cloudwatch_logs_exports),
            storage_encrypted:               attrs.get(storage_encrypted),
            db_subnet_group_name:            attrs.get(db_subnet_group_name),
            global_cluster_identifier:       attrs.get(global_cluster_identifier),
        }

    # aws_rds_cluster_parameter_group
    def rds_cluster_parameter_group_parser(self, json: dict, rds_type: str) -> dict:
        attributes = "attributes"

        arn = "arn"
        id = "id"
        name = "name"
        family = "family"
        tags = "tags"
        tags_all = "tags_all"
        parameter = "parameter"
        description = "description"
        attrs = json.get(attributes, {})

        return {
            id:          attrs.get(id),
            arn:         attrs.get(arn),
            name:        attrs.get(name),
            tags:        attrs.get(tags),
            tags_all:    attrs.get(tags_all),
            family:      attrs.get(family),
            parameter:   attrs.get(parameter),
            description: attrs.get(description)
        }

    # aws_db_instance
    def db_instance_parser(self, json: dict, rds_type: str) -> dict:
        attributes = "attributes"
        id = "id"
        arn = "arn"
        name = "name"
        port = "port"
        tags = "tags"
        tags_all = "tags_all"
        engine = "engine"
        engine_version = "engine_version"
        address = "address"
        timezone = "timezone"
        endpoint = "endpoint"
        allocated_storage = "allocated_storage"
        allow_major_version_upgrade = "allow_major_version_upgrade"

        backup_retention_period = "backup_retention_period"
        backup_window = "backup_window"
        db_subnet_group_name = "db_subnet_group_name"
        delete_automated_backups = "delete_automated_backups"
        deletion_protection = "deletion_protection"
        enabled_cloudwatch_logs_exports = "enabled_cloudwatch_logs_exports"
        identifier = "identifier"
        instance_class = "instance_class"
        maintenance_window = "maintenance_window"
        publicly_accessible = "publicly_accessible"
        security_group_names = "security_group_names"
        snapshot_identifier = "snapshot_identifier"
        storage_encrypted = "storage_encrypted"
        storage_type = "storage_type"

        vpc_security_group_ids = "vpc_security_group_ids"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            id:   attrs.get(id),
            arn:  attrs.get(arn),
            name: attrs.get(name),
            port: attrs.get(port),
            tags: attrs.get(tags),
            tags_all: attrs.get(tags_all),
            engine:   attrs.get(engine),
            engine_version: attrs.get(engine_version),
            address:        attrs.get(address),
            timezone:       attrs.get(timezone),
            endpoint:       attrs.get(endpoint),
            identifier:     attrs.get(identifier),
            instance_class: attrs.get(instance_class),
            storage_type:   attrs.get(storage_type),
            storage_encrypted:        attrs.get(storage_encrypted),
            allocated_storage:        attrs.get(allocated_storage),
            publicly_accessible:      attrs.get(publicly_accessible),
            security_group_names:     attrs.get(security_group_names),
            snapshot_identifier:      attrs.get(snapshot_identifier),
            backup_retention_period:  attrs.get(backup_retention_period),
            backup_window:            attrs.get(backup_window),
            delete_automated_backups: attrs.get(delete_automated_backups),
            deletion_protection:      attrs.get(deletion_protection),
            enabled_cloudwatch_logs_exports: attrs.get(enabled_cloudwatch_logs_exports),
            maintenance_window:              attrs.get(maintenance_window),
            vpc_security_group_ids:          attrs.get(vpc_security_group_ids),
            allow_major_version_upgrade: attrs.get(allow_major_version_upgrade),
            db_subnet_group_name:        attrs.get(db_subnet_group_name),
            dependencies:                json.get(dependencies)
        }

    # aws_db_subnet_group
    def db_subnet_group_parser(self, json: dict, rds_type: str) -> dict:
        attributes = "attributes"
        id = "id"
        arn = "arn"
        name = "name"
        tags = "tags"
        tags_all = "tags_all"
        subnet_ids = "subnet_ids"
        description = "description"
        dependencies = "dependencies"
        attrs = json.get(attributes, {})

        return {
            id:   attrs.get(id),
            arn:  attrs.get(arn),
            name: attrs.get(name),
            tags: attrs.get(tags),
            description:  attrs.get(description),
            tags_all:     attrs.get(tags_all),
            subnet_ids:   attrs.get(subnet_ids),
            dependencies: json.get(dependencies)
        }

        # unknow type
    def unknown_type(self, json: dict, rds_type: str) -> dict:
        logger.warning(f"{rds_type} is not defined")
        return json

    def parse(self, json: dict, rds_type: str) -> dict:
        switcher = {
            "aws_rds_cluster": self.rds_cluster_parser,
            "aws_db_instance": self.db_instance_parser,
            "aws_rds_cluster_parameter_group": self.rds_cluster_parameter_group_parser,
            "aws_db_subnet_group": self.db_subnet_group_parser,
        }
        return switcher.get(rds_type, self.unknown_type)(json=json, rds_type=rds_type)
