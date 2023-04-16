import json
from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Undefined:
    def __init__(self) -> None:
        pass

    def parser(self, json_data: dict, type_str: str):
        data = {}
        for k in json_data.keys():
            v = self.format(json_data[k])
            data[k] = v if v != "" else "None"
        return data

    def format(self, data: any):
        v = None
        if type(data) is dict:
            v = pretty_json(json.dumps(data))
        elif type(data) is list:
            v = []
            for d in data:
                tmp = self.format(d)
                v.append(tmp)
            v = pretty_array(v)
        elif v == "null" or v == None:
            v = "None"

        return v
