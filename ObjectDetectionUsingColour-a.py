import numpy as np
import cv2

img=cv2.imread("images/Picture3.png")
cv2.namedWindow('Processed Hue')
waitDone = 0

def on_trackbar(number):
    hsv=cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    height, width,depth = hsv.shape
    print number
    for i in range(0, height):
        for j in range(0, width):
                x=hsv[i,j]
                if  number != x[0]:
                    hsv[i,j]= [0,0,0]
    rgb=cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    cv2.imshow("Processed Hue",rgb)
    if waitDone != 0: 
        cv2.destroyAllWindows()

cv2.createTrackbar('trackbar', 'Processed Hue', 0 , 360, on_trackbar)
if cv2.waitKey(0) != -1:
    waitDone = 1
    print cv2.getTrackbarPos('trackbar','Processed Hue')
    on_trackbar(0)
