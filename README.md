# View spot finder
There is a map excerpt of a hilly landscape. We call it a mesh. The mesh is partitioned in
triangles; we call them elements. For each element a scalar value is assigned, which represents
the average spot height in this triangle as compared to the sea level.
Mesh definition: A mesh is a collection of elements and nodes. Each node is a location on the
map, given as a 2-dimensional point. It has an identification number (ID), two coordinates and
can serve as a vertex for an element. Every element has an ID and is defined by three vertices
– by three node IDs
blablabla...
## usage
### finding spots:
`python3 view_spot_finder.py {filename} {number_of_spots}` -> `python3 view_spot_finder.py mesh_x_sin_cos_20000.json 10000`
### to test if element id is a spot:
`python3 test_spots.py {filename} {spot_element_id}` -> `python3 test_spots.py mesh_x_sin_cos_20000.json 15800`

## dependencies
### python versions
`Python 3.10.12`
### others
only `mypy` for typings