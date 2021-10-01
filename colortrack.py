# Adapted from: https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/
# and adapted from: https://automaticaddison.com/how-to-detect-and-draw-contours-in-images-using-opencv/

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while(1):
	_, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower1_red = np.array([0, 150, 20])
	upper1_red = np.array([9, 255, 255])

	lower2_red = np.array([160,150,20])
	upper2_red = np.array([179,255,255])
 
	lower_mask = cv2.inRange(hsv, lower1_red, upper1_red)
	upper_mask = cv2.inRange(hsv, lower2_red, upper2_red)

	result = cv2.bitwise_and(frame, frame, mask = lower_mask + upper_mask)
	new_image = result.copy()
	cv2.imshow('frame', frame)
	gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)

	contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	with_contours = cv2.drawContours(result, contours, -1,(255,0,255),3)
	
	for c in contours:
	  x, y, w, h = cv2.boundingRect(c)

	  if (cv2.contourArea(c)) > 10:
	   cv2.rectangle(with_contours,(x,y), (x+w,y+h), (255,0,0), 5)
		 
	cv2.imshow('Bounding box', with_contours)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cap.release()
