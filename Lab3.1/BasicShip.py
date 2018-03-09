from graphics import *
#win = GraphWin('Navy',1000,650,autoflush= False)
class basicShip(object):

    def __init__(self,x,y,win,color = (color_rgb(150, 155, 163))):
        self.x = x
        self.y = y
        self.color = color
        self.hit = False
        self.win = win
        self.hull()
        self.controlCenter()
        self.windows()

    def hull(self):
        hull = Polygon(Point(self.x,self.y),Point((self.x + 75), (self.y + 50)), Point((self.x + 225 ), (self.y + 50)), Point((self.x + 300), (self.y)))
        hull.setFill(self.color)
        hull.draw(self.win)

    def controlCenter(self):
        controlCenter = Polygon(Point((self.x + 150 ), (self.y - 0)),Point((self.x + 175 ), (self.y - 75)),Point((self.x + 250 ), (self.y - 75)),Point((self.x + 250 ), (self.y - 0)))
        controlCenter.setFill(self.color)
        controlCenter.draw(self.win)

    def windows(self):
        addX = 165.5
        for i in range(0,4):
            window = Rectangle(Point((self.x + addX),(self.y - 50)), Point((self.x + (addX + 12.5)),(self.y - 37.5)))
            window.setFill(color_rgb(198,244,242))
            window.draw(self.win)
            addX += 15

#ship = basicShip(600,350,win)
#win.getMouse()
