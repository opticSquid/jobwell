import json


def load_json(text: str) -> dict:
    return json.loads(text)


def dump_json(payload: dict) -> str:
    return json.dumps(payload, indent=2)
