import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from fluidfoam import readvector
from fluidfoam import readscalar
from fluidfoam import readmesh
from scipy.interpolate import griddata
import shutil

class externalFlow:
    def __init__(self):
        self.eventName = 'vesthimmerlandsGym'
        self.year = '2021'

    def getClCd(self, folderPath):
        data = np.loadtxt(os.path.join(folderPath, 'simulation', 'postProcessing', 'forces','0','forceCoeffs.dat'), skiprows=9)
        Cd = data[-1,2]
        Cl = data[-1,3]
        return [Cd, Cl];
    
    def printClCd(self, aoa_arr, Cl_arr, Cd_arr, groupName, eventName, year, month, day, baseDir, subDir):
        fig = plt.figure(constrained_layout=True)
        gs = fig.add_gridspec(2, 2)
        fig.suptitle('Results for '+groupName+' from '+eventName+' on '+year+'-'+month+'-'+day)
        
        fig1_ax1 = fig.add_subplot(gs[0,0])
        fig1_ax1.plot(aoa_arr,Cl_arr,'sk')
        fig1_ax1.set_xlabel('Angle of attack (deg)')
        fig1_ax1.set_ylabel("Lift coefficient")
        fig1_ax1.grid()
        
        fig1_ax2 = fig.add_subplot(gs[0,1])
        fig1_ax2.plot(aoa_arr,Cd_arr,'sk')
        fig1_ax2.set_xlabel('Angle of attack (deg)')
        fig1_ax2.set_ylabel('Drag coefficient')
        fig1_ax2.grid()
        
        fig1_ax3 = fig.add_subplot(gs[1,:])
        fig1_ax3.plot(np.array(aoa_arr),np.array(Cl_arr)/np.array(Cd_arr),'sk')
        fig1_ax3.set_xlabel("Angle of attack (deg)")
        fig1_ax3.set_ylabel('Lift coefficient / drag coefficient')
        fig1_ax3.grid()
        fig.savefig(os.path.join(baseDir, subDir,year+'-'+month+'-'+day+'-'+eventName+'-'+groupName+'-'+'results.svg'))
        fig.clf()
        
    def printContours(self, aoaDir, xyCoords, groupName, eventName, year, month, day, baseDir, subDir):
        timename = '2000'
        x, y, z = readmesh(os.path.join(baseDir, subDir, aoaDir,'simulation'))
        vel = readvector(os.path.join(baseDir, subDir, aoaDir,'simulation'), timename, 'U')
        p = readscalar(os.path.join(baseDir, subDir, aoaDir,'simulation'), timename, 'p')
        
        ngridx = 200
        ngridy = 200
        
        xinterpmin = -0.5
        xinterpmax = 1.5
        yinterpmin = -1
        yinterpmax = 1
        
        xi = np.linspace(xinterpmin, xinterpmax, ngridx)
        yi = np.linspace(yinterpmin, yinterpmax, ngridy)
        
        xinterp, yinterp = np.meshgrid(xi, yi)

        # Interpolation of scalra fields and vector field components
        
        p_i = griddata((x, y), p, (xinterp, yinterp), method='linear')
        velx_i = griddata((x, y), vel[0, :], (xinterp, yinterp), method='linear')
        vely_i = griddata((x, y), vel[1, :], (xinterp, yinterp), method='linear')
        
        pV = max(abs(min(p)),abs(max(p)))
        
        fig = plt.figure()
        plt.xlabel('x/c')
        plt.ylabel('y/c')
        cs = plt.contourf(xi, yi, p_i*2.0, 100, cmap=plt.cm.coolwarm)
        cbar = fig.colorbar(cs)
        plt.fill(xyCoords[:-2,0], xyCoords[:-2,1], facecolor='lightgrey', edgecolor='black', linewidth=1)
        plt.title('Pressure contours for an angle of attack of '+aoaDir+' deg')
        plt.axis('scaled')
        plt.savefig(os.path.join(baseDir, subDir,year+'-'+month+'-'+day+'-'+eventName+'-'+groupName+'-'+'pressure_aoa'+aoaDir+'_results.svg'))
        plt.clf()
        
        fig = plt.figure()
        plt.xlabel('x/c')
        plt.ylabel('y/c')
        cs = plt.contourf(xi, yi, np.sqrt(velx_i**2.0+vely_i**2.0), levels=np.linspace(0,2,100), cmap=plt.cm.coolwarm)
        cbar = fig.colorbar(cs, ticks=np.arange(0,2,0.1))
        plt.fill(xyCoords[:-2,0], xyCoords[:-2,1], facecolor='lightgrey', edgecolor='black', linewidth=1)
        plt.title('Velocity contours for an angle of attack of '+aoaDir+' deg')
        plt.axis('scaled')
        plt.savefig(os.path.join(baseDir, subDir,year+'-'+month+'-'+day+'-'+eventName+'-'+groupName+'-'+'velocity_aoa'+aoaDir+'_results.svg'))
        plt.clf()
        
    def runProgram(self):      
        baseDir = os.path.dirname(os.path.abspath(__file__))
        for subDir in os.listdir(baseDir):
            if subDir.startswith(self.year):
                year = subDir.split('-')[0]
                month = subDir.split('-')[1]
                day = subDir.split('-')[2]
                eventName = subDir.split('-')[3]
                groupName = subDir.split('-')[4]
                aoa_arr = []
                Cl_arr = []
                Cd_arr = []
                for aoaDir in os.listdir(os.path.join(baseDir,subDir)):
                    if os.path.isdir(os.path.join(baseDir,subDir,aoaDir)):
                        folderPath = os.path.join(baseDir,subDir,aoaDir)
                        aoa_arr.append(float(aoaDir))
                        [Cd, Cl] = self.getClCd(folderPath)
                        Cl_arr.append(Cl)
                        Cd_arr.append(Cd)
                        xyCoords = np.loadtxt(os.path.join(folderPath,'coordinates.xy'), skiprows=0)
                        self.printContours(aoaDir, xyCoords, groupName, eventName, year, month, day, baseDir, subDir)
                self.printClCd(aoa_arr, Cl_arr, Cd_arr, groupName, eventName, year, month, day, baseDir, subDir)
                shutil.move(os.path.join(baseDir,subDir,groupName+'.jpg'),os.path.join(baseDir, subDir,year+'-'+month+'-'+day+'-'+eventName+'-'+groupName+'-'+'airfoil.jpg'))

if __name__ == "__main__":
    e = externalFlow()
    e.runProgram()
