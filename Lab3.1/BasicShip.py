from graphics import *
#win = GraphWin('Navy',1000,650,autoflush= False)
class basicShip(object):

    def __init__(self,x,y,win,color = (color_rgb(150, 155, 163))):
        self.x = x
        self.y = y
        self.color = color
        self.win = win
        self._hull()
        self._controlCenter()
        self._windows()
        self.addX = 0

    def _hull(self):
        '''Draws ship hull'''
        self.hull = Polygon(Point(self.x,self.y),Point((self.x + 75), (self.y + 50)), Point((self.x + 225 ), (self.y + 50)), Point((self.x + 300), (self.y)))
        self.hull.setFill(self.color)
        self.hull.draw(self.win)

    def _controlCenter(self):
        '''Draws ship's control center'''
        self.controlCenter = Polygon(Point((self.x + 150 ), (self.y - 0)),Point((self.x + 175 ), (self.y - 75)),Point((self.x + 250 ), (self.y - 75)),Point((self.x + 250 ), (self.y - 0)))
        self.controlCenter.setFill(self.color)
        self.controlCenter.draw(self.win)

    def _windows(self):
        '''Draws ship windows'''
        self.windows = []
        self.addX = 165.5
        for i in range(0,4):
            window = Rectangle(Point((self.x + self.addX),(self.y - 50)), Point((self.x + (self.addX + 12.5)),(self.y - 37.5)))
            window.setFill(color_rgb(198,244,242))
            window.draw(self.win)
            self.windows.append(window)
            self.addX += 15

    def move(self,x,y,win):
        '''Moves ship'''
        time.sleep(.5)
        self.x = x
        self.y = y
        self.hull.undraw()
        self.controlCenter.undraw()
        for i in self.windows:
            i.undraw()
        self._hull()
        self._controlCenter()
        self.addX = 165.5 + (self.x - x)
        self._windows()
