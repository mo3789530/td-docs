from provider.aws.ecs import ECS
from provider.aws.ec2 import EC2
from provider.aws.iam import Iam


class AWSPerser:
    ecs = ECS()
    ec2 = EC2()
    iam = Iam()
    def __init__(self) -> None:
        pass