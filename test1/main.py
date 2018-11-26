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

# Define simulation values
gross_mass = 30708 #kg, 67,700 earth-lbs, SLS (second stage)
base_mass = 3490

#ion = engine("Ion Propulsion", 8000, 500) # From Rocket Propulsion Elements
#meth_ox = engine("LOX-Methane", 311, 10000) # 311 is shifting, 296 for frozen (vacuum figure?), 10000 is null
ion = eng.engine("Ion Propulsion", 50, 8000, 500) # From Wikipedia 50 is max of range 20-50
meth_ox = eng.engine("LOX-Methane", 3.8, 311, 10000) # exhaust speed in km/s

base_speed = 16.25 #km/s
print("\n\nStarting Sim:\n")
#sim.sim_single_one_print(universe,math.pi/4,math.pi/4,604800*52,ion,meth_ox,gross_mass,base_speed)

total_paths = st.star_path_set(10)
sim.sim_rec_print(universe,604800*52,ion,gross_mass,base_mass,16.25,total_paths)
print("size of total_paths is "+str(total_paths.total_considered))

# Assumptions:
# Single stage, no payload, little exterior (essentially all fuel), all stars are main-series

