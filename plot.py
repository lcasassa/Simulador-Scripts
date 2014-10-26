#!/usr/bin/python

import matplotlib.pyplot as plt
#from pprint import pprint as pp

def load_data(file):
    with open(file) as f:
        content = f.readlines()

    data = []
    data.append([])
    data.append([])
    for c in content:
        line_data = c.split(" ")
        data[0].append(line_data[0])
        data[1].append(line_data[1].strip("\n"))

    #pp(data)
    #pp(data[0])
    return data

def plot(files, output_image = 'image.png', show = False):

    fig, ax = plt.subplots()

    for f in files:
        data = load_data(f)
        f = f.split('.')[0].split('_')[1]
        ax.plot(range(0, len(data[0])), data[0], '.', label=f)
        ax.plot(range(0, len(data[1])), data[1], '')

    legend = ax.legend(loc='upper left', shadow=True)

    plt.savefig(output_image)
    if show:
        plt.show()

if __name__ == "__main__":
    import sys
    files = sys.argv[1:]
    plot(files)
