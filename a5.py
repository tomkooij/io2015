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


def vind_volgende(bord):
    for (rij, regel) in enumerate(bord):
        for (kolom, karakter) in enumerate(regel):
            if karakter == '0':
                return rij, kolom
    # niet gevonden
    return (-1, -1)


def kleur_vlak_in(rij, kolom, bord):

    bord = kleur_in(rij, kolom, bord)

    # boven
    if (rij > 0) and (bord[rij-1][kolom] == '0'):
        bord = kleur_vlak_in(rij-1, kolom, bord)
    # onder
    if (rij < 9) and (bord[rij+1][kolom] == '0'):
        bord = kleur_vlak_in(rij+1, kolom, bord)
    # links
    if (kolom > 0) and (bord[rij][kolom-1] == '0'):
        bord = kleur_vlak_in(rij, kolom-1, bord)
    # onder
    if (kolom < 9) and (bord[rij][kolom+1] == '0'):
        bord = kleur_vlak_in(rij, kolom+1, bord)

    return bord


def kleur_in(rij, kolom, bord):
    # bord[rij][kolom] = '1' DOES NOT WORK! Strings are immutable
    bord[rij] = bord[rij][0:kolom]+'1'+bord[rij][kolom+1:]
    return bord


if __name__ == '__main__':
    if TEST:
        bord = ['0111000101',
                '0101000110',
                '1001111100',
                '0010000001',
                '0101010101',
                '1100010011',
                '0000000000',
                '0101010101',
                '1010101010',
                '0010010010']
    else:
        bord = [raw_input("") for _ in range(10)]

    if DEBUG:
        print(bord)

    rij = 0
    kolom = 0
    count = 0

    while (1):
        rij, kolom = vind_volgende(bord)
        if DEBUG:
            print("gevonden: ", rij, kolom)
        if (rij == -1):
            break
        bord = kleur_vlak_in(rij, kolom, bord)
        count += 1

    if DEBUG:
        print(bord)

    print(count)
