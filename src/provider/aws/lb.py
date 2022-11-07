from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Lb:

    def __init__(self) -> None:
        pass

    # aws_lb
    def lb_parser(self, json: dict, lb_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        access_logs = "access_logs"
        arn = "arn"
        arn_suffix = "arn_suffix"
        customer_owned_ipv4_pool = "customer_owned_ipv4_pool"
        dns_name = "dns_name"
        drop_invalid_header_fields = "drop_invalid_header_fields"
        enable_cross_zone_load_balancing = "enable_cross_zone_load_balancing"
        enable_deletion_protection = "enable_deletion_protection"
        enable_http2 = "enable_http2"
        id = "id"
        idle_timeout = "idle_timeout"
        internal = "internal"
        ip_address_type = "ip_address_type"
        load_balancer_type = "load_balancer_type"
        name = "name"
        name_prefix = "name_prefix"
        security_groups = "security_groups"
        subnet_mapping = "subnet_mapping"
        subnets = "subnets"
        tags = "tags"
        timeouts = "timeouts"
        vpc_id = "vpc_id"
        zone_id = "zone_id"

        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            access_logs: attrs.get(access_logs),
            arn: attrs.get(arn),
            arn_suffix: attrs.get(arn_suffix),
            customer_owned_ipv4_pool: attrs.get(customer_owned_ipv4_pool),
            dns_name: attrs.get(dns_name),
            drop_invalid_header_fields: attrs.get(drop_invalid_header_fields),
            enable_cross_zone_load_balancing: attrs.get(enable_cross_zone_load_balancing),
            enable_deletion_protection: attrs.get(enable_deletion_protection),
            enable_http2: attrs.get(enable_http2),
            id: attrs.get(id),
            idle_timeout: attrs.get(idle_timeout),
            internal: attrs.get(internal),
            ip_address_type: attrs.get(ip_address_type),
            load_balancer_type: attrs.get(load_balancer_type),
            name: attrs.get(name),
            name_prefix: attrs.get(name_prefix),
            security_groups: attrs.get(security_groups),
            subnet_mapping: pretty_json(attrs.get(subnet_mapping, {})),
            subnets: attrs.get(subnets),
            tags: attrs.get(tags),
            timeouts: attrs.get(timeouts),
            vpc_id: attrs.get(vpc_id),
            zone_id: attrs.get(zone_id),
            dependencies: pretty_array(json.get(dependencies, []))
        }

    # aws_lb_listener
    def lb_listener_parser(self, json: dict, lb_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        arn = "arn"
        certificate_arn = "certificate_arn"
        default_action = "default_action"
        id = "id"
        load_balancer_arn = "load_balancer_arn"
        port = "port"
        protocol = "protocol"
        ssl_policy = "ssl_policy"
        timeouts = "timeouts"

        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            arn: attrs.get(arn),
            certificate_arn: attrs.get(certificate_arn),
            default_action: attrs.get(default_action),
            id: attrs.get(id),
            load_balancer_arn: attrs.get(load_balancer_arn),
            port: attrs.get(port),
            protocol: attrs.get(protocol),
            ssl_policy: attrs.get(ssl_policy),
            timeouts: attrs.get(timeouts),
            dependencies: pretty_array(json.get(dependencies, []))
        }

    # aws_lb_listener_rule
    def lb_listener_rule_parser(self, json: dict, lb_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        action = "action"
        arn = "arn"
        condition = "condition"
        id = "id"
        listener_arn = "listener_arn"
        priority = "priority"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            arn: attrs.get(arn),
            action: pretty_json(attrs.get(action, {})),
            arn: attrs.get(arn),
            condition: pretty_json(attrs.get(condition, {})),
            id: attrs.get(id),
            listener_arn: attrs.get(listener_arn),
            priority: attrs.get(priority),
            dependencies: pretty_array(json.get(dependencies, []))
        }

    # aws_lb_target_group
    def lb_target_group_parser(self, json: dict, lb_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        arn = "arn"
        arn_suffix = "arn_suffix"
        deregistration_delay = "deregistration_delay"
        health_check = "health_check"
        id = "id"
        lambda_multi_value_headers_enabled = "lambda_multi_value_headers_enabled"
        load_balancing_algorithm_type = "load_balancing_algorithm_type"
        name = "name"
        name_prefix = "name_prefix"
        port = "port"
        protocol = "protocol"
        proxy_protocol_v2 = "proxy_protocol_v2"
        slow_start = "slow_start"
        stickiness = "stickiness"
        tags = "tags"
        target_type = "target_type"
        vpc_id = "vpc_id"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            arn: attrs.get(arn),
            arn_suffix: attrs.get(arn_suffix),
            deregistration_delay: attrs.get(deregistration_delay),
            health_check: pretty_array(attrs.get(health_check, [])),
            id: attrs.get(id),
            lambda_multi_value_headers_enabled: attrs.get(lambda_multi_value_headers_enabled),
            load_balancing_algorithm_type: attrs.get(load_balancing_algorithm_type),
            name: attrs.get(name),
            name_prefix: attrs.get(name_prefix),
            port: attrs.get(port),
            protocol: attrs.get(protocol),
            proxy_protocol_v2: attrs.get(proxy_protocol_v2),
            slow_start:  attrs.get(slow_start),
            stickiness: pretty_json(attrs.get(stickiness, {})),
            tags: attrs.get(tags),
            target_type: attrs.get(target_type),
            vpc_id: attrs.get(vpc_id),
            dependencies: pretty_array(json.get(dependencies, []))
        }

    # aws_elb
    def elb_parser(self, json: dict, lb_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        access_logs = "access_logs"
        arn = "arn"
        availability_zones = "availability_zones"
        connection_draining = "connection_draining"
        connection_draining_timeout = "connection_draining_timeout"
        cross_zone_load_balancing = "cross_zone_load_balancing"
        dns_name = "dns_name"
        health_check = "health_check"
        id = "id"
        idle_timeout = "idle_timeout"
        instances = "instances"
        internal = "internal"
        listener = "listener"
        name = "name"
        name_prefix = "name_prefix"
        security_groups = "security_groups"
        source_security_group = "source_security_group"
        source_security_group_id = "source_security_group_id"
        subnets = "subnets"
        tags = "tags"
        tags_all = "tags_all"
        zone_id = "zone_id"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            arn: attrs.get(arn),

            access_logs: attrs.get(access_logs),
            arn: attrs.get(arn),
            availability_zones: attrs.get(availability_zones),
            connection_draining: attrs.get(connection_draining),
            connection_draining_timeout: attrs.get(connection_draining_timeout),
            cross_zone_load_balancing: attrs.get(cross_zone_load_balancing),
            dns_name: attrs.get(dns_name),
            health_check: pretty_json(attrs.get(health_check, {})),
            id: attrs.get(id),
            idle_timeout: attrs.get(idle_timeout),
            instances: attrs.get(instances),
            internal: attrs.get(internal),
            listener: pretty_json(attrs.get(listener, {})),
            name: attrs.get(name),
            name_prefix: attrs.get(name_prefix),
            security_groups: attrs.get(security_groups),
            source_security_group: attrs.get(source_security_group),
            source_security_group_id: attrs.get(source_security_group_id),
            subnets: attrs.get(subnets),
            tags: attrs.get(tags),
            tags_all: attrs.get(tags_all),
            zone_id: attrs.get(zone_id),

            dependencies: pretty_array(json.get(dependencies, []))
        }

    # aws_alb
    def alb_parser(self, json: dict, lb_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        access_logs = "access_logs"
        arn = "arn"
        arn_suffix = "arn_suffix"
        dns_name = "dns_name"
        drop_invalid_header_fields = "drop_invalid_header_fields"
        enable_deletion_protection = "enable_deletion_protection"
        id = "id"
        idle_timeout = "idle_timeout"
        internal = "internal"
        ip_address_type = "ip_address_type"
        load_balancer_type = "load_balancer_type"
        name = "name"
        security_groups = "security_groups"
        subnet_mapping = "subnet_mapping"
        subnets = "subnets"
        tags = "tags"
        vpc_id = "vpc_id"
        zone_id = "zone_id"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            access_logs: attrs.get(access_logs),
            arn: attrs.get(arn),
            arn_suffix: attrs.get(arn_suffix),
            dns_name: attrs.get(dns_name),
            drop_invalid_header_fields: attrs.get(drop_invalid_header_fields),
            enable_deletion_protection: attrs.get(enable_deletion_protection),
            id: attrs.get(id),
            idle_timeout: attrs.get(idle_timeout),
            internal: attrs.get(internal),
            ip_address_type: attrs.get(ip_address_type),
            load_balancer_type: attrs.get(load_balancer_type),
            name: attrs.get(name),
            security_groups: attrs.get(security_groups),
            subnet_mapping: attrs.get(subnet_mapping),
            subnets: attrs.get(subnets),
            tags: attrs.get(tags),
            vpc_id: attrs.get(vpc_id),
            zone_id: attrs.get(zone_id),

            dependencies: pretty_array(json.get(dependencies, []))
        }

    # unknow type
    def unknown_type(self, json: dict, lb_type: str):
        logger.warning(f"{lb_type} is not defined")
        return json

    def parse(self, json: dict, lb_type: str):
        switcher = {
            "aws_lb": self.lb_parser,
            "aws_lb_listener": self.lb_listener_parser,
            "aws_lb_listener_rule": self.lb_listener_rule_parser,
            "aws_lb_target_group": self.lb_target_group_parser,
            "aws_elb": self.elb_parser,
            "aws_alb": self.alb_parser
        }
        return switcher.get(lb_type, self.unknown_type)(json=json, lb_type=lb_type)
