from jinja2 import Template


class MarkdownTemplateAWSIam:
    project_id = None

    def __init__(self) -> None:
        pass

    def role_template(self, data: dict, name: str) -> str:
        format = '''
        # Role ({{role_name}})
        | Items                         | values                                 |
        | ----------------------------- | -------------------------------------- |
        | schema_version                | {{data.schema_version}}                |
        | attributes_arn                | {{data.arn}}                |
        | attributes_assume_role_policy | {{data.assume_role_policy}} |
        | attributes_description        | {{data.description}}        |
        | attributes_tags               | {{data.tags}}               |
        | dependencies                  | {{data.dependencies}}                  |
        '''
        template = Template(format)
        dst = template.render(data=data, role_name=name)
        return str(dst)

    def policy_template(self, data: dict, name: str) -> str:
        format = '''
        # Role ({{name}})

        | Items                         | values                                 |
        | ----------------------------- | -------------------------------------- |
        | schema_version                | {{data.schema_version}}                |
        | attributes_arn                | {{data.arn}}                |
        | attributes_name               | {{data.name}}               |
        | attributes_assume_role_policy | {{data.assume_role_policy}} |
        | attributes_description        | {{data.description}}        |
        | attributes_policy             | {{data.policy}}             |
        | attributes_tags               | {{data.tags}}               |
        | dependencies                  | {{data.dependencies}}                  |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name)
        return str(dst)

    def policy_document_template(self, data: dict, name: str) -> str:
        format = '''
        # Role ({{name}})

        | Items                 | values                         |
        | --------------------- | ------------------------------ |
        | schema_version        | {{data.schema_version}}        |
        | attributes_id         | {{data.id}}         |
        | attributes_name       | {{data.name}}       |
        | attributes_json       | {{data.json}}       |
        | attributes_state      | {{data.state}}      |
        | attributes_tags       | {{data.tags}}       |
        | attributes_condition  | {{data.condition}}  |
        | attributes_principals | {{data.principals}} |
        | resources             | {{data.resources}}             |
        '''

        template = Template(format)
        dst = template.render(data=data, name=name)
        return str(dst)

    def instance_profile_template(self, data: dict, name: str) -> str:
        return ""

    def unknown_template(self, data: dict, name: str) -> str:
        print(f"unknown_template: {name}")
        return ""

    def create_markdown_facade(self, data: dict, name: str, iam_type: str) -> str:
        switcher = {
            "aws_iam_instance_profile": self.instance_profile_template,
            "aws_iam_role": self.role_template,
            "aws_iam_policy": self.policy_template,
            "aws_iam_policy_document": self.policy_document_template,
        }

        return switcher.get(iam_type, self.unknown_template)(data=data, name=name)
