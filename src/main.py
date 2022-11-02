import argparse
import json

import provider.terraform.state as State


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
        print(data.get("resources"))
    except Exception as e:
        print(e)
        exit(-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    args = parser.parse_args()
    main(args=args)
