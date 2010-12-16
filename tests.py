# -*- coding: utf-8

from galaxySolver import Board
import unittest

#class OtherTests(unittest.TestCase):
class OtherTests():
    def testFillBoardDumb(self):
        b = Board(7, 7)
        return
        b.fillBoard("7x7:ab") # 14 dots 
#        b.fillBoard("7x7:abbbccxhh") # 14 dots 
        print
        print b.toString()
        return
        self.assertEqual(
            """  0 1 2 3 4 5 6 j
 +-+-+-+-+-+-+-+
0|o o o o  o  o|
 + + + + + + + +
1|          o  |
 + + + # + + + +
2|o            |
 + + + + + + + +
3|             |
 + + + + + + + +
4|             |
 + + + + + + + +
5|             |
 + + + + + + + +
6|             |
 +-+-+-+-+-+-+-+
i
""", b.toString())


class SelfSufficiantTest(unittest.TestCase):
    def testFillBoardDumb(self):
        b = Board(7, 7)
        return
        b.fillBoard("7x7:abbbccxh") # 14 dots 
        self.assertEqual(
            """  0 1 2 3 4 5 6 j
 +-+-+-+-+-+-+-+
0|o o o o  o  o|
 + + + + + + + +
1|          o  |
 + + + # + + + +
2|             |
 + + + + + + + +
3|             |
 + + + + + + + +
4|             |
 + + + + + + + +
5|             |
 + + + + + + + +
6|             |
 +-+-+-+-+-+-+-+
i
""", b.toString())

    def testFillBoardDumb(self):
        b = Board(7, 7)
        return
        b.fillBoard("7x7:abbbccxhh") # 14 dots 
        print
        print b.toString()
        return
        self.assertEqual(
            """  0 1 2 3 4 5 6 j
 +-+-+-+-+-+-+-+
0|o o o o  o  o|
 + + + + + + + +
1|          o  |
 + + + # + + + +
2|o            |
 + + + + + + + +
3|             |
 + + + + + + + +
4|             |
 + + + + + + + +
5|             |
 + + + + + + + +
6|             |
 +-+-+-+-+-+-+-+
i
""", b.toString())


    def testFillBoardReal(self):
        b = Board(7, 7)
#        b.fillBoard("7x7:hiinifpzkeqbsh") # 14 dots
        return
        b.fillBoard("7x7:hiin") # 14 dots
        print
        print b.toString()
        return
        self.assertEqual(
            """  0 1 2 3 4 5 6 j
 +-+-+-+-+-+-+-+
0|o o o o  o  o|
 + + + + + + + +
1|          o  |
 + + + # + + + +
2|             |
 + + + + + + + +
3|             |
 + + + + + + + +
4|             |
 + + + + + + + +
5|             |
 + + + + + + + +
6|             |
 +-+-+-+-+-+-+-+
i
""", b.toString())


    def testEmptyBoardPossibleDots(self):
        expectedCells = []
        expectedCells.append({"i":1, "j":1})
        expectedCells.append({"i":1, "j":2})
        expectedCells.append({"i":1, "j":3})
        expectedCells.append({"i":2, "j":1})
        expectedCells.append({"i":2, "j":2})
        expectedCells.append({"i":2, "j":3})
        expectedCells.append({"i":3, "j":1})
        expectedCells.append({"i":3, "j":2})
        expectedCells.append({"i":3, "j":3})
        b = Board(2,2)
        i = 0
        for c in b.dotsPossiblePlaces():
            self.assertEquals(c, expectedCells[i])
            i = i + 1

    def testPosPlusOffsetLineOverflow(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(3, 2, 6), {"i": 4, "j": 1})

    def testPosPlusZero(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(3, 2, 0), {"i": 3, "j": 2})

    def testPosPlusOffsetLineInnerBorder(self):
        b = Board(3, 3)
        self.assertEquals(b._posPlusOffset(1, 5, 1), {"i": 2, "j": 1})

    def testPosPlusOffsetExactOverflow(self):
        b = Board(3, 3)
        self.assertEquals(b._posPlusOffset(1, 5, 6), {"i": 3, "j": 1})

    def testPosPlusOffsetOutOfRange(self):
        b = Board(2, 2)
        self.assertEquals(b._posPlusOffset(1, 1, 10), None)

    def testPosPlusOffsetOutOfRangeBorder(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 49), None)

    def testPosPlusOffset(self):
        b = Board(2, 2)
        self.assertEquals(b._posPlusOffset(1, 1, 3), {"i": 2,"j": 1})

    def testPosPlusOffsetWIthinColumn(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 4), {"i": 1,"j": 5})

    def testPosPlusOffsetMultiColumn(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 7), {"i": 2,"j": 1})

    def testPosPlusOffsetCellToWall(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 1), {"i": 1,"j": 2})

    def testPosPlusOffsetCellToCrossing(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(2, 1, 1), {"i": 2,"j": 2})

    def testPosPlusOffsetWholeBoard(self):
        b = Board(4, 4)
        self.assertEquals(b._posPlusOffset(1, 1, 48), {"i": 7,"j": 7})

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
        self.assertFalse(b.cellIsWithinBoard(1, 10))

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
 + # + + +
1|       |
 + + + + +
2|       |
 + + + + +
3|       |
 +-+-+-+-+
i
""", b.toString())


    def testToStringOnCrossing(self):
        b = Board(4, 4)
        b.addDot(2, 2)
        b.addDot(3, 3)
        self.assertEqual(
            """  0 1 2 3 j
 +-+-+-+-+
0|       |
 + # + + +
1|  o    |
 + + + + +
2|       |
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
        expectedDots.append({"i":0, "j":0})
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
        b.addDot(3, 2)
#        print b.toString()


    def testDotOnWall(self):
        b = Board(2,2)
        b.addWallShort(1, 2)
        b.addDot(1, 2)
        self.assertEquals(
            """  0 1 j
 +-+-+
0| ø |
 + + +
1|   |
 +-+-+
i
""", b.toString())


    def testAddDotOnCrossing(self):
        b = Board(4, 4)
        b.addDot(4, 4)
        self.assertTrue(b.isDot(4, 4))

    def testFloats(self):
        b = Board(4, 4)
        self.assertTrue(b.cellIsWithinBoard(1, 1))
        b.addDot(3, 5)
        self.assertTrue(b.cellContainsDot(3, 5))

    def testCellIsFilledByOnlyOneDotOnItsEdge(self):
        b = Board(4, 4)
        b.addDot(3, 2)
        self.assertTrue(b.cellContainsDot(2, 2))
        self.assertTrue(b.cellContainsDot(3, 1))
        self.assertTrue(b.cellContainsDot(3, 3))
        self.assertTrue(b.cellContainsDot(4, 1))

    def testCellCanBelongToDotFullCells(self):
        b = Board(4, 4)
        b.addDot(1, 2)
        self.assertTrue(b.cellCanBelongToDot(1, 1, 1, 2))

        b.addDot(2, 2)
        self.assertFalse(b.cellCanBelongToDot(0, 2, 1, 2))

    def testCellCanBelongToDotOutOfBoard(self):
        b = Board(4, 4)
        b.addDot(7, 7)
        self.assertFalse(b.cellCanBelongToDot(0, 0, 7, 7))
        self.assertFalse(b.cellCanBelongToDot(0, 0, 0, 6))

    def testCellCanBelongToDotEdged(self):
        b = Board(4, 4)
        b.addDot(1, 2)
        self.assertTrue(b.cellCanBelongToDot(1, 1, 1, 2))
        b.addDot(1, 4)
        self.assertFalse(b.cellCanBelongToDot(1, 1, 1, 2))

    def testCanPutDotOutOfBounds(self):
        b = Board(2, 2)
        self.assertFalse(b._canPutDot(-1, 0))
        self.assertFalse(b._canPutDot(2, -1))
        self.assertFalse(b._canPutDot(4, 0))
        self.assertFalse(b._canPutDot(1, 4))
        self.assertTrue(b._canPutDot(1, 2))

    def testCanPutDotAroundDots(self):
        b = Board(4, 4)
        self.assertTrue(b._canPutDot(1, 2))
        b.addDot(1, 2)
        self.assertFalse(b._canPutDot(1, 2))
        self.assertTrue(b._canPutDot(4, 3))

    def testCanPutDotAroundBorders(self):
        b = Board(4, 4)
        self.assertFalse(b._canPutDot(1, 0))
        self.assertTrue(b._canPutDot(1, 1))
        self.assertTrue(b._canPutDot(1, 2))
        self.assertTrue(b._canPutDot(1, 3))
        self.assertTrue(b._canPutDot(1, 4))
        self.assertTrue(b._canPutDot(1, 5))
        self.assertTrue(b._canPutDot(1, 6))
        self.assertTrue(b._canPutDot(1, 7))
        self.assertFalse(b._canPutDot(1, 8))

    def testCellContainsDotExcept(self):
        b = Board(4, 4)
        b.addDot(3, 3)
        self.assertFalse(b.cellContainsDotExcept(3, 3, 3, 3))
        self.assertTrue(b.cellContainsDotExcept(3, 3, 3, 2))


if __name__ == "__main__":
    unittest.main()
    exit (0)
