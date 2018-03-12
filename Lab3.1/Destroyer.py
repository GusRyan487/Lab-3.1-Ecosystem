from BasicShip import *
class Destroyer(basicShip):
    def __init__(self, x, y, win, color=(color_rgb(150, 155, 163))):
        super(Destroyerr,self).__init__(x,y,win,color)

    def turret(self):

from basicShip import *
class Destroyer(basicShip):
    def __init__(self, x, y, win, color=(color_rgb(150, 155, 163))):
        super(Destroyer, self).__init__(x, y, win, color)
        self.drawTurret()

    def drawTurret(self):
        turret = Arc(Point(650,425), Point(725,375),0,180,"chord")
        turret.draw(self.win)
