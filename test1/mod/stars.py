# stars.py
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

class star:
    def __init__(self,x,y,z,dis,vel_x,vel_y,vel_z,lum): 
        self.x = x #pars
        self.y = y #pars
        self.z = z #pars
        self.dis = dis # pars
        self.vel_x = vel_x * 977813.106 #kmps
        self.vel_y = vel_x * 977813.106 #kmps
        self.vel_z = vel_z * 977813.106 #kmps
        self.mass = math.pow(lum/1,1/3.5)*1.989*math.pow(10,30) # lum sun is 1, mass sun is 1.989*10^30 kg, a = 3.5 for main-series stars, mass in kg
    def __str__(self):
        rstring = ""
        rstring += str(self.x) + " " + str(self.y) + " " + str(self.z)
        rstring += " and mass is " + str(self.mass)
        return rstring
    def vel_tot(self):
        return math.sqrt(self.vel_x*self.vel_x+self.vel_y*self.vel_y+self.vel_z*self.vel_z)

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
                        xgraph.append(my_star.x)
                        ygraph.append(my_star.y)
                        zgraph.append(my_star.z)
                        #print("x y z "+ str(my_star.x))                        
        ax.scatter3D(xgraph,ygraph,zgraph)
        plt.show()
    def graph_path_set(self,star_paths):
        ax = plt.axes(projection='3d')
        xgraph = []
        ygraph = []
        zgraph = []
        for i in self.structure:
            for j in i:
                for z in j:
                    for my_star in z:
                        xgraph.append(my_star.x)
                        ygraph.append(my_star.y)
                        zgraph.append(my_star.z)

        ax.scatter3D(xgraph,ygraph,zgraph)
        plt.show()
    def pos_to_bucket(self,x,y,z):
        return

class star_path:
    def __init__(self):
        self.fin_vel = 0
        self.fuel1 = 0
        self.fuel2 = 0
        self.stars = []
    def __lt__(self,other_path):
        return self.fin_vel < other_path.fin_vel
    def __eq__(self,other_path):
        return self.fin_vel == other_path.fin_vel
    def fuel_ratio(self):
        return fuel1 / fuel2
    
class star_path_set:
    def __init__(self,size): # Use 10 for size
        self.size = size
        self.paths = []
        self.total_considered = 0
    def add_path(self,path):
        self.total_considered += 1
        if (len(self.paths) < self.size):
            for some_path in self.paths:
                if (abs(some_path.fin_vel - path.fin_vel) < 0.01):
                    return
            self.paths.append(path)
            self.paths.sort(reverse=True)
        else:
            self.paths.sort(reverse=True)
            for some_path in self.paths:
                if (abs(some_path.fin_vel - path.fin_vel) < 0.01):
                    return
            for i in range(len(self.paths)):
                if (path.fin_vel > self.paths[i].fin_vel):
                    self.paths.insert(i,path)
                    del[self.paths[self.size-1]]

        
