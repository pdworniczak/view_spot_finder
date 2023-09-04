import sys, json
from typing import List, Set
from mesh_types import Mesh, ElementWithValue
from view_spot_finder import map_element_to_element_with_value

def find_element(elements: List[ElementWithValue], element_id: int):
    for element in elements:
        if element['id'] == element_id:
            return element
        
    return None

def find_neighbor_elements(elements: List[ElementWithValue], node_ids: List[int]):
    neighbor_elements = []
    for element in elements:
        if set(node_ids).intersection(set(element['nodes'])):
            neighbor_elements.append(element)
    return neighbor_elements

def test_spots(mesh: Mesh, spot_id: int):
    elements = map_element_to_element_with_value(mesh)
    print('==============================')
    print(spot_id)
    spot_element = find_element(elements, spot_id)
    print('spot:: ', spot_element)
    print('neighbours:: ')
    neighbour_elements = find_neighbor_elements(elements, spot_element['nodes'])
    for index, neighbour_element in enumerate(neighbour_elements):
        print('{}: {}'.format(index, neighbour_element))
    print('is spot:: ', spot_element['value'] >= max(el['value'] for el in neighbour_elements)) # >= because only one element id with same value could be a spot


if __name__ == '__main__':

    args = sys.argv

    if len(args) != 3:
        sys.exit('Please provide two arguments. You have provided {}'.format(len(args)-1))

    _, file_name, spot_id = args

    with open(file_name) as meshes_file:
        meshe: Mesh = json.load(meshes_file)


    test_spots(meshe, int(spot_id))

