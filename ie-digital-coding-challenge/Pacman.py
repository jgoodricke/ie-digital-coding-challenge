class Pacman(object):
    """Class containing Pacman's position and direction,
    As well as commands to move, turn, place and report position"""

    def __init__(self):
        #Cardinal directions - Used to be defined as an enum, but the enum was intefering with the unit tests.
        self.NILL = "NILL"
        self.NORTH = "NORTH"
        self.EAST = "EAST"
        self.SOUTH = "SOUTH"
        self.WEST = "WEST"

        #Position on grid (initialised as -1 until placed)
        self.__posX = -1
        self.__posY = -1
    
        #Grid maximum and minimun size
        self.__maxX = 5
        self.__maxY = 5
        self.__minX = 0
        self.__minY = 0

        #facing on grid (initialised as nill until placed)
        self.__face = self.NILL

    #Place Pacman on Grid
    def Place(self,x,y,face):
        self.__posX = x
        self.__posY = y
        self.__face = face

    #Report current position
    def Report(self):
        if self.__face != self.NILL:
            return str(self.__posX) + ","+ str(self.__posY) + "," + str(self.__face)
        else:
            return ""

    #Move Pacman in the direction it's facing
    def Move(self):
        #If pacman isn't placed, do nothing
        if self.__face != self.NILL:
            #If facing north, move north
            if self.__face == self.NORTH and self.__posY < self.__maxY:
                self.__posY += 1
            elif self.__face == self.SOUTH and self.__posY > self.__minY:
                self.__posY -= 1
            elif self.__face == self.EAST and self.__posX < self.__maxX:
                self.__posX += 1
            elif self.__face == self.WEST and self.__posX > self.__minX:
                self.__posX -= 1
    
    #Turn Pacman left
    def Left(self):
        #If pacman isn't placed, do nothing
        if self.__face != self.NILL:
             if self.__face == self.NORTH:
                 self.__face = self.WEST
             elif self.__face == self.WEST:
                 self.__face = self.SOUTH             
             elif self.__face == self.SOUTH:
                 self.__face = self.EAST
             elif self.__face == self.EAST:
                 self.__face = self.NORTH

    #Turn Pacman right
    def Right(self):
        #If pacman isn't placed, do nothing
        if self.__face != self.NILL:
             if self.__face == self.NORTH:
                 self.__face = self.EAST
             elif self.__face == self.EAST:
                 self.__face = self.SOUTH             
             elif self.__face == self.SOUTH:
                 self.__face = self.WEST
             elif self.__face == self.WEST:
                 self.__face = self.NORTH