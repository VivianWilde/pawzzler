#!/usr/bin/env ipython3
from os import mkdir
import dill
from pathlib import Path
from interactions import InteractableObject, NonInteractable,Door

from character import PC
from gamestate import WANDERING_WIDTH, WANDERING_HEIGHT
from locations import Location


def try_create(path, folder=True):
    if not path.exists():
        path.mkdir() if folder else path.touch()


SAVE_DIR = "./resources/objects"
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

def main(gamestate):
    """Tedious actual generation of objects goes here."""

    wandering_map = Location("Wandering_Screen", "grass", WANDERING_WIDTH, WANDERING_HEIGHT)
    to_file(wandering_map)
    start_map = Location("Homebase", "floor")
    to_file(start_map)

    Dungeon_master = InteractableObject("Dungeon_Master", "Dungeon_Master_image.png", "something.org")
    to_file(Dungeon_master)
    Desk = InteractableObject("Desk", "Desk_image.png", "desk_menu.org")
    #homebase & door
    door_to_homebase = Door()




