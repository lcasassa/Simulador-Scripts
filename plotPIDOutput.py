#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
import os

def pid(dist, vel):
    p = 0.0509804
    d = 0.8700588
    return p*dist*10+d*vel*100


def plotPidOutput(fi = None):
    title = "PID"

    ny, nx = 500, 1000
    ymin, ymax = 0, 1
    xmin, xmax = -1, 1
    zmin, zmax = -2, 1

    y = np.append(np.linspace(ymin, ymax, 10), np.linspace(ymin, ymax, 10))
    x = np.append(np.linspace(xmin, xmax, 10), np.linspace(xmax, xmin, 10))
    z = pid(y, x)

    xi = np.linspace(xmin, xmax, nx)
    yi = np.linspace(ymin, ymax, ny)
    zi = ml.griddata(x, y, z, xi, yi)

    plt.clf()
    plt.title('Algoritmo ' + title)
    #plt.figure().suptitle('Algoritmo ' + title, fontsize=20)
    #plt.contour(xi, yi, zi, 15, linewidths = 0.5, colors = 'k')
    plt.pcolormesh(xi, yi, zi, cmap = plt.get_cmap('rainbow'), vmin=zmin, vmax=zmax)

    plt.colorbar() 
    #plt.scatter(x, y, marker = 'o', c = 'b', s = 5, zorder = 10)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    plt.xlabel("Velocidad")
    plt.ylabel("Distancia")

    if fi is None:
        plt.show()
    else:
        plt.savefig(fi)

def joinImages(imageFiles, outputImage):
    import Image

    images = [Image.open(x) for x in imageFiles]

    print len(images)

    w = sum(i.size[0] for i in images)
    mh = max(i.size[1] for i in images)

    result = Image.new("RGBA", (w, mh))

    x = 0
    for i in images:
        result.paste(i, (x, 0))
        x += i.size[0]

    result.save(outputImage)


def plotFuzzyOutputAll(show = False):
    import glob
    fuzzyFiles = glob.glob('data*_fuzzy.txt')
    fuzzyOutputFiles = [x[:-4] + '_out.txt' for x in fuzzyFiles]

    import subprocess
    for i in xrange(len(fuzzyFiles)):
        cmd = "./plotFuzzy %s %s" % (fuzzyFiles[i], fuzzyOutputFiles[i])
        proc = subprocess.Popen(cmd.split(' '), shell=False)
        proc.communicate()

    fuzzyOutputImageFiles = [x[:-4] + '.png' for x in fuzzyOutputFiles]

    for i in xrange(len(fuzzyOutputFiles)):
        plotFuzzyOutput(fuzzyOutputFiles[i], fuzzyOutputImageFiles[i], show)

    joinImages(fuzzyOutputImageFiles, 'fuzzy_output_result_all_images.png')

if __name__ == "__main__":
    import sys
    plotPidOutput()

