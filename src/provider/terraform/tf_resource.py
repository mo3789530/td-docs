from src.provider.terraform.vender import ProviderVendor


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
        data = list(map(lambda x: self.parse(x), json[self.resources]))
        return data

    def parse(self, json: dict) -> dict:
        mode = json.get(self.mode)
        terraform_type = json.get(self.terraform_type)
        provider = json.get(self.provider, "")
        instances = json.get(self.instances)
        if "aws" in provider:
            provider = ProviderVendor.AWS.value
        else:
            provider = ProviderVendor.NA.value
        return {
            "mode": mode,
            "type": terraform_type,
            "provider": provider,
            "instances": instances
        }
