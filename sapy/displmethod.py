from sapy import gmsh
from sapy import plotter
from sapy import structure
from sapy import kinematics
from sapy import stiffness
from sapy import load
from sapy import index
import numpy as np


def solver(mesh_file, ele, bound, nodal_load):
    """Displacement method of analysis solver

    """
    mesh = gmsh.Parse(mesh_file)

    model = structure.Builder(mesh, ele, bound)

    plotter.undeformed(model)

    A = kinematics.A_matrix(model, ele)

    Ks = stiffness.Ks_matrix(model, ele)

    K = np.dot(A.T, np.dot(Ks, A))

    P = load.P_vector(model, nodal_load)

    Kf, Pf = index.fdof(model, K, P)

    Uf = np.linalg.solve(Kf, Pf)

    U = index.tdof(model, Uf)

    plotter.deformed(model, U)

    V = np.dot(A, U)

    Q = np.dot(Ks, V)

    plotter.axialforce(model, Q)

    plotter.show()
