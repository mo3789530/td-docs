from logging import getLogger

from jinja2 import Template

logger = getLogger("src").getChild(__name__)  # type: ignore


class MarkdownTemplateAWSSubnet:
    # aws_subnet
    def subnet_template(self, data: dict, name: str, subnet_type: str) -> str:
        format = '''
        # aws_subnet ({{name}})
        
        | Items                           | values                                 |
        | ------------------------------- | -------------------------------------- |
        | arn                             | {{data.arn                             | default("None")}} |
        | assign_ipv6_address_on_creation | {{data.assign_ipv6_address_on_creation | default("None")}} |
        | availability_zone               | {{data.availability_zone               | default("None")}} |
        | availability_zone_id            | {{data.availability_zone_id            | default("None")}} |
        | cidr_block                      | {{data.cidr_block                      | default("None")}} |
        | id                              | {{data.id                              | default("None")}} |
        | ipv6_cidr_block                 | {{data.ipv6_cidr_block                 | default("None")}} |
        | ipv6_cidr_block_association_id  | {{data.ipv6_cidr_block_association_id  | default("None")}} |
        | map_public_ip_on_launch         | {{data.map_public_ip_on_launch         | default("None")}} |
        | outpost_arn                     | {{data.outpost_arn                     | default("None")}} |
        | owner_id                        | {{data.owner_id                        | default("None")}} |
        | tags                            | {{data.tags                            | default("None")}} |
        | timeouts                        | {{data.timeouts                        | default("None")}} |
        | vpc_id                          | {{data.vpc_id                          | default("None")}} |
        '''
        template = Template(format)
        dst = template.render(data=data, name=name, vpc_type=subnet_type)
        return str(dst)

    def unknown_template(self, data: dict, name: str, subnet_type: str) -> str:
        logger.warning(f"unknown_template: {subnet_type} {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, subnet_type: str) -> str:
        switcher = {
            "aws_subnet": self.subnet_template
        }

        return switcher.get(subnet_type, self.unknown_template)(data=data, name=name, subnet_type=subnet_type)
