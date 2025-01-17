import cv2
import numpy as np



####Variables######

#True while mouse button up, false when mouse button UP
drawing= False
ix,iy= -1, -1

#Function

def draw_rectangle(event, x,y, flags, params):
    global ix,iy,drawing

    if event ==cv2.EVENT_LBUTTONDOWN:
        drawing =True
        ix,iy= x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing== True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), thickness=-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,(ix,iy),(x,y), (0,255,0),-1)

#Showing the Image


img=np.zeros((512,512,3))

cv2.namedWindow(winname="my_drawing")

cv2.setMouseCallback("my_drawing",draw_rectangle())

cv2.imshow("my_drawing",img)
cv2.waitKey()
cv2.destroyAllWindows()