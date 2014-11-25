#!/usr/bin/python

import glob
fuzzyFiles = glob.glob('data*_fuzzy.txt')
print fuzzyFiles

import plotFuzzy
fuzzyImageFiles = ['', '', '', '']
for i in xrange(len(fuzzyFiles)):
    fuzzyImageFiles[i] = fuzzyFiles[i][:-4] + '_progress.png'
    print fuzzyImageFiles[i]
    plotFuzzy.plotFuzzy(fuzzyFiles[i], fuzzyImageFiles[i], show = False)


import Image

images = [0,0,0,0]
for i in xrange(len(fuzzyImageFiles)):
    print fuzzyImageFiles[i]
    images[i] = Image.open(fuzzyImageFiles[i])

w = sum(i.size[0] for i in images)
mh = max(i.size[1] for i in images)

result = Image.new("RGBA", (w, mh))

x = 0
for i in images:
    result.paste(i, (x, 0))
    x += i.size[0]



result.save('fuzzy_result_all_images.png')

