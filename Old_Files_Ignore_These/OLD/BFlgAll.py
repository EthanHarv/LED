import board
import neopixel
import time
import random

PIN = board.D18 # Only 10, 12, 18, 21
PIXEL_NUM = 300
BRIGHTNESS = .5
ORDER = neopixel.GRB # Alt: RGBW/GRBW/(RGB?)

pixels = neopixel.NeoPixel(PIN, PIXEL_NUM, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRB)

state = 1

for x in range(300):
	if (state == 1):
		pixels[x] = (214, 2, 112)
		state = 2
	elif (state == 2):
		pixels[x] = (155, 79, 150)
		state = 3
	else:
		pixels[x] = (0, 56, 168)
		state = 1

pixels.show()
