from logging import getLogger
from typing import Optional
import re

from src.provider.terraform.tf_resource import Resources
from src.provider.common import CommonParser
from src.template.awa.common import MarkdownTemplateCommon
from src.template.format import Format
from src.libs.xlsx import ExelWriter
from src.libs.md import is_exist_md, write_md
from src.libs.html import md_to_html, save
from src.libs.pretty import pretty_markdwon

logger = getLogger("src").getChild(__name__)

class AWSService():

    def __init__(self) -> None:
        pass

    def service_bridge(self, dic: list, format: Format, filename: str) -> str:
        res = []
        pretty = False
        if format == format.MD or format == Format.HTML:
            pretty = True
        for d in dic:
            logger.debug(d)
            logger.debug("------------")
            r = Resources().parse(d)
            data = CommonParser().parser(json_data=r.get("attributes", {}), type_str=r.get("type", ""), pretty=pretty)
            if type(data) != dict:
                raise Exception("Error parsed data type")
            res.append(data)
        logger.debug(format)
        if format == Format.HTML:
            pass
        elif format == Format.XLSX:
            self.__create_xlsx(data=res, name="aaa")
        else:
            self.__create_markdown(data=res, name=filename)

    
    def __create_markdown(self, data: list, name: str) -> str:
        dst = ""
        for d in data:
            dst += pretty_markdwon(MarkdownTemplateCommon().create_markdown_facade(data=d, common_type=d['type']))
            dst += "\n"
        
        self.output(file=name, format='', data=dst)


    def output(self, file: str, format: Optional[str], data: str):
        # file check
        if format == "html":
            output = re.sub(".json", ".html", file)
        else:
            output = re.sub(".json", ".md", file)
            is_exist_md(output)

        if format == "html":
            save(output=output, html=md_to_html(data))
        else:
            write_md(output=output, dst=data)

    def __aws_common_adapter(self, dic: list, name: str, aws_type: str, format: Format) -> str:
        data = CommonParser().parser(json_data=dic, type_str=aws_type)
        if type(data) != dict:
            raise Exception("Error parsed data type")

        print(str(format))
        # TODO support out format 
       
        return pretty_markdwon(MarkdownTemplateCommon().create_markdown_facade(data=data, name=name, common_type=aws_type))

    def __create_xlsx(self, data: list, name: str) -> str:
        xlsx = ExelWriter()
        xlsx.write_sheet(dic=data, name=name)
        xlsx.save_workbook("aaa")
        return "aaa.xlsx"