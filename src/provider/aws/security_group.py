from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class SecurityGroup:
    def __init__(self) -> None:
        pass

    # aws_security_group
    def security_group_parse(self, json: dict, sg_type: str) -> tuple[dict, str]:
        attributes = "attributes"
        arn = "arn"
        description = "description"
        egress = "egress"
        id = "id"
        ingress = "ingress"
        name = "name"
        name_prefix = "name_prefix"
        owner_id = "owner_id"
        revoke_rules_on_delete = "revoke_rules_on_delete"
        tags = "tags"
        timeouts = "timeouts"
        vpc_id = "vpc_id"
        dependencies = "dependencies"

        attrs = json.get(attributes, {})

        return {
            arn: attrs.get(arn),
            description: attrs.get(description),
            egress: pretty_json(attrs.get(egress, {})),
            id: attrs.get(id),
            ingress: pretty_json(attrs.get(ingress, {})),
            name: attrs.get(name),
            name_prefix: attrs.get(name_prefix),
            owner_id: attrs.get(owner_id),
            revoke_rules_on_delete: attrs.get(revoke_rules_on_delete),
            tags: attrs.get(tags),
            timeouts: attrs.get(timeouts),
            vpc_id: attrs.get(vpc_id),
            dependencies: pretty_array(json.get(dependencies, []))
        }, sg_type

    # unknown type
    def unknown_type(self, json: dict, sg_type: str) -> tuple[dict, str]:
        logger.warning(f"{sg_type} is not defined")
        return json, None

    def parse(self, json: dict, sg_type: str) -> tuple[dict, str]:
        switcher = {
            "aws_security_group": self.security_group_parse
        }
        return switcher.get(sg_type, self.unknown_type)(json=json, sg_type=sg_type)
