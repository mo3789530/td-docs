# aws_lb {{name| default("None")}}
| Items                            | values                                  |
| -------------------------------- | --------------------------------------- |
| access_logs                      | {{data.access_logs                      | default("None")}} |
| arn                              | {{data.arn                              | default("None")}} |
| arn_suffix                       | {{data.arn_suffix                       | default("None")}} |
| customer_owned_ipv4_pool         | {{data.customer_owned_ipv4_pool         | default("None")}} |
| dns_name                         | {{data.dns_name                         | default("None")}} |
| drop_invalid_header_fields       | {{data.drop_invalid_header_fields       | default("None")}} |
| enable_cross_zone_load_balancing | {{data.enable_cross_zone_load_balancing | default("None")}} |
| enable_deletion_protection       | {{data.enable_deletion_protection       | default("None")}} |
| enable_http2                     | {{data.enable_http2                     | default("None")}} |
| id                               | {{data.id                               | default("None")}} |
| idle_timeout                     | {{data.idle_timeout                     | default("None")}} |
| internal                         | {{data.internal                         | default("None")}} |
| ip_address_type                  | {{data.ip_address_type                  | default("None")}} |
| load_balancer_type               | {{data.load_balancer_type               | default("None")}} |
| name                             | {{data.name                             | default("None")}} |
| name_prefix                      | {{data.name_prefix                      | default("None")}} |
| security_groups                  | {{data.security_groups                  | default("None")}} |
| subnet_mapping                   | {{data.subnet_mapping                   | default("None")}} |
| subnets                          | {{data.subnets                          | default("None")}} |
| tags                             | {{data.tags                             | default("None")}} |
| timeouts                         | {{data.timeouts                         | default("None")}} |
| vpc_id                           | {{data.vpc_id                           | default("None")}} |
| zone_id                          | {{data.zone_id                          | default("None")}} |


# aws_lb_listener {{name| default("None")}}
| Items             | values                   |
| ----------------- | ------------------------ |
| arn               | {{data.arn               | default("None")}} |
| certificate_arn   | {{data.certificate_arn   | default("None")}} |
| default_action    | {{data.default_action    | default("None")}} |
| id                | {{data.id                | default("None")}} |
| load_balancer_arn | {{data.load_balancer_arn | default("None")}} |
| port              | {{data.port              | default("None")}} |
| protocol          | {{data.protocol          | default("None")}} |
| ssl_policy        | {{data.ssl_policy        | default("None")}} |
| timeouts          | {{data.timeouts          | default("None")}} |

# aws_lb_listener_rule {{name| default("None")}}
| Items        | values              |
| ------------ | ------------------- |
| action       | {{data.action       | default("None")}} |
| arn          | {{data.arn          | default("None")}} |
| condition    | {{data.condition    | default("None")}} |
| id           | {{data.id           | default("None")}} |
| listener_arn | {{data.listener_arn | default("None")}} |
| priority     | {{data.priority     | default("None")}} |


# aws_lb_target_group {{name| default("None")}}
| Items                              | values                                    |
| ---------------------------------- | ----------------------------------------- |
| arn                                | {{data.arn                                | default("None")}} |
| arn_suffix                         | {{data.arn_suffix                         | default("None")}} |
| deregistration_delay               | {{data.deregistration_delay               | default("None")}} |
| health_check                       | {{data.health_check                       | default("None")}} |
| id                                 | {{data.id                                 | default("None")}} |
| lambda_multi_value_headers_enabled | {{data.lambda_multi_value_headers_enabled | default("None")}} |
| load_balancing_algorithm_type      | {{data.load_balancing_algorithm_type      | default("None")}} |
| name                               | {{data.name                               | default("None")}} |
| name_prefix                        | {{data.name_prefix                        | default("None")}} |
| port                               | {{data.port                               | default("None")}} |
| protocol                           | {{data.protocol                           | default("None")}} |
| proxy_protocol_v2                  | {{data.proxy_protocol_v2                  | default("None")}} |
| slow_start                         | {{data.slow_start                         | default("None")}} |
| stickiness                         | {{data.stickiness                         | default("None")}} |
| tags                               | {{data.tags                               | default("None")}} |
| target_type                        | {{data.target_type                        | default("None")}} |
| vpc_id                             | {{data.vpc_id                             | default("None")}} |


# aws_elb {{name| default("None")}}
| Items                       | values                             |
| --------------------------- | ---------------------------------- |
| access_logs                 | {{data.access_logs                 | default("None")}} |
| arn                         | {{data.arn                         | default("None")}} |
| availability_zones          | {{data.availability_zones          | default("None")}} |
| connection_draining         | {{data.connection_draining         | default("None")}} |
| connection_draining_timeout | {{data.connection_draining_timeout | default("None")}} |
| cross_zone_load_balancing   | {{data.cross_zone_load_balancing   | default("None")}} |
| dns_name                    | {{data.dns_name                    | default("None")}} |
| health_check                | {{data.health_check                | default("None")}} |
| id                          | {{data.id                          | default("None")}} |
| idle_timeout                | {{data.idle_timeout                | default("None")}} |
| instances                   | {{data.instances                   | default("None")}} |
| internal                    | {{data.internal                    | default("None")}} |
| listener                    | {{data.listener                    | default("None")}} |
| name                        | {{data.name                        | default("None")}} |
| name_prefix                 | {{data.name_prefix                 | default("None")}} |
| security_groups             | {{data.security_groups             | default("None")}} |
| source_security_group       | {{data.source_security_group       | default("None")}} |
| source_security_group_id    | {{data.source_security_group_id    | default("None")}} |
| subnets                     | {{data.subnets                     | default("None")}} |
| tags                        | {{data.tags                        | default("None")}} |
| tags_all                    | {{data.tags_all                    | default("None")}} |
| zone_id                     | {{data.zone_id                     | default("None")}} |


# aws_alb {{name| default("None")}}
| Items                      | values                            |
| -------------------------- | --------------------------------- |
| access_logs                | {{data.access_logs                | default("None")}} |
| arn                        | {{data.arn                        | default("None")}} |
| arn_suffix                 | {{data.arn_suffix                 | default("None")}} |
| dns_name                   | {{data.dns_name                   | default("None")}} |
| drop_invalid_header_fields | {{data.drop_invalid_header_fields | default("None")}} |
| enable_deletion_protection | {{data.enable_deletion_protection | default("None")}} |
| id                         | {{data.id                         | default("None")}} |
| idle_timeout               | {{data.idle_timeout               | default("None")}} |
| internal                   | {{data.internal                   | default("None")}} |
| ip_address_type            | {{data.ip_address_type            | default("None")}} |
| load_balancer_type         | {{data.load_balancer_type         | default("None")}} |
| name                       | {{data.name                       | default("None")}} |
| security_groups            | {{data.security_groups            | default("None")}} |
| subnet_mapping             | {{data.subnet_mapping             | default("None")}} |
| subnets                    | {{data.subnets                    | default("None")}} |
| tags                       | {{data.tags                       | default("None")}} |
| vpc_id                     | {{data.vpc_id                     | default("None")}} |
| zone_id                    | {{data.zone_id                    | default("None")}} |