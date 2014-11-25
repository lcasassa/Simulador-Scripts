#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
#from pprint import pprint as pp

def load_data(file):
    with open(file) as f:
        content = f.readlines()

    data = []
    data.append([])
    data.append([])
    for c in content:
        line_data = c.split(" ")
        data[0].append(float(line_data[0]))
        data[1].append(float(line_data[1].strip("\n")))

    #pp(data)
    #pp(data[0])
    return data

def plot(files, output_image = 'image.png', show = False):

    fig, ax = plt.subplots()

    #files = [files]
    for f in files:
        data = load_data(f)
        f = f.split('.')[0].split('_')[1]
        ax.plot(range(0, len(data[0])), data[0], '.', label=f)
        ax.plot(range(0, len(data[1])), data[1], '')

    legend = ax.legend(loc='upper right', shadow=True)
    plt.xlim(0, 25000)
    #plt.ylim(ymin, ymax)

    plt.xlabel("Simulation number")
    plt.ylabel("Fitness score")

    plt.savefig(output_image)
    if show:
        plt.show()

    data_run = []
    for i in xrange(len(data[0]) / 2000 ):
        data_run.append(data[0][(2000*i):(2000*(i+1))])

    data_run_max = []
    for d in data_run:
        data_run_max.append(max(d))

    print 'number of experiments: ', len(data_run_max)
    print 'experiment results: ', data_run_max
    print 'max: ', max(data_run_max)
    print 'min: ', min(data_run_max)
    print 'mean: ', np.mean(data_run_max)
    print 'standard deviation: ', np.std(data_run_max)

if __name__ == "__main__":
    import sys
    files = sys.argv[1:]
    plot(files)
