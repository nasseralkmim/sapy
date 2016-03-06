import re
import os


class Parse:
    """Produce mesh with gmsh file.

    Args:
        filename (str): Name of the file with the mesh geometry and properties.

    """
    def __init__(self, filename):
        self.name = filename
        geo_path = os.path.join(filename+'.geo')
        geo_file = open(geo_path, 'r')

        xyz = {}
        con = {}

        for line in geo_file:
            line = line.strip()

            if line.startswith('Point'):
                search_points = [float(f) for f in
                                 re.findall(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)',
                                            line)]
                xyz[search_points[0]] = search_points[1:4]

            if line.startswith('Line'):
                search_lines = [int(f)-1 for f in
                                re.findall(r'[+-]?(?:\d+(?:\.\d*)?|\.\d+)',
                                           line)]
                con[search_lines[0]] = search_lines[1:]

        self.xyz = list(xyz.values())
        self.con = list(con.values())

if __name__ == '__main__':
    mesh = Parse("patch")
