#!/usr/bin/env ipython3
"""Interact with game elements through dialogues and menus."""

"""
Common callbacks - resolve/open/advance questlines,

"""
from locations import Location


class DialogueEntry:
    def __init__(self, line, callback= lambda *args: 5):
        self.line = line
        self.callback=callback

    def __call__(self, *args):
        self.callback(*args)


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, data, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.data = data
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ", " + repr(self.branches)
        else:
            branch_str = ""
        return "Tree({0}{1})".format(self.data, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = "  " * indent + str(t.data) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()


class InteractableObject:
    """Includes a dialogue tree. TODO: How to populate the tree? Basically, the idea is that it pretends to be a tree, but we actually have a bunch of other weird stuff going on, so weird graph with pointers looping around. But to the user, it's a tree. And we can treat it as a git-style graph. Oh god."""

    def __init__(self, menu):
        self.dialogue_tree = Tree(menu, [])
        self.current = self.dialogue_tree
        self.image = None

    @property
    def menu(self):
        return self.dialogue_tree.data

    def interact(self):
        choice = self.menu.make_choice()  # TODO: make it prompt or something
        self.current = self.dialogue_tree.branches[choice]
        # NOTE: interaction also requires a callback (like updating state) associated with a particular dialogue object
        pass

class Door(InteractableObject):
    def __init__(self, new_map, image=None):
        self.target=new_map
        self.image=image

    def interact(self):






class DialogueMenu:
    """"""

    def __init__(self, args):
        self.options = [DialogueEntry("")]
        self.selected = 0
        self.skip = -1  # Entry corresponding to doing nothing

    def notes(self):
        """
        We also need to do something to note which options are allowed, to display the menu, and to return/report the finally selected option. Needs to be interactive. Dialogue tree.
        """

    def make_choice(self):
        magic(frontend)
        chosen = self.options[self.selected]
        if self.selected == self.skip:
            return
        chosen.callback()
        return self.selected


magic = lambda *args: 42
frontend = "1/0 is infinity"
