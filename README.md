# View spot finder
There is a map excerpt of a hilly landscape. We call it a mesh. The mesh is partitioned in
triangles; we call them elements. For each element a scalar value is assigned, which represents
the average spot height in this triangle as compared to the sea level.
Mesh definition: A mesh is a collection of elements and nodes. Each node is a location on the
map, given as a 2-dimensional point. It has an identification number (ID), two coordinates and
can serve as a vertex for an element. Every element has an ID and is defined by three vertices
– by three node IDs
blablabla...
## example usage
`python3 view_spot_finder.py mesh_x_sin_cos_20000.json 10000`
## used python versions
`Python 3.10.12`