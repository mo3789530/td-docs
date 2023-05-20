from logging import getLogger

from src.libs.pretty import pretty_markdwon
from src.provider.common import CommonParser
from src.template.awa.common import MarkdownTemplateCommon
from src.template.format import Format

logger = getLogger("src").getChild(__name__)

class AWSService():

    def __init__(self) -> None:
        pass

    def service_bridge(self, dic: dict, name: str, aws_type: str) -> str:
        logger.debug(aws_type)
        return self.__aws_common_adapter(dic=dic, name=name, aws_type=aws_type)

    def __aws_common_adapter(self, dic: dict, name: str, aws_type: str, format: Format) -> str:
        data = CommonParser().parser(json_data=dic, type_str=aws_type)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        # TODO support out format 
        if format == Format.HTML:
            pass
        elif format == Format.XLSX:
            pass
        
        return pretty_markdwon(MarkdownTemplateCommon().create_markdown_facade(data=data, name=name, common_type=aws_type))

    # def __aws_iam_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = Iam().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSIam().create_markdown_facade(data=data, name=name, iam_type=aws_tpye))

    # def __aws_rds_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = Rds().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSRds().create_markdown_facade(data=data, name=name, rds_type=aws_tpye))

    # def __aws_ecs_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = Ecs().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSEcs().create_markdown_facade(data=data, name=name, ecs_type=aws_tpye))

    # def __aws_vpc_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = Vpc().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSVpc().create_markdown_facade(data=data, name=name, vpc_type=aws_tpye))

    # def __aws_subnet_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = Subnet().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSSubnet().create_markdown_facade(data=data, name=name, subnet_type=aws_tpye))

    # def __aws_sg_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = SecurityGroup().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSSg().create_markdown_facade(data=data, name=name, sg_type=aws_tpye))

    # def __aws_lb_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
    #     data = Lb().parse(dic, aws_tpye)
    #     if type(data) != dict:
    #         raise Exception("Error parsed data type")
    #     return pretty_markdwon(MarkdownTemplateAWSLb().create_markdown_facade(data=data, name=name, lb_type=aws_tpye))
