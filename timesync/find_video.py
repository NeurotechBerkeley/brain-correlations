
# coding: utf-8

import imageio
import pylab
import numpy as np


fname = '../data/IMG_5745s.mov'
vid = imageio.get_reader(fname)
vid.get_length()


sums = [vid.get_data(i).sum() for i in range(vid.get_length())]
sums = np.array(sums)


img = vid.get_data(302)
fig = pylab.figure()
pylab.imshow(img)

img.sum()


white_index = np.argmax(np.diff(sums/1000.0))+1

meta = vid.get_meta_data()


print(white_index*meta['duration']/meta['nframes'])
