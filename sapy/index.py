import numpy as np


def fdof(model, K, P):
    """Return the matrix and vector correspondent to the free dof

    """
    idf, idr = id_fr(model)
    Kf = K[np.ix_(idf, idf)]
    Pf = P[np.ix_(idf)]

    return Kf, Pf


def id_fr(model):
        """Return index for free and restrained DOF

        """
        idf = []
        idr = []

        for n, bound in enumerate(model.BOUND):
            for dof, b in enumerate(bound):
                if b == 0:
                    idf.append(model.DOF[n, dof])
                if b == 1:
                    idr.append(model.DOF[n, dof])

        return idf, idr


def tdof(model, Uf):
    """Return the vector with the total number of dof

    """
    U = np.zeros(model.nt)

    idf, idr = id_fr(model)

    U[np.ix_(idf)] = Uf[:]

    return U
