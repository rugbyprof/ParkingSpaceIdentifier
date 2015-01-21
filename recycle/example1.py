import numpy as np
import matplotlib.pyplot as plt
import skimage
from scipy import ndimage
from skimage import io
from skimage import filter
from skimage import data
import os

#https://www.dropbox.com/s/fydtz4kiqm6rt70/bolin_parkinglot.png?dl=0

filename = os.path.join(skimage.data_dir, 'nightemp.jpg')
img = io.imread('nightemp.jpg')
gray = np.sqrt((img*img).sum(-1))
print gray

# Generate noisy image of a square
im = np.zeros((128, 128))
im[32:-32, 32:-32] = 1

im = ndimage.rotate(im, 15, mode='constant')
im = ndimage.gaussian_filter(im, 4)
im += 0.2 * np.random.random(im.shape)

# Compute the Canny filter for two values of sigma
edges1 = filter.canny(gray)
edges2 = filter.canny(gray, sigma=28)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax1.imshow(gray, cmap=plt.cm.jet)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=10$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=25$', fontsize=20)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)

plt.show()
