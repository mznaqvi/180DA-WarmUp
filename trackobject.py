# Adapted from: https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/
# and adapted from: https://automaticaddison.com/how-to-detect-and-draw-contours-in-images-using-opencv/

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while(1):
	_, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower1_red = np.array([0, 100, 20])
	upper1_red = np.array([10, 255, 255])

	lower2_red = np.array([160,100,20])
	upper2_red = np.array([179,255,255])
 
	lower_mask = cv2.inRange(hsv, lower1_red, upper1_red)
	upper_mask = cv2.inRange(hsv, lower2_red, upper2_red)
	 
	full_mask = lower_mask + upper_mask;
	result = cv2.bitwise_and(frame, frame, mask = full_mask)
	new_image = result.copy()
	gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Gray image', gray)  
	cv2.waitKey(0) # Wait for keypress to continue
	cv2.destroyAllWindows() # Close windows

	ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_OTSU)
	cv2.imshow('Binary image', binary)
	cv2.waitKey(0) # Wait for keypress to continue
	cv2.destroyAllWindows() # Close windows

	#inverted_binary = ~binary
	#cv2.imshow('Inverted binary image', inverted_binary)
	#cv2.waitKey(0) # Wait for keypress to continue
	#cv2.destroyAllWindows() # Close windows

	contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	with_contours = cv2.drawContours(result, contours, -1,(255,0,255),3)
	cv2.imshow('Detected contours', with_contours)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	first_contour = cv2.drawContours(new_image, contours, 0,(255,0,255),3)
	cv2.imshow('First detected contour', first_contour)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	x, y, w, h = cv2.boundingRect(contours[0])
	cv2.rectangle(first_contour,(x,y), (x+w,y+h), (255,0,0), 5)
	cv2.imshow('First contour with bounding box', first_contour)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	for c in contours:
	  x, y, w, h = cv2.boundingRect(c)
 
	# Make sure contour area is large enough
	  if (cv2.contourArea(c)) > 10:
	   cv2.rectangle(with_contours,(x,y), (x+w,y+h), (255,0,0), 5)
		 
	cv2.imshow('All contours with bounding box', with_contours)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	#for c in contours:
	 #x, y, w, h = cv2.boundingRect(c)
 
	# Make sure contour area is large enough
	#if (cv2.contourArea(c)) > 10:
	#cv2.rectangle(with_contours,(x,y), (x+w,y+h), (255,0,0), 5)
		 
#cv2.imshow('All contours with bounding box', with_contours)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#   cv2.imshow('frame', frame)
#   cv2.imshow('result', result)
#   cv2.imshow('mask', full_mask) 

#   cv2.waitKey(0)
 
#cv2.destroyAllWindows()
#cap.release()