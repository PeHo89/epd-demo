from .visuals import Text, Font, Image, Position
from .display import Display

font24 = Font('Font.tcc', 24)

text1 = Text('Hi there', font24)
text2 = Text('my name is Peter', font24)

image = Image()
image.text(Position(10, 10), text1).text(Position(50, 50), text2)

display = Display()
display.show_images(black_image=image)
