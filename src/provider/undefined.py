import json
from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Undefined:
    def __init__(self) -> None:
        pass

    def parser(seld, json_data: dict, type_str: str):
        data = {}
        for k in json_data.keys():
            v = json_data[k]
            if type(v) is dict:
                v = pretty_json(json.dumps(v))
            elif type(v) is list:
                v = pretty_array(v)
            elif v is "null" or v is None:
                v = "None"
            data[k] = v if v is not "" else "None"

        return data
