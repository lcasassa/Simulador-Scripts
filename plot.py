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

def plot(files):

    fig, ax = plt.subplots()

    for f in files:
        data = load_data(f)
        ax.plot(range(0, len(data[0])), data[0], '.', label=f)
        ax.plot(range(0, len(data[1])), data[1], '', label=f)

    legend = ax.legend(loc='lower right', shadow=True)

    plt.savefig('image.png')
    plt.show()

if __name__ == "__main__":
    import sys
    files = sys.argv[1:]
    plot(files)
