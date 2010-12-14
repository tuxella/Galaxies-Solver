# -*- coding: utf-8

"""
A dot is the representant of every cells around it that form its shape.
A cell can belong to a shape if the symetric cell on the other side of the dot:
    - Is within the limits of the board
    - Doesn't have a dot inside or on any of its edges
"""

class Board(object):
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

