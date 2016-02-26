import numpy as np


def A_matrix(model, ele):
    """Return the global kinematic matrix

    """
    A = np.zeros((model.ne, model.nt))
    for e in range(model.ne):
        xyz, incd = ele.localize(model, e)

        ag = ag_matrix(model.TYPE[e], xyz, ele)

        A[e, incd[:]] = ag[:]

    return A


def ag_matrix(type, xyz, ele):
    """Return the elemental kinematics matrix for any element type

    """
    L, dcx = ele.length_dircos(xyz)

    if type == 'Truss':
        ag = np.concatenate((-dcx, dcx))

    if type == 'Frame':
        raise Exception('Frame element not implemented yet!')

    return ag


def Af_matrix(model, A):
    """Return only the free dof matrix entries

    """
    idf, idr = model.index_fr()
    print(idf, idr)
    Af = A[np.ix_(idf, idf)]

    return Af
