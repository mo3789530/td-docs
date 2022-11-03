from logging import getLogger

from libs.pretty import pretty_markdwon
from provider.aws.iam import Iam
from template.awa.markdown.iam import MarkdownTemplateAWSIam

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
        else:
            return ""

    def __aws_iam_adapter(self, dic: dict, name: str, aws_tpye: str) -> str:
        data = Iam().parse(dic, aws_tpye)
        if type(data) != dict:
            raise Exception("Error parsed data type")
        return pretty_markdwon(MarkdownTemplateAWSIam().create_markdown_facade(data=data, name=name, iam_type=aws_tpye))
