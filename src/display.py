import os
from typing import Any, Union, Tuple
from PIL import Image
from ..lib import epd7in5b_HD

resources_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'resources')


class Display:

    _epd: Any
    _empty_image: Any


    def _init_(self):

        self._epd = epd7in5b_HD.EPD()
        self._empty_image = Image.new('1',
            (self._epd.width, self._epd.height),
            255)


    def show_images_by_files(self,
            black_image_file: Union[str, None] = None,
            red_image_file: Union[str, None] = None
            ) -> None:

        self._init()

        black_image_buffer = self._epd.getbuffer(self._empty_image)
        red_image_buffer = self._epd.getbuffer(self._empty_image)

        if black_image_file and black_image_file != '':
            black_image_buffer = self._epd.getbuffer(Image.open(os.path.join(resources_dir, black_image_file)))

        if red_image_file and red_image_file != '':
            red_image_buffer = self._epd.getbuffer(Image.open(os.path.join(resources_dir, red_image_file)))

        self._epd.display(black_image_buffer, red_image_buffer)

        self._sleep()


    def show_images(self,
        black_image: Union[Any, None] = None,
        red_image: Union[Any, None] = None
        ) -> None:

        self._init()

        if black_image is None:
            black_image = self._empty_image

        if red_image is None:
            red_image = self._empty_image

        self._epd.display(self._epd.getbuffer(black_image), self._epd.getbuffer(red_image))

        self._sleep()


    def get_width_height(self) -> Tuple[int, int]:
        return (self._epd.width, self._epd.height)


    def clear(self) -> None:
        self._epd.Clear()


    def exit(self) -> None:
        epd7in5b_HD.epdconfig.module_exit()


    def _init(self) -> None:
        self._epd.init()


    def _sleep(self) -> None:
        self._epd.sleep()
