from logging import getLogger

from src.libs.pretty import pretty_markdwon
from src.provider.common import CommonParser
from src.template.awa.common import MarkdownTemplateCommon
from src.template.format import Format
from src.libs.xlsx import ExelWriter


logger = getLogger("src").getChild(__name__)

class AWSService():

    def __init__(self) -> None:
        pass

    def service_bridge(self, dic: list, format: Format, filename: str) -> str:
        res = []
        for d in dic:
            data = CommonParser().parser(json_data=d.get("attributes", {}), type_str=d.get("type", ""))
            if type(data) != dict:
                raise Exception("Error parsed data type")
            res.append(data)
        logger.debug(format)
        if format == Format.HTML:
            pass
        elif format == Format.XLSX:
            self.__create_xlsx(data=res, name="aaa")
        else:
            self.__create_markdown(data=res, name="aaa")

    
    def __create_markdown(self, data: list, name: str) -> str:
        pass



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