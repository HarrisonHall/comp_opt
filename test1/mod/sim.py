# sim.py by Harrison Hall
from mod import stars as st
from mod import engine as eng
import math
import time
import random
random.seed(time.clock())

def sim_single_one_print(universe,d_theta,d_phi,d_t,engine1,engine2, mass_kg, speed_kmps): 
    x,y,z = (0,0,0)
    dir_x = 1 * math.cos(d_theta) * math.sin(d_phi) * (180 / math.pi) * (180 / math.pi)
    dir_y = 1 * math.sin(d_theta) * math.sin(d_phi) * (180 / math.pi) * (180 / math.pi)
    dir_z = 1 * math.cos(d_phi) * (180 / math.pi)
    orig_mass = mass_kg
    vel_cur = to_vel(mass_kg, engine2.exhaust_velocity, 0, speed_kmps/2, speed_kmps)
    fuel1 = 0
    fuel2 = 0
    i = 1
    while (mass_kg > 500 and x >= 0 and y >= 0 and z >= 0 and (fuel1+fuel2) < orig_mass):
        print("Step "+str(i)+": ")
        old_mass = mass_kg
        #mass_kg = to_vel(mass_kg, engine2.exhaust_velocity, 0, speed_kmps/2, speed_kmps)
        mydis = dis_pars(x,y,z,universe)
        try:
            rand_star = random.choice(universe.structure[map_to_unit(x,mydis,universe)][map_to_unit(y,mydis,universe)][map_to_unit(z,mydis,universe)])
            print(str(rand_star))
            mass_kg, dir_x, dir_y, dir_z, x, y, z = dir_to_vel(mass_kg, engine2.exhaust_velocity, vel_cur, speed_kmps, dir_x, dir_y, dir_z, rand_star)
            print("Went to star [insert ID]")
            print(str(len(universe.structure[map_to_unit(x,mydis,universe)][map_to_unit(y,mydis,universe)][map_to_unit(z,mydis,universe)]))+" number of stars in current bucket.")
        except:
            print("Continued forward")
            mass_kg = to_vel(mass_kg, engine2.exhaust_velocity, 0, 99*speed_kmps/100, speed_kmps)
            x,y,z = new_pos(x,y,z,dir_x,dir_y,dir_z,d_t,speed_kmps)
        fuel2 += old_mass - mass_kg
        #x,y,z = new_pos(x,y,z,dir_x,dir_y,dir_z,d_t,speed_kmps)
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
        #time.sleep(1)
        # Check near  stars and recursive gravity assist
        print("---")
        i += 1
        if (map_to_unit(x,mydis,universe) > 50 or map_to_unit(y,mydis,universe) > 50 or map_to_unit(z,mydis,universe) > 50):
            print("Outside of scope.")
            break
    return

def sim_rec_print(universe,d_theta,d_phi,d_t,engine1,engine2, mass_kg, speed_kmps): #d_theta from x, d_phi from x-y
    '''
    Check base cases{
        if out of fuel:
            print/record details
            return
    }
    Move/update stars
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
    new_mass = mass_kg/(math.pow(math.e,(abs(vel_fin-vel_cur))/v_ex))
    return new_mass

def dir_to_vel(mass_kg, v_ex, vel_cur, vel_fin, dir_x, dir_y, dir_z, dir_star):
    new_vel = dot_p(dir_x,dir_y,dir_z,dir_star.x,dir_star.y,dir_star.z)/mag(dir_star.x,dir_star.y,dir_star.z)
    mass_kg = to_vel(mass_kg, v_ex, 0, vel_cur, new_vel)
    mass_kg = to_vel(mass_kg, v_ex, 0, new_vel, vel_fin)
    dir_x = dir_x + dir_star.x
    dir_y = dir_y + dir_star.y
    dir_z = dir_z + dir_star.z
    # Add Gravity assist here! TODO
    return (mass_kg, dir_x, dir_y, dir_z, dir_star.x, dir_star.y, dir_star.z)

def dot_p(x1, y1, z1, x2, y2, z2):
    return x1*x2 + y1*y2 + z1* z2

def mag(x, y, z):
    return math.sqrt(x*x+y*y+z*z)

def dis_km(x,y,z,universe):
    dis = math.sqrt(x*x+y*y+z*z)
    return dis
    
def dis_pars(x,y,z,universe):
    dis = km_to_par(math.sqrt(x*x+y*y+z*z))
    return dis

def map_to_unit(x,mag,universe):
    new_x = math.floor(km_to_par(x)*universe.unit)
    return new_x

def grav_assist(v,some_star,angle):
    u = some_star.vel_tot()
    new_vel = (u*2 + v)*math.sqrt(1 - ((4*u*v*(1 - (cos(angle)*180/math.pi)))/math.pow(v+2*u,2)))
    return new_vel

def star_near_me(x,y,z,universe,mydis):
    num = 0
    i = map_to_unit(x,mydis,universe) 
    j = map_to_unit(y,mydis,universe) 
    k = map_to_unit(z,mydis,universe) 
    x1 = i -1
    y1 = j -1
    z1 = k -1
    while (x1 <= i+1):
        y1 = j-1
        while (y1 <= j+1):
            z1 = k-1
            while (z1 <= k+1):
                try:
                    if len(universe.structure[x1][y1][z1]) > 0:
                        print("True: Stars near ship")
                        return
                except:
                    pass
                z1 += 1
            y1 += 1
        x1 += 1
    print("False: No stars in bucket")
    return