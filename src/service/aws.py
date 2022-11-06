from logging import getLogger

from src.libs.pretty import pretty_markdwon
from src.provider.aws.ecs import Ecs
from src.provider.aws.iam import Iam
from src.provider.aws.rds import Rds
from src.provider.aws.security_group import SecurityGroup
from src.provider.aws.subnet import Subnet
from src.provider.aws.vpc import Vpc
from src.template.awa.markdown.ecs import MarkdownTemplateAWSEcs
from src.template.awa.markdown.iam import MarkdownTemplateAWSIam
from src.template.awa.markdown.rds import MarkdownTemplateAWSRds
from src.template.awa.markdown.security_group import MarkdownTemplateAWSSg
from src.template.awa.markdown.subnet import MarkdownTemplateAWSSubnet
from src.template.awa.markdown.vpc import MarkdownTemplateAWSVpc

logger = getLogger("src").getChild(__name__)


class AWSService():
    # ecs = ECS()
    # ec2 = ec2.EC2()

    def __init__(self) -> None:
        pass

    def service_bridge(self, dic: dict, name: str, aws_type: str) -> str:
        if "iam" in aws_type:
            logger.debug("iam_type " + aws_type)
            return self.__aws_iam_adapter(dic=dic, name=name, aws_tpye=aws_type)
        elif "rds" in aws_type or "db" in aws_type:
            return self.__aws_rds_adapter(dic=dic, name=name, aws_tpye=aws_type)
        elif "ecs" in aws_type:
            return self.__aws_ecs_adapter(dic=dic, name=name, aws_tpye=aws_type)
        elif "subnet" in aws_type:
            return self.__aws_subnet_adapter(dic=dic, name=name, aws_tpye=aws_type)
        elif "vpc" in aws_type:
            return self.__aws_vpc_adapter(dic=dic, name=name, aws_tpye=aws_type)
        elif "aws_security_group" in aws_type:
            return self.__aws_sg_adapter(dic=dic, name=name, aws_tpye=aws_type)
        else:
            return ""

    def __aws_iam_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = Iam().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSIam().create_markdown_facade(data=data, name=name, iam_type=aws_tpye))

    def __aws_rds_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = Rds().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSRds().create_markdown_facade(data=data, name=name, rds_type=aws_tpye))

    def __aws_ecs_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = Ecs().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSEcs().create_markdown_facade(data=data, name=name, ecs_type=aws_tpye))

    def __aws_vpc_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = Vpc().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSVpc().create_markdown_facade(data=data, name=name, vpc_type=aws_tpye))

    def __aws_subnet_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = Subnet().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSSubnet().create_markdown_facade(data=data, name=name, subnet_type=aws_tpye))

    def __aws_sg_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = SecurityGroup().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSSg().create_markdown_facade(data=data, name=name, sg_type=aws_tpye))
