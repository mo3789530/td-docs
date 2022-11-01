from jinja2 import Template


class MarkdownTemplateAWSIam:
    project_id = None

    def __init__(self) -> None:
        pass

    def role_template(self, data: dict, role_name: str) -> str:
        format = '''
        ### Role ({{role_name}})  
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
        dst = template.render(data=data, role_name=role_name)
        return str(dst)

    def policy_template(self, data: dict, name: str) -> str:
        format = '''
        ### Role ({{name}})  

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
        dst = template.render(data=data, name=name)
        return str(dst)

    def policy_document_template(self, data: dict, name: str) -> str:
        format = '''
        ### Role ({{name}})  
        
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
        dst = template.render(data=data, name=name)
        return str(dst)
