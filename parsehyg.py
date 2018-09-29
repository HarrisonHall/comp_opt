import csv
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

totx = []
toty = []
totz = []
size = 1000
with open("hygdata_v3.csv") as datafile:
    hyg = csv.reader(datafile,delimiter=',',quotechar='|')
    tot = 0
    num = 0
    for row in hyg:
        if num > 0:
            x = int(float(row[17]))
            y = int(float(row[18]))
            z = int(float(row[19]))
            #if (x >= 0 and y > 0):
            if (z > 0):
                #print("x "+str(x)+" y "+str(y)+" z "+str(z))
                tot += 1
                totx.append(x)
                toty.append(y)
                totz.append(z)
        num += 1
        
# map to size x size
xmax = max(totx)
ymax = max(toty)
zmax = max(totz)
graphx = []
graphy = []
graphz = []
for i in range(len(totx)):
    totx[i] = int((totx[i])/(xmax) * (size))
    toty[i] = int((toty[i])/(ymax) * (size))
    totz[i] = int((totz[i])/(zmax) * (size))
    if (toty[i] != 0):
        graphx.append(totx[i])
        graphy.append(toty[i])
        graphz.append(totz[i])
        
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
    
