from basicShip import *
from Background import *
from AircraftCarrier import *
from Destroyer import *
import time



def main():
    '''runs the program'''
    win.setBackground(color_rgb(20, 200, 255))
    back = Background(win)
    ac= AircraftCarrier(625,400,win)
    dest = Destroyer(600,200,win)



    dest.destMove(400,200)

main()

win.getMouse()
win.close()
