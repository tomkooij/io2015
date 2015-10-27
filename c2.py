# Opgave c2
from __future__ import division
from __future__ import print_function

import sys
import random
import copy

TEST = 0
DEBUG = 0


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

def check_sorteer_recept(rij, recept):

    for (eerste, tweede) in recept:
        rij = omkeren(rij, eerste, tweede)
        print(rij)

    assert(rij==sorted(rij))


def sorteer_naar_achter(rij):
    gesorteerd = sorted(rij)
    if DEBUG: print(gesorteerd)
    if rij == gesorteerd:
        return []

    recept = []
    # bepaal welke nu de max is
    # zoek de plek in de rij
    # keer om
    for i in range(len(rij)-1,0,-1):
        if rij[i] != gesorteerd[i]:
            if i == 2:
                if rij[1]==gesorteerd[1]:
                    if DEBUG:
                        print("SHORTCUT")
                        rij = omkeren(rij,0,2)
                        print (rij)
                    recept.append((0,2))
                    return recept
            laatste = i
            eerste = rij.index(max(rij[0:i]))
            if (eerste == laatste):
                print("STOP",eerste, laatste, rij)
                assert(0)
            rij = omkeren(rij, eerste, laatste)
            if DEBUG:
                print("*", laatste, "(", eerste+1, ",", laatste+1, ")", rij)
            recept.append((eerste,laatste))

    return recept

def sorteer_op_lange_afstand(rij):

    gesorteerd = sorted(rij)
    if DEBUG: print(rij)

    # kleinste en grootste die al op hun plek staan
    kleinste = 0
    grootste = len(rij)-1

    rest = list(rij)  # copy!
    recept = []

    while rij != gesorteerd:
        # bepaal afstand naar links (kleinste)
        links = rij.index(min(rest)) - kleinste
        rechts = grootste - rij.index(max(rest))
        if DEBUG:
            print("links, rechts:",links, rechts)
        if links <= rechts:
            laatste = grootste
            grootste -= 1
            eerste = rij.index(max(rest))
            rest.remove(max(rest))
        else:
            eerste = kleinste
            kleinste += 1
            laatste = rij.index(min(rest))
            rest.remove(min(rest))
        rij = omkeren(rij, eerste, laatste)
        if DEBUG:
            print("*", laatste, "(", eerste+1, ",", laatste+1, ")", rij)
            print("rest", rest)
        recept.append((eerste,laatste))

    return recept


def sorteer_naar_voor(rij):
    gesorteerd = sorted(rij)
    if DEBUG: print(gesorteerd)
    if rij == gesorteerd:
        return []

    recept = []
    # bepaal welke nu de max is
    # zoek de plek in de rij
    # keer om
    for i in range(len(rij)):
        if rij[i] != gesorteerd[i]:
            if i == len(rij)-3:
                if rij[len(rij)-2]==gesorteerd[len(rij)-2]:
                    if DEBUG:
                        print("SHORTCUT")
                        rij = omkeren(rij,len(rij)-3,len(rij)-1)
                        print (rij)
                    recept.append((len(rij)-3,len(rij)-1))
                    return recept
            eerste = i
            laatste = rij.index(min(rij[i:]))
            if (eerste == laatste):
                print("STOP",eerste, laatste, rij)
                assert(0)
            rij = omkeren(rij, eerste, laatste)
            if DEBUG:
                print("*", laatste, "(", eerste+1, ",", laatste+1, ")", rij)
            recept.append((eerste,laatste))

    return recept

def findBP(lijst):
    lst = [0]
    for i in xrange(1, len(lijst)):
        if abs(lijst[i-1] - lijst[i]) > 1:
            lst.append(i)
    lst.append(len(lijst))
    return lst

def transform_to_range(rij):
    """
    maak van een oplopende lijst een lijst range(len(rij)) in dezelfde volgorde
    [5, 20, 4, 22, 23, 26, 27, 1, 14, 21]
    wordt:
    [2, 4, 1, 6, 7, 8, 9, 0, 3, 5]
    """
    s = sorted(rij)
    return [s.index(rij[x]) for x in range(len(s))]


def generate_moves(rij):
    """
    genereer alle mogelijke omkeer reversals die minstens 1 minder bp oplevert

    returns: [(aantal bp minder, i, j), ...]
    """
    resultaat = []
    print ("rij = ", rij)
    bp = findBP(rij)
    print("bp = ", bp)
    aantal_bp = len(bp)

    for i in range(aantal_bp):
        for j in range(1,aantal_bp):
            #print (i,j)
            #print (bp[i], bp[j])
            eerste, laatste = bp[i],bp[j]
            if laatste-eerste > 1:
                nw_rij = omkeren(rij, eerste, laatste-1)
                delta = aantal_bp - len(findBP(nw_rij))
                print("nw_Rij", nw_rij, delta)
                if delta > 0:
                    resultaat.append([delta, (eerste, laatste-1)])

    return resultaat


def sort_by_breakpoints(rij):
    pass



if __name__ == '__main__':
    if TEST == 1:
        N = 10
        rij = [5, 20, 4, 22, 23, 26, 27, 1, 14, 21]
    elif TEST == 2:
        N = 10
        rij = range(N)
        random.shuffle(rij)

    elif TEST == 3:
        N = random.randint(2,20)
        rij = list(set([random.randint(0,100) for _ in range(N)]))
        random.shuffle(rij)
    elif TEST == 4:
        N = 10
        rij = [5, 7, 4, 22, 23, 5, 27, 1, 14, 21] # dubbel
    else:
        N = int(raw_input())
        getallen = str(raw_input()).split(' ')
        rij = []
        for getal in getallen:
            if getal != '':
                rij.append(int(getal))
        assert(len(rij) == N)

    if DEBUG:
        print(rij)

    # maak een kopie om te testen
    originele_rij = copy.deepcopy(rij)

    transform_to_range(rij)

    recept = sorteer_naar_achter(rij)
    naam_recept = 'sorteer_naar_achter'

    alt_methods = [sorteer_naar_voor, sorteer_op_lange_afstand]

    for sorteer_methode in alt_methods:
        alternatief = sorteer_methode(rij)
        if len(alternatief) < len(recept):
            recept = alternatief
            naam_recept = sorteer_methode

    if DEBUG:
        check_sorteer_recept(originele_rij, recept)
        print ("winnende methode: ", sorteer_methode)

    io_print(len(recept))
    for (eerste,laatste) in recept:
        io_print(str(eerste+1)+' '+str(laatste+1))
