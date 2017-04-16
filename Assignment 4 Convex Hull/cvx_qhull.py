import math
import random
import timeit

def ccw(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0])

def ch_qhull(points):
    start_time = timeit.default_timer()
    mn, mx = min(points), max(points)
    ch = qhull(points, mn, mx)
    ch = ch + qhull(points, mx, mn)
    elapsed = timeit.default_timer() - start_time
    print len(ch), str(elapsed)
    return len(ch), elapsed

def qhull(points, mn, mx):
    left_pts = get_left_pts(points, mn, mx)
    pmx = get_max_pt(left_pts, mn, mx)
    if len(pmx) < 1:
        return [mx]

    hull = qhull(left_pts, mn, pmx)
    hull = hull + qhull(left_pts, pmx, mx)
    return hull

def get_max_pt(points, st, end):
    mx_dist = 0

    mx_point = []

    for p in points:
        if p != st and p != end:
            dist = distance(st, end, p)
            if dist > mx_dist:
                mx_dist = dist
                mx_point = p

    return mx_point

def distance(start, end, pt):
    x1, y1 = start
    x2, y2 = end
    x0, y0 = pt
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    result = float(nom) / denom
    return result

def get_left_pts(points, mn, mx):
    pts = []
    for p in points:
        if ccw(mn, mx, p) > 0:
            pts.append(p)
    return pts

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
    # points = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2]]
    # points = generate_random_points(100)
    points = generate_super_points(1000)
    ch_qhull(points)
