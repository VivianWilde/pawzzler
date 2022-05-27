from pathlib import Path
from orgparse import load
from networkx import DiGraph

def parse(dialogue_filename):
    dialogues = Path("./resources/dialogues")
    filepath = dialogues / dialogue_filename
    file_node = load(filepath.absolute())
    begin_nodes = file_node.children
    scenes = []

    for begin_org_node in begin_nodes:
        scene = DiGraph()
        scene.add_node("sentinel")
        create_graph(begin_org_node,"sentinel", scene)
        scenes.append(scene)
    return scenes

def create_graph(org_node, parent_id,  scene):
    root_id = create_node(org_node, parent_id, scene)
    for child_org_node in org_node.children:
        create_graph(child_org_node, root_id, scene)

def create_node(org_node, parent_id, scene):
    line = org_node.get_heading()
    resp = org_node.get_body()

    callback = eval(org_node.get_property("callback", "lambda gamestate:None"))
    validator = eval(org_node.get_property("validator", "lambda gamestate:True"))

    if line == "BEGIN":
        new_id = line
    else:
        new_id = line + resp

    scene.add_node(new_id, line=line, resp=resp, callback= callback, validator= validator)
    scene.add_edge(parent_id, new_id)
    return new_id
