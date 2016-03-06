import numpy as np


class Builder():
    """Create a model for a structural problem

    """
    def __init__(self, mesh, elem, bound):
        self.name = mesh.name
        self.ne = len(mesh.con)
        self.nn = len(mesh.xyz)

        # XYZ =  [[ x1_e1, x2_e1, x3_e1]
        #         [ x1_e2, x2_e2, x3_e3]]
        self.XYZ = np.array(mesh.xyz)

        if all(self.XYZ[:, 2] == 0):
            self.ndm = 2
        else:
            self.ndm = 3

        # remove Z-component
        if self.ndm == 2:
            self.XYZ = np.delete(self.XYZ, np.s_[2], axis=1)

        # CON = [[n1_e1, n2_e1]
        #        [n1_e2, n2_e2]]
        self.CON = np.array(mesh.con)

        # TYPE = [ele1_type, ele2_type]
        TYPE = list(elem.TYPE.values())
        self.TYPE = np.array(TYPE)

        nq = []
        for t in self.TYPE:
            if t == 'Truss':
                nq.append(1)
            if t == 'Frame':
                nq.append(3)
        self.nq = np.sum(nq)

        # ndf = [num_dof_n1, num_dof_n2]
        ndf = []
        for n in range(self.nn):
            sharedele = np.where(n == self.CON)[0]
            type = self.TYPE[sharedele[:]]

            if all(type == 'Truss'):
                ndf.append(self.ndm)
            else:
                ndf.append((self.ndm - 1)*3)
        self.ndf = np.array(ndf)

        self.nt = np.sum(self.ndf)

        # BOUND = [[1=dof1_n1_r, 1=dof2_n1_r ...]
        #          [0=dof1_n2_f, 1=dof2_n2_r ...]]
        BOUND = []
        for n, dof in enumerate(self.ndf):
            if n in bound.keys():
                if len(bound[n]) != dof:
                    raise Exception("BC different from number of DOF!")

                BOUND.append(bound[n])
            else:
                BOUND.append([0 for i in range(dof)])
        self.BOUND = np.array(BOUND)

        self.nr = np.sum(self.BOUND)
        self.nf = self.nt - self.nr

        if self.nf > self.nq:
            raise Exception('Structure unstable!')

        # DOF = [[dof1_n1, dof2_n1 ...]
        #        [dof1_n2, dof2_n2 ...]]
        DOF = []
        for n, bound in enumerate(self.BOUND):
            DOF.append([n*self.ndf[n] + i for i in range(self.ndf[n])])
        self.DOF = np.array(DOF)

    
