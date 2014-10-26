#!/usr/bin/python

import matplotlib.pyplot as plt

def plotFuzzy(fn, fi, show = False):
    title = fn.split('.')[0].split('_')[1]
    with open(fn, 'r') as f:
        d = map(float, f)
    m = [0,1,2,3,4,5]
    m[0] = d[0]
    m[1] = (d[2] + d[3])/2
    m[2] = d[5]

    m[3] = d[6]
    m[4] = (d[8] + d[9])/2
    m[5] = d[11]

    segx = [d[0], m[0], d[1], d[0]]
    segy = [0,    1,    0,    0]
    segx2 = [d[2], m[1], d[3], d[2]]
    segy2 = [0,    1,    0,    0]
    segx3 = [d[4], m[2], d[5], d[4]]
    segy3 = [0,    1,    0,    0]

    segx4 = [d[6], m[3], d[7], d[0]]
    segy4 = [0,    1,    0,    0]
    segx5 = [d[8], m[4], d[9], d[2]]
    segy5 = [0,    1,    0,    0]
    segx6 = [d[10], m[5], d[11], d[4]]
    segy6 = [0,    1,    0,    0]

    plt.clf()
    plt.figure().suptitle('Algoritmo ' + title, fontsize=20)
    plt.subplot(2, 1, 1)
    plt.plot(segx, segy, segx2, segy2, segx3, segy3)
    plt.subplot(2, 1, 2)
    plt.plot(segx4, segy4, segx5, segy5, segx6, segy6)

    if show:
        plt.show()
    plt.savefig(fi)

if __name__ == "__main__":
    import sys
    fn = sys.argv[1]
    fi = sys.argv[2]
    plotFuzzy(fn, fi)

