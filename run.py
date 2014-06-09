#!/usr/bin/python

import subprocess
import time

jobs = [1, 2, 3]

maxSimultaneo = 4

procs = []
plotFiles = []

for j in jobs:

    while len(procs) >= maxSimultaneo:
        for p in procs:
            if p.poll():
                procs.remove(p)
        time.sleep(0.5)
    
    plotFile = "data_" + str(j) + ".txt"
    plotFiles.append(plotFile)
    job = ("./Simulador " + plotFile + " pso " + str(j)).split(' ')
    print "Running: " + " ".join(job)
    proc = subprocess.Popen(job)
    procs.append(proc)


print "############################################"
print "Waiting for " + str(len(procs)) + " runs more"
print "############################################"

while len(procs) > 0:
    for p in procs:
        if p.poll():
            procs.remove(p)
    time.sleep(0.5)


import plot
plot.plot(plotFiles)

print "Done!"
