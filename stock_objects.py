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

stock_char= PC("John Smith", "fez.png", "They/Them")
to_file(stock_char)
x=from_file(make_filepath(stock_char))
# print(x==stock_char)
equiv=(x.name==stock_char.name and x.appearance==stock_char.appearance and x.pronouns==stock_char.pronouns)
print(equiv)
