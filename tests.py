# -*- coding: utf-8

from galaxySolver import Board
import unittest

class SelfSufficiantTest(unittest.TestCase):
    def testOuterShapeSimple(self):
        b = Board(4, 4)
        cells = set()
        cells.add((3, 3))
        cells.add((3, 5))
        cells.add((5, 3))
        cells.add((5, 5))


        b.addWall(2, 3)
        b.addWall(2, 5)
        b.addWall(3, 2)
        b.addWall(3, 6)
        b.addWall(5, 2)
        b.addWall(5, 6)
        b.addWall(6, 3)
        b.addWall(6, 5)


        walls = set()
        walls.add((2, 3))
        walls.add((2, 5))
        walls.add((3, 2))
        walls.add((3, 6))
        walls.add((5, 2))
        walls.add((5, 6))
        walls.add((6, 3))
        walls.add((6, 5))

        resultWalls = b.findOuterWalls(cells)
        self.assertEquals(walls, resultWalls)

    def testOuterShapeConcav(self):
        b = Board(4, 4)
        cells = set()
        cells.add((1, 1))
        cells.add((1, 3))
        cells.add((1, 5))
        cells.add((1, 7))

        cells.add((3, 1))
        cells.add((3, 7))

        cells.add((5, 1))
        cells.add((5, 7))

        cells.add((7, 1))
        cells.add((7, 3))
        cells.add((7, 5))
        cells.add((7, 7))

        b.addWall(2, 3)
        b.addWall(2, 5)
        b.addWall(3, 2)
        b.addWall(3, 6)
        b.addWall(5, 2)
        b.addWall(5, 6)
        b.addWall(6, 3)
        b.addWall(6, 5)


        walls = set()
        walls.add((2, 3))
        walls.add((2, 5))
        walls.add((3, 2))
        walls.add((3, 6))
        walls.add((5, 2))
        walls.add((5, 6))
        walls.add((6, 3))
        walls.add((6, 5))

        walls.add((0, 1))
        walls.add((0, 3))
        walls.add((0, 5))
        walls.add((0, 7))

        walls.add((1, 0))
        walls.add((1, 8))
        walls.add((3, 0))
        walls.add((3, 8))
        walls.add((5, 0))
        walls.add((5, 8))
        walls.add((7, 0))
        walls.add((7, 8))

        walls.add((8, 1))
        walls.add((8, 3))
        walls.add((8, 5))
        walls.add((8, 7))

        resultWalls = b.findOuterWalls(cells)
        self.assertEquals(walls, resultWalls)

    def testOuterShapeEmptyBoard(self):
        b = Board(2, 2)
        cells = set()
        cells.add((1, 1))
        cells.add((1, 3))
        cells.add((3, 1))
        cells.add((3, 3))

        walls = set()
        walls.add((0, 1))
        walls.add((0, 3))
        walls.add((1, 0))
        walls.add((1, 4))
        walls.add((3, 0))
        walls.add((3, 4))
        walls.add((4, 1))
        walls.add((4, 3))

        resultWalls = b.findOuterWalls(cells)
        self.assertEquals(walls, resultWalls)


    def testOuterShapeSingleCell(self):
        b = Board(4, 4)
        cells = set()
        cells.add((3, 3))

        b.addWall(2, 3)
        b.addWall(3, 2)
        b.addWall(3, 4)
        b.addWall(4, 3)

        walls = set()
        walls.add((2, 3))
        walls.add((3, 2))
        walls.add((3, 4))
        walls.add((4, 3))

        resultWalls = b.findOuterWalls(cells)
        self.assertEquals(walls, resultWalls)

    def testOuterShapeEmptyBoardDumbWall(self):
        b = Board(2, 2)
        cells = set()
        cells.add((1, 1))
        cells.add((1, 3))
        cells.add((3, 1))
        cells.add((3, 3))

        b.addWall(1, 2) # A wall that doesn't frontier the shape

        walls = set()
        walls.add((0, 1))
        walls.add((0, 3))
        walls.add((1, 0))
        walls.add((1, 4))
        walls.add((3, 0))
        walls.add((3, 4))
        walls.add((4, 1))
        walls.add((4, 3))

        resultWalls = b.findOuterWalls(cells)
        self.assertEquals(walls, resultWalls)

    def testOuterShapeEmptyBoardFrontieringShape(self):
        b = Board(2, 2)
        cells = set()
        cells.add((1, 1))
        cells.add((1, 3))
        cells.add((3, 1))
        cells.add((3, 3))

        b.addWall(1, 2) # 2 walls that make another shape near the first one
        b.addWall(2, 3)

        walls = set()
        walls.add((0, 1))
        walls.add((0, 3))
        walls.add((1, 0))
        walls.add((1, 4))
        walls.add((3, 0))
        walls.add((3, 4))
        walls.add((4, 1))
        walls.add((4, 3))

        resultWalls = b.findOuterWalls(cells)
        self.assertEquals(walls, resultWalls)

    def testOuterShapeComplex(self):
        b = Board(4, 4)

    def testShapeInEmptyBoard(self):
        expected = set()
        expected.add((1, 1))
        expected.add((1, 3))
        expected.add((3, 1))
        expected.add((3, 3))
        b = Board(2,2)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))

    def testShapeInEmptyBoardWithFakeWall(self):
        expected = set()
        expected.add((1, 1))
        expected.add((1, 3))
        expected.add((3, 1))
        expected.add((3, 3))
        b = Board(2,2)
        b.addWall(1, 2)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))

    def testLittleShape(self):
        expected = set()
        expected.add((1, 1))
        expected.add((3, 1))
        b = Board(2,2)
        b.addWall(1, 2)
        b.addWall(3, 2)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))

    def testMonoCellShape(self):
        expected = set()
        expected.add((1, 1))
        b = Board(2,2)
        b.addWall(1, 2)
        b.addWall(2, 1)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))

    def testFindComplexShape(self):
        expected = set()
        expected.add((1, 1))
        expected.add((1, 3))
        expected.add((1, 5))
        expected.add((1, 7))
        b = Board(4,4)
        b.addWall(2, 1)
        b.addWall(2, 3)
        b.addWall(2, 5)
        b.addWall(2, 7)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))

    def testFindComplexShape2(self):
        expected = set()
        expected.add((1, 1))
        expected.add((1, 3))
        expected.add((1, 5))
        expected.add((1, 7))
        expected.add((3, 5))
        expected.add((3, 7))
        expected.add((5, 5))
        expected.add((5, 7))
        expected.add((7, 5))
        expected.add((7, 7))
        b = Board(4,4)
        b.addWall(2, 1)
        b.addWall(2, 3)
        b.addWall(3, 4)
        b.addWall(5, 4)
        b.addWall(7, 4)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))

    def testFindConcavShape(self):
        expected = set()
        expected.add((1, 1))
        expected.add((1, 3))
        expected.add((1, 5))
        expected.add((1, 7))

        expected.add((3, 7))
        expected.add((5, 7))
        expected.add((7, 7))

        expected.add((7, 5))
        expected.add((7, 3))
        expected.add((7, 1))

        expected.add((5, 1))
        expected.add((3, 1))
        expected.add((1, 1))

        b = Board(4,4)
        b.addWall(2, 3)
        b.addWall(2, 5)
        b.addWall(3, 6)
        b.addWall(5, 6)
        b.addWall(6, 5)
        b.addWall(6, 3)
        b.addWall(5, 2)
        b.addWall(3, 2)

        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))
        self.assertEquals(expected, b.findShapeAroundCell(7, 7, set()))

    def testFindCutConcavShape(self):
        expected = set()
        expected.add((1, 1))
        expected.add((1, 3))
        expected.add((1, 5))
        expected.add((1, 7))

        expected.add((3, 7))
        expected.add((5, 7))

        expected.add((7, 5))
        expected.add((7, 3))
        expected.add((7, 1))

        expected.add((5, 1))
        expected.add((3, 1))
        expected.add((1, 1))

        b = Board(4,4)
        b.addWall(2, 3)
        b.addWall(2, 5)
        b.addWall(3, 6)
        b.addWall(5, 6)
        b.addWall(6, 5)
        b.addWall(6, 3)
        b.addWall(5, 2)
        b.addWall(3, 2)

        b.addWall(7, 6)
        b.addWall(6, 7)
        self.assertEquals(expected, b.findShapeAroundCell(1, 1, set()))
        expected2 = set()
        expected2.add((7, 7))
        self.assertEquals(expected2, b.findShapeAroundCell(7, 7, set()))

    def testAdjacentCells11(self):
        b = Board(2, 2)
        expected = set()
        expected.add((3, 1))
        expected.add((1, 3))
        self.assertEquals(expected, b.adjacentCells(1, 1))

    def testAdjacentCellsCentral(self):
        b = Board(4, 4)
        expected = set()
        expected.add((5, 1))
        expected.add((5, 5))
        expected.add((3, 3))
        expected.add((7, 3))
        self.assertEquals(expected, b.adjacentCells(5, 3))

    def testAdjacentCellsOutOfBound(self):
        b = Board(4, 4)
        expected = set()
        expected.add((5, 7))
        expected.add((7, 5))
        self.assertEquals(expected, b.adjacentCells(7, 7))

    def testAdjacentCellsCrossing(self):
        b = Board(4, 4)
        expected = set()
        self.assertEquals(expected, b.adjacentCells(7, 6))

    def testAdjacentCellsAsym(self):
        b = Board(4, 4)
        expected = set()
        expected.add((7, 3))
        expected.add((7, 7))
        expected.add((5, 5))
        self.assertEquals(expected, b.adjacentCells(7, 5))

    def testAdjacentCellsCentralWithWall(self):
        b = Board(4, 4)
        expected = set()
        expected.add((5, 5))
        expected.add((3, 3))
        expected.add((7, 3))
        b.addWall(5, 2)
        self.assertEquals(expected, b.adjacentCells(5, 3))

    def testAdjacentCellsCentralWithWall(self):
        b = Board(2, 2)
        expected = set()
        expected.add((3, 1))
        b.addWall(1, 2)
        b.addWall(3, 2)
        self.assertEquals(expected, b.adjacentCells(1, 1))

    def testFillBoardDumb(self):
        b = Board(7, 7)
        b.fillBoard("7x7:abbbccxhh") # 14 dots
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
        b.fillBoard("7x7:hiinifpzkeqbsh") # 14 dots
        self.assertEqual(
            """  0 1 2 3 4 5 6 j
 +-+-+-+-+-+-+-+
0|       o     |
 + + # + + + +o+
1|             |
 +o+ + + + # + +
2|  o          |
 + + + # + + + +
3|             |
 + + + + + + + +
4|  o    o     |
 + + + + + + # +
5|o            |
 + + + +o+ + + +
6| o           |
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
        b.addWall(1, 2)
        self.assertTrue(b.isWall(1, 2))
        self.assertFalse(b.isWall(1, 4))
        self.assertFalse(b.isWall(2, 1))
        self.assertFalse(b.isDot(1, 3))
        b.addWall(0, 1)
        self.assertTrue(b.isWall(0, 1))
        self.assertTrue(b.isWall(1, 2))
        self.assertFalse(b.isWall(1, 4))
        self.assertFalse(b.isWall(2, 1))
        self.assertFalse(b.isDot(1, 3))

    def testWallsAroundCentralCell(self):
        b = Board(4,4)
        expected = set()
        expected.add((0, 1))
        expected.add((1, 0))
        self.assertEquals(b.wallsAroundCell(1, 1), expected)

    def testWallsAround00Cell(self):
        b = Board(4,4)
        expected = set()
        self.assertEquals(b.wallsAroundCell(0, 0), expected)

    def testWallsAroundSomeWalledCell(self):
        b = Board(4,4)
        expected = set()
        b.addWall(4, 5)
        expected.add((4, 5))
        self.assertEquals(b.wallsAroundCell(5, 5), expected)

    def testWallsAroundSomeFullyWalledCell(self):
        b = Board(4,4)
        expected = set()
        b.addWall(4, 5)
        b.addWall(6, 5)
        b.addWall(5, 4)
        b.addWall(5, 6)

        expected.add((4, 5))
        expected.add((6, 5))
        expected.add((5, 4))
        expected.add((5, 6))
        self.assertEquals(b.wallsAroundCell(5, 5), expected)

    def testWallsAroundSomeFullyWalledCellAsym(self):
        b = Board(4,4)
        expected = set()
        b.addWall(2, 5)
        b.addWall(4, 5)
        b.addWall(3, 4)
        b.addWall(3, 6)
        expected.add((2, 5))
        expected.add((4, 5))
        expected.add((3, 4))
        expected.add((3, 6))
        self.assertEquals(b.wallsAroundCell(3, 5), expected)


    def testEdgessAround00Cell(self):
        b = Board(4,4)
        expected = set()
        expected.add((0, 1))
        expected.add((1, 0))
        expected.add((2, 1))
        expected.add((1, 2))
        self.assertEquals(b.edgesAroundCell(1, 1), expected)

    def testEdgesAroundCentralCell(self):
        b = Board(4,4)
        expected = set()
        expected.add((2, 3))
        expected.add((3, 4))
        expected.add((5, 4))
        expected.add((6, 3))
        expected.add((5, 2))
        expected.add((3, 2))
        result = b.edgesAroundCell(4, 3)
        self.assertEquals(result, expected)
        self.assertEquals(len(result), len(expected))

    def testEdgesAroundAsymCell(self):
        b = Board(4,4)
        expected = set()
        expected.add((1, 0))
        expected.add((0, 1))
        expected.add((0, 3))
        expected.add((1, 4))
        expected.add((2, 3))
        expected.add((2, 1))
        result = b.edgesAroundCell(1, 2)
        self.assertEquals(result, expected)
        self.assertEquals(len(result), len(expected))


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

    def testAddDotIsNotDash(self):
        b = Board(4, 4)
        b.addDot(2, 2)
        b.addDot(2, 1)
        self.assertEqual("""  0 1 2 3 j
 +-+-+-+-+
0|       |
 +o# + + +
1|       |
 + + + + +
2|       |
 + + + + +
3|       |
 +-+-+-+-+
i
""", b.toString())

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
        self.assertFalse(b.isWall(2, 1))
        b.addWall(2, 1)
        self.assertTrue(b.isWall(2, 1))
        self.assertFalse(b.isWall(1, 2))
        b.addWall(1, 2)
        self.assertTrue(b.isWall(2, 1))
        self.assertTrue(b.isWall(1, 2))


    def testDotOnEdge(self):
        b = Board(2,2)
        b.addDot(3, 2)
#        print b.toString()


    def testDotOnWall(self):
        b = Board(2,2)
        b.addWall(1, 2)
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

    def testSymetricCell(self):
        b = Board(4, 4)
        self.assertEquals(b.symetricCell(1, 1, 1, 2), {"i": 1,"j":3})
        self.assertEquals(b.symetricCell(1, 1, 3, 3), {"i": 5,"j":5})

if __name__ == "__main__":
    unittest.main()
    exit (0)
