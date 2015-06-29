#!/usr/bin/env python3

import numpy
import matplotlib
import math
import sys

from shapely.geometry import Point
from shapely.geometry.linestring import LineString
from shapely.geometry.polygon import Polygon

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from astar import astar

steps = 360

# like range(), but with floats
def frange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

circles = []
circles.append(Point(-280, 120).buffer(50)) # o1
circles.append(Point(-350, -300).buffer(200)) # o2

polygons = []
polygons.append(Polygon([(150, -150), (150, -300), (300, -300), (150, -300)])) # o3
polygons.append(Polygon([(100, 300), (50, 400), (250, 400), (200, 300), (150, 250), (100, 300)])) # o4

def joints(*args):
    positions = [(0, 0)]
    A = 0
    for i in range(0, len(args), 2):
        x, y = positions[-1]
        a, l = args[i:i+2]
        A += a
        positions.append((x + l * math.cos(A), y + l * math.sin(A)))
    return positions

def sample(obstacles, a1, a2):
    # there is a '-' before a2 since a2 is measured clockwise
    j = joints(a1, 200, -a2, 200)
    manipulator = LineString(j)
    return any(map(manipulator.intersects, obstacles))

def lerp(x, a, b):
    return a + (b - a) * x

# sample the matrix
def sampler(steps, obstacles):
    def f(row, col):
        return sample(obstacles, 
                lerp(col/steps, 0, 2*math.pi),
                lerp(row/steps, 0, 2*math.pi)
                )
    return numpy.vectorize(f)


print("Sampling circular obstacles...")
mat1 = numpy.fromfunction(sampler(steps, circles), (steps, steps))

print("Sampling polygon obstacles...")
mat2 = numpy.fromfunction(sampler(steps, polygons), (steps, steps))

print("Combining c-obstacles...")
matboth = numpy.maximum(mat1, mat2)


def angle_to_pixel(a):
    return int(a / math.pi / 2 * steps)

def pixel_to_angle(p):
    x, y = p
    x += 0.5
    y += 0.5
    return x/steps*math.pi*2, y/steps*math.pi*2

def degrees(d):
    return d / 180 * math.pi

end   = tuple(map(angle_to_pixel, map(degrees, (45, 60))))
start = tuple(map(angle_to_pixel, map(degrees, (180, 0))))

print("Finding path...")
#path1 = list(map(pixel_to_angle, astar(mat1,    start, end)))
path2 = list(map(pixel_to_angle, astar(matboth, start, end)))


print("Plotting...")
c = matplotlib.colors.colorConverter
c1 = matplotlib.colors.ListedColormap([c.to_rgba('gray', 0), c.to_rgb('gray')], 'c1')
c2 = matplotlib.colors.ListedColormap([c.to_rgba('blue', 0), c.to_rgb('blue')], 'c2')

fig = plt.figure()
ax = fig.add_subplot(111)
ex = [0, math.pi*2, 0, math.pi*2]
ax.imshow(mat1, cmap=c1, origin='lower', extent=ex, interpolation='nearest')
ax.imshow(mat2, cmap=c2, origin='lower', extent=ex, interpolation='nearest')

p1  = (degrees(45)+0.5/steps, degrees(60)+0.5/steps)
p2  = (degrees(180)+0.5/steps, degrees(0)+0.5/steps)
p2x = (degrees(180)+0.5/steps, degrees(360)+0.5/steps)

plt.plot(*zip(*path2), marker='', color='black', ls='-')
plt.plot(*zip(p1, p2x), marker='', color='black', ls='--')

plt.plot(*p1, marker='o', color='r', ls='')
plt.plot(*p2, marker='o', color='r', ls='')
plt.plot(*p2x, marker='o', color='g', ls='')

ax.text(*p1, s='start', verticalalignment='top', horizontalalignment='right')
ax.text(*p2, s='goal', verticalalignment='bottom', horizontalalignment='right')
ax.text(*p2x, s='goal (alternative)', verticalalignment='top', horizontalalignment='left')

ax.set_xlabel('p1')
ax.set_ylabel('p2')

plt.axis(ex)
plt.show()
