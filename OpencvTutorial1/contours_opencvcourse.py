import argparse
import cv2
import imutils

ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

edged=cv2.Canny(gray,30,150)
cv2.imshow("Canny", edged)
cv2.waitKey(0)

thresh=cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh",thresh)
cv2.waitKey(0)

contours=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(contours)
output=image.copy()

for c in cnts:
    cv2.drawContours(output, [c], -1, (240,0,159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

text="I found {} objects!".format(len(cnts))
cv2.putText(output,text, (10,25), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,0))
cv2.imshow("Number of Contours", output)
cv2.waitKey(0)

mask=thresh.copy()
mask=cv2.erode(mask,None,iterations=5)
cv2.imshow("Eroded",mask)
cv2.waitKey()

mask=thresh.copy()
mask=cv2.dilate(mask,None,iterations=5)
cv2.imshow("Eroded",mask)
cv2.waitKey()

# mask=thresh.copy()
output=cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)

