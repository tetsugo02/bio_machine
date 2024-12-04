import json


def load_morse(path: str) -> dict:
    eng_morse: dict = open(path, "r")
    eng_morse: dict = json.load(eng_morse)
    return eng_morse
