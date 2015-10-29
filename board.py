from math import copysign
from random import choice

sign = lambda x: int(copysign(1, x))

N = 4   # 4x4 bord
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

RED = 1
BLUE = -1

class Bord(object):
    """
    2187 wordt met 2 spelers (rood, blauw)
    gespeeld en met machten van 3

    self.bord[0] = bovenste rij van het bord
    [0, 1, 0, -2] = leeg, 1 (rood), leeg, 3 (blauw)
        dwz: 3**(bord[i][j]-1)
    rood = positief, blauw negatief

    """

    def __init__(self, startpos = None):
        if startpos is not None:
            self.bord = startpos
        else:
            self.bord = [[None] * N for i in range(N)]

    def show(self):
        for i in range(N):
            for j in range(N):
                if self.bord[i][j]:
                    print '%4d' % copysign(3**(abs(self.bord[i][j])-1),self.bord[i][j]),
                else:
                    print '   .',
            print

    def rotate(self, number_of_rotations):    # roteer links om
        for i in range(number_of_rotations):
            y = [row[:] for row in self.bord]
            for i in range(N):
                for j in range(N):
                    self.bord[i][3-j] = y[j][i]

    def move(self, direction=UP):
        if direction==LEFT:
            self.merge()

        if direction==RIGHT:
            self.merge(mergeleft=False)

        if direction==UP:
            # omhoog is 3x linksom, links merge, 1x linksom
            self.rotate(3)
            self.merge()
            self.rotate(1)

        if direction==DOWN:
            # omlaag ook via rotaties.
            self.rotate(1)
            self.merge()
            self.rotate(3)


    def merge(self, mergeleft=True):
        for i in range(N):
            self.bord[i] = self._mergerow(self.bord[i], left=mergeleft)

    @staticmethod
    def _mergerow(rij, left=True):
        """
        2048 (2187) merge algoritme
        Waarschijnlijk de slechtse implementatie ooit...

        [0, 2, 0, 2] --> [4, 0, 0, 0]
        [2, 8, 8, 2] --> [2, 9, 2, 0]    exponenten!
        [2, 2, 2, 2] --> [3, 3, 0, 0]    slecht 1 merge ronde per keer
        """

        def shift_left(rij):
            """
            [0,1,0,0,1] --> [1,1,0,0,0]
            """
            for i,number in enumerate(rij):
                if not number:  # leeg vlakje?
                    for j,volgende in enumerate(rij[i:]): # vanaf i tot einde lijst
                        if volgende:  # getal?
                            rij[i] = volgende  # zet het getal op de plek van de 0
                            rij[i+j] = 0     # zet een nul op die plek
                            break
            return rij

        def merge_equal(rij):
            """
            [1,1,0,0] --> [2, 0, 0, 0]
            """
            for i in range(len(rij)-1):
                if rij[i]:
                    if rij[i] == rij[i+1]:
                        rij[i] += sign(rij[i])
                        rij[i+1] = 0
                    if (rij[i] == -rij[i+1]):   # twee tegenstelde verdwijnen
                        rij[i] = 0
                        rij[i+1] = 0

            return rij

        if left:
            return shift_left(merge_equal(shift_left(rij)))
        else:
            return shift_left(merge_equal(shift_left(rij[::-1])))[::-1]

    def _free_squares(self):
        """
        return a list of free squares
        """
        free_squares = []
        for row in range(N):
            for column in range(N):
                if not self.bord[row][column]:
                    free_squares.append((row, column))

        return free_squares

    def place_random_tile(self, color):
        """
        places a random tile, return position in game format ie: "24" -> [1][3]
        """
        place = choice(self._free_squares())

        row = place[0]
        column = place[1]

        self.bord[row][column] = color

        return '%d%d' % (row+1,column+1)


if __name__ == '__main__':
    b = Bord([[1,-1,0,0],[1,0,0,-1],[-1,1,1,0],[-1,0,0,0]])
    b.show()
    print "R:"
    b.move(RIGHT)
    b.show()
    print b._free_squares()
    print "L:"
    b.move(LEFT)
    b.show()
    print "Up:"
    b.move(UP)
    b.show()
    print "Down:"
    b.move(DOWN)
    b.show()
    print "Left"
    b.move(LEFT)
    b.show()
    print "random RED: ",
    print b.place_random_tile(RED)
    b.show()
    print "random BLUE: ",
    print b.place_random_tile(BLUE)
    b.show()
