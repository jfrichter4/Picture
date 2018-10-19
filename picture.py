"""
Ask Google: How to make a game in python without pygame
platformer.py
Author: Joe Richter
Credit: https://www.chegg.com/homework-help/questions-and-answers/make-snake-game-python-3-without-using-pygame-using-provided-code-graphics-module-using-ti-q24692355, Joe Richter
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
WW = 1000
WH = 800
#Colors Set:
blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)
#Lines:
thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)
LK = 'left key'
RK = 'right key'
UK = 'up key'
DK = 'down key'
Mainrect = RectangleAsset(15, 50, thinline, green)
Boxrect = RectangleAsset(75, 20, thinline, black)
Springrect = RectangleAsset(10, 5, thinline, blue)
Main = Sprite(Mainrect, (15, 50))
Boxes = Sprite(Boxrect, (75, 20))
Springs = Sprite(Springrect, (10, 5))
for a in Main:
    def input:
        if input == 'p':
            #Spawn a Main Player
for m in Main:
    def move(Main, key):
        if key == LK:
            #Move sprite to the left
        if key == RK:
            #Move sprite to the right
        if key == UK:
            #Move sprite up
        if key == DK:
            #Move sprite down
for b in Boxes:
    def input:
        if input == 'w':
            #Make a wall where the cursor is
for s in Springs:
    def input:
        if input == 's':
            #Make a spring where the cursor is
#Create a gravity engine-type thing
#Create a collision engine - the shell is below:
for c in main:
    if #the main collides with another sprite, delete the sprite.
app.run()
"""
#Dir:
DL = 'downleft'
DR = 'downright'
UL = 'upleft'
UR = 'upright'
MS = 4
# Boxes Set
b1 = RectangleAsset(15, 50, thinline, red)
boxes = [b1]
for b in boxes:
    if DL == True:
        b[].left -= MS
        -= MS
    if DR == True:
        b[].left += MS
        += MS
    if UL == True:
        b[].left -= MS
        -= MS
    if UR == True:
        b[].left += MS
        -= MS

    # Move the character data structure
    if b(direction) == DL:
        b[].left -= MS
        b['rect'].top += MS
    if b['dir'] == DR:
        b['rect'].left += MS
        b['rect'].top += MS
    if b['dir'] == UL:
        b['rect'].left -= MS
        b['rect'].top -= MS
    if b['dir'] == UR:
        b['rect'].left += MS
        b['rect'].top -= MS
    # Check whether the character has moved out of the window
    if b['rect'].top < 0:
        # The box has moved past the top
        if b['dir'] == UL:
            b['dir'] == DL
        if b['dir'] == UR:
            b['dir'] == DR
        if b['rect'].bottom > WH:
            # The box has moved past the bottom
            if b['dir'] == DL:
                b['dir'] == UL
            if b['dir'] == DR:
                b['dir'] == UR
        if b['rect'].left < 0:
            # The box has moved past the left side
            if b['dir'] == DL:
                b['dir'] == DR
            if b['dir'] == UL:
                b['dir'] == UR
        if b['rect'].right > WW:
            # The character has moved past the right side
            if b['dir'] == DR:
                b['dir'] == DL
            if b['dir'] == UR:
                b['dir'] == UL
        ggame.draw.rect(windowSurface, b['color'], b['rect'])
"""