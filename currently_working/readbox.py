import numpy as np
import cv2
import ast

#Creating on an image
img = cv2.imread('pslot.jpg')

# Draw a polygon
#using multiDmnt array
# the array representation with LH,RH,RD,LD points
#first left block

newfile = open("new.txt","r")
lines = newfile.readline(0)
print lines

for lines in newfile:
	pts = np.array(ast.literal_eval(lines), np.int32)
	print pts
	pts = pts.reshape((-1,1,2))
	cv2.polylines(img,[pts],True,(128,0,0),2)


#Display the image
cv2.imshow("img",img)

#saves image
cv2.imwrite('bimg.png',img)

cv2.waitKey(0)
newfile.close()
