from ClInput import ClInput
from FileInput import FileInput

#Print explanation on how to choose input method
print ('Wecome to Pacman!')
print ('Please select from one of the following options:')
print ('Please select from one of the following options:')
print ('1. Command line input')
print ('2. File input')

#Continue asking user for input until a correct selection is made.
while True:
    userInput = input()
    if userInput == "1":
        cl_in = ClInput()
        cl_in.execute()
        break
    elif userInput == "2":  
        fileIn = FileInput()
        fileIn.execute()
        break
    else:
        print ('Sorry, that was not a valid input.')


