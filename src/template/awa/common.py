from logging import getLogger

from jinja2 import Template

logger = getLogger("src").getChild(__name__)  # type: ignore


class MarkdownTemplateCommon:

    def common_template(self, data: dict, name: str, c_type: str) -> str:
        txt = ""
        for d in data.keys():
            txt += f'| {d} | {data.get(d, "None")} | \n'
        format = '''
# {{c_type}} {{name}} 
| Items                            | values                                  |
| -------------------------------- | --------------------------------------- |
'''
        format += txt
        template = Template(format)
        dst = template.render(data=data, name=name, c_type=c_type)
        return str(dst)

    def create_markdown_facade(self, data: dict, name: str, common_type: str) -> str:
        return self.common_template(data=data, name=name, c_type=common_type)
