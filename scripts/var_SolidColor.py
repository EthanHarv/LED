#color

import board
import neopixel
import time
import random

def run(pixels, stop, var):
	split = var.split(',')
	pixels.fill((int(var[0]),int(var[1]),int(var[2])))
	pixels.show()
