# -*- coding: utf-8
import re

"""
A dot is the representant of every cells around it that form its shape.
A cell can belong to a shape if the symetric cell on the other side of the dot:
    - Is within the limits of the board
    - Doesn't have a dot inside or on any of its edges
"""

class Board(object):
    _wallS="-|ø"
    _dotS="oø#"
    _wallv = "|"
    _wallh = "-"
    _wallDot = "ø"
    _dotCell = "o"
    _dotWall = "ø"
    _dotCross = "#"
    def __init__(self, width, height):
        """
        Creates the object from its width and height.
        This attributes are given in number of cells, begining at 1 (no mono-dimentional Boards)
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


    def fillBoard(self, gameDesc):
        """
        Ex: 7x7:bfzecdzdujfewjij

        Extract from the source of galaxies.c:
        /* Game description is a sequence of letters representing the number
        * of spaces (a = 0, y = 24) before the next dot; a-y for a white dot,
        * and A-Y for a black dot. 'z' is 25 spaces (and no dot).
        */
        """
#        tokenS = re.findall("([0123456789]*)x([0123456789]*):([abcdefghijklmnopqrstuvwxyz]*)", gameDesc)
        tokenS = re.findall("^(.*)x(.*):(.*)$", gameDesc)
        token = tokenS[0]
        i = 0
        width = -1
        height = -1
        desc = ""

        for t in token:
            if (0 == i):
                width = int(t)
            if (1 == i):
                height = int(t)
            if (2 == i):
                desc = t
            i = i + 1
        if (width <> self._width):
            """ Error """
        if (height <> self._height):
            """ Error """
        posi = 0
        posj = 0
#        print "desc : [%s]" % desc
        first = 1 # the offset "a" is only allowed as the first char of the description.
        for c in desc:
#            print "-------"
#            print "Former pos : (%d, %d)" % (posi, posj)
            offset = ord(c) - ord("a") + 1 - first
            first = 0
#            print "char : %s => offset = %d" % (c, offset)
            nextPos = self._posPlusOffset(posi, posj, offset)
            posi = nextPos["i"]
            posj = nextPos["j"]
            if self._canPutDot(int(posi * 2 + 1), int(posj * 2 + 1)):
#                print "Adding dot at (%.1f, %.1f) (%s)" % (posi, posj, c)
                self.addDot(posi / 2.0, posj / 2.0)
            else:
 #               print "Cannot put dot : (%.1f, %.1f) (%s)" % (posi, posj, c)
                return

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
        if ((0 == (i % 2)) and (0 == (j % 2))):
            self.board[i][j] = self._dotCross
            return
        if self.isWall(i, j):
            self.board[i][j] = self._dotWall
        else:
            self.board[i][j] = self._dotCell

    def addWall(self, i, j, orientation):
        """
        Orientation = h or v (horizontal or vertical)
        If horizontal : i = row number after which create the wall
        If vertical : i = row number after which create the wall
        j = the nth wall to add (1, 2, 3 ...)
        """
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

    def addWallShort(self, i, j):
        """
        Add a wall on the board.
        Arguments are taken in the wall way (full cells only)
        """
        assert not ((0 ==  i % 2) and (0 == j % 2)), "Cannot create a wall on crossings : (%d, %d)" % (i, j)

        if (self.board[i][j] in self._dotS):
            self.board[i][j] = self._dotWall
            return

        if (0 ==  i % 2):
            self.board[i][j] = self._wallh
            return

        if (0 ==  j % 2):
            self.board[i][j] = self._wallv
            return

    def _createPossibleBelongingsGraph(self):
        """
        For each cell, every dots it can belong to
        """
    def cellContainsDot(self, i, j):
#        print "cellContainsDot : cell = (%d, %d)" % (i, j)
        if self.isDot(i - 1, j - 1):
            return True
        if self.isDot(i - 1, j   ):
            return True
        if self.isDot(i - 1, j + 1):
            return True
        if self.isDot(i    , j - 1):
            return True
        if self.isDot(i    , j    ):
            return True
        if self.isDot(i    , j + 1):
            return True
        if self.isDot(i + 1, j - 1):
            return True
        if self.isDot(i + 1, j    ):
            return True
        if self.isDot(i + 1, j + 1):
            return True

        return False

    def cellContainsDotExcept(self, i, j, ei, ej):
        if self.isDot(i - 1, j - 1) and not ((i - 1 == ei) and (j - 1 == ej)):
            return True
        if self.isDot(i - 1, j   ) and not ((i - 1 == ei) and (j     == ej)):
            return True
        if self.isDot(i - 1, j + 1) and not ((i - 1 == ei) and (j + 1 == ej)):
            return True
        if self.isDot(i    , j - 1) and not ((i     == ei) and (j - 1 == ej)):
            return True
        if self.isDot(i    , j    ) and not ((i     == ei) and (j     == ej)):
            return True
        if self.isDot(i    , j + 1) and not ((i     == ei) and (j + 1 == ej)):
            return True
        if self.isDot(i + 1, j - 1) and not ((i + 1 == ei) and (j - 1 == ej)):
            return True
        if self.isDot(i + 1, j    ) and not ((i + 1 == ei) and (j     == ej)):
            return True
        if self.isDot(i + 1, j + 1) and not ((i + 1 == ei) and (j + 1 == ej)):
            return True

        return False


    def symetricCell(self, ci, cj, centerI, centerJ):
        return {"i":centerI + (centerI - ci), "j":centerJ + (centerJ - cj)}

    def cellIsWithinBoard(self, i, j):
        if ((i < 0) or (j < 0)):
            return False
        if ((i >= len(self.board)) or (j >= len(self.board[0]))):
            return False
        return True

    def cellCanBelongToDot(self,ci, cj, di, dj):
        """
        True if the cell on the oposite side of the dot:
            - belongs to the Board
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
        if (self.cellContainsDotExcept(si, sj, di, dj)):
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

    def dotsPossiblePlaces(self, firsti = 1, firstj = 1):
#        print "Init DPP"
        for i in range(firsti, len(self.board) - 1):
            for j in range(firstj, len(self.board[i]) - 1):
                yield {"i":i, "j":j}
            firstj = 1

    def dots(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if (self.board[i][j] in self._dotS):
                    yield {"i":i, "j":j}

    def cells(self):
        for i in range(1, len(self.board), 2):
            for j in range(1, len(self.board[i]), 2):
                yield {"i":i, "j":j}

    def _posPlusOffset(self, i, j, offset):
        for pos in self.dotsPossiblePlaces(i, j):
#            print "PPO : (%d, %d) + %d => (%d, %d)" % (i, j, offset, pos["i"], pos["j"])
            if (0 >= offset):
                return {"i":pos["i"], "j":pos["j"]}
            offset = offset - 1

    def isSolved(self):
        return False


    def cellBelongsToValidShape(self, i, j):
        """
        A cell is inside a valid shape is this shape:
            - Contains 1 and only 1 dot
            - Doesn't contain any wall (excepting for its edges)
        """

    def wallsAroundCell(self, i, j):
        """
        """
        ret = set()
        for edge in self.edgesAroundCell(i, j):
            if self.isWall(edge[0], edge[1]):
                ret.add(edge)
        return ret

    def edgesAroundCell(self, i, j):
        """
        Gives the coordinates of edges around a cell.
        Thus it converts coordinates from one system (cells mesured by halfs) to the other (edges
        mesured by whole edges)
        """
        ret = set()
        ret.add((i * 2, j * 2 + 1))
        ret.add((i * 2 + 1, j * 2))
        ret.add(((i + 1) * 2, j * 2 + 1))
        ret.add(((i * 2 + 1, (j + 1) * 2)))
        return ret

    def shapeAroundCell(self, i, j):
        """
        Returns the list of cells which are inside the same shape (range of cells delimited by walls
        """

    def _canPutDot(self, i, j):
#        print "CPD (%d, %d)" % (i, j)
#        print "1"
        if ((0 >= i) or (0 >= j)):
            return False
 #       print "2 (%d, %d)" % (i, j)
 #       print "%d" % (len(self.board) - 1)
 #       print "%d" % (len(self.board[0]) - 1)
        if (((len(self.board) - 1) <= i) or
            ((len(self.board[0]) - 1) <= j)):
            return False
  #      print "3"
        if self.isDot(i - 1, j - 1):
            return False
        if self.isDot(i - 1, j):
            return False
        if self.isDot(i - 1, j + 1):
            return False
        if self.isDot(i, j - 1):
            return False
        if self.isDot(i, j):
            return False
        if self.isDot(i, j + 1):
            return False
        if self.isDot(i + 1, j - 1):
            return False
        if self.isDot(i + 1, j):
            return False
        if self.isDot(i + 1, j + 1):
            return False

        return True
