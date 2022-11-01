import argparse


def main(args):
    print(args.file)
    print(args.format)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--format")
    args = parser.parse_args()
    main(args=args)
