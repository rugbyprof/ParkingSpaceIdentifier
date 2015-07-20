#combining readbox.py and avgcolor.py
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
import ast
#Creating on an image
img = cv2.imread('pslot.jpg')
#open a file to read the image
newfile = open("new.txt","r")
#reading each line from the file
lines = newfile.readline(0)

def averagergb_image_color(newfile):
    i = Image.open('pslot.jpg')
    h = i.histogram()
    # split into red, green, blue
    r = h[0:255]
    g = h[255:255*2]
    b = h[255*2: 255*3]
    # perform the weighted average of each channel:
    # the *index* is the channel value, and the *value* is its weight
    return (
        sum( i*w for i, w in enumerate(r) ) / sum(r),
        sum( i*w for i, w in enumerate(g) ) / sum(g),
        sum( i*w for i, w in enumerate(b) ) / sum(b)
    )

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
       print 'Prints the average color of the complete image'
       print averagergb_image_color(sys.argv[1])
       for lines in newfile:
	 pts = np.array(ast.literal_eval(lines), np.int32)
	 pts = pts.reshape((-1,1,2))
	 cv2.polylines(img,[pts],True,(128,0,0),2)
	
    else:
       print 'use the printing format as average_image_color.py    image'
       print 'prints the average color of the image as (R,G,B) where R,G,B are between 0 and 255.'
#Display the image
cv2.imshow("img",img)

#saves image
cv2.imwrite('bimg.png',img)

cv2.waitKey(0)
newfile.close()








