from sapy import displmethod
from sapy import element


def main():
    """Problem statement

    """
    mesh_file = 'patch2'

    ele = element.Data()
    for i in range(5):
        ele.E[i] = 100.
        ele.A[i] = 10.
        ele.TYPE[i] = 'Truss'

    bound = {0: [1, 1],
             2: [0, 1]}

    nodal_load = {3: [10.0, -20.0]}

    displmethod.solver(mesh_file, ele, bound, nodal_load)

main()
