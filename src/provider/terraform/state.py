
class State:

    version = "version"
    terraform_version = "terraform_version"
    value = "value"
    serial = "serial"
    resources = "resources"

    def __init__(self) -> None:
        pass

    def parse(self, json) -> dict:
        version = json.get(self.version)
        terraform_version = json.get(self.terraform_version)
        serial = json.get(self.serial)
        resources = json.get(self.resources)

        return {
            "version": version,
            "terraform_version": terraform_version,
            "serial": serial,
            "resources": resources
        }
