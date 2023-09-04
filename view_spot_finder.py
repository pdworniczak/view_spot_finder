import sys, json
from typing import List, Set
from mesh_types import Mesh, ElementWithValue

def map_element_to_element_with_value(mesh: Mesh) -> List[ElementWithValue]:
    elements:List[ElementWithValue] = []

    for e in mesh['elements']:
        for v in mesh['values']:
            if v['element_id'] == e['id']:
                match_value = v
                break
        mesh['values'].remove(match_value)
        # values = [v['value'] for v in mesh['values'] if v['element_id'] == e['id']]
        elements.append(ElementWithValue(id=e['id'], nodes=e['nodes'], value=match_value['value']))

    return elements

def find_view_spots(mesh: Mesh):
    spots: List[int] = []
    nodes_allready_used_by_spots: Set[int] = set([])

    elements_with_value = map_element_to_element_with_value(mesh)
    elements_with_value.sort(key=lambda e: e['value'])

    # print(elements_with_value)

    first_spot = elements_with_value.pop()

    spots.append(first_spot['value'])
    nodes_allready_used_by_spots.update(first_spot['nodes'])

    while len(spots) < int(view_spot_number) and len(elements_with_value) > 0:
        potential_spot = elements_with_value.pop()
        # if not set(potential_spot['nodes']).(nodes_allready_used_by_spots):
        #     spots.append(potential_spot['value'])
        # for node_id in potential_spot['nodes']:
        #     if node_id in nodes_allready_used_by_spots:
        #         break
        # if not any(node_id in potential_spot['nodes'] for node_id in nodes_allready_used_by_spots):
        #     spots.append(potential_spot['value'])
        len_used = len(nodes_allready_used_by_spots)
        nodes_allready_used_by_spots.update(potential_spot['nodes'])
        if len_used + 3 == len(nodes_allready_used_by_spots):
            spots.append(potential_spot['value'])



    print(nodes_allready_used_by_spots)
    print(spots)


if __name__ == '__main__':

    args = sys.argv

    if len(args) != 3:
        sys.exit('Please provide two arguments. You have provided {}'.format(len(args)-1))

    _, file_name, view_spot_number = args

    with open(file_name) as meshes_file:
        meshe: Mesh = json.load(meshes_file)


    find_view_spots(meshe)

