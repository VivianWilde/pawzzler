#!/usr/bin/env ipython3

from parse_dialogue import parse
"""Interact with game elements through dialogues and menus."""

"""
Common callbacks - resolve/open/advance questlines,

"""
from locations import Location
from networkx import DiGraph




class InteractableObject:
    """Includes a dialogue tree. Basically, the idea is that it pretends to be a tree, but we actually have a bunch of other weird stuff going on, so weird graph with pointers looping around. But to the user, it's a tree. And we can treat it as a git-style graph. Oh god."""
    # DONE: We need to be able to pass GUI and Gamestate into interactions somehow.
    # DONE: How to populate the tree?
    # TODO: Refactor to use the digraph library
    # TODO: Way to check if a path is valid - are we allowed to continue from the current point?
    def __init__(self, name, gamestate, appearance, scene_filename): # appearance is a filepath
        self.name = name
        self.scenes = parse(scene_filename) # List of digraphs
        self.scene_index = 0
        self.current_id = self.get_root_node() # Pointer to where the user is in the dialogue tree.
        self.appearance = appearance
        self.gamestate=gamestate

        @property
        def dialogue_tree(self):
            return self.scenes[self.scene_index]

        @property
        def current(self):
            return self.dialogue_tree[self.current_id]

        # DONE: Do we want to immediately exit upon hitting a leaf, or do we want an option for NPC to give a final message/warning or something. Ominous prophecies are important.
        # DONE: Comprehensive story for feedback - NPC response/acknowledgement of character choices. So the idea is Npc-prompt -> character chooses a response -> display choice and npc response -> repeat.
    def interact(self):
        self.gamestate.gui.display_line(self.current["response"])
        self.current["callback"](self.gamestate)
        if self.at_leaf():
            self.next_interaction()
            return
        chosen_idx = self.gamestate.gui.dialogue(self.valid_branches)
        chosen_option = self.valid_branches[chosen_idx]
        self.current_id = chosen_option # TODO: get label if necessary
        self.interact()

    @property
    def branches(self):
        return list(self.dialogue_tree.successors(self.current_id))

    @property
    def valid_branches(self):
        return list(filter(lambda x: x["validator"](self.gamestate), self.branches))

    def get_root_node(self):
        return self.dialogue_tree.nodes["BEGIN"]
    # TODO: In parser, BEGIN is a special heading (breaks rules for labelling)

    def at_leaf(self):
        return len(list(valid_options))==0


    def next_interaction(self):
        if self.next_exists():
            self.scene_index+=1 # TODO: Bounds checks
        self.current_id=self.get_root_node()

    def next_exists(self):
        return self.scene_index+1<len(self.scenes)


class Door(InteractableObject):
    def __init__(self, name, gamestate, appearance, new_map,  target_coords):
        self.name = name
        self.target = new_map
        self.target_coords = target_coords
        self.gamestate = gamestate
        self.appearance = appearance
        # self.dialogue_tree = Tree(
        #     DialogueEntry(f"Exit to {self.target.name}?"),
        #     [
        #         DialogueEntry(
        #             "Congratulations. Now get out.", "Yes", callback=self.teleport()
        #         ),
        #         DialogueEntry("Really?", "No"),
        #     ],
        # )
    def interact(self):
        self.teleport()
    def teleport(self):
        self.gamestate.current_map.remove_character()
        self.target.add_character(*self.target_coords)
        self.gamestate.update_map(self.target)

class NonInteractable(InteractableObject):
    def __init__(self, name, appearance):
        self.name = name
        self.appearance = appearance
    def interact(self):
        pass
