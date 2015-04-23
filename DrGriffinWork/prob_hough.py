import cv2
import numpy as np

img = cv2.imread('empty_example.jpg')
img2 = cv2.imread('corners_detected_copy.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('corners_and_lines.png',img2)