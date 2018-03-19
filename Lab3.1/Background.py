from graphics import *
from BasicShip import *
from Destroyer import *
from AircraftCarrier import *

win = GraphWin("Navy Fleet", 1000, 650)


class Background(object):

    def __init__(self,win):
        self.win = win
        self.drawHouse()
        self.drawLand()
        self.drawOcean()
        self.drawSun()


    def drawOcean(self):
        """Drawing an ocean"""
        ocean = Rectangle(Point(0, 450), Point(999, 649))
        ocean.setFill(color_rgb(15, 144, 219))
        ocean.draw(self.win)

    def drawLand(self):
        """Drawing land"""
        land = Rectangle(Point(0, 300), Point(300, 450))
        land.setFill(color_rgb(249, 235, 184))
        land.draw(self.win)


    def drawHouse(self):
        """Drawing a housed with a door window on land"""
        self.house = Rectangle(Point(100, 200), Point(225, 300))
        self.house.setFill(color_rgb(73, 49, 5))
        self.house.draw(win)
        self.roof = Polygon(Point(100, 200), Point(125, 175), Point(200, 175), Point(225, 200))
        self.roof.setFill(color_rgb(40, 27, 2))
        self.roof.draw(win)
        self.door = Rectangle(Point(125, 300), Point(150, 250))
        self.door.setFill(color_rgb(196, 135, 70))
        self.door.draw(win)
        self.window = Rectangle(Point(175, 250), Point(200, 225))
        self.window.setFill(color_rgb(104, 222, 255))
        self.window.draw(self.win)
    def undrawHouse(self):
        self.house.undraw()
        self.roof.undraw()
        self.door.undraw()
        self.window.undraw()

    def drawSun(self):
        """Drawing a sun"""
        sun = Circle(Point(999, 0), 100)
        sun.setFill("yellow")
        sun.draw(self.win)
    def blast(self):
        """shooting land with destroyer"""
        blast = Arc(Point(325, 300), Point(225, 450), 90, 180, "sector")
        blast.setFill(color_rgb(20, 200, 255))
        blast.draw(self.win)
        blast.setOutline(color_rgb(20, 200, 255))
        xtraBlast = Rectangle(Point(275,300),Point(300,450))
        xtraBlast.setFill(color_rgb(20, 200, 255))
        xtraBlast.draw(self.win)
        xtraBlast.setOutline(color_rgb(20, 200, 255))



