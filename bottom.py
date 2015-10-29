#!/usr/bin/python
# bottom.py
# 2187 bot voor nio3.codecup.nl

import sys
from board import *

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
                # kies een shift die een score groter dan 0 geeft
                for move in ['U','D','L','R']:
                    temp = Bord(b.dump())  # maak kopie
                    temp.move_game_notation('U')
                    if temp.score():
                        break

            print >>sys.stderr, "played: ", move
            print >>sys.stdout, move

            #b.show()
            beurt += 1
            sys.stdout.flush()
            sys.stderr.flush()
            inbuf = sys.stdin.readline().split()[0]
            print >>sys.stderr, "read from stdin: ", inbuf

            if inbuf == 'Quit':
                break
            b.move_game_notation(inbuf, zet_type[beurt % 6])
            #b.show()
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
            #b.show()
            beurt += 1

            color =  zet_type[beurt % 6]    # welke kleur?
            if color != 0:
                move =  b.place_random_tile(color)
            else:
                # kies een shift die een score groter dan 0 geeft
                for move in ['U','D','L','R']:
                    temp = Bord(b.dump())  # maak kopie
                    temp.move_game_notation('U')
                    if temp.score():
                        break
            #b.show()
            beurt += 1
            print >>sys.stderr, "we played: ", move

            print >>sys.stdout, move

            sys.stderr.flush()
            sys.stdout.flush()
