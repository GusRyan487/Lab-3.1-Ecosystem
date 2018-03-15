from BasicShip import *
import random


class AircraftCarrier(basicShip):
    def __init__(self, x, y, win, color=(color_rgb(150, 155, 163))):
        super(AircraftCarrier, self).__init__(x, y, win, color)
        self.acName = 'Aircraft Carrier #'
        self.createAcName()
        self._plane()

    def createAcName(self):
        '''Creates Aircraft carriers number'''
        ran = random.randint(1, 100)
        if ran < 10:
            ran = '0' + str(ran)
        self.acName += str(ran)
        print('Created',self.acName)

    def _plane(self):
        '''Draws plane on ship'''
        self.plane = Image(Point(self.x + 75, self.y - 20), 'plane_v2.png')
        self.plane.draw(self.win)
        self.bomb = Image(Point(500,300),'bomb.png')
        self.bomb.draw(self.win)

    def move(self,x,y,win):
        super(AircraftCarrier,self).move(x,y,win)
        self.plane.undraw()
        self.plane.draw(win)



