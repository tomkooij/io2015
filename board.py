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
            self.bord = [startpos]
        else:
            self.bord = [[0] * N for i in range(N)]

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

        elif direction==RIGHT:
            self.merge(mergeleft=False)

        elif direction==UP:
            # omhoog is 3x linksom, links merge, 1x linksom
            self.rotate(3)
            self.merge()
            self.rotate(1)

        elif direction==DOWN:
            # omlaag ook via rotaties.
            self.rotate(1)
            self.merge()
            self.rotate(3)

        else:
            print "illegal move: ", direction
            assert(0)

    def place(self, row, column, kleur):
        self.bord[row][column] = kleur

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
    """
    testgame from caia
    """

    MOVES=['12', '33', '22', '11', 'R', 'L', '22', '41', '42', '12', 'U', 'R', '31', '33', '11', '41', 'R', 'D', '13', '21', '41', '32', 'U', 'D', '21', '23', '13', '22', 'U', 'D', '12', '23', '13', '22', 'R', 'U', '11', '44', '33', '43', 'D', 'R', '12', '41', '32', '13', 'R', 'L', '24', '34', '14', '23', 'R', 'U', '44', '32', '41', '33', 'U', 'D', '14', '31', '33', '13', 'R', 'U', '41', '23', '44', '31', 'U', 'R', '43', '32', '23', '41', 'R', 'L', '24', '33', '43', '42', 'U', 'L', '34', '43', '24', '32', 'R', 'R', '41', '43', '32', '31', 'D', 'U', '21', '34', '41', '31', 'R', 'L', '34', '42', '33', '32', 'U', 'R', '42', '31', '11', '21', 'D', 'U', '31', '44', '21', '41', 'U', 'L', '33', '42', '34', '23', 'L', 'R', '42', '43', '21', '32', 'L', 'R', '43', '41', '31', '42', 'U', 'D', '12', '14', '21', '22', 'L', 'U', '14', '43', '34', '24', 'L', 'D', '24', '11', '13', '34', 'R', 'L', '13', '14', '24', '34', 'D', 'U', '42', '34', '44', '33', 'R', 'U', '43', '21', '41', '44', 'R', 'L', '23', '33', '44', '13', 'D', 'U', '33', '24', '34', '43', 'L', 'R', '12', '21', '11', '32', 'U', 'D', '11', '42', '32', '13', 'U', 'L', '33', '24', '34', '44', 'R', 'L', '33', '42', '34', '43', 'U', 'R', '31', '43', '42', '41', 'R', 'U', '42', '41'];

    b = Bord()
    b.show()
    print "Start!"

    zetteller = 0  # hulpje om blauw, rood, rood, blauw t regelen
    aanzet = [BLUE, RED, RED, BLUE]

    for move in MOVES:
        print "Move : ", move
        if move in ['U', 'D', 'R', 'L']:
            if move == 'U':
                b.move(UP)
            elif move == 'D':
                b.move(DOWN)
            elif move == 'R':
                b.move(RIGHT)
            elif move == 'L':
                b.move(LEFT)
            else:
                assert(0)
            zetteller = 0
        else:

            print "place ", aanzet[zetteller]
            b.place(int(move[0])-1, int(move[1])-1, aanzet[zetteller])
            zetteller += 1 # de ander is nu aan zet
        b.show()
        raw_input()
