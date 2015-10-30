#!/usr/bin/python
# bottom.py
# 2187 bot voor nio3.codecup.nl

from copy import deepcopy
from math import copysign
import random
import sys

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
            self.bord = [[0] * N for i in range(N)]

    def show(self):
        for i in range(N):
            for j in range(N):
                if self.bord[i][j]:
                    #print >>sys.stderr, '%4d' % copysign(3**(abs(self.bord[i][j])-1),self.bord[i][j]),
                    print >>sys.stderr, '%4d' % self.bord[i][j],
		else:
                    print >>sys.stderr, '   .',
            print >>sys.stderr, '|\n'
        print >>sys.stderr, '----------------\n'

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
            print >>sys.stderr, "illegal move: ", direction
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

    def place_random_tile(self, kleur):
        """
        places a random tile, return position in game format ie: "24" -> [1][3]
        """
        place = random.choice(self._free_squares())

        row = place[0]
        column = place[1]

        self.bord[row][column] = int(kleur)

        return '%d%d' % (row+1,column+1)

    def move_game_notation(self, move, color=RED):
        """
        verwerk een zet in "game notation"
        move => str '23' of 'U'
        """
        if len(move)==2:
            self.place(int(move[0])-1, int(move[1])-1, color)
        elif move == 'U':
            self.move(UP)
        elif move == 'D':
            self.move(DOWN)
        elif move == 'R':
            self.move(RIGHT)
        elif move == 'L':
            self.move(LEFT)
        else:
            print >>sys.stderr, "illegal move!"
            assert(0)

    def score(self):
        score = 0
        for i in range(N):
            for j in range(N):
                score += abs(self.bord[i][j])
        return score

    def dump(self):
        return self.bord




BLUE = -1
RED = 1
SHIFT = 0
zet_type = [BLUE, RED, RED, BLUE, SHIFT, SHIFT]

if __name__ == '__main__':

    b = Bord()
    print >>sys.stderr, "bottom.py 2187 Bot."

    inbuf = sys.stdin.readline().split()[0]
    print >>sys.stderr, "read from stdin: ", inbuf
    beurt = 0

    if inbuf == 'A':
        # we zijn player1 (wit)
        print >>sys.stderr, "Wit!"
        while 1:
            print >>sys.stderr, "beurt: ", beurt
            color = zet_type[beurt % 6]     # welke kleur?

            if color != 0:
                move = b.place_random_tile(color)
            else:
                huidige_toestand = deepcopy(b.dump())
                # kies een shift die een score groter dan 0 geeft
                # EN GEEN VERANDERING!!
                for move in ['U','D','L','R']:
                    temp = Bord(deepcopy(b.dump()))  # maak kopie
                    temp.move_game_notation(move)

                    if temp.dump() == huidige_toestand: # geen verandering!
                        continue
                    if temp.score():  # gevonden!
                        break
            	b.move_game_notation(move)

            print >>sys.stderr, "played: ", move
            print >>sys.stdout, move

            b.show()
            beurt += 1
            sys.stdout.flush()
            sys.stderr.flush()
            inbuf = sys.stdin.readline().split()[0]
            print >>sys.stderr, "read from stdin: ", inbuf

            if inbuf == 'Quit':
                break
            b.move_game_notation(inbuf, zet_type[beurt % 6])
            b.show()
            beurt += 1
    else:

        print >>sys.stderr, "Zwart!"
        while 1:

            print >>sys.stderr, "beurt: ", beurt
            inbuf = sys.stdin.readline().split()[0]
            print >>sys.stderr, "read from stdin: ", inbuf

            if inbuf == 'Quit':
                break

            b.move_game_notation(inbuf, zet_type[beurt % 6])
            b.show()
            beurt += 1

            color =  int(zet_type[beurt % 6])    # welke kleur?

            if color != 0:
                move =  b.place_random_tile(color)
            else:
                huidige_toestand = deepcopy(b.dump())
                # kies een shift die een score groter dan 0 geeft
                # EN GEEN VERANDERING!!
                for move in ['U','D','L','R']:
                    temp = Bord(deepcopy(b.dump()))  # maak kopie
                    temp.move_game_notation(move)

                    if temp.dump() == huidige_toestand: # geen verandering!
                        continue
                    if temp.score():  # gevonden!
                        break
            	b.move_game_notation(move)

            b.show()
            beurt += 1
            print >>sys.stderr, "we played: ", move

            print >>sys.stdout, move

            sys.stderr.flush()
            sys.stdout.flush()
