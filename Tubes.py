# Python3 code to illustrate above approach

import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image as im
import cv2
import random

l = 500  # should be  l_x, l_y ...


# function to calculate distance btw center and given point
def check(cx, cy, x, y, ):
    x1 = math.pow((x - cx), 2)
    y1 = math.pow((y - cy), 2)

    # distance between the centre and given point
    return (x1 + y1)


def check2d(cx, cy, x, y, ):
    x1 = math.pow((x - cx), 2)
    y1 = math.pow((y - cy), 2)

    # distance between the centre and given point
    return math.sqrt(x1 + y1)

# coordinates of the first centre
cx = l / 2
cy = l / 4
cz = l / 2

# cx = l / 2
# cy = l / 2
# cz = l / 4

# coordinates of the second centre
cx1 = l / 2
cy1 = 3*l / 4
cz1 = l / 2

# radius of external cylinder
r1 = l / 8

# radius of cylinder inside (cavity)
r2 = l / 10

# wall label
wall_label = 255

# background and air labels
background_label = 0
air_label = 20

# create 3d numpy array
shape = (l, l, l)
a = np.zeros(shape=shape, dtype=np.uint16)

##WALL AND AIR
##TUBE 1
for x in range(0, l):
    for y in range(0, l):
        for z in range(0, l):
            ans = check(cx, cy, y, z)
            if ans < (r1 ** 2):
                a[x, y, z] = wall_label

for x in range(0, l):
    for y in range(0, l):
        for z in range(0, l):
            ans = check(cx, cy, y, z)
            if ans < (r2 ** 2):
                a[x, y, z] = air_label

##TUBE 2
for x in range(0, l):
    for y in range(0, l):
        for z in range(0, l):
            ans = check(cx1, cy1, y, z)
            if ans < (r1 ** 2):
                a[x, y, z] = wall_label

for x in range(0, l):
    for y in range(0, l):
        for z in range(0, l):
            ans = check(cx1, cy1, y, z)
            if ans < (r2 ** 2):
                a[x, y, z] = air_label

print(a)
print(a.shape)

# percentage of height for cylinder
pl = 80

# remove the bottom
for x in range(0, l):
    for y in range(0, l):
        for o in range(0, l - round((l*pl)/100)):
            a[o, x, y] = background_label

# remove the top
for x in range(0, l):
    for y in range(0, l):
        for o in range(round((pl*l)/100), l):
            a[o, x, y] = background_label


# thikness of the bottom floor of the cylinder == thickness of the wall (delta)
delta = int(r1 - r2)


##CLOSE THE TUBE FROM THE BOTTOM
##TUBE1
for x in range(l - round((l*pl)/100) - delta, l - round((l*pl)/100)):
    for y in range(0, l):
        for z in range(0, l):
            ans = check(cx, cy, y, z)
            if ans < (r1 ** 2):
                a[x, y, z] = wall_label

##TUBE2
for x in range(l - round((l*pl)/100) - delta, l - round((l*pl)/100)):
    for y in range(0, l):
        for z in range(0, l):
            ans = check(cx1, cy1, y, z)
            if ans < (r1 ** 2):
                a[x, y, z] = wall_label


# Full spheres ##########################################

# function to calculate distance btw center and given point
def checksp(cx, cy, cz, x, y, z, ):
    x1 = math.pow((x - cx), 2)
    y1 = math.pow((y - cy), 2)
    z1 = math.pow((z - cz), 2)
    return (x1 + y1 + z1)  # distance between the centre and given point





# maximum number of random spheres per stack
n = 4

# different sphere intensities
sp_col = [40, 80, 120, 160, 200, 240] # material labels


# Spheres randomly distributed inside of the middle cylinders

##FIRST TUBE SPHERES
for x in range(l - round((l*pl)/100), round((pl*l)/100)): # from 20% to 80%
    y = []
    z = []

    # randomly choose the number of spheres for this stack
    sp_num = random.randint(0, n)

    print('#########################################################################################################################')
    print('the stack', x)

    # coordinates of the first centre
    # cx = l / 2
    # cy = l / 4
    # cz = l / 2

    for i in range(0, sp_num):

        y.append(round(random.uniform(cy - r2, cy + r2 - 1)))
        z.append(round(random.uniform(cz - r2, cz + r2 - 1)))

        if (check(cy, cz, y[i], z[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y[i]', y[i])
            print('coordinates z[i]', z[i])

            ans = check2d(cy, cz, y[i], z[i])
            d = r2 - ans
            d = abs(d)

            print('distance 2 wall', d)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d = min(d, abs((l/100)*(pl-50)-abs(x-(l/2))))



            # print('distance to center', ans)
            # print('distance point to cylinder', d)

            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.

            # if d is less than 1 continue
            p = round(random.uniform(1, d),0)

            print('raduius', p)

            # print("the radius randomly generated is:", p)
            # if (check(cy, cz, y[i], z[i]) > r2):
            #     print('#########################################################################################################################')




            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, l):
                        ans = checksp(x, z[i], y[i], x1, y1, z1)
                        if ans < (p ** 2):
                            a[x1, y1, z1] = sp_col[col]



##SECOND TUBE SPHERES

for x in range(l - round((l*pl)/100), round((pl*l)/100)): # from 20% to 80%
    y = []
    z = []

    # randomly choose the number of spheres for this stack
    sp_num = random.randint(0, n)

    print('#########################################################################################################################')
    print('the stack', x)

    for i in range(0, sp_num):

        y.append(round(random.uniform(cy1 - r2, cy1 + r2 - 1)))
        z.append(round(random.uniform(cz1 - r2, cz1 + r2 - 1)))

        if (check(cy1, cz1, y[i], z[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y[i]', y[i])
            print('coordinates z[i]', z[i])

            ans = check2d(cy1, cz1, y[i], z[i])
            d = r2 - ans
            d = abs(d)

            print('distance 2 wall', d)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d = min(d, abs((l/100)*(pl-50)-abs(x-(l/2))))


            # print('distance to center', ans)
            # print('distance point to cylinder', d)

            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.

            # if d is less than 1 continue
            p = round(random.uniform(1, d),0)

            print('raduius', p)

            # print("the radius randomly generated is:", p)
            # if (check(cy, cz, y[i], z[i]) > r2):
            #     print('#########################################################################################################################')




            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, l):
                        ans = checksp(x, z[i], y[i], x1, y1, z1)
                        if ans < (p ** 2):
                            a[x1, y1, z1] = sp_col[col]


##TUBE HOLDER CODE


holderlabel = 222

def cuboid(x1, y1, z1, x2,
              y2, z2, x, y, z):
    if (x > x1 and x < x2 and
 y > y1 and y < y2 and z > z1 and z < z2):
        return True
    else:
        return False

##CUBOID EDGES
x1 = 0
y1 = l/4
z1 = 0

x2 = l/5
y2 = 3*l/4
z2 = l




for x in range(0, l):
    for y in range(0, l):
        for z in range(0, l):
            if cuboid(x1, y1, z1, x2, y2, z2, x, y, z):
                a[x, y, z] = holderlabel





for i in range(1, l):

    # creating image object of above array
    data = im.fromarray(a[i]) #.convert('L')

    # saving the final output as a TIFF file
    data.save('bubbletea/bubble%04d.tif' % i)



