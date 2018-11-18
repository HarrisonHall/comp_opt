# stars.py
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

class star:
    x = 0
    y = 0
    z = 0
    dis = 0
    vel_x = 0
    vel_y = 0
    vel_z = 0
    mass = 0
    def __init__(self,x,y,z,dis,vel_x,vel_y,vel_z,lum):
        # ID or name?
        self.x = x #pars
        self.y = y #pars
        self.z = z #pars
        self.dis = dis
        self.vel_x = vel_x
        self.vel_y = vel_x
        self.vel_z = vel_z
        self.mass = math.pow(lum/1,1/3.5)*1.989*math.pow(10,30) # lum sun is 1, mass sun is 1.989*10^30 kg, a = 3.5 for main-series stars, mass in kg

class universe:
    structure = []
    unit = 0 #parsecs
    size = 0
    def __init__(self,size_int):
        structure = []
        for i in range(size_int):
            structure.append([])
            for j in range(size_int):
                structure[i].append([])
                for z in range(size_int):
                    structure[i][j].append([])
        self.structure = structure
        self.size = size_int

    def graph(self):
        ax = plt.axes(projection='3d')
        xgraph = []
        ygraph = []
        zgraph = []
        for i in self.structure:
            for j in i:
                for z in j:
                    for my_star in z:
                        #ax.scatter(my_star.x,my_star.y,my_star.z)
                        xgraph.append(my_star.x)
                        ygraph.append(my_star.y)
                        zgraph.append(my_star.z)
        ax.scatter3D(xgraph,ygraph,zgraph)
        plt.show()
        
    def pos_to_bucket(self,x,y,z):
        return

    def recompute_positions():
        return
