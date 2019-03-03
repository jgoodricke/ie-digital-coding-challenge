from CommandInput import CommandInput

class ClInput(CommandInput):
    """Reads commands via command line from user."""

    #Read and execute commands from user input
    def execute(self):
        userIn = ""
        output = ""
        
        self.__explanation()

        while userIn != "QUIT":
            userIn = input()
            output = super()._execute(userIn)

            if output != "":
                print (output)
    
    #Print explanation to user on how to enter commands
    def __explanation(self):
        print ('Here are the commands you can enter:')
        print ('PLACE X,Y,Dirction - Places Pacman on the grid (e.g. PLACE 3,3,NORTH).')
        print ('MOVE - Moves Pacman forward.')
        print ('LEFT - Turns Pacman left.')
        print ('RIGHT - Turns Pacman right.')
        print ('REPORT - Tells you where Pacman is on the grid.')
        print ('QUIT - Stop playing.')