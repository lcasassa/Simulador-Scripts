#!/usr/bin/python

import subprocess
import time

import sys
jobs = sys.argv[1:]

maxSimultaneo = 4

procs = []
outputFiles = []
f = {} 

for j in jobs:
    density = 1
    #for algorithm in ['pso']:
    for algorithm in ['pso', 'sh', 'sa', 'ga']:

        while len(procs) >= maxSimultaneo:
            for p in procs:
                if p.poll() is not None:
                    procs.remove(p)
            time.sleep(0.5)
        outputFile = "data_" + algorithm + "_" + str(j)
	f[algorithm] = open("console_" + outputFile + ".txt", "w")
        outputFiles.append(outputFile)
        job = ("./Simulador " + outputFile + " " + algorithm + " " + str(j) + " " + str(density)).split(' ')
        print "Running: " + " ".join(job)
        proc = subprocess.Popen(job, shell=False, stdout=f[algorithm], stderr=subprocess.STDOUT)
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

plotFiles = []
fuzzyFiles = []
fuzzyImageFiles = []

for f in outputFiles:
    plotFiles.append(f + ".txt")
    fuzzyFiles.append(f + "_fuzzy.txt")
    fuzzyImageFiles.append(f + "_fuzzy.png")

import plot
plot.plot(plotFiles, "summary_plot.png")

import plotFuzzy
for i in xrange(len(fuzzyFiles)):
    plotFuzzy.plotFuzzy(fuzzyFiles[i], fuzzyImageFiles[i])

print "Done!"
