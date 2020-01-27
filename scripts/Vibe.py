import neopixel
import board

def run(pixels, stop):
	for x in range(300):
		if (x < 99):
			pixels[x] = (0, 56, 168)
		elif (x < 199):
			pixels[x] = (155, 79, 150)
		else:
			pixels[x] = (175, 2, 112)
	pixels.show()
