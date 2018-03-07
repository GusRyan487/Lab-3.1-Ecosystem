from updatedGraphics import *
win = GraphWin('Navy',1000,650,autoflush= False)
class basicShip(object):

    def __init__(self,x,y,color = (color_rgb(150, 155, 163))):
        self.X = x
        self.Y = y
        self.color = color
        self.hit = False

    def draw(self):
        hull = Polygon()