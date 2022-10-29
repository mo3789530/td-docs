class Resources:
    mode = "mode"
    terraform_type = "type"
    name = "name"
    provider = "provider"
    instances = "instances"
    resources = "resources"


    def __init__(self) -> None:
        pass

    def resource_parse(self, json) -> list[dict]:
        data = list( map(lambda x: self.parse(x), json[self.resources]))
        return data

    def parse(self, json) -> dict:
        mode = json[self.mode]
        terraform_type = json[self.terraform_type]
        provider = json[self.provider]
        instances = json[self.instances]
        if "aws" in provider:
            provider = "aws"
        else:
            provider = "NA"
        return {
            "mode": mode,
            "type": terraform_type,
            "provider": provider,
            "instances": instances
        }
