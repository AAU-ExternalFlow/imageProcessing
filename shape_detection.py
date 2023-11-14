import os
import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform
from concaveHull import hull
from stl import mesh
import matplotlib.tri as mtri
import fileinput
import subprocess
import time
import shutil
import sys



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

def flip_coords_hor(coords):
    abs_max_x = np.abs(np.max(coords))
    flipped_coords = np.copy(coords)
    flipped_coords[:, 0] = abs_max_x - flipped_coords[:, 0]
    return flipped_coords

def flip_coords_ver(coords):
    coords_array = np.array(coords)
    flipped_coords = np.copy(coords_array)
    flipped_coords[:, 1] = -flipped_coords[:, 1]
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

import fileinput
import subprocess


#Okay det virker næsten. Lige nu replacer den bare hele linje 12 i mesh.py filerne. Dog er der problemer med at de filer
#den gemmer ikke ændres. Så omkring linje 495 bliver ikke ændret men den linje er ikke ens for alle. 
#Måske kopier en fil ud til alle og så bare ændrer positionen af kameraet. 
#Kameraet passer dårligt til andre aoa. 

def paraviewResults(aoa_array):
    file_paths = ['/externalflow/imageProcessing/Mesh1.py', '/externalflow/imageProcessing/Mesh2.py', '/externalflow/imageProcessing/Mesh3.py', '/externalflow/imageProcessing/U1.py', '/externalflow/imageProcessing/U2.py', '/externalflow/imageProcessing/P1.py', '/externalflow/imageProcessing/P2.py']

    # Define the common value
    value = aoa_array[0]

    # Define the lines to replace for each file
    lines_to_replace = {
        '/externalflow/imageProcessing/Mesh1.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (501, "SaveScreenshot('/externalflow/assets/{value}/mesh1.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/Mesh2.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (495, "SaveScreenshot('/externalflow/assets/{value}/mesh2.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/Mesh3.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (495, "SaveScreenshot('/externalflow/assets/{value}/mesh3.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/U1.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'D/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (604, "SaveScreenshot('/externalflow/assets/{value}/U1.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/U2.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (601, "SaveScreenshot('/externalflow/assets/{value}/U2.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/P1.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (539, "SaveScreenshot('/externalflow/assets/{value}/P1.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
        '/externalflow/imageProcessing/P2.py': [
            (12, 'foamfoam = OpenFOAMReader(registrationName=\'foam.foam\', FileName=\'/externalflow/simulation/{value}/simulation/foam.foam\')\n'),
            (539, "SaveScreenshot('/externalflow/assets/{value}/P2.png', renderView1, ImageResolution=[3000, 3000],\n")
        ],
    }

    for i, value in enumerate(aoa_array):
        previous_value = aoa_array[i - 1] if i > 0 else 0
        print(f"Current value: {value}, Previous value: {previous_value}")

        for file_path in file_paths:
            replacements = lines_to_replace.get(file_path, [])  # Get the replacements for this file
            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for j, line in enumerate(lines, 1):
                    for line_number, new_line in replacements:
                        if j == line_number:
                            f.writelines(new_line.format(value=value))
                            break
                    else:
                        f.writelines(line)

            subprocess.run(['/externalflow/paraview/bin/pvpython', file_path])



# def paraviewResults(aoa_array):
#     file_paths = ['../imageProcessing/Mesh1.py', '../imageProcessing/Mesh2.py', '../imageProcessing/Mesh3.py']
#     for file_path in file_paths:
#         for value in aoa_array:
#             for i, line in enumerate(fileinput.input(file_path, inplace=True)):
#                 if 'FileName=' in line or 'SaveScreenshot' in line:
#                     line = line.replace(f'FileName={aoa_array[0]}', f'FileName={value}')
#                     line = line.replace(f'simulation/{aoa_array[0]}/simulation', f'simulation/{value}/simulation')
#                 print(line, end='')
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/Mesh1.py'])
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/Mesh2.py'])
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/Mesh3.py'])
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/P1.py'])
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/P2.py'])
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/U1.py'])
#             subprocess.run(['D:\\Program Files\\ParaView 5.11.1\\bin\\pvpython.exe', '../imageProcessing/U2.py'])