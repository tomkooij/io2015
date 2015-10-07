# Opgave c2
from __future__ import division
from __future__ import print_function

import sys
from random import shuffle

TEST = 1
DEBUG = 1


# Uit het voorschrift van de olympiade
def io_print(string):
    sys.stdout.write(str(string) + "\n")
    sys.stdout.flush()


def omkeren(rij, eerste,tweede):
    """
    implementatie van omkeren() functie uit de opgave
    wissel de volgorde getallen van de posities "eerste" t/m "tweede" om

    nummer van python dus 0, 1, 2...
    omkeren(7,9) van de opgave is dus omkeren(6,8) in deze code
    """
    assert(tweede <= len(rij)-1)
    return rij[0:eerste]+list(reversed(rij[eerste:tweede+1]))+rij[tweede+1:]

def sorteer(rij):
    recept = [(6,9),(5,8),(4,7),(3,6),(1,4),(1,3),(0,2)]

    for (eerste, tweede) in recept:
        rij = omkeren(rij, eerste, tweede)
        print(rij)

    assert(rij==sorted(rij))


def sorteer_naar_achter(rij):
    gesorteerd = sorted(rij)

    if rij == gesorteerd:
        return []

    recept = []
    # bepaal welke nu de max is
    # zoek de plek in de rij
    # keer om
    for kolom in range(len(rij)-1,0,-1):
        fout = [i for i,j in zip(rij,gesorteerd) if i != j]  # welke staan niet goed
        # als slecht 2 posities fout, wissel alleen die
        if len(fout) == 2:
            eerste = rij.index(fout[0])
            laatste = rij.index(fout[1])
            if DEBUG:
                rij = omkeren(rij, eerste, laatste)
                print("laatste: ", rij)
            recept.append((eerste, laatste))
            return recept
        grootste = max(fout)
        laatste = len(fout)-1
        eerste = rij.index(grootste)
        rij = omkeren(rij, eerste, laatste)
        if DEBUG:
            print("*", laatste, "(", eerste+1, ",", laatste+1, ")", rij)
        recept.append((eerste,laatste))

    return recept


if __name__ == '__main__':
    if TEST == 1:
        N = 10
        rij = [5, 20, 4, 22, 23, 26, 27, 1, 14, 21]
    elif TEST == 2:
        pass
    elif TEST == 3:
        N = 10
        rij = range(N)
        shuffle(rij)

    else:
        N = int(raw_input())
        rij = [int(x) for x in str(raw_input()).split(' ')]

    assert(len(rij) == N)

    if DEBUG:
        print(rij)

    recept = sorteer_naar_achter(rij)

    io_print(len(recept))
    for (eerste,laatste) in recept:
        io_print(str(eerste)+' '+str(laatste))
