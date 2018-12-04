# main.py, Harrison Hall
import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math as math
from mod import stars as st
from mod import read
from mod import sim
from mod import engine as eng

universe = read.csv_to_stars("mod/hygdata_v3.csv")
universe.graph()

# Define simulation values, SLS
gross_mass = 30708 #kg, 67,700 earth-lbs, SLS (second stage)
base_mass = 3490 # kg
ion = eng.engine("Ion Propulsion", 50, 8000, 500) # From Wikipedia 50 is max of range 20-50
meth_ox = eng.engine("LOX-Methane", 5, 311, 10000) # exhaust speed in km/s
EUROJET_EJ200 = eng.engine("EJ200", 58.4, 0, 0) # exhaust speed in km/s
VSIMR = eng.engine("Variable Specific Impulse Magnetoplasma Rocket", 120, 8000, 500)

base_speed = 16.25 #km/s
total_paths = st.star_path_set(100000)
# Max speed would naturally be ~108.74 km/s

# Run
print("\nStarting Simulation:\n")
#sim.sim_single_one_print(universe,math.pi/4,math.pi/4,604800*52,ion,meth_ox,gross_mass,base_speed)
sim.sim_rec_print(universe,604800*52,ion,gross_mass,base_mass,base_speed,total_paths)

# Analyze
print(ion.name)
print("size of total_paths is "+str(total_paths.total_considered))
i = 1
lastpv = 0
lastcount = 0
for path in total_paths.paths:
    if ((abs(lastpv - path.fin_vel) < 0.01) or path.fin_vel < 0):
        continue
    lastpv = path.fin_vel
    lastcount = len(path.stars)
    if (len(path.stars) == 0):
        print("**")
    print("Stars:\t" + str(len(path.stars)) + "\tFinal Velocity:\t" + str(path.fin_vel) + "\tkm/s")
    i += 1
print("\n"+str(i)+" unique paths")

# Graph - N/A
'''
i = 1
lastpv = 0
lastcount = 0
fig = plt.figure()
ax = fig.gca(projection='3d')
for path in total_paths.paths:
    if (i > 1000):
        continue
    if ((abs(lastpv - path.fin_vel) < 0.01) or path.fin_vel < 0):
        continue
    if (len(path.stars) < 3):
        continue
    lastpv = path.fin_vel
    lastcount = len(path.stars)
    i += 1
    u = [0.001]
    v = [0.001]
    w = [0.001]
    x = []
    y = []
    z = []
    for c in range(len(path.stars)): #arg
        if (path.stars[c].x < 0):
            print("invalid position")
        u.append(path.stars[c].x)
        v.append(path.stars[c].y)
        w.append(path.stars[c].z)
        x.append(path.stars[c].x)
        y.append(path.stars[c].y)
        z.append(path.stars[c].z)
    x.append(path.stars[len(path.stars)-1].x-u[len(path.stars)-1])
    y.append(path.stars[len(path.stars)-1].y-v[len(path.stars)-1])
    z.append(path.stars[len(path.stars)-1].z-w[len(path.stars)-1])
    arrowprops=dict(arrowstyle='<->, head_width=10', facecolor='black')
    ax.quiver(u,v,w,x,y,z,pivot="tail")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)
ax.set_zlim(-1, 10)
plt.show()
'''

# Graph color points
i = 0
ax = plt.axes(projection='3d')
for path in total_paths.paths:
    i += 1
    if (i > 1 or i > len(total_paths.paths)):
        break
    x = [0]
    y = [0]
    z = [0]
    for some_star in path.stars:
        x.append(some_star.x)
        y.append(some_star.y)
        z.append(some_star.z)
    ax.scatter3D(x,y,z,c='r')
    for row in universe.structure:
        for col in row:
            for depth in col:
                for s in depth:
                    ax.scatter3D(s.x,s.y,s.z,c='b')
plt.show()

'''
i = 0
colors = ['b','g','r','c','m','y','k']
ax = plt.axes(projection='3d')
for path in total_paths.paths:
    i += 1
    if (i > 1000 or i > len(total_paths.paths)):
        break
    x = [0]
    y = [0]
    z = [0]
    for some_star in path.stars:
        x.append(some_star.x)
        y.append(some_star.y)
        z.append(some_star.z)
    ax.scatter3D(x,y,z,c=colors[i%len(colors)])
plt.show()
'''
    
    
