import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math as math
from mod import stars as st

def csv_to_stars(filename):
    totx = []
    toty = []
    totz = []
    totdis = []
    totvel = []
    totlum = []
    size = 100 
    uni = st.universe(size)
    with open(filename) as datafile:
        hyg = csv.reader(datafile,delimiter=',',quotechar='|')
        tot = 0
        num = 0
        for row in hyg:
            if num > 0:
                dis = float(row[9]) # Parsecs
                x = float(row[17])
                y = float(row[18])
                z = float(row[19])
                if (z > 0 and x > 0 and y > 0 and dis < 15): # Use 900000
                    tot += 1
                    totx.append(x)
                    toty.append(y)
                    totz.append(z)
                    totdis.append(dis)
                    totvel.append([float(row[20]),float(row[21]),float(row[22])])
                    totlum.append(float(row[33])) # or 13
            num += 1

    max_cart = max([max(totx),max(toty),max(totz)]) # Will define size of 3D bucket

    # Make data structure - works
    for i in range(len(totx)):
        mag = math.sqrt(totx[i]*totx[i]+toty[i]*toty[i]+totz[i]*totz[i])
        x = math.floor(int((totx[i] *totdis[i] / mag)*size/max_cart)-1)
        y = math.floor(int((toty[i] *totdis[i] / mag)*size/max_cart)-1)
        z = math.floor(int((totz[i] *totdis[i] / mag)*size/max_cart)-1)
        uni.structure[x][y][z].append(st.star(totx[i],toty[i],totz[i],totdis[i],totvel[i][0],totvel[i][1],totvel[i][2],totlum[i]))

        max_dis = 0
    for i in uni.structure:
        for j in i:
            for z in j:
                for s_star in z:
                    if s_star.dis > max_dis:
                        max_dis = s_star.dis
    uni.unit = max_dis / size
    print("Size max_distance is " + str(uni.unit) +" parsecs per 1 unit")
    print("num is "+str(num))

    return uni
