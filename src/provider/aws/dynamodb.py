from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)

class DynamoDb:
    def __init__(self) -> None:
        pass

    def dynamo_parse(self, json: dict, dynamo_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        id = "id"

        attr = json.get(attributes, {})
        return {
            
        }

    def unknown_type(self, json: dict, dynamo_type: str):
        logger.warning(f"{dynamo_type} is not defined")
        return json

    def parse(self, json: dict, dynamo_type: str):
        switcher = {

        }
        return switcher.get(dynamo_type, self.unknown_type)(json=json, dynamo_type=dynamo_type)
