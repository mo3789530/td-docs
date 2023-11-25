from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)

class OpenSearch:
    def __init__(self) -> None:
        pass

    def opensearch_parse(self, json: dict, opensearch_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        id = "id"

        attr = json.get(attributes, {})
        return {
            
        }

    def unknown_type(self, json: dict, opensearch_type: str):
        logger.warning(f"{opensearch_type} is not defined")
        return json

    def parse(self, json: dict, opensearch_type: str):
        switcher = {

        }
        return switcher.get(opensearch_type, self.unknown_type)(json=json, dynamo_type=opensearch_type)
