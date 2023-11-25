from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)

class Cloudfront:
    def __init__(self) -> None:
        pass

    def cloudfront_parse(self, json: dict, cloudfront_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        id = "id"

        attr = json.get(attributes, {})
        return {
            
        }

    def unknown_type(self, json: dict, cloudfront_type: str):
        logger.warning(f"{cloudfront_type} is not defined")
        return json

    def parse(self, json: dict, cloudfront_type: str):
        switcher = {

        }
        return switcher.get(cloudfront_type, self.unknown_type)(json=json, cloudfront_type=cloudfront_type)
