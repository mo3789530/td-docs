import re


def pretty_json(txt: str) -> str:
    txt = "<pre>" + txt + "</pre>"
    return re.sub("\n", "<br>", txt)


def pretty_markdwon(txt: str) -> str:
    return re.sub("    ", "", txt)
