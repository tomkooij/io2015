# Opgave A4
from __future__ import division
from __future__ import print_function

import sys

TEST = 0
DEBUG = 0


# Uit het voorschrift van de olympiade
def io_print(string):
    sys.stdout.write(str(string) + "\n")
    sys.stdout.flush()


def selecteer_foto(lijst):

    if DEBUG:
        io_print(lijst)

    eerste_10 = lijst[0:10]

    grootste = max(eerste_10)
    io_print(grootste)

    plaats_grootste = eerste_10.index(grootste)

    lijst = lijst[plaats_grootste+1:]
    if DEBUG:
        io_print(lijst)

    return lijst


def selecteer_fotos(stapel):

    while (len(stapel) > 0):
        stapel = selecteer_foto(stapel)
        if (len(stapel) < 10):
                break

if __name__ == '__main__':
    if TEST:
        N = 22
        stapel = [9, 12, 17, 22, 8, 1, 20, 3, 15, 21, 2, 19, 4,
                  18, 5, 16, 14, 13, 11, 7, 6, 10]
        #stapel = range(N)
    else:
        N = int(raw_input(""))
        stapel = [int(raw_input("")) for _ in range(N)]

    assert(len(stapel) == N)
    selecteer_fotos(stapel)
