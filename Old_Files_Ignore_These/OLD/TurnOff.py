import board
import neopixel
import time
import random

PIN = board.D18 # Only 10, 12, 18, 21
PIXEL_NUM = 300
BRIGHTNESS = 0
ORDER = neopixel.GRB # Alt: RGBW/GRBW/(RGB?)

pixels = neopixel.NeoPixel(PIN, PIXEL_NUM, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRB)

pixels.show()
