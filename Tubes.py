import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image as im
import cv2
import random
import json

json_file = open("configfile.json")
variables = json.load(json_file)
json_file.close()

print(variables)
print(variables["length"])

l = variables["length"]  # should be  l_x, l_y ...

lx = l
ly = l
lz = round(7*l / 4)

# coordinates of the first centre
cx = l / 2
cy = l / 4
cz = l / 2

# coordinates of the second centre
cx1 = l / 2
cy1 = l / 2
cz1 = l / 2

# coordinates of the third centre
cx2 = l / 2
cy2 = 3*l / 4
cz2 = l / 2

# coordinates of the fourth centre
cx3 = l / 2
cy3 = l
cz3 = l / 2

# coordinates of the fifth centre
cx4 = l / 2
cy4 = 5*l / 4
cz4 = l / 2

# coordinates of the sixth centre
cx5 = l / 2
cy5 = 3*l / 2
cz5 = l / 2

# radius of external cylinder
r1 = l / 16

# radius of cylinder inside (cavity)
r2 = l / 18

# wall label
wall_label = 255
# background and air labels
background_label = 0
air_label = 20
# tube holder label value
holderlabel = 222

# percentage of height for cylinder
pl = 80

##CUBOID EDGES
xc1 = 0
yc1 = l/4
zc1 = 0

xc2 = l/5
yc2 = 3*l/4
zc2 = 2*l

nb_tube = 6 #useless for now


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


def cuboid(x1, y1, z1, x2,
              y2, z2, x, y, z):
    if (x > x1 and x < x2 and
 y > y1 and y < y2 and z > z1 and z < z2):
        return True
    else:
        return False




# create 3d numpy array
shape = (lx, ly, lz)
a = np.zeros(shape=shape, dtype=np.uint16)

##WALL AND AIR
for x in range(0, lx):
    for y in range(0, ly):
        for z in range(0, lz):
            #TUBE1
            ans = check(cx, cy, y, z)
            if ans < (r1 ** 2):
                a[x, y, z] = wall_label
            if ans < (r2 ** 2):
                a[x, y, z] = air_label

            ##TUBE2
            ans1 = check(cx1, cy1, y, z)
            if ans1 < (r1 ** 2):
                a[x, y, z] = wall_label
            if ans1 < (r2 ** 2):
                a[x, y, z] = air_label

            ##TUBE3
            ans2 = check(cx2, cy2, y, z)
            if ans2 < (r1 ** 2):
                a[x, y, z] = wall_label
            if ans2 < (r2 ** 2):
                a[x, y, z] = air_label

            ##TUBE4
            ans3 = check(cx3, cy3, y, z)
            if ans3 < (r1 ** 2):
                a[x, y, z] = wall_label
            if ans3 < (r2 ** 2):
                a[x, y, z] = air_label

            ##TUBE5
            ans4 = check(cx4, cy4, y, z)
            if ans4 < (r1 ** 2):
                a[x, y, z] = wall_label
            if ans4 < (r2 ** 2):
                a[x, y, z] = air_label

            ##TUBE6
            ans5 = check(cx5, cy5, y, z)
            if ans5 < (r1 ** 2):
                a[x, y, z] = wall_label
            if ans5 < (r2 ** 2):
                a[x, y, z] = air_label





for x in range(0, l):
    for y in range(0, lz):
        # remove the bottom
        for o in range(0, l - round((l*pl)/100)):
            a[o, x, y] = background_label
        # remove the top
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


    y1 = []
    z1 = []

    y2 = []
    z2 = []

    y3 = []
    z3 = []

    y4 = []
    z4 = []

    y5 = []
    z5 = []

    y6 = []
    z6 = []

    # randomly choose the number of spheres for this stack
    sp_num1 = random.randint(0, n)
    sp_num2 = random.randint(0, n)
    sp_num3 = random.randint(0, n)
    sp_num4 = random.randint(0, n)
    sp_num5 = random.randint(0, n)
    sp_num6 = random.randint(0, n)

    print('#########################################################################################################################')
    print('the stack', x)


    for i in range(0, sp_num1):

        # y1.append(round(random.uniform(cy - r2, cy + r2 - 1)))
        # z1.append(round(random.uniform(cz - r2, cz + r2 - 1)))

        y1.append(round(random.uniform(cy - r2, cy + r2 - 1)))
        z1.append(round(random.uniform(cz - r2, cz + r2 - 1)))

        if (check(cy, cz, y1[i], z1[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y1[i]', y1[i])
            print('coordinates z1[i]', z1[i])

            ans = check2d(cy, cz, y1[i], z1[i])
            d1 = r2 - ans
            d1 = abs(d1)

            print('distance 2 wall', d1)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d1 = min(d1, abs((l/100)*(pl-50)-abs(x-(l/2))))



            # print('distance to center', ans)
            # print('distance point to cylinder', d)

            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.

            # if d is less than 1 continue
            p1 = round(random.uniform(1, d1),0)

            print('raduius', p1)

            # print("the radius randomly generated is:", p)
            # if (check(cy, cz, y[i], z[i]) > r2):
            #     print('#########################################################################################################################')

            for xl in range(0, l):
                for yl in range(0, l):
                    for zl in range(0, l):
                        ans = checksp(x, z1[i], y1[i], xl, yl, zl)
                        if ans < (p1 ** 2):
                            a[xl, yl, zl] = sp_col[col]


    for i in range(0, sp_num2):

        y2.append(round(random.uniform(cy1 - r2, cy1 + r2 - 1)))
        z2.append(round(random.uniform(cz1 - r2, cz1 + r2 - 1)))

        if (check(cy1, cz1, y2[i], z2[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y2[i]', y2[i])
            print('coordinates z2[i]', z2[i])

            ans = check2d(cy1, cz1, y2[i], z2[i])
            d2 = r2 - ans
            d2 = abs(d2)

            print('distance 2 wall', d2)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d2 = min(d2, abs((l/100)*(pl-50)-abs(x-(l/2))))


            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.
            # if d is less than 1 continue
            p2 = round(random.uniform(1, d2),0)
            print('raduius', p2)

            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, l):
                        ans = checksp(x, z2[i], y2[i], x1, y1, z1)
                        if ans < (p2 ** 2):
                            a[x1, y1, z1] = sp_col[col]


    for i in range(0, sp_num3):

        y3.append(round(random.uniform(cy2 - r2, cy2 + r2 - 1)))
        z3.append(round(random.uniform(cz2 - r2, cz2 + r2 - 1)))

        if (check(cy2, cz2, y3[i], z3[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y3[i]', y3[i])
            print('coordinates z3[i]', z3[i])

            ans = check2d(cy2, cz2, y3[i], z3[i])
            d3 = r2 - ans
            d3 = abs(d3)

            print('distance 2 wall', d3)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d3 = min(d3, abs((l/100)*(pl-50)-abs(x-(l/2))))


            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.
            # if d is less than 1 continue
            p3 = round(random.uniform(1, d3),0)
            print('raduius', p3)

            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, l):
                        ans = checksp(x, z3[i], y3[i], x1, y1, z1)
                        if ans < (p3 ** 2):
                            a[x1, y1, z1] = sp_col[col]


    for i in range(0, sp_num4):

        y4.append(round(random.uniform(cy3 - r2, cy3 + r2 - 1)))
        z4.append(round(random.uniform(cz3 - r2, cz3 + r2 - 1)))

        if (check(cy3, cz3, y4[i], z4[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y4[i]', y4[i])
            print('coordinates z4[i]', z4[i])

            ans = check2d(cy3, cz3, y4[i], z4[i])
            d4 = r2 - ans
            d4 = abs(d4)

            print('distance 2 wall', d4)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d4 = min(d4, abs((l/100)*(pl-50)-abs(x-(l/2))))


            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.
            # if d is less than 1 continue
            p4 = round(random.uniform(1, d4),0)
            print('raduius', p4)

            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, lz):
                        ans = checksp(x, z4[i], y4[i], x1, y1, z1)
                        if ans < (p4 ** 2):
                            a[x1, y1, z1] = sp_col[col]



    for i in range(0, sp_num5):

        y5.append(round(random.uniform(cy4 - r2, cy4 + r2 - 1)))
        z5.append(round(random.uniform(cz4 - r2, cz4 + r2 - 1)))

        if (check(cy4, cz4, y5[i], z5[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print('_________________________________________________________________________________________________________________________')

            print('coordinates y5[i]', y5[i])
            print('coordinates z5[i]', z5[i])

            ans = check2d(cy4, cz4, y5[i], z5[i])
            d5 = r2 - ans
            d5 = abs(d5)

            print('distance 2 wall', d5)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d5 = min(d5, abs((l/100)*(pl-50)-abs(x-(l/2))))


            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.
            # if d is less than 1 continue
            p5 = round(random.uniform(1, d5),0)
            print('raduius', p5)

            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, lz):
                        ans = checksp(x, z5[i], y5[i], x1, y1, z1)
                        if ans < (p5 ** 2):
                            a[x1, y1, z1] = sp_col[col]

    for i in range(0, sp_num6):

        y6.append(round(random.uniform(cy5 - r2, cy5 + r2 - 1)))
        z6.append(round(random.uniform(cz5 - r2, cz5 + r2 - 1)))

        if (check(cy5, cz5, y6[i], z6[i]) < (r2 ** 2)):
            # randomly choose the intensity for the sphere
            col = random.randint(0, 5)

            print(
                '_________________________________________________________________________________________________________________________')

            print('coordinates y6[i]', y6[i])
            print('coordinates z6[i]', z6[i])

            ans = check2d(cy5, cz5, y6[i], z6[i])
            d6 = r2 - ans
            d6 = abs(d6)

            print('distance 2 wall', d6)
            print('distance 2 roof', abs((l / 100) * (pl - 50 - abs(x - (l / 2)))))

            # get the min between the distance to wall and distance to roofs
            # d = min(d, abs(x-l+round((pl*l)/100)))
            # print('d1', d)
            d6 = min(d6, abs((l / 100) * (pl - 50) - abs(x - (l / 2))))

            # generate random number between .01 and d which is the maximum the radius could take to not touch the cylinder.
            # if d is less than 1 continue
            p6 = round(random.uniform(1, d6), 0)
            print('raduius', p6)

            for x1 in range(0, l):
                for y1 in range(0, l):
                    for z1 in range(0, lz):
                        ans = checksp(x, z6[i], y6[i], x1, y1, z1)
                        if ans < (p6 ** 2):
                            a[x1, y1, z1] = sp_col[col]


##SECOND TUBE SPHERES




##TUBE HOLDER CODE


for x in range(0, lx):
    for y in range(0, ly):
        for z in range(0, lz):
            if cuboid(xc1, yc1, zc1, xc2, yc2, zc2, x, y, z):
                a[x, y, z] = holderlabel





for i in range(1, l):

    # creating image object of above array
    data = im.fromarray(a[i]) #.convert('L')

    # saving the final output as a TIFF file
    data.save('bubbletea/bubble%04d.tif' % i)



