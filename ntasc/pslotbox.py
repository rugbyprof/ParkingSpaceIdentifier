import numpy as np
import cv2

# Create a black image
#img = np.zeros((512,512,3), np.uint8)

#Creating on an image
img = cv2.imread('pslot.jpg')

# Draw a polygon
#using multiDmnt array
# the array representation with LH,RH,RD,LD points
#first left block
pts = np.array([[381,3],[418,7],[383,64],[346,50]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[418,6],[451,19],[413,77],[380,64]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[451,19],[483,31],[444,90],[413,77]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[483,31],[515,44],[478,104],[444,90]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)
#LH,RD,RH,LD
pts = np.array([[515,44],[550,58],[512,118],[478,104]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[512,118],[544,132],[582,72],[550,58]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[544,132],[575,144],[614,84],[582,72]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[515,44],[550,58],[585,1],[543,2]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)
#LH,RD,RH,LD
pts = np.array([[582,72],[550,58],[585,1],[619,11]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)
#LH,RD,RH,LD
pts = np.array([[582,72],[615,85],[653,24],[619,11]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

#first right block
# the array representation with LH,RH,RD,LD point
pts = np.array([[735,57],[770,71],[730,130],[697,116]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[770,71],[805,83],[765,143],[730,130]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[805,83],[839,96],[800,156],[765,143]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[839,96],[874,111],[836,171],[800,156]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[874,111],[909,121],[870,184],[836,171]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[909,121],[945,134],[906,198],[870,184]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[945,134],[981,147],[943,212],[906,198]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[943,212],[979,226],[940,290],[904,276]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[906,198],[943,212],[904,276],[868,261]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[870,184],[906,198],[868,261],[832,248]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[836,171],[870,184],[832,248],[797,234]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[800,156],[836,171],[797,234],[762,220]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[765,143],[800,156],[762,220],[727,206]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[730,130],[765,143],[727,206],[693,192]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[697,116],[730,130],[693,192],[659,178]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

# left block
#the array representation is LH,RH,RD,LD 
pts = np.array([[46,11],[78,24],[38,84],[3,72]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[78,24],[110,37],[70,97],[38,84]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[110,37],[143,51],[102,112],[70,97]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[143,51],[175,63],[135,125],[102,112]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[175,63],[207,76],[167,138],[135,125]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[207,76],[240,90],[199,151],[167,138]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[240,90],[272,102],[232,164],[199,151]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[272,102],[304,115],[265,179],[232,164]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[304,115],[338,130],[298,192],[265,179]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[338,130],[370,143],[330,204],[298,192]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[370,143],[402,156],[363,219],[330,204]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[402,156],[435,170],[395,232],[363,219]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[435,170],[469,183],[429,246],[395,232]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[469,183],[502,197],[462,261],[429,246]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[502,197],[535,211],[496,275],[467,261]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[462,261],[496,275],[456,338],[422,324]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[429,246],[462,261],[422,324],[390,311]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[395,232],[429,246],[390,311],[356,296]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[363,219],[395,232],[356,296],[322,282]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[330,204],[363,219],[322,282],[290,268]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[298,192],[330,204],[290,268],[257,255]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[265,179],[298,192],[257,255],[224,241]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[232,164],[265,179],[224,241],[191,227]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[199,151],[232,164],[191,227],[158,213]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[167,138],[199,151],[158,213],[126,200]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[135,125],[167,138],[126,200],[93,187]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[102,112],[135,125],[93,187],[61,173]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[70,97],[102,112],[61,173],[28,160]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

# left block
# the array representation is LH,RH,RD,LD point
pts = np.array([[48,252],[81,266],[38,331],[5,318]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[81,266],[114,280],[71,346],[38,331]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[114,280],[148,293],[105,359],[71,346]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[148,293],[180,308],[138,373],[105,359]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[180,308],[213,321],[171,387],[138,373]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[213,321],[247,335],[204,401],[171,387]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[247,335],[280,350],[238,416],[204,401]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[280,350],[313,363],[271,431],[238,416]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[313,363],[347,378],[305,444],[271,431]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[347,378],[380,393],[340,459],[305,444]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[380,393],[414,408],[373,474],[340,459]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[340,459],[373,474],[331,543],[298,528]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[305,444],[340,459],[298,528],[263,512]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[271,431],[305,444],[263,512],[229,498]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[238,416],[271,431],[229,498],[196,482]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[204,401],[238,416],[196,482],[162,469]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[171,387],[204,401],[162,469],[129,454]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[138,373],[171,387],[129,454],[95,439]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[105,359],[138,373],[95,439],[62,426]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[71,346],[105,359],[62,426],[28,412]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[38,331],[71,346],[28,412],[0,396]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

# right block
# the array representation is LH,RH,RD,LD point
pts = np.array([[618,245],[651,259],[613,323],[580,309]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[651,259],[686,273],[647,338],[613,323]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[686,273],[721,288],[682,353],[647,338]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[721,288],[756,301],[717,367],[682,353]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[756,301],[791,316],[752,382],[717,367]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[791,316],[827,330],[788,396],[752,382]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[827,330],[863,345],[824,411],[788,396]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[863,345],[899,360],[860,427],[824,411]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[899,360],[936,375],[897,442],[860,427]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[936,375],[973,390],[935,458],[897,442]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[935,458],[972,473],[934,542],[896,526]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[897,442],[935,458],[896,526],[859,510]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[860,427],[897,442],[859,510],[822,494]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[824,411],[860,427],[822,494],[785,479]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[788,396],[824,411],[785,478],[748,463]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[752,382],[788,396],[750,463],[713,448]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[717,367],[752,382],[713,448],[678,433]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[682,353],[717,367],[678,433],[643,418]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[647,338],[682,353],[643,418],[608,403]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[613,323],[647,338],[608,403],[575,389]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[580,309],[613,323],[575,389],[540,373]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)


#last right block
# the array representation is LH,RH,RD,LD point
pts = np.array([[498,444],[532,458],[491,526],[457,511]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[532,458],[566,473],[527,542],[491,526]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

pts = np.array([[566,473],[601,489],[561,557],[527,542]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(128,0,0),2)

#polylines syntax is img, pts from array, is the Curve should be #closed, BGR color values, thinkness of the line
#the color are arranged as BGR
#cv2.polylines(img,[pts],True,(128,0,0),2)

#Display the image
cv2.imshow("img",img)

#saves image
cv2.imwrite('box.png',img)

cv2.waitKey(0)
