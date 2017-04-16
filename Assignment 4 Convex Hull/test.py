import math
import random
import timeit

import cvx_qhull, cvx_graham, cvx_gift

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

if __name__ == "__main__":
    x = []
    qhull = []
    gift = []
    graham = []
    for num in [100, 1000, 2000, 5000, 10000]:
        x.append(num)
        points = generate_random_points(num)
        _, time = cvx_gift.ch_gift(points)
        gift.append(time)
        _, time = cvx_graham.ch_graham(points)
        graham.append(time)
        _, time = cvx_qhull.ch_qhull(points)
        qhull.append(time)
    import matplotlib.pyplot as plt
    plt.plot(x, gift)
    plt.plot(x, graham)
    plt.plot(x, qhull)
    plt.legend(['Gift wrapping', 'Graham Scan', 'Quickhull'], loc='upper left')
    plt.savefig('comparison.png')


    x = []
    y = []
    points = generate_random_points(1000)
    _, time = cvx_gift.ch_gift(points)
    x.append(_)
    y.append(time)
    points = generate_random_points(200)
    points.extend(generate_super_points(800))
    _, time = cvx_gift.ch_gift(points)
    x.append(_)
    y.append(time)
    points = generate_super_points(1000)
    _, time = cvx_gift.ch_gift(points)
    x.append(_)
    y.append(time)
    plt.close()
    plt.plot(x, y)
    plt.savefig('gift.png')

    x = []
    y = []
    points = generate_random_points(1000)
    _, time = cvx_graham.ch_graham(points)
    x.append(_)
    y.append(time)
    points = generate_random_points(200)
    points.extend(generate_super_points(800))
    _, time = cvx_graham.ch_graham(points)
    x.append(_)
    y.append(time)
    points = generate_super_points(1000)
    _, time = cvx_graham.ch_graham(points)
    x.append(_)
    y.append(time)
    plt.close()
    plt.plot(x, y)
    plt.savefig('graham.png')

    x = []
    y = []
    points = generate_random_points(1000)
    _, time = cvx_qhull.ch_qhull(points)
    x.append(_)
    y.append(time)
    points = generate_random_points(200)
    points.extend(generate_super_points(800))
    _, time = cvx_qhull.ch_qhull(points)
    x.append(_)
    y.append(time)
    points = generate_super_points(1000)
    _, time = cvx_qhull.ch_qhull(points)
    x.append(_)
    y.append(time)
    plt.close()
    plt.plot(x, y)
    plt.savefig('qhull.png')
