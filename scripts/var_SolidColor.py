#color

import board
import neopixel
import time
import random

def run(pixels, stop, var):
	split = var.split(',')
	pixels.fill((int(split[0]), int(split[1]), int(split[2])))
	pixels.show()
