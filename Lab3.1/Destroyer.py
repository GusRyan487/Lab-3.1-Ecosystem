from BasicShip import *
import random
import time
class Destroyer(basicShip):
    def __init__(self,x,y,win,color = (color_rgb(150, 155, 163))):
        super(Destroyer,self).__init__(x,y,win,color)
        self.dName = "Destroyer #"
        ran = random.randint(1, 100)
        if ran < 10:
            ran = '0' + str(ran)
        self.dName += str(ran)
        self.move = True
        self.drawTurret()
        self.missle()


    def drawTurret(self):
        """drawing an arc for a turret and a gun to shoot the land"""
        gun = Rectangle(Point(650, 387.5), Point(600, 400))
        gun.setFill(color_rgb(150, 155, 163))
        gun.draw(self.win)
        turret = Arc(Point(650, 425), Point(725, 375), 0, 180, "chord")
        turret.setFill(color_rgb(150, 155, 163))
        turret.draw(self.win)

    def missle(self):
        missle = Rectangle(Point(512.5,393.75), Point(537.5,400))
        missle.setFill("black")
        missle.draw(self.win)
        while self.move == True:
            if missle.getP1() == Point(300.0, 393.0):
                missle.undraw()
                self.move= False
            else:
                if self.move == True:
                    #time.sleep(.5)
                    missle.move(50,0)







