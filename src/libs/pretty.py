import json
import pprint
import re
import textwrap


def pretty_json(txt) -> str:
    if type(txt) == str and len(txt) > 0:
        txt = json.loads(txt)
        txt = json.dumps(txt, indent=2)
    # txt = "<pre>" + pprint.pformat(txt, 1) + "</pre>"
    txt = "<pre>" + str(txt) + "</pre>"
    return re.sub("\n", "<br>", txt)


def pretty_markdwon(txt: str) -> str:
    return textwrap.dedent(txt).strip()


def pretty_array(array: list) -> str:
    txt = pprint.pformat(array, 1)
    return re.sub("\n", "<br>", txt)
