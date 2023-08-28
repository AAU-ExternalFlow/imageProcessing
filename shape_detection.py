import os
import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform
from concaveHull import hull
from stl import mesh
import matplotlib.tri as mtri
import shutil

def gaussian_blur(image, value):
    return cv2.GaussianBlur(image, (value, value), 0)

def canny(image, min_value, max_value):
    return cv2.Canny(image, min_value, max_value)

def bitwise_not(image):
    return cv2.bitwise_not(image)

def get_points(image):
    points = np.argwhere(image == 0)
        
    if len(points) == 0:
        raise Exception('No points detected after image processing. Try adjusting the parameters')

    ch = hull()
    ch.loadpoints(points)
    ch.calculatehull()
    boundary_points = np.vstack(ch.boundary.exterior.coords.xy).T

    # Calculate pairwise distances between points
    D = pdist(boundary_points)
    D = squareform(D)
    N, [I_row, I_col] = np.nanmax(D), np.unravel_index(np.argmax(D), D.shape)
    vect = [[boundary_points[I_col, 0], boundary_points[I_col, 1]],
            [boundary_points[I_row, 0], boundary_points[I_row, 1]]]
    theta = np.arctan2(vect[1][1] - vect[0][1], vect[1][0] - vect[0][0])
    rotationMatrix = np.array([[np.cos(-theta), -np.sin(-theta)], [np.sin(-theta), np.cos(-theta)]])

    coords = np.zeros(boundary_points.shape)
    boundary_points_shifted = boundary_points - np.array([boundary_points[I_col, 0], boundary_points[I_col, 1]])
    for i, v in enumerate(boundary_points_shifted):
        coords[i] = np.dot(rotationMatrix, v) / N
    return coords

def rotate_points(aoa, coords):
        R = np.array([[np.cos(-float(aoa)*np.pi/180), -np.sin(-float(aoa)*np.pi/180)], [np.sin(-float(aoa)*np.pi/180), np.cos(-float(aoa)*np.pi/180)]])
        o = np.atleast_2d((0, 0))
        coords_array = np.array(coords)
        return np.squeeze((R @ (coords_array.T-o.T) + o.T).T)

def flip_coords(coords):
    flipped_coords = np.copy(coords)
    flipped_coords[:, 0] = -flipped_coords[:, 0]
    return flipped_coords

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


def generateSubFolder(folderName):
    os.makedirs(folderName, exist_ok=True)

    
