#b4
# woorden leggen

from copy import deepcopy

woorden = ['DELFT', 'EINDHOVEN', 'LEIDEN', 'NYMEGEN', 'TWENTE']

HORIZONTAAL = 0
VERTICAAL = 1

MAX_X_BORD = 18
MAX_Y_BORD = 18

RECORD = 70

def print_bord(bord):
    for y in range(MAX_Y_BORD):
        print bord[y]

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
    if x > MAX_X_BORD-5 or y > MAX_Y_BORD-5:
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


def do(bord, woordenlijst):

    global RECORD

    print("ENTERING RECURSION!", woordenlijst)
    hetbord = deepcopy(bord)
    woord = woordenlijst[0]

    for x in range(MAX_X_BORD):
        for y in range(MAX_Y_BORD):
            karakter = bord[y][x]
            if karakter != '.':
                #print "optie", x, y, karakter
                # HIER 2 of 3 opties toestaan
                offset = woord.find(karakter)
                if offset != -1:
                    # gevonden, probeer te leggen:
                    tmp_bord = deepcopy(hetbord) # maak kopie!
                    if leg_woord(tmp_bord, x-offset,y, HORIZONTAAL, woord):
                        #print "HORIZONTAAL! :",x,y,offset
                        #print_bord(tmp_bord)
                        if len(woordenlijst) > 1:
                            do(tmp_bord, woordenlijst[1:])
                        else:
                            area = bord_area(tmp_bord)
                            if area <= RECORD:
                                RECORD = area
                                print "RECORD! ", area
                                print_bord(tmp_bord)
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
                                RECORD = area
                                print "RECORD! ", area
                                print_bord(tmp_bord)
                            #print "Branch finished!"


    print "END OF do() ", woordenlijst

def leg_voorbeeld(bord):
    print leg_woord(bord, 2, 1, HORIZONTAAL, 'DELFT')
    print leg_woord(bord, 1, 4, HORIZONTAAL, 'EINDHOVEN')
    print leg_woord(bord, 4, 1, VERTICAAL, 'LEIDEN')
    #print leg_woord(bord, 4, 6, HORIZONTAAL, 'NYMEGEN')
    #print leg_woord(bord, 9, 1, VERTICAAL, 'TWENTE')
    return bord

if __name__ == '__main__':

    leeg_bord = [['.' for x in range(MAX_X_BORD)] for y in range(MAX_Y_BORD)]
    volbord = leg_voorbeeld(leeg_bord)
    print_bord(volbord)
    print bord_area(volbord)
    do(volbord, ['NYMEGEN','TWENTE'])
