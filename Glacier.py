import cv2
import numpy as np

img =cv2.imread('Glacier.jpg')

blur = cv2.blur(img,(5,5))
blur0=cv2.medianBlur(blur,5)
blur1= cv2.GaussianBlur(blur0,(5,5),0)
blur2= cv2.bilateralFilter(blur1,9,75,75)

hsv = cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)

low_blue = np.array([55, 0, 0])
high_blue = np.array([118, 255, 255])
mask = cv2.inRange(hsv, low_blue, high_blue)

res = cv2.bitwise_and(img,img, mask= mask)
cv2.imwrite("res.jpg",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()