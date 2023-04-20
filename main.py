import sys
import os
import cv2
import numpy as np
from datetime import datetime
from concaveHull import hull
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import csv
import shutil
from stl import mesh
import _thread

class externalFlow:
    def __init__(self):
        self.eventName = 'test'
        self.imageFolder = 'images'
        self.aoaArr = [0, 5, 10, 15] #array for angles of attasck
        self.blurValue = 5 #should be an odd number
        self.cannyMinValue = 5 #seems to work well for most pictures
        self.cannyMaxValue = 200 #seems to work well for most pictures

    def initialCheck(self, filePath):
        if not os.path.isfile(filePath):
            raise Exception('File '+fileName+' does not exist in '+filePath)

    def processImage(self, filePath):
        print('Processsing images')
        self.frame = []
        self.frame.append(cv2.imread(filePath,0))
        self.frame.append(cv2.GaussianBlur(self.frame[-1], (self.blurValue, self.blurValue), 0))
        self.frame.append(cv2.Canny(self.frame[-1], 10, 200))
        self.frame.append(cv2.bitwise_not(self.frame[-1]))

    def getPoints(self):
        self.frame.append(np.rot90(self.frame[-1], 3))
        points = np.argwhere(self.frame[-1] == 0)
        
        if len(points) == 0:
            raise Exception('No points detected after image processsing. Try adjusting the parameters')

        ch = hull()
        ch.loadpoints(points)
        ch.calculatehull()
        boundary_points = np.vstack(ch.boundary.exterior.coords.xy).T        

        D = pdist(boundary_points)
        D = squareform(D);
        N, [I_row, I_col] = np.nanmax(D), np.unravel_index( np.argmax(D), D.shape )
        vect = [[boundary_points[I_col,0], boundary_points[I_col,1]],
                [boundary_points[I_row,0], boundary_points[I_row,1]]]
        theta = np.arctan2(vect[1][1]-vect[0][1],vect[1][0]-vect[0][0])
        rotationMatrix = np.matrix([[np.cos(-theta), -np.sin(-theta)], [np.sin(-theta), np.cos(-theta)]])

        coords = np.zeros(boundary_points.shape)
        boundary_points_shifted = boundary_points-np.array([boundary_points[I_col,0],boundary_points[I_col,1]])
        for i,v in enumerate(boundary_points_shifted):
            coords[i] = (rotationMatrix @ v)/N
        return coords
            
    def rotatePoints(self, aoa, coords):
        R = np.matrix([[np.cos(-float(aoa)*np.pi/180), -np.sin(-float(aoa)*np.pi/180)], [np.sin(-float(aoa)*np.pi/180), np.cos(-float(aoa)*np.pi/180)]])
        o = np.atleast_2d((0, 0))
        return np.squeeze((R @ (coords.T-o.T) + o.T).T)
            
    def generateSubFolder(self, folderName, aoa):
        os.mkdir(folderName+'/'+aoa)
            
    def generateSTL(self, rotatedCoords):
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
                
    def savelocally(self, folderName, aoa, rotatedCoords, geometry):
        for i in range(len(self.frame)):
            cv2.imwrite(folderName+'/'+aoa+'/'+'step'+str(i)+'.png', self.frame[i])
        
        fig = plt.figure(folderName)
        ax = fig.add_subplot(111, aspect='equal')
        ax.plot(rotatedCoords[:,0], rotatedCoords[:,1], '-sk', markersize=2, linewidth=0.25)
        ax.set_ylim(-0.2, 0.2);
        plt.grid()
        plt.savefig(folderName+'/'+aoa+'/'+'points.svg', bbox_inches='tight')
        plt.clf()
        
        np.savetxt(folderName+'/'+aoa+'/'+'coordinates.xy', rotatedCoords)
    
        geometry.save(folderName+'/'+aoa+'/'+'object.stl')
        
    def OpenFOAMParallel(self, folderName, aoa):
        destination = shutil.copytree("templateCase", folderName+'/'+aoa+"/simulation")
        shutil.copy(folderName+'/'+aoa+'/'+'object.stl', destination+"/constant/triSurface/object.stl")
        _thread.start_new_thread(os.system, ('bash '+folderName+'/'+aoa+'/simulation/Allrun',))
        
    def runProgram(self):
        for fileName in os.listdir(self.imageFolder):
            print('Processing '+fileName)
            groupName = fileName.split(".")[0]
            now = datetime.now()
            directory = os.getcwd()
            folderName = directory+"/"+now.strftime("%Y")+'-'+now.strftime("%m")+'-'+now.strftime("%d")+'-'+self.eventName+'-'+groupName
            os.mkdir(folderName)
            #shutil.move(os.path.join(directory,self.imageFolder,fileName), folderName)
            shutil.copy(os.path.join(directory,self.imageFolder,fileName), folderName)
            filePath = os.path.join(directory,folderName,fileName)
            
            self.initialCheck(filePath)
            self.processImage(filePath)
            coords = self.getPoints()
            for aoa in ["%.1f" % x for x in self.aoaArr]:
                self.generateSubFolder(folderName, aoa)
                rotatedCoords = self.rotatePoints(aoa, coords)
                geometry = self.generateSTL(rotatedCoords)
                self.savelocally(folderName, aoa, rotatedCoords, geometry)
                self.OpenFOAMParallel(folderName, aoa)

if __name__ == "__main__":
    e = externalFlow()
    e.runProgram()
