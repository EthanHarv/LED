import board
import neopixel
import time
import random

def run(pixels, stop):
	while True:
		pixels.fill((random.randint(0,255), random.randint(0, 255), random.randint(0,255)))
		pixels.show()
		time.sleep(.02)
		if stop():
			break
