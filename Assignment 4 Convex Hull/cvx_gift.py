import math
import random
import timeit

def ccw(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

def d(p, q):
    return (p[0]-q[0])*(p[0]-q[0])+(p[1]-q[1])*(p[1]-q[1])

def next_pt(points, p):
    q = p
    for r in points:
        t = ccw(p, q, r)
        if t < 0 or (t == 0 and d(p, r) > d(p, q)):
            q = r
    return q

def ch_gift(points):
    start_time = timeit.default_timer()
    ch = [min(points)]
    for p in ch:
        q = next_pt(points, p)
        if q != ch[0]:
            ch.append(q)
    elapsed = timeit.default_timer() - start_time
    print len(ch), str(elapsed)
    return len(ch), elapsed

def generate_random_points(number):
    sq = number
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
    ch_gift(points)
