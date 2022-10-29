
class State:

    version   = "version"
    terraform_version = "terraform_version"
    region    = "region"
    outputs   = "outputs"
    value     = "value"
    resources = "resources"

    def __init__(self) -> None:
        pass

    def parse(self, json) -> dict:
        version = json[self.version]
        region = json[self.outputs][self.region][self.value]
        resources = json[self.resources]

        return {
            "version": version,
            "region": region,
            "resources": resources
        }


