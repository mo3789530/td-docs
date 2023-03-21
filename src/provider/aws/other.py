from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Other:

    def __init__(self) -> None:
        pass

    def parse(self, json: dict, other_type: str):
        pass