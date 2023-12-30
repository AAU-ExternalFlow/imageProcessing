import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform
from concaveHull import hull


def gaussian_blur(image, value):
    return cv2.GaussianBlur(image, (value, value), 0)

def canny(image, min_value, max_value):
    return cv2.Canny(image, min_value, max_value)

def bitwise_not(image):
    return cv2.bitwise_not(image)

# Extract coordinates from bitwise image.
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

# Rotate points based on given aoa.
def rotate_points(aoa, coords):
    R = np.array([[np.cos(-float(aoa)*np.pi/180), -np.sin(-float(aoa)*np.pi/180)], [np.sin(-float(aoa)*np.pi/180), np.cos(-float(aoa)*np.pi/180)]])
    o = np.atleast_2d((0, 0))
    coords_array = np.array(coords)
    return np.squeeze((R @ (coords_array.T-o.T) + o.T).T)

#Flip coordinates horizontally
def flip_coords_hor(coords):
    abs_max_x = np.abs(np.max(coords))
    flipped_coords = np.copy(coords)
    flipped_coords[:, 0] = abs_max_x - flipped_coords[:, 0]
    return flipped_coords

# Flip coordinates vertically
def flip_coords_ver(coords):
    coords_array = np.array(coords)
    flipped_coords = np.copy(coords_array)
    flipped_coords[:, 1] = -flipped_coords[:, 1]
    return flipped_coords
