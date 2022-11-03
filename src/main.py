import argparse
import json

from service.aws import AWSService


def json_open(file_path: str) -> dict:
    json_data = open(file=file_path, mode='r')
    return json.load(json_data)


def parse(data: dict):
    pass


def main(args):
    print(f'start tf-doc file: {args.file}')
    # print(args.file)
    # print(args.format)
    data = None
    try:
        data = json_open(args.file)
        data.get("resources")
    except Exception as e:
        print(e)
        exit(-1)

    data = data.get("resources", {})
    aws = AWSService()
    for d in data:
        if len(d.get("instances", [])) >= 1:
            s = aws.service_bridge(d.get("instances", [])[0],
                                   d.get("name", ""), d.get("type", ""))
            print(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    args = parser.parse_args()
    main(args=args)
