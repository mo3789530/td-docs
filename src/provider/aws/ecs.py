from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Ecs:

    def __init__(self) -> None:
        pass

    # aws_ecs_cluster
    def ecs_cluster_parse(self, json: dict, ecs_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        id = "id"
        arn = "arn"
        name = "name"
        tags = "tags"
        tags_all = "tags_all"
        setting = "setting"
        configuration = "configuration"
        capacity_providers = "capacity_providers"
        sensitive_attributes = "sensitive_attributes"
        default_capacity_provider_strategy = "default_capacity_provider_strategy"

        attr = json.get(attributes, {})
        return {
            "type":                   ecs_type,
            schema_version:           json.get(schema_version),
            id:                       attr.get(id),
            arn:                      attr.get(arn),
            name:                     attr.get(name),
            tags:                     attr.get(tags),
            tags_all:                 attr.get(tags_all),
            setting:                  pretty_json(attr.get(setting, {})),
            configuration:            attr.get(configuration),
            capacity_providers:       attr.get(capacity_providers),
            sensitive_attributes:     json.get(sensitive_attributes),
            default_capacity_provider_strategy: attr.get(
                default_capacity_provider_strategy)
        }

    # aws_ecs_service
    def ecs_service_parse(self, json: dict, ecs_type: str):
        schema_version = "schema_version"

        attributes = "attributes"
        id = "id"
        name = "name"
        tags = "tags"
        tags_all = "tags_all"
        cluster = "cluster"
        timeouts = "timeouts"
        iam_role = "iam_role"
        launch_type = "launch_type"
        load_balancer = "load_balancer"
        desired_count = "desired_count"
        propagate_tags = "propagate_tags"
        task_definition = "task_definition"
        platform_version = "platform_version"
        service_registries = "service_registries"
        scheduling_strategy = "scheduling_strategy"
        force_new_deployment = "force_new_deployment"
        network_configuration = "network_configuration"
        deployment_controller = "deployment_controller"
        enable_execute_command = "enable_execute_command"
        wait_for_steady_state = "wait_for_steady_state"
        placement_constraints = "placement_constraints"
        enable_ecs_managed_tags = "enable_ecs_managed_tags"
        ordered_placement_strategy = "ordered_placement_strategy"
        deployment_maximum_percent = "deployment_maximum_percent"
        deployment_circuit_breaker = "deployment_circuit_breaker"
        capacity_provider_strategy = "capacity_provider_strategy"
        health_check_grace_period_seconds = "health_check_grace_period_seconds"
        deployment_minimum_healthy_percent = "deployment_minimum_healthy_percent"

        dependencies = "dependencies"

        attr = json.get(attributes, {})
        return {
            "type":                   ecs_type,
            schema_version:           json.get(schema_version),
            id:                       attr.get(id),
            name: attr.get(name),
            tags: attr.get(tags),
            tags_all: attr.get(tags_all),
            cluster: attr.get(cluster),
            timeouts: attr.get(timeouts),
            iam_role: attr.get(iam_role),
            launch_type: attr.get(launch_type),
            load_balancer: attr.get(load_balancer),
            desired_count: attr.get(desired_count),
            propagate_tags: attr.get(propagate_tags),
            task_definition: attr.get(task_definition),
            platform_version: attr.get(platform_version),
            service_registries: attr.get(service_registries),
            scheduling_strategy: attr.get(scheduling_strategy),
            force_new_deployment: attr.get(force_new_deployment),
            network_configuration: attr.get(network_configuration),
            deployment_controller: attr.get(deployment_controller),
            enable_execute_command: attr.get(enable_execute_command),
            wait_for_steady_state: attr.get(wait_for_steady_state),
            placement_constraints: attr.get(placement_constraints),
            enable_ecs_managed_tags: attr.get(enable_ecs_managed_tags),
            ordered_placement_strategy: attr.get(ordered_placement_strategy),
            deployment_maximum_percent: attr.get(deployment_maximum_percent),
            deployment_circuit_breaker: pretty_json(attr.get(deployment_circuit_breaker, {})),
            capacity_provider_strategy: attr.get(capacity_provider_strategy),
            health_check_grace_period_seconds: attr.get(health_check_grace_period_seconds),
            deployment_minimum_healthy_percent: attr.get(deployment_minimum_healthy_percent),

            dependencies:             pretty_array(
                json.get(dependencies, []))
        }

    # aws_ecs_task_definition
    def ecs_task_definition_parse(self,  json: dict, ecs_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        id = "id"
        arn = "arn"
        cpu = "cpu"
        tags = "tags"
        tags_all = "tags_all"
        family = "family"
        memory = "memory"
        volume = "volume"
        ipc_mode = "ipc_mode"
        network_mode = "network_mode"
        task_role_arn = "task_role_arn"
        execution_role_arn = "execution_role_arn"
        proxy_configuration = "proxy_configuration"
        inference_accelerator = "inference_accelerator"
        container_definitions = "container_definitions"
        placement_constraints = "placement_constraints"
        requires_compatibilities = "requires_compatibilities"

        dependencies = "dependencies"

        attr = json.get(attributes, {})

        return {
            "type":                   ecs_type,
            schema_version:           json.get(schema_version),
            id:                       attr.get(id),
            arn:                      attr.get(arn),
            cpu:                      attr.get(cpu),
            tags:                     attr.get(tags),
            tags_all:                 attr.get(tags_all),
            family:                   attr.get(family),
            memory:                   attr.get(memory),
            volume:                   attr.get(volume),
            ipc_mode:                 attr.get(ipc_mode),
            network_mode:             attr.get(network_mode),
            task_role_arn:            attr.get(task_role_arn),
            execution_role_arn:       attr.get(execution_role_arn),
            proxy_configuration:      attr.get(proxy_configuration),
            inference_accelerator:    attr.get(inference_accelerator),
            container_definitions:    attr.get(container_definitions),
            placement_constraints:    attr.get(placement_constraints),
            requires_compatibilities: attr.get(requires_compatibilities),
            dependencies:             pretty_array(json.get(dependencies, []))
        }

    # unknow type
    def unknown_type(self, json: dict, ecs_type: str):
        logger.warning(f"{ecs_type} is not defined")
        # raise Exception(f"{iam_type} is not defined in iam type")
        return json

    def parse(self, json: dict, ecs_type: str):
        switcher = {
            "aws_ecs_cluster": self.ecs_cluster_parse,
            "aws_ecs_service": self.ecs_service_parse,
            "aws_ecs_task_definition": self.ecs_task_definition_parse,
        }
        return switcher.get(ecs_type, self.unknown_type)(json=json, ecs_type=ecs_type)
