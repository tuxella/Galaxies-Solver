# -*- coding: utf-8

from galaxySolver import Board
import unittest

class SelfSufficiantTest(unittest.TestCase):

#    def testFillBoard(self):
#        b = Board(7, 7)
#        b.fillBoard("7x7:bfzecdzdujfewjij")

    def testEmptyBoardPossibleDots(self):
        expectedCells = []
        expectedCells.append({"i":1, "j":1})
        expectedCells.append({"i":1, "j":2})
        expectedCells.append({"i":1, "j":3})
        expectedCells.append({"i":2, "j":1})
        expectedCells.append({"i":2, "j":3})
        expectedCells.append({"i":3, "j":1})
        expectedCells.append({"i":3, "j":2})
        expectedCells.append({"i":3, "j":3})
        b = Board(2,2)
        i = 0
        for c in b.dotsPossiblePlaces():
            self.assertEquals(c, expectedCells[i])
            i = i + 1

    def testPosPlusOffset(self):
        b = Board(2, 2)
        self.assertEquals(b._posPlusOffset(1, 1, 3), {"i": 2,"j": 1})

    def testPosPlusOffsetWIthinColumn(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 4), {"i": 1,"j": 5})

    def testPosPlusOffsetMultiColumn(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 7), {"i": 2,"j": 1})

    def testPosPlusOffsetWholeBoard(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 39), {"i": 7,"j": 7})

    def testAddWallShortForm(self):
        b = Board(4, 4)
        b.addWallShort(1, 2)
        self.assertTrue(b.isWall(1, 2))
        self.assertFalse(b.isWall(1, 4))
        self.assertFalse(b.isWall(2, 1))
        self.assertFalse(b.isDot(1, 3))
        b.addWallShort(0, 1)
        self.assertTrue(b.isWall(0, 1))
        self.assertTrue(b.isWall(1, 2))
        self.assertFalse(b.isWall(1, 4))
        self.assertFalse(b.isWall(2, 1))
        self.assertFalse(b.isDot(1, 3))

    def testAddWall(self):
        b = Board(4, 4)
        b.addWall(1, 1, "h")
        self.assertTrue(b.isWall(2, 1))

    def testWallsAroundCentralCell(self):
        b = Board(4,4)
        expected = set()
        expected.add((0, 1))
        expected.add((1, 0))
        expected.add((2, 1))
        expected.add((1, 2))
        self.assertEquals(b.wallsAroundCell(1, 1), set())

    def testWallsAround00Cell(self):
        b = Board(4,4)
        expected = set()
        expected.add((0, 1))
        expected.add((1, 0))
        self.assertEquals(b.wallsAroundCell(0, 0), expected)

    def testWallsAroundSomeWalledCell(self):
        b = Board(4,4)
        expected = set()
        b.addWallShort(4, 5)
        expected.add((4, 5))
        self.assertEquals(b.wallsAroundCell(2, 2), expected)

    def testWallsAroundSomeFullyWalledCell(self):
        b = Board(4,4)
        expected = set()
        b.addWallShort(4, 5)
        b.addWallShort(6, 5)
        b.addWallShort(5, 4)
        b.addWallShort(5, 6)

        expected.add((4, 5))
        expected.add((6, 5))
        expected.add((5, 4))
        expected.add((5, 6))
        self.assertEquals(b.wallsAroundCell(2, 2), expected)

    def testWallsAroundSomeFullyWalledCellAsym(self):
        b = Board(4,4)
        expected = set()
        b.addWallShort(2, 5)
        b.addWallShort(4, 5)
        b.addWallShort(3, 4)
        b.addWallShort(3, 6)
        expected.add((2, 5))
        expected.add((4, 5))
        expected.add((3, 4))
        expected.add((3, 6))
        self.assertEquals(b.wallsAroundCell(1, 2), expected)


    def testEdgessAround00Cell(self):
        b = Board(4,4)
        expected = set()
        expected.add((0, 1))
        expected.add((1, 0))
        expected.add((2, 1))
        expected.add((1, 2))
        self.assertEquals(b.edgesAroundCell(0, 0), expected)

    def testEdgesAroundCentralCell(self):
        b = Board(4,4)
        expected = set()
        expected.add((3, 2))
        expected.add((2, 3))
        expected.add((4, 3))
        expected.add((3, 4))
        self.assertEquals(b.edgesAroundCell(1, 1), expected)

    def testEdgesAroundAsymCell(self):
        b = Board(4,4)
        expected = set()
        expected.add((3, 4))
        expected.add((3, 6))
        expected.add((2, 5))
        expected.add((4, 5))
        self.assertEquals(b.edgesAroundCell(1, 2), expected)


    def testIsCellWithin(self):
        b = Board(4, 4)
        self.assertTrue(b.cellIsWithinBoard(0, 0))
        self.assertTrue(b.cellIsWithinBoard(1, 1))
        self.assertTrue(b.cellIsWithinBoard(2, 2))
        self.assertTrue(b.cellIsWithinBoard(3, 3))
        self.assertFalse(b.cellIsWithinBoard(-1, 1))
        self.assertFalse(b.cellIsWithinBoard(1, 4))

    def testAddDotWithinBounds(self):
        b = Board(4, 4)
        b.addDot(2, 2)

    def testToString(self):
        b = Board(4, 4)
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
        b = Board(4, 4)
        b.addDot(1, 1)
        self.assertFalse(b.isSolved())

    def testMinimalSolvedBoard(self):
        b = Board(3, 3)
        b.addDot(1, 1)
#        self.assertTrue(b.isSolved())

    def testEmptyBoardCells(self):
        expectedCells = []
        expectedCells.append({"i":1, "j":1})
        expectedCells.append({"i":1, "j":3})
        expectedCells.append({"i":3, "j":1})
        expectedCells.append({"i":3, "j":3})
        b = Board(2,2)
        i = 0
        for c in b.cells():
            self.assertEquals(c, expectedCells[i])
            i = i + 1

    def testMinimalBoardDots(self):
        expectedDots = []
        expectedDots.append({"i":1, "j":1})
        b = Board(2,2)
        b.addDot(0,0)
        i = 0
        for d in b.dots():
            self.assertEquals(d, expectedDots[i])
            i = i + 1

    def testIsWall(self):
        b = Board(2,2)
        self.assertFalse(b.isWall(1, 1))
        b.addWall(1, 1, "h")
        self.assertTrue(b.isWall(2, 1))
        self.assertFalse(b.isWall(1, 2))
        b.addWall(1, 1, "v")
        self.assertTrue(b.isWall(2, 1))
        self.assertTrue(b.isWall(1, 2))


    def testDotOnEdge(self):
        b = Board(2,2)
        b.addDot(1.5, 1)
#        print b.toString()


    def testDotOnWall(self):
        b = Board(2,2)
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
        b = Board(4, 4)
        self.assertTrue(b.cellIsWithinBoard(0.5, 0.5))
        b.addDot(1.5, 2.5)
        self.assertTrue(b.cellContainsDot(1.5, 2.5))


    def testCellIsFilledByOnlyOneDotOnItsEdge(self):
        b = Board(4, 4)
        b.addDot(1.5, 1)
        self.assertTrue(b.cellContainsDot(1, 1))
        self.assertTrue(b.cellContainsDot(2, 1))
        self.assertFalse(b.cellContainsDot(1, 2))

    def testCellCanBelongToDotFullCells(self):
        b = Board(4, 4)
        b.addDot(1, 2)
        self.assertTrue(b.cellCanBelongToDot(0, 2, 1, 2))
        b.addDot(2, 2)
        self.assertFalse(b.cellCanBelongToDot(0, 2, 1, 2))

    def testCellCanBelongToDotOutOfBoard(self):
        b = Board(4, 4)
        b.addDot(3, 3)
        self.assertFalse(b.cellCanBelongToDot(0, 0, 3, 3))
        self.assertFalse(b.cellCanBelongToDot(0, 0, 2, 0))

    def testCellCanBelongToDotEdged(self):
        b = Board(4, 4)
        b.addDot(1, 2)
        self.assertTrue(b.cellCanBelongToDot(0, 2, 1, 2))
        b.addDot(2, 1.5)
        self.assertFalse(b.cellCanBelongToDot(0, 2, 1, 2))



if __name__ == "__main__":
    unittest.main()
    exit (0)
