from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Subnet:

    def __init__(self) -> None:
        pass

    # aws_subnet
    def subnet_parse(self, json: dict, subnet_type: str) -> tuple[dict, str]:
        attributes = "attributes"
        arn = "arn"
        assign_ipv6_address_on_creation = "assign_ipv6_address_on_creation"
        availability_zone = "availability_zone"
        availability_zone_id = "availability_zone_id"
        cidr_block = "cidr_block"
        id = "id"
        ipv6_cidr_block = "ipv6_cidr_block"
        ipv6_cidr_block_association_id = "ipv6_cidr_block_association_id"
        map_public_ip_on_launch = "map_public_ip_on_launch"
        outpost_arn = "outpost_arn"
        owner_id = "owner_id"
        tags = "tags"
        timeouts = "timeouts"
        vpc_id = "vpc_id"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})
        return {
            arn: attrs.get(arn),
            assign_ipv6_address_on_creation: attrs.get(assign_ipv6_address_on_creation),
            availability_zone: attrs.get(availability_zone),
            availability_zone_id: attrs.get(availability_zone_id),
            cidr_block: attrs.get(cidr_block),
            id: attrs.get(id),
            ipv6_cidr_block: attrs.get(ipv6_cidr_block),
            ipv6_cidr_block_association_id: attrs.get(ipv6_cidr_block_association_id),
            map_public_ip_on_launch: attrs.get(map_public_ip_on_launch),
            outpost_arn: attrs.get(outpost_arn),
            owner_id: attrs.get(owner_id),
            tags: attrs.get(tags),
            timeouts: attrs.get(timeouts),
            vpc_id: attrs.get(vpc_id),
            dependencies: pretty_json(json.get(dependencies, []))
        }, subnet_type

    # unknown type
    def unknown_type(self, json: dict, subnet_type: str) -> tuple[dict, str]:
        logger.warning(f"{subnet_type} is not defined")
        return (json, None)

    def parse(self, json: dict, subnet_type: str) -> tuple[dict, str]:
        switcher = {
            "aws_subnet": self.subnet_parse
        }
        return switcher.get(subnet_type, self.unknown_type)(json=json, subnet_type=subnet_type)
