#!/usr/bin/env ipython3
from os import mkdir
import dill
from pathlib import Path

from character import PC


def try_create(path, folder=True):
    if not path.exists():
        path.mkdir() if folder else path.touch()


SAVE_DIR = Path.home() / ".local/share/pawzzler"
try_create(SAVE_DIR)


def to_file(thing):
    path = make_filepath(thing)
    with path.open("wb") as f:
        dill.dump(thing, f)


def make_filepath(thing):
    folder = SAVE_DIR / thing.__class__.__name__
    try_create(folder)
    filename = folder / thing.name
    return filename


def from_file(f):
    with f.open("rb") as filename:
        return dill.load(filename)


def from_info(obj_name, obj_class):
    savefile=SAVE_DIR / obj_class / obj_name
    return from_file(savefile)


def recreate(thing):
    path = make_filepath(thing)
    if not path.exists():
        to_file(thing)
    return from_file(path)

def test():
    stock_char = PC("John Smith", "fez.png", "They/Them")
    to_file(stock_char)
    x = recreate(stock_char)
    equiv = (
        x.name == stock_char.name
        and x.appearance == stock_char.appearance
        and x.pronouns == stock_char.pronouns
    )
    print(equiv)

def main():
    """Tedious actual generation of objects goes here."""
    pass
