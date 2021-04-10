import os
from typing import Any, Tuple
from PIL import Image as PILImage, ImageDraw, ImageFont

resources_dir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'resources')

class Font:

    _font: Any


    def __init__(self, font_file: str, font_size: int):
        self._font = ImageFont.truetype(os.path.join(resources_dir, font_file), font_size)


    @property
    def font(self) -> Any:
        return self._font



class Text:
    _content: str
    _font: Font


    def __init__(self, content: str, font: Font):
        self._content = content
        self._font = font


    @property
    def content(self) -> str:
        return self._content


    @property
    def font(self) -> Any:
        return self._font



class Position:
    _x: int
    _y: int


    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y


    @property
    def x_y(self) -> Tuple[int, int]:
        return (self._x, self._y)



class Image:
    _image: Any
    _draw: Any

    def create(self, width: int = 880, height: int = 528) -> 'Image':
        self._image = PILImage.new('1', (width, height), 255)
        self._draw = ImageDraw.Draw(self._image)

        return self


    def text(self, position: Position, text: Text) -> 'Image':
        self._draw.text(position.x_y, text.content, font=text.font, fill=0)

        return self


    def get_image(self) -> Any:
        return self._image
