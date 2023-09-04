from typing import TypedDict, List


class Node(TypedDict):
    id: int
    x: float
    y: float

class Element(TypedDict):
    id: int
    nodes: List[int]

class Value(TypedDict):
    element_id: int
    value: float

class Mesh(TypedDict):
    nodes: List[Node]
    elements: List[Element]
    values: List[Value]

class ElementWithValue(TypedDict):
    id: int
    nodes: List[int]
    value: float