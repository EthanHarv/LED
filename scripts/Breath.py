import neopixel
import board
import time

def run(pixels, stop):
	for x in range(300):
		if (x < 99):
			pixels[x] = (0, 56, 168)
		elif (x < 199):
			pixels[x] = (155, 79, 150)
		else:
			pixels[x] = (175, 2, 112)
	pixels.show()
	dir = False # Up = True, Down = False
	while True:
		if (pixels.brightness == 0):
			dir = True # Go back up
		elif (pixels.brightness == 1):
			dir = False # Go back down

		if (dir): #Up
			pixels.brightness += .001
			pixels.show()
			time.sleep(.01)
		else:
			pixels.brightness -= .001
			pixels.show()
			time.sleep(.01)

		if stop():
			pixels.brightness = .5
			break
