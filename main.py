import cv2
import time
import numpy as np
cap = cv2.VideoCapture(0)
time.sleep(1)
count = 0
background = 0
for i in range(10):
    return_val, background = cap.read()
    if return_val == False :
        continue
background=np.flip(background,axis=1)
while(cap.isOpened()):
  ret,img=cap.read()
  if not ret:
    break
  count=count+1
  img=np.flip(img,axis=1)
  hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lower_blue = np.array([90,70,50])
  upper_blue = np.array([128,255,255])
  mask1=cv2.inRange(hsv,lower_blue,upper_blue)
  mask2=cv2.bitwise_not(mask1)
  res1 = cv2.bitwise_and(background, background, mask=mask1)
  res2 = cv2.bitwise_and(img, img, mask=mask2)
  cv2.imshow("magic",res1+res2)
  k = cv2.waitKey(10)
  if k == 27:
    break
cap.release()
cv2.destroyAllWindows()
