from BasicShip import *
from Background import *
from AircraftCarrier import *
from Destroyer import *
import time





def main():
    '''runs the program'''
    win.setBackground(color_rgb(20, 200, 255))
    back = Background(win)
    t = Turret(win,600,400)
    dest = Destroyer(600, 400, win,t)
    time.sleep(2)
    x = 600
    while x != 400:
        dest.destMove(x,400)
        x-= 5
    dest.destMove(400, 400)
    time.sleep(2)
    back.blast()
    dest.turret.explosion.draw(win)
    time.sleep(1.5)
    x = 400
    while x != 1000:
        dest.destMove(x,400)
        x+=5

    ac = AircraftCarrier(625,400,win)
    time.sleep(.5)
    ac.acmove(600,400)
    ac.Plane.dropTheBomb()
    back.undrawHouse()


main()

win.getMouse()
win.close()
