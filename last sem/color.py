import matplotlib.pyplot as plt
import numpy as np

from skimage import data
from skimage.color import rgb2hed , rgb2hsv
from skimage.exposure import rescale_intensity
from skimage.data import camera,imread

image = imread('/home/surekha/ParkingSpaceIdentifier/withshadow.jpeg',0)

ihc_rgb = data.immunohistochemistry()
ihc_hed = rgb2hsv(image)
#ihc_hed = image

fig, axes = plt.subplots(2, 2, figsize=(7, 6))
ax0, ax1, ax2, ax3 = axes.ravel()

ax0.imshow(ihc_hed)
ax0.set_title("Original image")

ax1.imshow(ihc_hed[:, :, 0], cmap=plt.cm.gray)
ax1.set_title("Hematoxylin")

ax2.imshow(ihc_hed[:, :, 1], cmap=plt.cm.gray)
ax2.set_title("Eosin")

ax3.imshow(ihc_hed[:, :, 2], cmap=plt.cm.gray)
ax3.set_title("DAB")

for ax in axes.ravel():
    ax.axis('off')

fig.subplots_adjust(hspace=0.3)

# Rescale hematoxylin and DAB signals and give them a fluorescence look
h = rescale_intensity(ihc_hed[:, :, 0], out_range=(0, 1))
d = rescale_intensity(ihc_hed[:, :, 2], out_range=(0, 1))
zdh = np.dstack((np.zeros_like(h), d, h))

fig, ax = plt.subplots()
ax.imshow(zdh)
ax.set_title("Stain separated image (rescaled)")
ax.axis('off')
plt.show()
