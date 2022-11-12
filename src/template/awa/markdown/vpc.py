from logging import getLogger

from jinja2 import Template

logger = getLogger("src").getChild(__name__)  # type: ignore


class MarkdownTemplateAWSVpc:

    # aws_vpc
    def vpc_template(self, data: dict, name: str, vpc_type: str) -> str:
        format = '''
        # aws_vpc ({{name}})
        
        | Items                            | values                                  |
        | -------------------------------- | --------------------------------------- |
        | arn                              | {{data.arn                              | default("None")}} |
        | assign_generated_ipv6_cidr_block | {{data.assign_generated_ipv6_cidr_block | default("None")}} |
        | cidr_block                       | {{data.cidr_block                       | default("None")}} |
        | default_network_acl_id           | {{data.default_network_acl_id           | default("None")}} |
        | default_route_table_id           | {{data.default_route_table_id           | default("None")}} |
        | default_security_group_id        | {{data.default_security_group_id        | default("None")}} |
        | dhcp_options_id                  | {{data.dhcp_options_id                  | default("None")}} |
        | enable_classiclink               | {{data.enable_classiclink               | default("None")}} |
        | enable_classiclink_dns_support   | {{data.enable_classiclink_dns_support   | default("None")}} |
        | enable_dns_hostnames             | {{data.enable_dns_hostnames             | default("None")}} |
        | enable_dns_support               | {{data.enable_dns_support               | default("None")}} |
        | id                               | {{data.id                               | default("None")}} |
        | instance_tenancy                 | {{data.instance_tenancy                 | default("None")}} |
        | ipv6_association_id              | {{data.ipv6_association_id              | default("None")}} |
        | ipv6_cidr_block                  | {{data.ipv6_cidr_block                  | default("None")}} |
        | main_route_table_id              | {{data.main_route_table_id              | default("None")}} |
        | owner_id                         | {{data.owner_id                         | default("None")}} |
        | tags                             | {{data.tags                             | default("None")}} |
        '''
        template = Template(format)
        dst = template.render(data=data, name=name, vpc_type=vpc_type)
        return str(dst)

    def unknown_template(self, data: dict, name: str, vpc_type: str) -> str:
        logger.warning(f"unknown_template: {vpc_type} {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, vpc_type: str) -> str:
        switcher = {
            "aws_vpc": self.vpc_template
        }

        return switcher.get(vpc_type, self.unknown_template)(data=data, name=name, vpc_type=vpc_type)
