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
        # {{iam_type}} ({{name}})

        | Items              | values                    |
        | ------------------ | ------------------------- |
        | arn                | {{data.arn                | default("None") }} |
        | assume_role_policy | {{data.assume_role_policy | default("None") }} |
        | description        | {{data.description        | default("None") }} |
        | tags               | {{data.tags               | default("None") }} |
        | dependencies       | {{data.dependencies       | default("None") }} |
        '''
        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_policy
    def policy_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})
        
        | Items              | values                    |
        | ------------------ | ------------------------- |
        | arn                | {{data.arn                | default("None")}} |
        | name               | {{data.name               | default("None")}} |
        | assume_role_policy | {{data.assume_role_policy | default("None")}} |
        | description        | {{data.description        | default("None")}} |
        | policy             | {{data.policy             | default("None")}} |
        | tags               | {{data.tags               | default("None")}} |
        | dependencies       | {{data.dependencies       | default("None")}} |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_policy_document
    def policy_document_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                |
        | -------------- | --------------------- |
        | id             | {{data.id             | default("None")}} |
        | name           | {{data.name           | default("None")}} |
        | json           | {{data.json           | default("None")}} |
        | state          | {{data.state          | default("None")}} |
        | tags           | {{data.tags           | default("None")}} |
        | condition      | {{data.condition      | default("None")}} |
        | principals     | {{data.principals     | default("None")}} |
        | resources      | {{data.resources      | default("None")}} |
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

        | Items          | values                |
        | -------------- | --------------------- |
        | id             | {{data.id             | default("None")}} |
        | role           | {{data.role           | default("None")}} |
        | policy_arn     | {{data.policy_arn     | default("None")}} |
        | tags           | {{data.tags           | default("None")}} |
        | dependencies   | {{data.dependencies   | default("None")}} |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    #  aws_iam_user_policy_attachment
    def iam_user_policy_attachment_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                |
        | -------------- | --------------------- |
        | id             | {{data.id             | default("None")}} |
        | policy_arn     | {{data.policy_arn     | default("None")}} |
        | dependencies   | {{data.dependencies   | default("None")}} |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    #  aws_iam_user
    def iam_use_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                |
        | -------------- | --------------------- |
        | id             | {{data.id             | default("None")}} |
        | arn            | {{data.arn            | default("None")}} |
        | name           | {{data.name           | default("None")}} |
        | tags           | {{data.tags           | default("None")}} |
        | dependencies   | {{data.dependencies   | default("None")}} |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    #  aws_iam_policy_attachment
    def iam_policy_attachment_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                |
        | -------------- | --------------------- |
        | id             | {{data.id             | default("None")}} |
        | name           | {{data.name           | default("None")}} |
        | policy_arn     | {{data.policy_arn     | default("None")}} |
        | tags           | {{data.tags           | default("None")}} |
        | roles          | {{data.roles          | default("None")}} |
        | users          | {{data.users          | default("None")}} |
        | dependencies   | {{data.dependencies   | default("None")}} |
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
            "aws_iam_user_policy_attachment": self.iam_user_policy_attachment_template,
            "aws_iam_user": self.iam_use_template,
            "aws_iam_policy_attachment": self.iam_policy_attachment_template
        }

        return switcher.get(iam_type, self.unknown_template)(data=data, name=name, iam_type=iam_type)
