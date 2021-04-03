import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import epd7in5b_HD
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

resourcesdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'resources')

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5b_HD Demo")

    epd = epd7in5b_HD.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font24 = ImageFont.truetype(os.path.join(resourcesdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(resourcesdir, 'Font.ttc'), 18)

    image = Image.open(os.path.join(resourcesdir, 'demo.bmp'))
    empty_image = Image.new('1', (epd.width, epd.height), 255)

    epd.display(epd.getbuffer(image), epd.getbuffer(empty_image))

    time.sleep(5)

    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_HD.epdconfig.module_exit()
    exit()
