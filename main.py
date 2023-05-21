import argparse
import json
import re
from logging import config, getLogger
from typing import Optional
from src.libs.s3 import get_list_buckets_with_prefix

from src.libs.md import is_exist_md, write_md
from src.service.aws import AWSService
from src.provider.terraform.state import State
from src.provider.terraform.tf_resource import Resources
from src.libs.html import md_to_html, save
from src.template.format import Format

logger = getLogger(__name__)


def json_open(file_path: str) -> dict:
    json_data = open(file=file_path, mode="r")
    return json.load(json_data)


def output(file: str, output: Optional[str], format: Optional[str], data: str):
    # file check
    if output == None:
        if format == "html":
            output = re.sub(".json", ".html", file)
        else:
            output = re.sub(".json", ".md", file)
            is_exist_md(output)
    else:
        output = output

    if format == "html":
        save(output=output, html=md_to_html(data))
    else:
        write_md(output=output, dst=data)


def main(args):
    logger.info(f"start tf-doc file: {args.file}")
    data = None

    try:
        data = json_open(args.file)
    except Exception as e:
        logger.error(e)
        exit(-1)

    data = State().parse(data).get("resources", [])

    # soted by type
    data = sorted(data, key=lambda x: x["type"])

    aws = AWSService()
    result = ""
    aws.service_bridge(data, Format.XLSX)
    for d in data:
        logger.info(d)
        r = Resources().parse(d)

        dst = aws.service_bridge(
            r.get("attributes", {}), r.get("name", ""),
            r.get("type", ""), format=Format.XLSX
        )
        result += dst
        result += "\n"

    output(file=args.file, output=args.output, format=args.format, data=result)

    logger.info(f"end tf-doc file: {args.file}")


def test_main():
    res = get_list_buckets_with_prefix("test")
    print(res)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    parser.add_argument("--output")
    args = parser.parse_args()
    with open("./log_config.json", "r") as f:
        log_conf = json.load(f)
    config.dictConfig(log_conf)
    main(args=args)
