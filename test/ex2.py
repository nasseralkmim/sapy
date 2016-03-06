from sapy import displmethod
from sapy import element
from sapy import gmsh
from sapy import structure
from sapy import plotter
import matplotlib.pyplot as plt


mesh_file = 'patch2'

mesh = gmsh.Parse(mesh_file)

ele = element.Data()
for i in range(5):
    ele.E[i] = 100.
    ele.A[i] = 10.
    ele.TYPE[i] = 'Truss'

bound = {0: [1, 1],
         2: [0, 1]}

model = structure.Builder(mesh, ele, bound)

nodal_load = {3: [10.0, -20.0]}

U, Q = displmethod.solver(mesh, model, ele, nodal_load)

plotter.undeformed(model)
plotter.deformed(model, U)
plotter.axialforce(model, Q)

plt.show()
