from utils.json import read_json, write_json
from os import scandir


def fmt(path: str):
    write_json(read_json(path), path)


def fmt_excel():
    dir = scandir("data/excel/")

    for item in dir:
        path = item.path
        if path.endswith(".json"):
            fmt(path)


def fmt_cfg():
    dir = scandir("config/")

    for item in dir:
        path = item.path
        if path.endswith(".json"):
            fmt(path)
