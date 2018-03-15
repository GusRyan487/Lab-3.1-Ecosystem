from basicShip import *
import random

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
        #self.missle()


    def drawTurret(self):
        """drawing an arc for a turret and a gun to shoot the land"""
        gun = Rectangle(Point(self.x-50,self.y - 12.5), Point(self.x + 50,self.y - 5))
        gun.setFill(color_rgb(150, 155, 163))
        gun.draw(self.win)
        turret = Arc(Point(self.x + 25, self.y+25), Point(self.x+100, self.y-25), 0, 180, "chord")
        turret.setFill(color_rgb(150, 155, 163))
        turret.draw(self.win)
        self.explosion = Image(Point(self.x - 100, self.y - 10), 'nope.png')
        self.explosion.draw(self.win)

    #def missle(self):









