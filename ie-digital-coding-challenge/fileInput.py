from commandInput import CommandInput

class FileInput(CommandInput):
    """Reads input commands from file."""
    
    #Read file line by line and execute commands
    def execute(self):
        output = ""

        self.__explanation()
        f = open("input.txt", "r")
        if f.mode == 'r':
            fLines = f.readlines()
            for x in fLines:
                x=x.rstrip()
                print(x)
                output = super()._execute(x)

                if output != "":
                    print (output)
    
    #Prints explanation to command line on how to use file input
    def __explanation(self):
        print ('Place your input file "input.txt" with the Pacman executable file')
        input("Press Enter when you are ready...")