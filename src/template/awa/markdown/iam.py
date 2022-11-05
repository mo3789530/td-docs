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

        | Items              | values                      |
        | ------------------ | --------------------------- |
        | arn                | {{data.arn}}                |
        | assume_role_policy | {{data.assume_role_policy}} |
        | description        | {{data.description}}        |
        | tags               | {{data.tags}}               |
        | dependencies       | {{data.dependencies}}       |
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_policy
    def policy_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})
        
        | Items              | values                      |
        | ------------------ | --------------------------- |
        | arn                | {{data.arn}}                |
        | name               | {{data.name}}               |
        | assume_role_policy | {{data.assume_role_policy}} |
        | description        | {{data.description}}        |
        | policy             | {{data.policy}}             |
        | tags               | {{data.tags}}               |
        | dependencies       | {{data.dependencies}}       |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    # aws_iam_policy_document
    def policy_document_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items                 | values                    |
        | --------------------- | ------------------------- |
        | id                    | {{data.id}}               |
        | name                  | {{data.name}}             |
        | json                  | {{data.json}}             |
        | state                 | {{data.state}}            |
        | tags                  | {{data.tags}}             |
        | condition             | {{data.condition}}        |
        | principals            | {{data.principals}}       |
        | resources             | {{data.resources}}        |
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
        | id                    | {{data.id}}                    |
        | role                  | {{data.role}}                  |
        | policy_arn            | {{data.policy_arn}}            |
        | tags                  | {{data.tags}}                  |
        | dependencies          | {{data.dependencies}}          |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    #  aws_iam_user_policy_attachment
    def iam_user_policy_attachment_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                  |
        | -------------- | ----------------------- |
        | id             | {{data.id}}             |
        | policy_arn     | {{data.policy_arn}}     |
        | dependencies   | {{data.dependencies}}   |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    #  aws_iam_user
    def iam_use_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                  |
        | -------------- | ----------------------- |
        | id             | {{data.id}}             |
        | arn            | {{data.arn}}            |
        | name           | {{data.name}}           |
        | tags           | {{data.tags}}           |
        | dependencies   | {{data.dependencies}}   |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name, iam_type=iam_type)
        return str(dst)

    #  aws_iam_policy_attachment

    def iam_policy_attachment_template(self, data: dict, name: str, iam_type: str) -> str:
        format = '''
        # {{iam_type}} ({{name}})

        | Items          | values                  |
        | -------------- | ----------------------- |
        | id             | {{data.id}}             |
        | name           | {{data.name}}           |
        | policy_arn     | {{data.policy_arn}}     |
        | tags           | {{data.tags}}           |
        | roles          | {{data.roles}}          |
        | users          | {{data.users}}          |
        | dependencies   | {{data.dependencies}}   |
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
