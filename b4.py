#b4
# woorden leggen
#
# TODO: Handle EERSTE met met 3x 'E'
# maak lijst met alle oplossingen voor 60 en 56 en controleer juistheid


"""
mogelijke opl: {42, 48, 49, (50), 54, 56, 60, 63, 64, 72, 81}
RECORD!  54
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', 'E', '.', '.', '.', 'B', '.', '.', '.', '.', '.']
['.', 'R', 'O', 'N', 'D', 'E', '.', 'N', 'I', 'O', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', 'R', '.', '.', '.', 'R', '.', '.', '.', '.', '.']
['.', '.', '.', 'R', 'U', 'S', 'L', 'A', 'N', 'D', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', 'T', '.', '.', '.', 'E', '.', '.', '.', '.', '.']
['.', 'W', 'E', 'I', 'G', 'E', 'R', 'T', '.', 'R', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
"""

from copy import deepcopy
from random import shuffle
from itertools import permutations
from re import finditer

test2 = ['EEN', 'TWEE', 'DRIEEE', 'EERSTE']
opgave = ['NIO', 'EERSTE', 'RONDE','RUSLAND', 'BORDER', 'WEIGERT']

TEST = 0

HORIZONTAAL = 0
VERTICAAL = 1

MAX_X_BORD = 30
MAX_Y_BORD = 30

RECORD = 100
ABS_RECORD = 53

RECORDBORD = []

def print_bord(bord):
    for y in range(2,25):
        print bord[y][7:25]

def bord_area(bord):
    x_min = MAX_X_BORD
    y_min = MAX_Y_BORD
    x_max = 0
    y_max = 0

    for y in range(MAX_Y_BORD):
        for x in range(MAX_X_BORD):
            if bord[y][x] != '.':
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y

    #print x_min, x_max, y_min, y_max

    return (x_max-x_min+1)*(y_max-y_min+1)


def leg_woord(bord, x, y, orientatie, woord):
    if x > MAX_X_BORD-9 or y > MAX_Y_BORD-9:
        return False

    if orientatie == HORIZONTAAL:
        if bord[y][x-1] != '.':
            # woord ligt in verlengde van bestaand woord
            return False
        for idx,x_coord in enumerate(range(x,x+len(woord))):
            if (bord[y-1][x_coord]+bord[y][x_coord]+bord[y+1][x_coord] != '...') and (bord[y][x_coord] != woord[idx]):
                # woord ligt direct naast of doorkruist bestaand woord
                return False
        for idx,x_coord in enumerate(range(x,x+len(woord))):
            bord[y][x_coord] = woord[idx]

    elif orientatie == VERTICAAL:
        if bord[y-1][x] != '.':
            # woord ligt in verlengde van bestaand woord
            return False
        for idx,y_coord in enumerate(range(y,y+len(woord))):
            if (bord[y_coord][x-1:x+2] != list('...')) and (bord[y_coord][x] != woord[idx]):
                return False
        for idx,y_coord in enumerate(range(y,y+len(woord))):
            bord[y_coord][x] = woord[idx]

    else:
        print 'lp0 on fire in leg_woord()'
        assert(0)

    return True

def findall_iter(sub, string):
    """
    >>> text = "Allowed Hello Hollow"
    >>> tuple(findall_iter('ll', text))
    (1, 10, 16)
    """
    def next_index(length):
        index = 0 - length
        while True:
            index = string.find(sub, index + length)
            yield index
    return iter(next_index(len(sub)).next, -1)


def do(bord, woordenlijst):

    global RECORD, RECORDBORD

    #print("ENTERING RECURSION!", woordenlijst)
    hetbord = deepcopy(bord)
    woord = woordenlijst[0]

    for x in range(MAX_X_BORD):
        for y in range(MAX_Y_BORD):
            karakter = bord[y][x]
            if karakter != '.':
                #print "optie", x, y, karakter
                # HIER 2 of 3 opties toestaan
                for offset in findall_iter(karakter, woord):

                    tmp_bord = deepcopy(hetbord) # maak kopie!
                    if leg_woord(tmp_bord, x-offset,y, HORIZONTAAL, woord):
                        #print "HORIZONTAAL! :",x,y,offset
                        #print_bord(tmp_bord)
                        if len(woordenlijst) > 1:
                            do(tmp_bord, woordenlijst[1:])
                        else:
                            area = bord_area(tmp_bord)
                            if area <= RECORD:
                                if area <= ABS_RECORD:
                                    print_bord(tmp_bord)
                                RECORD = area
                                print "RECORD! ", area
                                RECORDBORD = deepcopy(tmp_bord)
                                #print_bord(tmp_bord)
                            #print "Branch finished!"

                    tmp1_bord = deepcopy(hetbord)
                    if leg_woord(tmp_bord, x,y-offset, VERTICAAL, woord):
                        #print "VERTICAAL! :",x,y,offset
                        #print_bord(tmp_bord)
                        if len(woordenlijst) > 1:
                            do(tmp_bord, woordenlijst[1:])
                        else:
                            area = bord_area(tmp_bord)
                            if area <= RECORD:
                                if area <= ABS_RECORD:
                                    print_bord(tmp_bord)
                                RECORD = area
                                print "RECORD! ", area
                                RECORDBORD = deepcopy(tmp_bord)
                                #print_bord(tmp_bord)
                            #print "Branch finished!"


    #print "END OF do() ", woordenlijst

def leg_voorbeeld(bord):
    #print leg_woord(bord, 2, 1, HORIZONTAAL, 'DELFT')
    #print leg_woord(bord, 1, 4, HORIZONTAAL, 'EINDHOVEN')
    print leg_woord(bord, 4, 1, VERTICAAL, 'LEIDEN')
    #print leg_woord(bord, 4, 6, HORIZONTAAL, 'NYMEGEN')
    #print leg_woord(bord, 9, 1, VERTICAAL, 'TWENTE')
    return bord

if __name__ == '__main__':
    if TEST:
        leeg_bord = [['.' for x in range(MAX_X_BORD)] for y in range(MAX_Y_BORD)]
        volbord = leg_voorbeeld(leeg_bord)
        print_bord(volbord)
        print bord_area(volbord)
        rest = ['DELFT','EINDHOVEN','NYMEGEN','TWENTE']
        for case in permutations(rest):
            bord = deepcopy(volbord)
            print case
            do(leeg_bord, case)
    else:
        for case in permutations(opgave):
            leeg_bord = [['.' for x in range(MAX_X_BORD)] for y in range(MAX_Y_BORD)]
            print case
            leg_woord(leeg_bord,10,5,VERTICAAL,case[0])
            do(leeg_bord, case[1:])
        print "min = ", RECORD
        print_bord(RECORDBORD)
