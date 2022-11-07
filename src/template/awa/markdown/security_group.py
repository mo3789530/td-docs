from logging import getLogger

from jinja2 import Template

logger = getLogger("src").getChild(__name__)  # type: ignore


class MarkdownTemplateAWSSg:
    # aws_security_group
    def sg_template(self, data: dict, name: str, sg_type: str) -> str:
        format = '''
        # aws_security_group {{name| default("None")}}
        | Items                  | values                        |
        | ---------------------- | ----------------------------- |
        | arn                    | {{data.arn                    | default("None")}} |
        | description            | {{data.description            | default("None")}} |
        | egress                 | {{data.egress                 | default("None")}} |
        | id                     | {{data.id                     | default("None")}} |
        | ingress                | {{data.ingress                | default("None")}} |
        | name                   | {{data.name                   | default("None")}} |
        | name_prefix            | {{data.name_prefix            | default("None")}} |
        | owner_id               | {{data.owner_id               | default("None")}} |
        | revoke_rules_on_delete | {{data.revoke_rules_on_delete | default("None")}} |
        | tags                   | {{data.tags                   | default("None")}} |
        | timeouts               | {{data.timeouts               | default("None")}} |
        | vpc_id                 | {{data.vpc_id                 | default("None")}} |
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name, sg_type=sg_type)
        return str(dst)

    def unknown_template(self, data: dict, name: str, sg_type: str) -> str:
        logger.warning(f"unknown_template: {sg_type} {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, sg_type: str) -> str:
        switcher = {
            "aws_security_group": self.sg_template
        }

        return switcher.get(sg_type, self.unknown_template)(data=data, name=name, sg_type=sg_type)
