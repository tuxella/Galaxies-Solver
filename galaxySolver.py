# -*- coding: utf-8

"""
A dot is the representant of every cells around it that form its shape.
A cell can belong to a shape if the symetric cell on the other side of the dot:
    - Is within the limits of the board
    - Doesn't have a dot inside or on any of its edges
"""

"""
"""
cellExample = {"x" : 0, "y" : 0}

class board(object):
    def __init__(self, width, height):
        """
        Creates the object from its width and height.
        This attributes are given in number of cells, begining at 1 (no mono-dimentional boards)
        """
        self._width = width
        self._height = height
        self.board = []
        for i in range(0, 2 * width + 1):
            self.board.append([])
            for j in range(0, 2 * height + 1):
                if ((0 == (j % 2)) and (0 == (i % 2))):
                    self.board[i].append("+")
                    continue
                if ((0 == i) or (2 * width == i)):
                    self.board[i].append("-")
                    continue
                if (0 == j) or (2 * height == j):
                    self.board[i].append("|")
                    continue
                if (0 == (j % 2)):
                    self.board[i].append(" ")
                    continue
                if (0 == (i % 2)):
                    self.board[i].append(" ")
                    continue
                self.board[i].append(" ")

    def toString(self):
        ret = " "
        ret = ret + ""
        for j in range(0, len(self.board[0])):
            if (0 <> (j % 2)):
                ret = ret + "%d" % ((j - 1) / 2)
            else:
                ret = ret + " "
        ret = ret + "j\n"
        for i in range(0, len(self.board)):
            if (0 <> (i % 2)):
                ret = ret + "%d" % ((i - 1) / 2)
            else:
                ret = ret + " "
            for j in range(0, len(self.board[i])):
                ret = ret + self.board[i][j]
#        print self.board
            ret = ret + "\n"
        ret = ret + "i\n"
        return ret

    def addDot(self, i, j):
 #       print "addDot(%d, %d)" % (i, j)
        self.board[i * 2 + 1][j * 2 + 1] = "o"

    def addWall(self, i, j, orientation):
        """
        Orientation = h or v (horizontal or vertical)
        If horizontal : i = row number after which create the wal
        If vertical : i = row number after which create the wall
        j = the nth wall to add (1, 2, 3 ...)
        """
#        print "addWall(%d, %d) : %s" % (i, j, orientation)
        if ("h" == orientation):
            self.board[i * 2][j * 2 - 1] = "-"
        if ("v" == orientation):
            self.board[i * 2 - 1][j * 2] = "|"

    def _createPossibleBelongingsGraph(self):
        """
        For each cell, every dots it can belong to
        """
    def _cellContainsDot(self, i, j):
#        print "cellContainsDot : cell = (%d, %d)" % (i, j)
        if ("o" == self.board[2 * i + 1][2 * j + 1]):
            return True
        return False

    def _symetricCell(self, ci, cj, centerI, centerJ):
        return {"i":centerI + (centerI - ci), "j":centerJ + (centerJ - cj)}

    def cellIsWithinBoard(self, i, j):
        if ((i < 0) or (j < 0)):
            return False
        if ((i >= self._width) or (j >= self._height)):
            return False
        return True

    def cellCanBelongToDot(self,ci, cj, di, dj):
        """
        True if the cell on the oposite side of the dot:
            - belongs to the board
            - doesn't contain a dot
            - isn't edged by a dot
        """
        print "cellCanBelongToDot : cell = (%d, %d) dot = (%d, %d)" % (ci, cj, di, dj)
        cellToDoti = di - ci
        cellToDotj = dj - cj
        sPoint = self._symetricCell(ci, cj, di, dj)
        si = sPoint["i"]
        sj = sPoint["j"]
        print "Symetric point : (%d, %d)" % (si, sj)
        if ((si < 0) or (sj < 0)):
            return False
        if ((si > self._width) or (sj > self._height)):
            return False
        if (self._cellContainsDot(si, sj)):
            return False

        return True
    def dots(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if ("o" == self.board[i][j]):
                    yield {"i":i, "j":j}

    def cells(self):
        for i in range(1, len(self.board), 2):
            for j in range(1, len(self.board[i]), 2):
                yield {"i":i, "j":j}
    def isSolved(self):
        return False

import unittest

class SelfSufficiantTest(unittest.TestCase):

    def testIsCellWithin(self):
        b = board(4, 4)
        self.assertTrue(b.cellIsWithinBoard(0, 0))
        self.assertTrue(b.cellIsWithinBoard(1, 1))
        self.assertTrue(b.cellIsWithinBoard(2, 2))
        self.assertTrue(b.cellIsWithinBoard(3, 3))
        self.assertFalse(b.cellIsWithinBoard(-1, 1))
        self.assertFalse(b.cellIsWithinBoard(1, 4))

    def testAddDotWithinBounds(self):
        b = board(4, 4)
        b.addDot(2, 2)

    def testToString(self):
        b = board(4, 4)
        b.addDot(2, 2)
        self.assertEqual(
            """  0 1 2 3 j
 +-+-+-+-+
0|       |
 + + + + +
1|       |
 + + + + +
2|    o  |
 + + + + +
3|       |
 +-+-+-+-+
i
""", b.toString())



if __name__ == "__main__":
    unittest.main()
    exit (0)


myBoard = board(4,4)
#myBoard.board[3][3] = "o"


myBoard.addDot(1, 0)
myBoard.addDot(1, 1)
myBoard.addDot(2, 2)
myBoard.addWall(1, 1, "h")
myBoard.addWall(1, 2, "h")
myBoard.addWall(1, 3, "h")
myBoard.addWall(1, 1, "v")
myBoard.addWall(1, 2, "v")
myBoard.addWall(1, 3, "v")



myBoard.pprint()

#print myBoard.cellCanBelongToDot(1, 1, 1, 0)
#print myBoard.cellCanBelongToDot(2, 2, 1, 1)
#print myBoard.cellCanBelongToDot(1, 1, 1, 0)
print myBoard.cellCanBelongToDot(0, 0, 1, 1)

#print myBoard._cellContainsDot(1, 0)
#print myBoard._cellContainsDot(1, 1)
#print myBoard._cellContainsDot(2, 2)
#print myBoard._cellContainsDot(2, 3)
#print myBoard._cellContainsDot(3, 3)



#myBoard.addWall(0, 0, "v")



"""
Example of a board (7 x 7):
c = cell
o = dot
| or - = edge
. : no edge
+ = empty (nothing can be put at the crossing of 2 edges)

+ - + - + - +
|   | c |   |
+ - + - + - +
|   | o |   |
+ - + - + - +
|   |   |   |
+ - + - + - +


Positions : 
+ - + - + - +
|0,0.   .   |
+ . + . + . +
|1,0.   .   |
+ . + . + . +
|   .   .   |
+ - + - + - +

"""
