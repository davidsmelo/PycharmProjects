import numpy as np
import argparse
import cv2
import imutils
from pyimagesearch.transform import four_point_transform
from skimage.filters import threshold_local

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Image to be used as an input")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
ratio= image.shape[0]/500.0
orig=image.copy()
image=imutils.resize(image,height=500)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5), 0)
edged=cv2.Canny(gray,75,200)

print("STEP 1: Edge Detection")
cv2.imshow("Original Size", orig)
cv2.imshow("Image", image)
cv2.imshow("Blurred", blurred)
cv2.imshow("Gray", gray)
cv2.imshow("Edged", edged)
cv2.waitKey()
cv2.destroyAllWindows()

cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cnts=sorted(cnts, key= cv2.contourArea, reverse=True) [:5]

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02* peri,True)

    if len(approx)== 4:
        screenCnt= approx
        break

print("STEP2:Find contours of the paper")
cv2.drawContours(image, [screenCnt], -1,(0,0,255), 2)
cv2.imshow("Outline",image)
cv2.waitKey(0)

warped=four_point_transform(orig,screenCnt.reshape(4,2) *ratio)

warped=cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
T=threshold_local(warped, 11, offset=10, method="gaussian")
warped=(warped>T).astype("uint8") *255
warped=imutils.rotate_bound(warped,-90)

print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)


