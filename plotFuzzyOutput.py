#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
import os

def plotFuzzyOutput(fn, fi, show = False):
    title = os.path.basename(fn).split('.')[0].split('_')[1]

    data = np.loadtxt(fn)
 
    ny, nx = 500, 1000
    ymin, ymax = 0, 1
    xmin, xmax = -1, 1
    zmin, zmax = -1, 1

    y = [d2[0] for d2 in data]
    x = [d2[1] for d2 in data]
    z = [d2[2] for d2 in data]

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

    if show:
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
    if len(sys.argv) == 3:
        fn = sys.argv[1]
        fi = sys.argv[2]
        plotFuzzyOutput(fn, fi, True)
    else:
        plotFuzzyOutputAll(False)

