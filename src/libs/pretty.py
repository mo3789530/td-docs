import pprint
import re


def pretty_json(txt: str) -> str:
    txt = "<pre>" + pprint.pformat(txt, 1) + "</pre>"
    return re.sub("\n", "<br>", txt)


def pretty_markdwon(txt: str) -> str:
    return re.sub("    ", "", txt)


def pretty_array(array: list) -> str:
    txt = pprint.pformat(array, 1)
    return re.sub("\n", "<br>", txt)
