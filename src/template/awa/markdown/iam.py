from logging import getLogger

from jinja2 import Template


class MarkdownTemplateAWSIam:
    project_id = None
    logger = getLogger("src").getChild(__name__)  # type: ignore

    def __init__(self) -> None:
        pass

    # aws_iam_role
    def role_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{role_name}})
        | Items                         | values                                 |
        | ----------------------------- | -------------------------------------- |
        | schema_version                | {{data.schema_version}}                |
        | attributes_arn                | {{data.attributes_arn}}                |
        | attributes_assume_role_policy | {{data.attributes_assume_role_policy}} |
        | attributes_description        | {{data.attributes_description}}        |
        | attributes_tags               | {{data.attributes_tags}}               |
        | dependencies                  | {{data.dependencies}}                  |
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_policy_document
    def policy_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})
        
        | Items                         | values                                 |
        | ----------------------------- | -------------------------------------- |
        | schema_version                | {{data.schema_version}}                |
        | attributes_arn                | {{data.attributes_arn}}                |
        | attributes_name               | {{data.attributes_name}}               |
        | attributes_assume_role_policy | {{data.attributes_assume_role_policy}} |
        | attributes_description        | {{data.attributes_description}}        |
        | attributes_policy             | {{data.attributes_policy}}             |
        | attributes_tags               | {{data.attributes_tags}}               |
        | dependencies                  | {{data.dependencies}}                  |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_policy_document
    def policy_document_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items                 | values                         |
        | --------------------- | ------------------------------ |
        | schema_version        | {{data.schema_version}}        |
        | attributes_id         | {{data.attributes_id}}         |
        | attributes_name       | {{data.attributes_name}}       |
        | attributes_json       | {{data.attributes_json}}       |
        | attributes_state      | {{data.attributes_state}}      |
        | attributes_tags       | {{data.attributes_tags}}       |
        | attributes_condition  | {{data.attributes_condition}}  |
        | attributes_principals | {{data.attributes_principals}} |
        | resources             | {{data.resources}}             |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_instance_profile
    def instance_profile_template(self, data: dict, name: str, iam_type: str) -> str:
        return ""

    # aws_iam_role_policy_attachment
    def role_policy_attachment_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items                 | values                         |
        | --------------------- | ------------------------------ |
        | schema_version        | {{data.schema_version}}        |
        | attributes_id         | {{data.attributes_id}}         |
        | attributes_role       | {{data.attributes_role}}       |
        | attributes_policy_arn | {{data.attributes_policy_arn}} |
        | attributes_tags       | {{data.attributes_tags}}       |
        | dependencies          | {{data.dependencies}}          |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    def unknown_template(self, data: dict, name: str, iam_type: str) -> str:
        self.logger.warning(f"unknown_template: {iam_type} {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, iam_type: str) -> str:
        switcher = {
            "aws_iam_instance_profile": self.instance_profile_template,
            "aws_iam_role": self.role_template,
            "aws_iam_policy": self.policy_template,
            "aws_iam_policy_document": self.policy_document_template,
            "aws_iam_role_policy_attachment": self.role_policy_attachment_template,
        }

        return switcher.get(iam_type, self.unknown_template)(data=data, name=name, iam_type=iam_type)
