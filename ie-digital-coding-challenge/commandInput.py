from Pacman import Pacman

class CommandInput(object):
    """Interprets commands and sends them to Pacman class"""
    def __init__(self):
        self.pac = Pacman()


    #Method for interpreting inputCommand
    def _execute(self, inputCommand):
        inputCommandSplit = inputCommand.split(" ")
        #Move
        if inputCommand == "MOVE":
            self.pac.Move()
        #turn left
        elif inputCommand == "LEFT":
            self.pac.Left()
        #turn right
        elif inputCommand == "RIGHT":
            self.pac.Right()
        #report position
        elif inputCommand == "REPORT":
            return self.pac.Report()   
        #Place pacman
        elif len(inputCommandSplit) == 2 and inputCommandSplit[0] == "PLACE":
            #get coordinates
            posSplit = inputCommandSplit[1].split(",")
            #Check coordinates are correct
            if len(posSplit) == 3 and self.__isNumber(posSplit[1]) and self.__isNumber(posSplit[1]) and self.__isFacing(posSplit[2]):
                self.pac.Place(int(posSplit[0]), int(posSplit[1]), posSplit[2])
        #Return empty string by default
        return ""

    # Checks if user inputCommand for facing is valid
    def __isFacing(self, input):
        if input == self.pac.NORTH or input == self.pac.SOUTH or input == self.pac.EAST or input == self.pac.WEST:
            return True
        return False
    
    # Checks if user inputCommand for facing is valid
    def __isNumber(self, input):
        try:
            int(input)
            return True
        except ValueError:
            return False