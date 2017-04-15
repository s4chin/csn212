#!/usr/bin/env python
import math
import random
import timeit
from operator import attrgetter
import pandas as pd
import seaborn as sns

MAX = float('Inf')

def ccw(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

def theta(p):
    global p0
    return math.fabs(math.atan2(p[1] - p0[1], p[0] - p0[0])*180.0/math.pi)

def dist(p):
    global p0
    return math.sqrt((p[0]-p0[0])*(p[0]-p0[0])+(p[1]-p0[1])*(p[1]-p0[1]))

def thetacmp(a, b):
    if theta(a) < theta(b):
        return -1
    return 1

p0 = [MAX, MAX]
def ch_graham(points):
    start_time = timeit.default_timer()
    global p0
    p0 = [MAX, MAX]
    ind = 0
    for i in range(len(points)):
        if points[i][1] < points[ind][1]:
            ind = i
        elif points[i][1] == p0[1]:
            if points[i][0] <  points[ind][0]:
                ind = i

    points[0], points[ind] = points[ind], points[0]
    p0 = points[0]

    pts = points[0:1] + sorted(points[1:], cmp=thetacmp)
    # Remove points whose angles are equal from p0, keeping the farthest one
    for i in xrange(len(pts) - 1, 1, -1):
        if theta(pts[i]) == theta(pts[i-1]):
            if dist(pts[i]) < dist(pts[i-1]):
                del pts[i]
            elif dist(pts[i]) > dist(pts[i-1]):
                del pts[i-1]
    print len(pts)

    ch = []
    for p in pts:
        while len(ch) > 1 and ccw(ch[-2], ch[-1], p) <= 0:
            ch.pop()
        ch.append(p)
    elapsed = timeit.default_timer() - start_time
    print len(ch), str(elapsed)
    return len(ch), elapsed

def generate_random_points(number):
    sq = number/100
    sq = sq if sq > 1 else 1
    P = []
    for i in xrange(number):
        succ = False
        while not succ:
            rand = random.randint
            x = rand(-sq, sq)
            y = rand(-sq, sq)
            if [x, y] not in P:
                P.append([x, y])
                succ = True
            # succ = True # Because 10000 points generation took too much time :(
    print "Points generated!"
    return P

def generate_super_points(number):
    sq = number
    sq = sq if sq > 1 else 1
    P = []
    for i in xrange(number):
        succ = False
        while not succ:
            x = random.randint(-sq, sq)
            y = math.sqrt(sq*sq-x*x)
            if [x, y] not in P:
                P.append([x, y])
                succ = True
    print "Points generated!"
    return P


if __name__ == '__main__':
    # points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(0, 1), Point(1, 0)]
    points = generate_random_points(10000)
    # points = generate_super_points(1000)
    ch_graham(points)
    # ch_gift(points)
