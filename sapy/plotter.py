import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
from matplotlib.lines import Line2D
import numpy as np


def window(name):
    return plt.figure(name)


def show():
    plt.show()
    return None


def undeformed(model):
    """Plot the undeformed structure according to the dimension

    """
    if model.ndm == 2:
        undeformed = window('Undeformed')
        axes = undeformed.add_subplot(111, aspect='equal')
        geo2d(model.XYZ, model.CON, axes, color='black')
        label2d(model.XYZ, model.CON, axes)
        undeformed.tight_layout()

    if model.ndm == 3:
        undeformed = window('Undeformed')
        axes = undeformed.add_subplot(111, projection='3d', aspect='equal')
        geo3d(model.XYZ, model.CON, axes, 'black')
        label3d(model.XYZ, model.CON, axes)
        undeformed.tight_layout()


def deformed(model, U):
    """Plot the deformed structure according to the dimension

    """
    CON = model.CON

    XYZ = np.copy(model.XYZ)
    for n in range(model.nn):
        for d in range(model.ndf[n]):
            dof = model.DOF[n, d]
            XYZ[n, d] += U[dof]

    if model.ndm == 2:
        deformed = window('Deformed')
        axes = deformed.add_subplot(111, aspect='equal')
        geo2d(XYZ, CON, axes, 'tomato')
        geo2d(model.XYZ, model.CON, axes, 'black')
        label2d(XYZ, CON, axes)
        deformed.tight_layout()

    if model.ndm == 3:
        deformed = window('Deformed')
        axes = deformed.add_subplot(111, projection='3d', aspect='equal')
        geo3d(model.XYZ, model.CON, axes, 'black')
        geo3d(XYZ, CON, axes, 'tomato')
        label3d(XYZ, CON, axes)
        deformed.tight_layout()


def geo3d(XYZ, CON, axes, color):
    """Plot the 3d model

    """
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_zlabel('z')

    # draw nodes
    for node, xyz in enumerate(XYZ):
        axes.scatter(xyz[0], xyz[1], xyz[2], c='k', alpha=1, marker='s')

    # draw edges
    for ele, con in enumerate(CON):
        xs = [XYZ[con[0]][0], XYZ[con[1]][0]]
        ys = [XYZ[con[0]][1], XYZ[con[1]][1]]
        zs = [XYZ[con[0]][2], XYZ[con[1]][2]]
        line = Line3D(xs, ys, zs, linewidth=1.0, color=color)
        axes.add_line(line)


def label3d(XYZ, CON, axes):
    """Plot the nodes and element label

    """
    for node, xyz in enumerate(XYZ):
        axes.text(xyz[0], xyz[1], xyz[2], str(node), color='b', size=10)

    for ele, con in enumerate(CON):
        xm = (XYZ[con[0]][0] + XYZ[con[1]][0])/2
        ym = (XYZ[con[0]][1] + XYZ[con[1]][1])/2
        zm = (XYZ[con[0]][2] + XYZ[con[1]][2])/2
        axes.text(xm, ym, zm, str(ele), color='g', size=10)


def geo2d(XYZ, CON, axes, color):
    """Plot the 2d model

    """
    axes.set_xlabel('x')
    axes.set_ylabel('y')

    # draw nodes
    for xyz in XYZ:
        axes.scatter(xyz[0], xyz[1], c='k', alpha=1, marker='s')

    # draw edges
    for con in CON:
        xs = [XYZ[con[0]][0], XYZ[con[1]][0]]
        ys = [XYZ[con[0]][1], XYZ[con[1]][1]]
        line = Line2D(xs, ys, linewidth=1.0, color=color)
        axes.add_line(line)


def label2d(XYZ, CON, axes):
    """Plot the nodes and element label

    """
    for node, xyz in enumerate(XYZ):
        axes.text(xyz[0], xyz[1], str(node), color='b', size=10)

    for ele, con in enumerate(CON):
        xm = (XYZ[con[0]][0] + XYZ[con[1]][0])/2
        ym = (XYZ[con[0]][1] + XYZ[con[1]][1])/2
        axes.text(xm, ym, str(ele), color='g', size=10)


def axialforce(model, Q):
    """Plot axial force

    """
    if model.ndm == 2:
        axial = window('Axial')
        axes = axial.add_subplot(111, aspect='equal')
        geo2d(model.XYZ, model.CON, axes, color='black')
        axial2d(model.XYZ, model.CON, Q, axes)
        axial.tight_layout()

    if model.ndm == 3:
        axial = window('Axial')
        axes = axial.add_subplot(111, projection='3d', aspect='equal')
        geo3d(model.XYZ, model.CON, axes, 'black')
        axial3d(model.XYZ, model.CON, Q, axes)
        axial.tight_layout()


def axial2d(XYZ, CON, Q, axes):
    """Plot text with axial force value

    """
    for ele, con in enumerate(CON):
        xm = (XYZ[con[0]][0] + XYZ[con[1]][0])/2
        ym = (XYZ[con[0]][1] + XYZ[con[1]][1])/2
        axes.text(xm, ym, str(np.round_(Q[ele], 1)), color='g', size=10)


def axial3d(XYZ, CON, Q, axes):
    """Plot text with axial force value for 3d plot

    """
    for ele, con in enumerate(CON):
        xm = (XYZ[con[0]][0] + XYZ[con[1]][0])/2
        ym = (XYZ[con[0]][1] + XYZ[con[1]][1])/2
        zm = (XYZ[con[0]][2] + XYZ[con[1]][2])/2
        axes.text(xm, ym, zm, str(np.round_(Q[ele], 1)), color='g', size=10)
