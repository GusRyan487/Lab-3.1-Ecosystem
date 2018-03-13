from graphics import *
from BasicShip import *
from Destroyer import *
from AircraftCarrier import *

win = GraphWin("Navy Fleet", 1000, 650, autoflush=False)


class Background(object):

    def __init__(self,win):

        self.win = win

        self.drawHouse()
        self.drawLand()
        self.drawOcean()
        self.drawSun()
        self.shell = False


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
        house = Rectangle(Point(100, 200), Point(225, 300))
        house.setFill(color_rgb(73, 49, 5))
        house.draw(win)
        roof = Polygon(Point(100, 200), Point(125, 175), Point(200, 175), Point(225, 200))
        roof.setFill(color_rgb(40, 27, 2))
        roof.draw(win)
        door = Rectangle(Point(125, 300), Point(150, 250))
        door.setFill(color_rgb(196, 135, 70))
        door.draw(win)
        window = Rectangle(Point(175, 250), Point(200, 225))
        window.setFill(color_rgb(104, 222, 255))
        window.draw(self.win)

    def drawSun(self):
        """Drawing a sun"""
        sun = Circle(Point(999, 0), 100)
        sun.setFill("yellow")
        sun.draw(self.win)
    def blast(self):
        """shooting land with destroyer"""
        if self.shell == True:
            blast = Arc(Point(325, 300), Point(225, 450), 90, 180, "sector")
            blast.setFill("white")
            blast.draw(self.win)
            blast.setOutline("white")
            xtraBlast = Rectangle(Point(275,300),Point(300,450))
            xtraBlast.setFill("white")
            xtraBlast.draw(self.win)
            xtraBlast.setOutline("white")
        else:
            print("Your island survives another day")



win.setBackground(color_rgb(20, 200, 255))
back = Background(win)
ship = basicShip(625,400,win)
ac= AircraftCarrier(2,2,win)
print(ac.acName)
dest = Destroyer(2,2,win)
print(dest.dName)



win.getMouse()
win.close()
