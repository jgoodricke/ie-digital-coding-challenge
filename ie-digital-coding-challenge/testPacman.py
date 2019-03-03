import unittest
from Pacman import Pacman

class Test_testPacman(unittest.TestCase):
    #-------
    #Placing
    #-------
    def test_Place(self):
        expected = "3,3,NORTH"
        pac = Pacman()
        pac.Place(3,3,pac.NORTH)
        self.assertEqual(pac.Report(), expected)

    #------
    #Moving
    #------
    #Base Test Method for Moving, called by other moving tests
    def moveTest(self, expected, pac, face):
        pac.Place(3,3,face)
        pac.Move()
        self.assertEqual(pac.Report(), expected)          

    #Moving north
    def test_MoveNorth(self):
        pac = Pacman()
        self.moveTest("3,4,NORTH", pac,  pac.NORTH)

    #Moving south
    def test_MoveSouth(self):
        pac = Pacman()
        self.moveTest("3,2,SOUTH", pac, pac.SOUTH)
   
    #Moving east
    def test_MoveEast(self):
        pac = Pacman()
        self.moveTest("4,3,EAST", pac, pac.EAST)

    #Moving west
    def test_MoveWest(self):
        pac = Pacman()
        self.moveTest("2,3,WEST", pac, pac.WEST)

    #------------
    #Turning Left
    #------------
    #Base test for turning left, called by other classes
    def turnLeftTest(self, expected, pac, face):
        pac.Place(3,3,face)
        pac.Left()
        self.assertEqual(pac.Report(), expected) 
    
    #Turning Left Facing North
    def test_TurnLeftNorth(self):
        pac = Pacman()
        self.turnLeftTest("3,3,WEST", pac, pac.NORTH)
    
    #Turning Left Facing WEST
    def test_TurnLeftWest(self):
        pac = Pacman()
        self.turnLeftTest("3,3,SOUTH", pac, pac.WEST)

    #Turning Left Facing SOUTH
    def test_TurnLeftSouth(self):
        pac = Pacman()
        self.turnLeftTest("3,3,EAST", pac, pac.SOUTH)

    #Turning Left Facing EAST
    def test_TurnLeftEast(self):
        pac = Pacman()
        self.turnLeftTest("3,3,NORTH", pac, pac.EAST)

    #------------
    #Turning Right
    #------------
    #Base test for turning left, called by other classes
    def turnRightTest(self, expected, pac, face):
        pac.Place(3,3,face)
        pac.Right()
        self.assertEqual(pac.Report(), expected) 
    
    #Turning Left Facing North
    def test_TurnRightNorth(self):
        pac = Pacman()
        self.turnRightTest("3,3,EAST", pac, pac.NORTH)
    
    #Turning Left Facing EAST
    def test_TurnRightEast(self):
        pac = Pacman()
        self.turnRightTest("3,3,SOUTH", pac, pac.EAST)

    #Turning Left Facing SOUTH
    def test_TurnRightSouth(self):
        pac = Pacman()
        self.turnRightTest("3,3,WEST", pac, pac.SOUTH)

    #Turning Left Facing WEST
    def test_TurnRightWest(self):
        pac = Pacman()
        self.turnRightTest("3,3,NORTH", pac, pac.WEST)

#--------------------------------
#Trying to Move Off Edge of Grid
#--------------------------------      
    #Moving North
    def test_moveOffNorth(self):
        expected = "3,5,NORTH"
        pac = Pacman()
        pac.Place(3,5,pac.NORTH)
        pac.Move()
        self.assertEqual(pac.Report(), expected)

    #Moving East
    def test_test_moveOffEast(self):
        expected = "5,3,EAST"
        pac = Pacman()
        pac.Place(5,3,pac.EAST)
        pac.Move()
        self.assertEqual(pac.Report(), expected)

    #Moving South
    def test_test_moveOffSouth(self):
        expected = "3,0,SOUTH"
        pac = Pacman()
        pac.Place(3,0,pac.SOUTH)
        pac.Move()
        self.assertEqual(pac.Report(), expected)

    #Moving West
    def test_test_moveOffWest(self):
        expected = "0,3,WEST"
        pac = Pacman()
        pac.Place(0,3,pac.WEST)
        pac.Move()
        self.assertEqual(pac.Report(), expected)

#--------------------------------
#Performing Actions Before PLaced
#--------------------------------
    #Turning Left before placed
    def test_failTurnLeft(self):
        expected = "NILL"
        pac = Pacman()
        pac.Left();
        self.assertEqual(pac._Pacman__face, expected)

    #Turning right before placed
    def test_failTurnRight(self):
        expected = "NILL"
        pac = Pacman()
        pac.Right();
        self.assertEqual(pac._Pacman__face, expected)

    #X Movement
    def test_failmoveX(self):
        expected = -1
        pac = Pacman()
        pac.Move()
        self.assertEqual(pac._Pacman__posX, expected)   

    #Y Movement
    def test_failMoveY(self):
        expected = -1
        pac = Pacman()
        pac.Move()
        self.assertEqual(pac._Pacman__posY, expected)

    #Report
    def test_failReport(self):
        expected = ""
        pac = Pacman()
        self.assertEqual (pac.Report(), "") 
        

if __name__ == '__main__':
    unittest.main()
