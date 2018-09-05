"""
picture.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/


# add your code here /\  /\  /\
from ggame import App
myapp = App()
myapp.run()
black=Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
white = Color(0xf8f8ff, 1.0)
thinline=LineStyle(1, black)
rectangleRed=RectangleAsset(75, 20, thinline, red)
circle = CircleAsset (200, thinline, white)
ellipse = EllipseAsset (1, 1, thinline, blue)
polygon = PolygonAsset ([(0,0), (100,-150), (200,0)] thinline, green)
Sprite(circle, (10, 0))
Sprite(rectangleRed, (120,50))
Sprite(rectangleRed, (230,50))
Sprite(ellipse, (0,0))
Sprite(polygon, (0,0))