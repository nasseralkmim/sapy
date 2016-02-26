from sapy import displmethod
from sapy import element

def main():
    """Problem statement

    """
    mesh_file = 'patch'

    ele = element.Data()
    for i in range(6):
        ele.E[i] = 10.
        ele.A[i] = 10.
        ele.TYPE[i] = 'Truss'

    bound = {0: [1, 1, 1],
             2: [0, 0, 1],
             1: [0, 1, 1]}

    nodal_load = {3: [10.0, -20.0, 50.0]}

    displmethod.solver(mesh_file, ele, bound, nodal_load)

if __name__ == '__main__':
    main()
