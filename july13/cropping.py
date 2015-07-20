#combine code of cropped image and average color
import cv2
import numpy as np
import ast
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# original image
image1 = cv2.imread('pslot.jpg')
image = cv2.imread('pslot.jpg')
#reading from a file named newfile
newfile = open("new.txt","r")
#reading all the lines from a file
lines = newfile.readline(0)
print lines

#for complete parking area the color is calculated
def averagergbimagecolor(newfile):
    i = Image.open('out.png')
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
#for each space in parking slot, color is calculate
def averagergb_image_color(newfile):
    i = Image.open('cropped_image.jpg')
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
       print averagergbimagecolor(sys.argv[1])
       for lines in newfile:
	print 'Prints the average color of the each space'
        print averagergb_image_color(sys.argv[1])
	#read each line and displaying with its boundaries
	roi_corners = np.array([ast.literal_eval(lines)], dtype=np.int32)
	roi_corners = roi_corners.reshape((-1,1,2))
	cv2.polylines(image,[roi_corners],True,(128,0,0),2)
	#now cropping each space from a parking area
	#mask which replaces corners
	mask = np.zeros(image.shape, dtype=np.uint8)
	roi_corners = np.array([ast.literal_eval(lines)], dtype=np.int32)
	#firstly, taking an empty image
	white = (255, 255, 255)
	#each space is masked with empty image 
	cv2.fillPoly(mask, roi_corners, white)
	# apply the mask
	masked_image = cv2.bitwise_and(image, mask)
	#displaying masked images 
	cv2.imshow('masked image', masked_image)
	cv2.imwrite('cropped_image.jpg',masked_image)
	croppedimage = cv2.imread('cropped_image.jpg')
	print averagergb_image_color(sys.argv[1])
	cv2.waitKey()
	
    else:
	#command used for printing lines
       	print 'use the printing format as average_image_color.py    image'
	#prints in the following format2
       	print 'prints the average color of the image as (R,G,B) where R,G,B are between 0 and 255.'

# displays the images
cv2.imshow('Actual image', image1)
cv2.imshow('complete image',image)
cv2.imshow('croped image', masked_image)
cv2.waitKey()
cv2.destroyAllWindows()
newfile.close()
