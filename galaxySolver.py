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

def c_(x, y):
    return {"x":x, "y":y}

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
                    self.board[i].append(".")
                    continue
                if (0 == (i % 2)):
                    self.board[i].append(".")
                    continue
                self.board[i].append(" ")
    # TODO: find a reasonable memory reresentation for the array"
    #Question: How to create a 2 dimensions array in python ?
    def pprint(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                print self.board[i][j],
#        print self.board
            print

    def _createPossibleBelongingsGraph(self):
        """
        For each cell, every dots it can belong to
        """

    def _cellCanBelongToDot(self):
        """
        True if the cell on the oposite side of the dot:
            - belongs to the board
            - doesn't contain a dot
            - isn't edged by a dot
        """

    def _symetricPosition(cell, dot):
        """
        """


myBoard = board(3,3) # 7 * 7 array
myBoard.board[3][3] = "o"
myBoard.pprint()


"""
Example of a board (7 x 7):
c = cell
o = dot
| or - = edge
+ = empty (nothing can be put at the crossing of 2 edges)

+ - + - + - +
|   | c |   |
+ - + - + - +
|   | o |   |
+ - + - + - +
|   |   |   |
+ - + - + - +


"""
