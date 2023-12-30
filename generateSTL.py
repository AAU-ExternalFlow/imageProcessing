import numpy as np
from stl import mesh
import matplotlib.tri as mtri

def generate_STL(rotatedCoords):
        Nz = 2 #Nz-1 number of triangles in z-direction. 2 for marginally lower file size
        x,y = np.tile(rotatedCoords,(Nz,1)).T
        z = np.repeat(np.linspace(0,1,Nz),len(rotatedCoords))
        xyzCoords = np.vstack((x,y,z))

        u = np.arange(len(rotatedCoords))
        v = np.arange(Nz)
        u, v = np.meshgrid(u, v)
        u, v = u.flatten(), v.flatten()
        tri = mtri.Triangulation(u, v)

        geometry = mesh.Mesh(np.zeros(tri.triangles.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(tri.triangles):
            for j in range(3):
                geometry.vectors[i][j] = xyzCoords.T[f[j],:]
        return geometry
