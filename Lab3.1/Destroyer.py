from BasicShip import *
import random

class Destroyer(basicShip):
    def __init__(self,x,y,win,color = (color_rgb(150, 155, 163))):
        super(Destroyer,self).__init__(x,y,win,color)
        self.dName = "Destroyer #"
        self.Turret.drawTurret()
        self.createDName()
        self.Turret(self.win)

    def createDName(self):
        '''creates the destroyer id number'''
        ran = random.randint(1, 99)
        if ran < 10:
            ran = '0' + str(ran)
        self.dName += str(ran)
        print("Created",self.dName)

    def destMove(self, x, y):
        '''moves gun and the destroyer'''
        self.move(x, y)
        self.Turret.gun.undraw()
        self.Turret.turret.undraw()
        self.Turret.explosion.undraw()
        self.Turret.drawTurret()

    class Turret(object):
        def __init__(self, win):
            self.x =
            self.gun = None
            self.turret = None
            self.explosion = None
            self.win = win

        def drawTurret(self):
            """drawing an arc for a turret and a gun to shoot the land"""
            self.gun = Rectangle(Point(self.x-50,self.y - 12.5), Point(self.x + 50,self.y - 5))
            self.gun.setFill(color_rgb(150, 155, 163))
            self.gun.draw(self.win)
            self.turret = Arc(Point(self.x + 25, self.y+25), Point(self.x+100, self.y-25), 0, 180, "chord")
            self.turret.setFill(color_rgb(150, 155, 163))
            self.turret.draw(self.win)
            self.explosion = Image(Point(self.x - 100, self.y - 10), 'nope.png')









