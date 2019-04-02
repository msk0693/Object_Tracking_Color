import cv2
import numpy as np
import tkinter as TK
from tkinter import messagebox

root = TK.Tk()
root.withdraw()
messagebox.showinfo("Options", "Enter key 'b' : Track blue ojects\nEnter key 'g' : Track green objects\nEnter key 'o' : Track orange objects\nEnter key 'y' : Track yellow objects\nEnter key 'a' : Track all color objects\nEnter key 'esc' : Exit Program")
root.withdraw()

cap = cv2.VideoCapture(0)

#color(s) to be tracked
color = "all"

while(1):
	#take each frame
	_, frame = cap.read()

	#BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#find lower/upper bound of color
	#my_color = np.uint8([[[b,g,r]]])
	#my_hsv_color = cv2.cvtColor(my_color, cv2.COLOR_BGR2HSV)
	#print(my_hsv_color)

	#range of blue color in HSV
	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])

	#range of green color in HSV
	lower_green = np.array([50, 100, 100])
	upper_green = np.array([70, 255, 255])

	#rand of orange color in HSV
	lower_orange = np.array([0, 100, 100])
	upper_orange = np.array([20, 255, 255])

	#rand of yellow color in HSV
	lower_yellow = np.array([20, 100, 100])
	upper_yellow = np.array([40, 255, 255])

	

	#HSV thresholds
	maskb = cv2.inRange(hsv, lower_blue, upper_blue)

	maskg = cv2.inRange(hsv, lower_green, upper_green)

	masko = cv2.inRange(hsv, lower_orange, upper_orange)

	masky = cv2.inRange(hsv, lower_yellow, upper_yellow)



	mask = maskb + maskg + masko + masky

	if color == "blue":
		mask = maskb
	elif color == "green":
		mask = maskg
	elif color == "orange":
		mask = masko
	elif color == "yellow":
		mask = masky


	#bitwiseAND mask and original image
	res = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('rest', res)

	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	elif k == ord('b'):
		color = "blue"
	elif k == ord('g'):
		color = "green"
	elif k == ord('o'):
		color = "orange"
	elif k == ord('y'):
		color = "yellow"
	elif k == ord('a'):
		color = "all"

cv2.destroyAllWindows()