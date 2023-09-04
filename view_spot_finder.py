import sys, json
from typing import List, Set
from mesh_types import Mesh, Value, ElementWithValue

def map_element_to_element_with_value(mesh: Mesh) -> List[ElementWithValue]:
    elements:List[ElementWithValue] = []

    for e in mesh['elements']:
        for v in mesh['values']:
            if v['element_id'] == e['id']:
                match_value = v
                break
        mesh['values'].remove(match_value)
        elements.append(ElementWithValue(id=e['id'], nodes=e['nodes'], value=match_value['value']))

    return elements


def find_view_spots(mesh: Mesh):
    spots: List[Value] = []
    nodes_allready_used_by_spots: Set[int] = set([])

    elements_with_value = map_element_to_element_with_value(mesh)
    elements_with_value.sort(key=lambda e: e['value'])

    first_spot = elements_with_value.pop()

    spots.append({'element_id': first_spot['id'], 'value': first_spot['value']})
    nodes_allready_used_by_spots.update(first_spot['nodes'])

    while len(spots) < int(view_spot_number) and len(elements_with_value) > 0:
        potential_spot = elements_with_value.pop()
        len_used = len(nodes_allready_used_by_spots)
        nodes_allready_used_by_spots.update(potential_spot['nodes'])
        if len_used + 3 == len(nodes_allready_used_by_spots):
            spots.append({'element_id': potential_spot['id'], 'value': potential_spot['value'] })

    print(spots)


if __name__ == '__main__':

    args = sys.argv

    if len(args) != 3:
        sys.exit('Please provide two arguments. You have provided {}'.format(len(args)-1))

    _, file_name, view_spot_number = args

    with open(file_name) as meshes_file:
        meshe: Mesh = json.load(meshes_file)


    find_view_spots(meshe)

