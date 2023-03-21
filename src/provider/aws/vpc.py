from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Vpc:

    def __init__(self) -> None:
        pass

    # aws_vpc
    def aws_vpc_parse(self, json: dict, vpc_type: str):
        attributes = "attributes"
        id = "id"
        arn = "arn"
        tags = "tags"
        owner_id = "owner_id"
        cidr_block = "cidr_block"
        dhcp_options_id = "dhcp_options_id"
        ipv6_cidr_block = "ipv6_cidr_block"
        instance_tenancy = "instance_tenancy"
        enable_classiclink = "enable_classiclink"
        enable_dns_support = "enable_dns_support"
        main_route_table_id = "main_route_table_id"
        ipv6_association_id = "ipv6_association_id"
        enable_dns_hostnames = "enable_dns_hostnames"
        default_network_acl_id = "default_network_acl_id"
        default_route_table_id = "default_route_table_id"
        default_security_group_id = "default_security_group_id"
        enable_classiclink_dns_support = "enable_classiclink_dns_support"
        assign_generated_ipv6_cidr_block = "assign_generated_ipv6_cidr_block"
        attr = json.get(attributes, {})

        return ({
            id: attr.get(id),
            arn: attr.get(arn),
            tags: attr.get(tags),
            owner_id: attr.get(owner_id),
            cidr_block: attr.get(cidr_block),
            dhcp_options_id: attr.get(dhcp_options_id),
            ipv6_cidr_block: attr.get(ipv6_cidr_block),
            instance_tenancy: attr.get(instance_tenancy),
            enable_classiclink: attr.get(enable_classiclink),
            enable_dns_support: attr.get(enable_dns_support),
            main_route_table_id: attr.get(main_route_table_id),
            enable_dns_hostnames: attr.get(enable_dns_hostnames),
            default_network_acl_id: attr.get(default_network_acl_id),
            default_route_table_id: attr.get(default_route_table_id),
            default_security_group_id: attr.get(default_security_group_id),
            enable_classiclink_dns_support: attr.get(enable_classiclink_dns_support),
            assign_generated_ipv6_cidr_block: attr.get(assign_generated_ipv6_cidr_block),
            ipv6_association_id: attr.get(ipv6_association_id),

        }, vpc_type)

    # unknow type
    def unknown_type(self, json: dict, vpc_type: str):
        logger.warning(f"{vpc_type} is not defined")
        return (json, vpc_type)

    def parse(self, json: dict, vpc_type: str):
        switcher = {
            "aws_vpc": self.aws_vpc_parse
        }
        return switcher.get(vpc_type, self.unknown_type)(json=json, vpc_type=vpc_type)
