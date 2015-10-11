#b4
# woorden leggen

from copy import deepcopy

woorden = ['DELFT', 'EINDHOVEN', 'LEIDEN', 'NYMEGEN', 'TWENTE']

HORIZONTAAL = 0
VERTICAAL = 1

MAX_X_BORD = 19
MAX_Y_BORD = 17



def print_bord(bord):
    for y in range(MAX_Y_BORD):
        print bord[y]


def leg_woord(bord, x, y, orientatie, woord):
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


def do(bord, woord):
    hetbord = deepcopy(bord)
    for x in range(MAX_X_BORD):
        for y in range(MAX_Y_BORD):
            karakter = bord[y][x]
            if karakter != '.':
                print "optie", x, y, karakter
                # HIER 2 of 3 opties toestaan
                offset = woord.find(karakter)
                if offset != -1:
                    tmp_bord = deepcopy(hetbord) # maak kopie!
                    if leg_woord(tmp_bord, x-offset,y, HORIZONTAAL, woord):
                        print "HORIZONTAAL! :",x,y,offset
                        print_bord(tmp_bord)
                    tmp1_bord = deepcopy(hetbord)
                    if leg_woord(tmp_bord, x,y-offset, VERTICAAL, woord):
                        print "VERTICAAL! :",x,y,offset
                        print_bord(tmp_bord)


def leg_voorbeeld(bord):
    print leg_woord(bord, 3, 2, HORIZONTAAL, 'DELFT')
    print leg_woord(bord, 1, 4, HORIZONTAAL, 'EINDHOVEN')
    #print leg_woord(bord, 4, 1, VERTICAAL, 'LEIDEN')
    print leg_woord(bord, 4, 6, HORIZONTAAL, 'NYMEGEN')
    print leg_woord(bord, 9, 1, VERTICAAL, 'TWENTE')
    return bord

if __name__ == '__main__':

    leeg_bord = [['.' for x in range(MAX_X_BORD)] for y in range(MAX_Y_BORD)]
    volbord = leg_voorbeeld(leeg_bord)
    print_bord(volbord)
    do(volbord, 'LEIDEN')
