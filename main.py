import argparse
import json
import re
from logging import config, getLogger

from src.libs.md import is_exist_md, write_md
from src.service.aws import AWSService
from src.provider.terraform.state import State
from src.provider.terraform.tf_resource import Resources

logger = getLogger(__name__)


def json_open(file_path: str) -> dict:
    json_data = open(file=file_path, mode='r')
    return json.load(json_data)


def main(args):
    logger.info(f'start tf-doc file: {args.file}')
    data = None
    output = ""

    # file check
    if args.output == None:
        output = re.sub(".json", ".md", args.file)
    else:
        output = args.output
    try:
        data = json_open(args.file)
        is_exist_md(output)
    except Exception as e:
        logger.error(e)
        exit(-1)

    data = State().parse(data)
    print(data)
    print("---------------------")
    data = data.get("resources", [])

    # soted by type
    data = sorted(data, key=lambda x: x['type'])

    print(data)

    aws = AWSService()
    for d in data:
        logger.info(d)
        r = Resources().parse(d)
        print("---------------------")
        print(d)

        dst = aws.service_bridge(
            d.get("values", {}), r.get("name", ""), r.get("type", ""))
        write_md(output=output, dst=dst)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    parser.add_argument("--output")
    args = parser.parse_args()
    with open("./log_config.json", 'r') as f:
        log_conf = json.load(f)
    config.dictConfig(log_conf)
    main(args=args)
