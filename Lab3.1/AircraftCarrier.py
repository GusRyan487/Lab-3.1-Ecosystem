from BasicShip import *
class AircraftCarrier(basicShip):
    def __init__(self, x, y, win, color=(color_rgb(150, 155, 163))):
        super(AircraftCarrier,self).__init__(x,y,win,color)

    def plane(self):

