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

        inbuf = raw_input().split()[0]
        print >>sys.stderr, "read from stdin: ", inbuf
        beurt = 0

        if inbuf == 'Start':
            # we zijn player1 (wit)
            while 1:
                color = zet_type[beurt % 6]     # welke kleur?

                if color != 0:
                    print b.place_random_tile(color)
                else:
                    print 'U'
                    b.move_game_notation('U')

                b.show()
                beurt += 1
                sys.stdout.flush()
                inbuf = raw_input().split()[0]
                print >>sys.stderr, "read from stdin: ", inbuf

                if inbuf == 'Quit':
                    break
                b.move_game_notation(inbuf, zet_type[beurt % 6])
                b.show()
                beurt += 1
        else:
            while 1:
                b.move_game_notation(inbuf, zet_type[beurt % 6])
                b.show()
                beurt += 1

                color =  zet_type[beurt % 6]    # welke kleur?
                if color != 0:
                    print b.place_random_tile(color)
                else:
                    print 'U'
                    b.move_game_notation('U')
                b.show()
                beurt += 1

                sys.stdout.flush()
                inbuf = raw_input().split()[0]
                print >>sys.stderr, "read from stdin: ", inbuf

                if inbuf == 'Quit':
                    break
