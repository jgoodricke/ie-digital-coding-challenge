import unittest
from commandInput import CommandInput

class inputTest(unittest.TestCase):
    #Place Pacman using input
    def test_place(self):
        expected = "3,3,NORTH"
        inp = CommandInput()
        inp._execute("PLACE " + expected)
        self.assertEqual(inp._execute("REPORT"), expected)

    #Move pacman using input
    def test_move(self):
        expected = "3,4,NORTH"
        inp = CommandInput()
        inp._execute("PLACE 3,3,NORTH")
        inp._execute("MOVE")
        self.assertEqual(inp._execute("REPORT"), expected)

    #Turn left using input
    def test_turnLeft(self):
        expected = "3,3,WEST"
        inp = CommandInput()
        inp._execute("PLACE 3,3,NORTH")
        inp._execute("LEFT")
        self.assertEqual(inp._execute("REPORT"), expected)

    #Turn left using input
    def test_turnRight(self):
        expected = "3,3,EAST"
        inp = CommandInput()
        inp._execute("PLACE 3,3,NORTH")
        inp._execute("RIGHT")
        self.assertEqual(inp._execute("REPORT"), expected)

if __name__ == '__main__':
    unittest.main()
