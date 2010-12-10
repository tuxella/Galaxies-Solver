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
    _wallS="-|ø"
    _dotS="oø"
    _wallv = "|"
    _wallh = "-"
    _wallDot = "ø"
    _dotCell = "o"
    _dotWall = "ø"
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
            ret = ret + "\n"
        ret = ret + "i\n"
        return ret

    def addDot(self, i, j):
 #       print "addDot(%d, %d)" % (i, j)
        #integerIfied positions
        ii = int(i * 2 + 1)
        ij = int(j * 2 + 1)
        assert not ((ii == ij) and (0 == ii % 2) and (0 == ij % 2)), "It is not possible to create a dot on an intersection (%d, %d)" % (ii, ij)
        if self.isWall(ii, ij):
            self.board[ii][ij] = self._dotWall
        else:
            self.board[ii][ij] = self._dotCell

    def addWall(self, i, j, orientation):
        """
        Orientation = h or v (horizontal or vertical)
        If horizontal : i = row number after which create the wal
        If vertical : i = row number after which create the wall
        j = the nth wall to add (1, 2, 3 ...)
        """
#        print "addWall(%d, %d) : %s" % (i, j, orientation)
        if self.isWall(i * 2 + 1, j * 2 + 1):
            self.board[i * 2 + 1][j * 2 + 1] = self._dotWall
        else:
            self.board[i * 2 + 1][j * 2 + 1] = self._dotCell

        if ("h" == orientation):
            if self.isDot(i * 2, j * 2 - 1):
                self.board[i * 2][j * 2 - 1] = self._dotWall
            else:
                self.board[i * 2][j * 2 - 1] = self._wallh
        if ("v" == orientation):
            if self.isDot(i * 2 - 1, j * 2):
                self.board[i * 2 - 1][j * 2] = self._dotWall
            else:
                self.board[i * 2 - 1][j * 2] = self._wallv

    def _createPossibleBelongingsGraph(self):
        """
        For each cell, every dots it can belong to
        """
    def cellContainsDot(self, i, j):
#        print "cellContainsDot : cell = (%d, %d)" % (i, j)
        if self.isDot(2 * i + 1, 2 * j + 1):
            return True

        if self.isDot(2 * i    , 2 * j + 1):
            return True
        if self.isDot(2 * i + 2, 2 * j + 1):
            return True
        if self.isDot(2 * i + 1, 2 * j    ):
            return True
        if self.isDot(2 * i + 1, 2 * j + 2):
            return True

        return False

    def symetricCell(self, ci, cj, centerI, centerJ):
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
#        print "cellCanBelongToDot : cell = (%d, %d) dot = (%d, %d)" % (ci, cj, di, dj)
        cellToDoti = di - ci
        cellToDotj = dj - cj
        sPoint = self.symetricCell(ci, cj, di, dj)
        si = sPoint["i"]
        sj = sPoint["j"]
        if not self.cellIsWithinBoard(si, sj):
            return False
        if (self.cellContainsDot(si, sj)):
            return False

        return True

    def isWall(self, i, j):
        ii = int(i)
        ij = int(j)
        if self.board[ii][ij] in self._wallS:
            return True
        return False

    def isDot(self, i, j):
        ii = int(i)
        ij = int(j)
        if self.board[ii][ij] in self._dotS:
            return True
        return False

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

    def testEmptyBoardIsNotSolved(self):
        b = board(4, 4)
        b.addDot(1, 1)
        self.assertFalse(b.isSolved())

    def testMinimalSolvedBoard(self):
        b = board(3, 3)
        b.addDot(1, 1)
#        self.assertTrue(b.isSolved())

    def testEmptyBoardCells(self):
        expectedCells = []
        expectedCells.append({"i":1, "j":1})
        expectedCells.append({"i":1, "j":3})
        expectedCells.append({"i":3, "j":1})
        expectedCells.append({"i":3, "j":3})
        b = board(2,2)
        i = 0
        for c in b.cells():
            self.assertEquals(c, expectedCells[i])
            i = i + 1

    def testMinimalBoardDots(self):
        expectedDots = []
        expectedDots.append({"i":1, "j":1})
        b = board(2,2)
        b.addDot(0,0)
        i = 0
        for d in b.dots():
            self.assertEquals(d, expectedDots[i])
            i = i + 1

    def testIsWall(self):
        b = board(2,2)
        self.assertFalse(b.isWall(1, 1))
        b.addWall(1, 1, "h")
        self.assertTrue(b.isWall(2, 1))
        self.assertFalse(b.isWall(1, 2))
        b.addWall(1, 1, "v")
        self.assertTrue(b.isWall(2, 1))
        self.assertTrue(b.isWall(1, 2))

    def testDotOnEdge(self):
        b = board(2,2)
        b.addDot(1.5, 1)
#        print b.toString()


    def testDotOnWall(self):
        b = board(2,2)
        b.addDot(1.5, 1)
        self.assertEquals(
            """  0 1 j
 +-+-+
0|   |
 + + +
1|   |
 +-+ø+
i
""", b.toString())

    def testFloats(self):
        b = board(4, 4)
        self.assertTrue(b.cellIsWithinBoard(0.5, 0.5))
        b.addDot(1.5, 2.5)
        self.assertTrue(b.cellContainsDot(1.5, 2.5))


    def testCellIsFilledByOnlyOneDotOnItsEdge(self):
        b = board(4, 4)
        b.addDot(1.5, 1)
        self.assertTrue(b.cellContainsDot(1, 1))
        self.assertTrue(b.cellContainsDot(2, 1))
        self.assertFalse(b.cellContainsDot(1, 2))


    def testCellCanBelongToDotFullCells(self):
        b = board(4, 4)
        b.addDot(1, 2)
        self.assertTrue(b.cellCanBelongToDot(0, 2, 1, 2))
        b.addDot(2, 2)
        self.assertFalse(b.cellCanBelongToDot(0, 2, 1, 2))

    def testCellCanBelongToDotOutOfBoard(self):
        b = board(4, 4)
        b.addDot(3, 3)
        self.assertFalse(b.cellCanBelongToDot(0, 0, 3, 3))
        self.assertFalse(b.cellCanBelongToDot(0, 0, 2, 0))

    def testCellCanBelongToDotEdged(self):
        b = board(4, 4)
        b.addDot(1, 2)
        print
        print b.toString()
        self.assertTrue(b.cellCanBelongToDot(0, 2, 1, 2))
        b.addDot(2, 1.5)
        self.assertFalse(b.cellCanBelongToDot(0, 2, 1, 2))

#        def cellCanBelongToDot(self,ci, cj, di, dj):
if __name__ == "__main__":
    unittest.main()
    exit (0)

