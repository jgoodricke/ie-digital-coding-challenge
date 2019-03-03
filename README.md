# ie-digital-coding-challenge

## Decicision on Coding Language
As I have experience developing applications like this one in other languages, I decided to implement this project in Python, as it is a language that I hadn't been exposed to before. The reason for this is twofold. First, I thought it would illustrate my ability to adapt to unfamiliar coding languages and conventions. Secondly, Python is a language that I have been wanting to learn, and this project provided an ideal opportunity to explore this language developing software that I am quite familiar with already. This did prove more difficult than I initially envisioned, as Python is far removed from the C-based languages that I am familiar with, but I feel that I did an reasonable job in implementing the functionality and testing of this project. 

That said, I did rely on more simple data structures than I would normally use, as reflective of my limited exposure to this language. In particular, I forwent the use of enumeration data structures, as I was unable to get them to work with my unit testing framework. Specifically, they would return the key-value pair when called during a unit test, whereas they would only return the value during runtime. I suspect this is due to a bug in the testing framework. 

## Test Cases
### Test Case 1 – Accessing Manual and File Input 
Description: Checks if the user can access the file input and manual input interfaces correctly from the starting screen.
Module: main method
Test Steps:
Enter the command for manual and file input from the main screen
Expected Result: Successful access for both
Result: Successful access for both
Comments: 

### Test Case 2 – User Cannot Leave Start Screen withou 
Description: Check that the user cannot get past the main screen without entering a valid input
Module: main method
Test Steps: 
Enter the following commands:
3
-1
1.5
Command Line Input
True
Expected Result: Unable to pass start screen.
Result: Unable to pass start screen.

### Test Case 3 – File Input – Testing Bounds and Reporting 
Description: User will enter file input mode, and submit a file that will take Pacman clockwise to each corner of the grid (turning right), attempt to move past the end of the grid, and report. It will then move to the centre of the grid, only turning left, and report.

This will test Pacmans movement, turning and reporting abilities, as well as the restricted movement on the grid

Test Data:
PLACE 5,3,EAST
MOVE
MOVE
MOVE
REPORT
RIGHT
MOVE
MOVE
MOVE
REPORT
RIGHT
MOVE
MOVE
MOVE
REPORT
RIGHT
MOVE
MOVE
MOVE
REPORT
LEFT
LEFT
MOVE
MOVE
LEFT
MOVE
MOVE
REPORT

Test Steps: 
Copy the above data into a text file and place in the project folder. 
Start the program in file input mode

Expected Result: 
5,5,EAST
5,0,SOUTH
0,0,WEST
0,5,NORTH
3,3,EAST

Result: 
5,5,EAST
5,0,SOUTH
0,0,WEST
0,5,NORTH
3,3,EAST

### Test Case 4 – User Input – Testing Bounds and Reporting 
Description: User will enter file manual input mode, and move Pacman clockwise to each corner of the grid (turning right), attempt to move past the end of the grid, and report. It will then move to the centre of the grid, only turning left, and report. This will test Pacmans movement, turning and reporting abilities, as well as the restricted movement on the grid.

Test Steps: 
Enter the following commands:
PLACE 5,3,EAST
MOVE
MOVE
MOVE
REPORT
RIGHT
MOVE
MOVE
MOVE
REPORT
RIGHT
MOVE
MOVE
MOVE
REPORT
RIGHT
MOVE
MOVE
MOVE
REPORT
LEFT
LEFT
MOVE
MOVE
LEFT
MOVE
MOVE
REPORT

Expected Result: 
5,5,EAST
5,0,SOUTH
0,0,WEST
0,5,NORTH
3,3,EAST

Result: 
5,5,EAST
5,0,SOUTH
0,0,WEST
0,5,NORTH
3,3,EAST

### Test Case 5 – Must Place Pacman First
Description: User will enter file input mode, and load a file that runs all commands without placing Pacman first. This will ensure users can’t give Pacman commands before he is placed. The user will then repeat the commands in manual mode.

Test Steps: 
Enter the following commands:
MOVE
RIGHT
LEFT
REPORT
MOVE
RIGHT
LEFT
REPORT
PLACE 3,3,EAST
MOVE
RIGHT
RIGHT
LEFT
REPORT

Expected Result: 
File Input Mode:
(No Report)
(No Report)
4,3,SOUTH

Manual Input Mode:
(No Report)
(No Report)
4,3,SOUTH


Result: 
File Input Mode:
(No Report)
(No Report)
4,3,SOUTH

Manual Input Mode:
(No Report)
(No Report)
4,3,SOUTH


## Specifications
This application is a simulation of Pacman moving on in a grid, of dimensions 5 units x 5 units.

Description:

- The application is a simulation of Pacman moving on in a grid, of dimensions 5 units x 5 units.
- There are no other obstructions on the grid.
- Pacman is free to roam around the surface of the grid, but must be prevented from moving off the grid. Any movement that would result in Pacman moving off the grid must  be prevented, however further valid movement commands must still be allowed.
- Create an application that can read in commands of the following form -

```
PLACE X,Y,F

MOVE

LEFT

RIGHT

REPORT
```

- PLACE will put the Pacman on the grid in positon X,Y and facing NORTH,SOUTH, EAST or WEST.
- The origin (0,0) can be considered the SOUTH WEST most corner.
- The first valid command to Pacman is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command. The application should discard all commands in the sequence until a valid PLACE command has been executed.
- MOVE will move Pacman one unit forward in the direction it is currently facing.
- LEFT and RIGHT will rotate Pacman 90 degrees in the specified direction without changing the position of Pacman.
- REPORT will announce the X,Y and F of Pacman. This can be in any form, but standard output is sufficient.
- Pacman that is not on the grid can choose the ignore the MOVE, LEFT, RIGHT and REPORT commands.
- Input can be from a file, or from standard input, as the developer chooses.
- Provide test data to exercise the application.

**Constraints:**

- Pacman must not move off the grid during movement. This also includes the initial placement of Pacman.
- Any move that would cause Pacman to fall must be ignored.

Example Input and Output:
```
a)
PLACE 0,0,NORTH

MOVE

REPORT

Output: 0,1,NORTH
```
```
b)

PLACE 0,0,NORTH

LEFT

REPORT

Output: 0,0,WEST
```
```
c)

PLACE 1,2,EAST

MOVE

MOVE

LEFT

MOVE

REPORT

Output: 3,3,NORTH
```
