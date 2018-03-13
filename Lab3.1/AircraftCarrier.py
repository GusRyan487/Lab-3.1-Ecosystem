from BasicShip import *
import random
class AircraftCarrier(basicShip):
    def __init__(self, x, y, win, color=(color_rgb(150, 155, 163))):
        super(AircraftCarrier,self).__init__(x,y,win,color)
        self.acName = 'Aircraft Carrier #'
        ran = random.randint(1, 100)
        if ran < 10:
            ran = '0' + str(ran)
            self.acName += ran


    #def plane(self):
        #self.body = Oval(Point())

