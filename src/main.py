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

    empty_image = Image.new('1', (epd.width, epd.height), 255)

    while True:
        epd.init()
        
        image = Image.open(os.path.join(resourcesdir, 'message.bmp'))

        epd.display(epd.getbuffer(image), epd.getbuffer(empty_image))

        logging.info("Goto Sleep...")
        epd.sleep()
        time.sleep(7200)

        epd.init()

        image = Image.open(os.path.join(resourcesdir, 'postbox.bmp'))

        epd.display(epd.getbuffer(image), epd.getbuffer(empty_image))

        logging.info("Goto Sleep...")
        epd.sleep()
        time.sleep(7200)
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5b_HD.epdconfig.module_exit()
    exit()
