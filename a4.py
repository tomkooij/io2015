# Opgave A4
from __future__ import division
from __future__ import print_function

import sys
from random import shuffle

TEST = 0
DEBUG = 0


# Uit het voorschrift van de olympiade
def io_print(string):
    sys.stdout.write(str(string) + "\n")
    sys.stdout.flush()


def selecteer_foto(lijst):

    eerste_10 = lijst[0:10]

    if DEBUG:
        print("eerste 10 = ", eerste_10, len(lijst))
    grootste = max(eerste_10)
    io_print(grootste)

    plaats_grootste = eerste_10.index(grootste)

    lijst = lijst[plaats_grootste+1:]
    if DEBUG:
        print("nu over = ", lijst, len(lijst))
    return lijst


def selecteer_fotos(stapel):

    while (len(stapel) > 0):
        stapel = selecteer_foto(stapel)
        if (len(stapel) <= 10) and (len(stapel) > 0):
            selecteer_foto(stapel)
            break

if __name__ == '__main__':
    if TEST == 1:
        N = 22
        stapel = [9, 12, 17, 22, 8, 1, 20, 3, 15, 21, 2, 19, 4,
                  18, 5, 16, 14, 13, 11, 7, 6, 10]
    elif TEST == 2:
        N = 24
        stapel = [9, 12, 17, 22, 8, 1, 20, 3, 15, 21, 2, 19, 4,
                  18, 5, 16, 14, 13, 11, 7, 6, 10, 23, 1]
    elif TEST == 3:
        N = 22
        stapel = range(N)
        shuffle(stapel)
        print(stapel)

    else:
        N = int(raw_input())
        stapel = [int(raw_input()) for _ in range(N)]

    if DEBUG:
        print(stapel)
    assert(len(stapel) == N)
    selecteer_fotos(stapel)
