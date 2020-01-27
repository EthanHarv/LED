import board
import neopixel
import time
import random

PIN = board.D18 # Only 10, 12, 18, 21
PIXEL_NUM = 300
BRIGHTNESS = .75
ORDER = neopixel.GRB # Alt: RGBW/GRBW/(RGB?)

pixels = neopixel.NeoPixel(PIN, PIXEL_NUM, brightness = BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRB)

clr = [0, 56, 186] # Initial Color (Probably best to use last color in the below tuple)

colors = ((214, 2, 112), (155, 79, 150), (0, 56, 168)) # 3 unique

def changeBy(clr, target): # Calculate if color is -/=/+ and return the direction as -1, 0, 1
	if (target == clr):
		return 0
	elif (target > clr):
		return 1
	elif (target < clr):
		return -1

def fillLast(color):
	for x in range(300):
		if (x > 260):
			pixels[x] = color
		else:
			pixels[x] = (0, 0, 0)

while True:
	for i in range(0, len(colors)): # Loop through each color
		fin = False
		while (fin == False): # Loop untill colors align
			R = changeBy(clr[0], colors[i][0]) # Compare colors
			G = changeBy(clr[1], colors[i][1])
			B = changeBy(clr[2], colors[i][2])
			clr[0] += R
			clr[1] += G
			clr[2] += B
			fillLast((clr[0], clr[1], clr[2]))
			pixels.show()
			time.sleep(.001)
			if (R == 0 and G == 0 and B ==0):
				fin = True



