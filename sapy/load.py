import numpy as np


def P_vector(model, nodal_load):
    """Return the load vector

    """
    P = np.zeros(model.nt)

    for n, p in nodal_load.items():

        if n not in model.CON:
            raise Exception('Not a valid DOF for the applied load!')

        for i, d in enumerate(model.DOF[n]):
            P[d] = p[i]

    return P
