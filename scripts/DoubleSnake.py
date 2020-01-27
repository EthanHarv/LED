import board
import neopixel
import time
import random

def run(pixels, stop):
	while True:
		color = ((random.randint(30, 255), random.randint(30, 255), random.randint(30, 255)))
		for i in range(150):
			pixels[i] = color
			pixels[300 - i - 1] = color
			if stop():
				break
			pixels.show()
		time.sleep(1)
		pixels.fill((0, 0, 0))
		pixels.show()
		if stop():
			break
