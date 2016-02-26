from scipy.linalg import block_diag


def Ks_matrix(model, ele):
    """Build the collection of element stiffness matrices

    """
    k = []
    for e in range(model.ne):
        xyz, incd = ele.localize(model, e)

        L, dcx = ele.length_dircos(xyz)

        k.append([k_matrix(model.TYPE[e], ele, e, L)])

    Ks = block_diag(*k)

    return Ks


def k_matrix(type, ele, e, L):
    """Build the element stiffness matrix

    """
    EA = ele.E[e]*ele.A[e]

    if type == 'Truss':
        k = EA/L

    if type == 'Frame':
        raise Exception('Frame element not implemented yet!')

    return k
