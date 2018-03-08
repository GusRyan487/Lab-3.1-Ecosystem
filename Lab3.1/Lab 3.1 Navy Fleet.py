from graphics import *
win = GraphWin("Navy Fleet",1000,650, autoflush=False)






class Background(object):
    def drawOcean(win):
        ocean = Rectangle(Point(0,450), Point(999,649))
        ocean.setFill(color_rgb(15, 144, 219))
        ocean.draw(win)
    def __init__(self,house,land):
        self.land = land
        self.house = house
        



    def drawLand(self,win):
        land = Rectangle(Point(0,300), Point(300,450))
        land.setFill(color_rgb(249, 235, 184))
        land.draw(win)
    def drawHouse(self,win):
        house = Rectangle(Point(100,200), Point(225,300))
        house.setFill(color_rgb(73,49,5))
        house.draw(win)
        roof = Polygon(Point(100,200), Point(125,175), Point(200,175), Point(225,200))
        roof.setFill(color_rgb(40,27,2))
        roof.draw(win)
        door = Rectangle(Point(125,300), Point(150,250))
        door.setFill(color_rgb(196, 135, 70))
        door.draw(win)
        window = Rectangle(Point(175,250), Point(200,225))
        window.setFill(color_rgb(104, 222, 255))
        window.draw(win)
    def drawSun(win):
        sun = Circle(Point(999,0), 100)
        sun.setFill("yellow")
        sun.draw(win)

win.setBackground(color_rgb(20,200,255))
Background.drawOcean(win)
Background.drawLand(win)
Background.drawHouse(win)
Background.drawSun(win)
win.getMouse()
win.close()

class Damage()








