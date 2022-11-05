# aws_ecs_cluster ({iam_name})  

| Items                              | values                                    |
| ---------------------------------- | ----------------------------------------- |
| schema_version                     | {{data.schema_version                     | default("None") }} |
| id                                 | {{data.id                                 | default("None") }} |
| arn                                | {{data.arn                                | default("None") }} |
| name                               | {{data.name                               | default("None") }} |
| tags                               | {{data.tags                               | default("None") }} |
| tags_all                           | {{data.tags_all                           | default("None") }} |
| setting                            | {{data.setting                            | default("None") }} |
| configuration                      | {{data.configuration                      | default("None") }} |
| capacity_providers                 | {{data.capacity_providers                 | default("None") }} |
| sensitive_attributes               | {{data.sensitive_attributes               | default("None") }} |
| default_capacity_provider_strategy | {{data.default_capacity_provider_strategy | default("None") }} |



# aws_ecs_service ({iam_name})  

| Items                              | values                                    |
| ---------------------------------- | ----------------------------------------- |
| schema_version                     | {{data.schema_version                     | default("None") }} |
| id                                 | {{data.id                                 | default("None") }} |
| name                               | {{data.name                               | default("None") }} |
| tags                               | {{data.tags                               | default("None") }} |
| tags_all                           | {{data.tags_all                           | default("None") }} |
| cluster                            | {{data.cluster                            | default("None") }} |
| timeouts                           | {{data.timeouts                           | default("None") }} |
| iam_role                           | {{data.iam_role                           | default("None") }} |
| launch_type                        | {{data.launch_type                        | default("None") }} |
| load_balancer                      | {{data.load_balancer                      | default("None") }} |
| desired_count                      | {{data.desired_count                      | default("None") }} |
| propagate_tags                     | {{data.propagate_tags                     | default("None") }} |
| task_definition                    | {{data.task_definition                    | default("None") }} |
| platform_version                   | {{data.platform_version                   | default("None") }} |
| service_registries                 | {{data.service_registries                 | default("None") }} |
| scheduling_strategy                | {{data.scheduling_strategy                | default("None") }} |
| force_new_deployment               | {{data.force_new_deployment               | default("None") }} |
| network_configuration              | {{data.network_configuration              | default("None") }} |
| deployment_controller              | {{data.deployment_controller              | default("None") }} |
| enable_execute_command             | {{data.enable_execute_command             | default("None") }} |
| wait_for_steady_state              | {{data.wait_for_steady_state              | default("None") }} |
| placement_constraints              | {{data.placement_constraints              | default("None") }} |
| enable_ecs_managed_tags            | {{data.enable_ecs_managed_tags            | default("None") }} |
| ordered_placement_strategy         | {{data.ordered_placement_strategy         | default("None") }} |
| deployment_maximum_percent         | {{data.deployment_maximum_percent         | default("None") }} |
| deployment_circuit_breaker         | {{data.deployment_circuit_breaker         | default("None") }} |
| capacity_provider_strategy         | {{data.capacity_provider_strategy         | default("None") }} |
| health_check_grace_period_seconds  | {{data.health_check_grace_period_seconds  | default("None") }} |
| deployment_minimum_healthy_percent | {{data.deployment_minimum_healthy_percent | default("None") }} |
| dependencies                       | {{data.dependencies                       | default("None") }} |

# aws_ecs_task_definition ({ecs_type})  

| Items                    | values                          |
| ------------------------ | ------------------------------- |
| schema_version           | {{data.schema_version           | default("None") }} |
| id                       | {{data.id                       | default("None") }} |
| arn                      | {{data.arn                      | default("None") }} |
| name                     | {{data.name                     | default("None") }} |
| tags                     | {{data.tags                     | default("None") }} |
| tags_all                 | {{data.tags_all                 | default("None") }} |
| family                   | {{data.family                   | default("None") }} |
| memory                   | {{data.memory                   | default("None") }} |
| volume                   | {{data.volume                   | default("None") }} |
| ipc_mode                 | {{data.ipc_mode                 | default("None") }} |
| network_mode             | {{data.network_mode             | default("None") }} |
| task_role_arn            | {{data.task_role_arn            | default("None") }} |
| execution_role_arn       | {{data.execution_role_arn       | default("None") }} |
| proxy_configuration      | {{data.proxy_configuration      | default("None") }} |
| inference_accelerator    | {{data.inference_accelerator    | default("None") }} |
| container_definitions    | {{data.container_definitions    | default("None") }} |
| placement_constraints    | {{data.placement_constraints    | default("None") }} |
| requires_compatibilities | {{data.requires_compatibilities | default("None") }} |
| dependencies             | {{data.dependencies             | default("None") }} |