# displayGraphics.py
#
# Description:
# Prints text and graphics to an SSD1306 display module using the
# Adafruit_Python_SSD1306 and Python Imaging Library (PIL) libraries.
#
# Created by John Woolsey on 07/03/2018.
# Copyright (c) 2018 Woolsey Workshop.  All rights reserved.


import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO


# Draws LED schematic symbol with size of 60x24
def drawLED(centerX, centerY):
   draw.polygon((centerX - 10, centerY + 12, centerX + 10, centerY + 2, centerX - 10, centerY - 8), fill=255)
   draw.line((centerX + 10, centerY - 8, centerX + 10, centerY + 12), fill=255)
   draw.line((centerX - 30, centerY + 2, centerX - 10, centerY + 2), fill=255)
   draw.line((centerX + 10, centerY + 2, centerX + 30, centerY + 2), fill=255)
   draw.line((centerX, centerY - 6, centerX + 3, centerY - 10), fill=255)
   draw.polygon((centerX + 6, centerY - 12, centerX + 6, centerY - 8, centerX + 2, centerY - 12), fill=255)
   draw.line((centerX - 22, centerY + 8, centerX - 18, centerY + 8), fill=255)
   draw.line((centerX - 20, centerY + 6, centerX - 20, centerY + 10), fill=255)
   draw.line((centerX + 18, centerY + 8, centerX + 22, centerY + 8), fill=255)


# Adafruit_Python_SSD1306 graphics library configuration for
# SunFounder OLED SSD1306 Display Module.
# Use the configuration compatible with your display module.
# See library "examples" directory for configuration selection.
# 128x64 display with hardware I2C and no reset pin
display = Adafruit_SSD1306.SSD1306_128_64(rst=None)

# Setup
display.begin()  # initialize graphics library for selected display module
display.clear()  # clear display buffer
display.display()  # write display buffer to physical display
displayWidth = display.width  # get width of display
displayHeight = display.height  # get height of display
image = Image.new('1', (displayWidth, displayHeight))  # create graphics library image buffer
draw = ImageDraw.Draw(image)  # create drawing object
font = ImageFont.load_default()  # load and set default font

# Draw text
draw.text(((displayWidth - font.getsize("Woolsey")[0]) / 2, 0), "Woolsey", font=font, fill=255)  # center text at top of screen
draw.text(((displayWidth - font.getsize("Workshop")[0]) / 2, 53), "Workshop", font=font, fill=255)  # center text at bottom of screen

# Draw LED symbol
drawLED(displayWidth / 2, displayHeight / 2)  # place symbol in middle of screen (between text)

# Display to screen
display.image(image)  # set display buffer with image buffer
display.display()  # write display buffer to physical display

# Cleanup
GPIO.cleanup()  # release all GPIO resources
