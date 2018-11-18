# sim.py by Harrison Hall
from mod import stars as st
from mod import engine as eng
import math
import time

def sim_single_one_print(universe,d_theta,d_phi,d_t,engine1,engine2, mass_kg, speed_kmps): #d_theta from x, d_phi from x-y
    # TODO: make stars move, iterate through d_theta and d_phi, modify gravity assist
    x = y = z = 0
    dir_x = 1 * math.cos(d_theta) * math.sin(d_phi) * (180 / math.pi) * (180 / math.pi)
    dir_y = 1 * math.sin(d_theta) * math.sin(d_phi) * (180 / math.pi) * (180 / math.pi)
    dir_z = 1 * math.cos(d_phi) * (180 / math.pi)
    orig_mass = mass_kg
    fuel1 = 0
    fuel2 = 0
    i = 1
    while (mass_kg > 0.5 and x >= 0 and y >= 0 and z >= 0 and (fuel1+fuel2) < orig_mass):
        print("Step "+str(i)+": ")
        old_mass = mass_kg
        mass_kg = to_vel(mass_kg, engine2.exhaust_velocity, 0, speed_kmps/2, speed_kmps)
        fuel2 += old_mass - mass_kg
        x,y,z = new_pos(x,y,z,dir_x,dir_y,dir_z,d_t,speed_kmps)
        mydis = dis_pars(x,y,z,universe)
        print("Distance:\t"+str(mydis))
        print("x (parsecs):\t"+str(km_to_par(x)))
        print("y (parsecs):\t"+str(km_to_par(y)))
        print("z (parsecs):\t"+str(km_to_par(z)))
        print("bin x:\t"+str(map_to_unit(x,mydis,universe)))
        print("bin y:\t"+str(map_to_unit(y,mydis,universe)))
        print("bin z:\t"+str(map_to_unit(z,mydis,universe)))
        print("fuel2(kg):\t"+str(fuel2))
        print("New mass:\t"+str(mass_kg))
        time.sleep(1)
        # Check near  stars and recursive gravity assist
        print("---")
        i += 1
    return

def sim_rec_print(universe,d_theta,d_phi,d_t,engine1,engine2, mass_kg, speed_kmps): #d_theta from x, d_phi from x-y
    '''
    Check base cases{
        if out of fuel:
            print/record details
            return
    }
    Moveupdate stars
    Move forward with d_t
    for star in bucket:
        if star near rocket:
            sim_rec_print() (fuel for new direction)
    
    '''
    return

def new_pos(x,y,z,dir_x,dir_y,dir_z,d_t,vel):
    x = (x + dir_x*vel*d_t) 
    y = (y + dir_y*vel*d_t) 
    z = (z + dir_z*vel*d_t) 
    return (x,y,z)

def km_to_par(x):
    return x * 3.24 * math.pow(10,-14)

def par_to_km(x):
    return x / 3.24 / math.pow(10,-14)

# Tsiolkovsky's equation
def to_vel(mass_kg, v_ex, vel_or, vel_cur, vel_fin):
    new_mass = mass_kg/(math.pow(math.e,(vel_fin-vel_cur)/v_ex))
    return new_mass

def dis_km(x,y,z,universe):
    dis = math.sqrt(x*x+y*y+z*z)
    return dis
    
def dis_pars(x,y,z,universe):
    dis = km_to_par(math.sqrt(x*x+y*y+z*z))
    return dis

def map_to_unit(x,mag,universe):
    new_x = math.floor(km_to_par(x)*universe.unit)
    return new_x

def grav_assist():
    return 0
