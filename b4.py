#b4
# woorden leggen

woorden = ['DELFT', 'EINDHOVEN', 'LEIDEN', 'NYMEGEN', 'TWENTE']

HORIZONTAAL = 0
VERTICAAL = 1

bord = []


def print_bord():
    for x in range(10):
        print bord[x]


def leg_woord(x, y, orientatie, woord):
    if orientatie == HORIZONTAAL:
        for idx,x_coord in enumerate(range(x,x+len(woord))):
            if (bord[y][x_coord] != '.') and (bord[y][x_coord] != woord[idx]):
                return False
        for idx,x_coord in enumerate(range(x,x+len(woord))):
            bord[y][x_coord] = woord[idx]

    elif orientatie == VERTICAAL:
        for idx,y_coord in enumerate(range(y,y+len(woord))):
            if (bord[y_coord][x] != '.') and (bord[y_coord][x] != woord[idx]):
                return False
        for idx,y_coord in enumerate(range(y,y+len(woord))):
            bord[y_coord][x] = woord[idx]

    else:
        print 'lp0 on fire in leg_woord()'
        assert(0)

    return True

def leg_voorbeeld():
    print leg_woord(2, 1, HORIZONTAAL, 'DELFT')
    print leg_woord(0, 3, HORIZONTAAL, 'EINDHOVEN')
    print leg_woord(3, 0, VERTICAAL, 'LEIDEN')
    print leg_woord(3, 5, HORIZONTAAL, 'NYMEGEN')
    print leg_woord(8, 0, VERTICAAL, 'TWENTE')

if __name__ == '__main__':

    bord = [['.' for x in range(15)] for y in range(20)]
    leg_voorbeeld()
    print_bord()
