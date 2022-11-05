import argparse
import json
from logging import config, getLogger

from src.service.aws import AWSService

logger = getLogger(__name__)


def json_open(file_path: str) -> dict:
    json_data = open(file=file_path, mode='r')
    return json.load(json_data)


def parse(data: dict):
    pass


def main(args):
    logger.info(f'start tf-doc file: {args.file}')
    # print(args.file)
    # print(args.format)
    data = None
    try:
        data = json_open(args.file)
        data.get("resources")
    except Exception as e:
        logger.error(e)
        exit(-1)

    data = data.get("resources", {})
    aws = AWSService()
    for d in data:
        if len(d.get("instances", [])) >= 1:
            s = aws.service_bridge(d.get("instances", [])[0],
                                   d.get("name", ""), d.get("type", ""))
            logger.debug(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    args = parser.parse_args()
    with open("./log_config.json", 'r') as f:
        log_conf = json.load(f)
    config.dictConfig(log_conf)
    main(args=args)
