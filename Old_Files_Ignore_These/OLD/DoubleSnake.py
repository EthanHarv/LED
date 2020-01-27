import board
import neopixel
import time
import random

PIN = board.D18 # Only 10, 12, 18, 21
PIXEL_NUM = 300
BRIGHTNESS = .5
ORDER = neopixel.GRB # Alt: RGBW/GRBW/(RGB?)

pixels = neopixel.NeoPixel(PIN, PIXEL_NUM, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRB)

#pixels[0] = (255, 0, 0)
#pixels[2] = (0, 255, 0)
#pixels[4] = (0, 0, 255)

while True:
	color = ((random.randint(30, 255), random.randint(30, 255), random.randint(30, 255)))
	for i in range(150):
		pixels[i] = color
		pixels[300 - i - 1] = color
		pixels.show()
	time.sleep(1)
	pixels.fill((0, 0, 0))
	pixels.show()
