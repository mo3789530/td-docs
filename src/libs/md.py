import os


def is_exist_md(file_name: str):
    if os.path.isfile(file_name) == True:
        raise Exception("File is exist")


def write_md(output: str, dst: str):
    with open(output, mode='a') as f:
        f.write(dst)
