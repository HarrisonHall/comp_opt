import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math as math

totx = []
toty = []
totz = []
totdis = []
size = 1000
with open("hygdata_v3.csv") as datafile:
    hyg = csv.reader(datafile,delimiter=',',quotechar='|')
    tot = 0
    num = 0
    for row in hyg:
        if num > 0:
            dis = float(row[9])
            x = float(row[17])
            y = float(row[18])
            z = float(row[19])
            #if (x >= 0 and y > 0):
            if (z > 0 and x > 0 and y > 0):
                #print("x "+str(x)+" y "+str(y)+" z "+str(z))
                tot += 1
                totx.append(x)
                toty.append(y)
                totz.append(z)
                totdis.append(dis)
        num += 1

print(str(max(totdis)))
# map to size x size
xmax = 0
ymax = 0
zmax = 0
graphx = []
graphy = []
graphz = []
'''
for i in range(len(totx)):
    totx[i] = int((totx[i])/(xmax) * (size))
    toty[i] = int((toty[i])/(ymax) * (size))
    totz[i] = int((totz[i])/(zmax) * (size))
    if (toty[i] != 0):
        graphx.append(totx[i])
        graphy.append(toty[i])
        graphz.append(totz[i])
'''
for i in range(len(totx)):
    mag = math.sqrt(totx[i]*totx[i]+toty[i]*toty[i]+totz[i]*totz[i])
    #print(str(totx[i]) + " "+str(toty[i]) + " "+str(totz[i])+ " mag and dis"+str(mag)+" "+str(totdis[i]) )
    x = totx[i] * totdis[i] / mag
    y = toty[i] * totdis[i] / mag
    z = totz[i] * totdis[i] / mag
    if (x < 20000 and y < 20000 and z < 20000):
        graphx.append(x)
        graphy.append(y)
        graphz.append(z)

        
print("graph data")
#for i in range(len(graphx)):
    #print("x "+str(graphx[i])+" y "+str(graphy[i])+" z "+str(graphz[i]))

print("numpoints "+str(len(graphx)))    
#plt.plot(graphx, graphy, 'ro')
ax = plt.axes(projection='3d')
'''
for i in range(len(graphx)):
    ax.scatter(graphx[i], graphy[i], graphz[i])
'''
#ax.plot3D(graphx,graphy,graphz)
ax.scatter3D(graphx,graphy,graphz)
plt.show()
#plt.show()
        
print("num is "+str(num))
    
