#!/usr/bin/python

import subprocess
import time

import sys
jobs = sys.argv[1:]

maxSimultaneo = 4

procs = []
plotFiles = []

for j in jobs:
    #for algorithm in ['pso', 'sh', 'sa', 'ga']:
    for algorithm in ['ga']:

        while len(procs) >= maxSimultaneo:
            for p in procs:
                if p.poll() is not None:
                    procs.remove(p)
            time.sleep(0.5)

        plotFile = "data_" + algorithm + "_" + str(j) + ".txt"
        plotFiles.append(plotFile)
        job = ("./Simulador " + plotFile + " " + algorithm + " " + str(j)).split(' ')
        print "Running: " + " ".join(job)
        proc = subprocess.Popen(job, shell=False)
        procs.append(proc)
        time.sleep(1)


print "##################################################"
print "Waiting for " + str(len(procs)) + " runs to finish"
print "##################################################"

while len(procs) > 0:
    for p in procs:
        if p.poll() is not None:
            procs.remove(p)
    time.sleep(0.5)


import plot
plot.plot(plotFiles)

print "Done!"
