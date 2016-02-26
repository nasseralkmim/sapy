import numpy as np


class Data():
    """Initialize element data

    """
    def __init__(self):
        self.E = {}
        self.A = {}
        self.I = {}
        self.TYPE = {}

    def localize(self, model, e):
        """Localize element properties in the model

        """
        xyz = model.XYZ[model.CON[e, :]]

        DOF = model.DOF
        CON = model.CON[e]

        # incd = [dof1_e dof2_e dof3_e dof4_e ... ]
        incd = np.concatenate((DOF[CON[:]]))

        return xyz, incd

    def length_dircos(self, xyz):
        """Return the element length and element directional cosine

        """
        # coordinates differences Dxyz = [ Dx, Dy, Dz]
        Dxyz = xyz[1, :] - xyz[0, :]

        L = np.sqrt(np.dot(np.transpose(Dxyz), Dxyz))

        # direction consine of element x-axis
        dcx = Dxyz/L

        return L, dcx
