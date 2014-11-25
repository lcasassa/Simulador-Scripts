#!/usr/bin/python

import glob
plotFiles = glob.glob('data*[!_fuzzy][!_out].txt')

import plot
#plot.plot(plotFiles, "progress_plot.png", show = True)
for plotFile in plotFiles:
    plot.plot(plotFile, plotFile + "r.png", show = True)

