from msgspec.json import Encoder, Decoder, format

JSON_ENCODER = Encoder(order="deterministic")
JSON_DECODER = Decoder(strict=False)


def read_json(file: str) -> dict:
    with open(file, "r") as f:
        return JSON_DECODER.decode(f.read())


def write_json(data, path: str, indent=4, **kwargs):
    with open(path, "w", **kwargs) as f:
        f.write(format(JSON_ENCODER.encode(data).decode(encoding="utf-8"), indent=indent))


def load_json(data):
    return JSON_DECODER.decode(data)


def dump_json(data):
    return JSON_ENCODER.encode(data).decode(encoding="utf-8")


def dumps_json(data, indent=4):
    return format(JSON_ENCODER.encode(data).decode(encoding="utf-8"), indent=indent)
