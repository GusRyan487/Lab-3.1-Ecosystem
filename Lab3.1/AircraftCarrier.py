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
        ran = random.randint(1, 99)
        if ran < 10:
            ran = '0' + str(ran)
        self.acName += str(ran)
        print('Created',self.acName)

    def acmove(self,x,y):
        '''moves ship and plane'''
        self.move(x,y)
        self.plane.undraw()
        self._plane()

    class Plane(object):

        def _plane(self):
            '''Draws plane on ship'''
            self.plane = Image(Point(self.x + 75, self.y - 20), 'plane_v2.png')
            self.plane.draw(self.win)
            self.bomb = Image(Point(250,100),'bomb.png')

            def dropTheBomb(self):
                '''moves plane and drops bomb'''
                dy = 420
                while dy != 100:
                    self.plane.move(-6.25, -5)
                    time.sleep(.1)
                    dy -= 5
                self.bomb.draw(self.win)
                dy = 100
                while dy != 300:
                    self.bomb.move(0, 10)
                    time.sleep(.25)
                    dy += 10
                self.bomb.undraw()
                self.boom = Image(Point(150, 237.5), 'nuke.png')
                self.boom.draw(self.win)
                dx = 175
                while dx != -10:
                    time.sleep(.1)
                    self.plane.move(-6.25, 0)
                    dx -= 5



