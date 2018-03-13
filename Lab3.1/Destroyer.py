from basicShip import *

class Destroyer(basicShip):
    def __init__(self, x, y, win, color=(color_rgb(150, 155, 163))):
        super(Destroyer, self).__init__(x, y, win, color)
        self.drawTurret()

    def drawTurret(self):
        gun = Rectangle(Point(650,387.5), Point(600,400))
        gun.setFill(color_rgb(150,155,163))
        gun.draw(self.win)
        turret = Arc(Point(650, 425), Point(725, 375), 0, 180, "chord")
        turret.setFill(color_rgb(150, 155, 163))
        turret.draw(self.win)






