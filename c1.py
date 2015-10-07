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


def delers(n):
    for i in xrange(2, int(n / 2 + 1)):
        if n % i == 0:
                yield i
    yield n


def codeer(woord):

    woord = list(woord)
    N = len(woord)

    for deler in delers(N):
        regel = []
        counter = 0
        for i in range(deler, N+1, deler):
            if DEBUG:
                print("i = ", i)
            regel.append(woord.pop(i - counter - 1))
            counter += 1
            if DEBUG:
                print(regel, woord)
        woord = regel + woord

    return ''.join(woord)


def decodeer(woord):
    woord = list(woord)
    N = len(woord)

    for deler in reversed(list(delers(N))):

        aantal_letters_eruit = len(range(deler, N+1, deler))
        prefix = woord[0:aantal_letters_eruit]
        rest = list(woord[aantal_letters_eruit:])

        for i, j in enumerate(range(deler, N+1, deler)):
            if DEBUG:
                print("i,j = ", i, j)
                print("prefix = ", prefix[i])

            # voeg de letters op de juiste plaats tussen
            rest[j-1:j-1] = prefix[i]

            if DEBUG:
                print("rest =", rest)

        woord = rest
    return ''.join(woord)


if __name__ == '__main__':
    if TEST == 1:
        woorden = 'MEDAILLESPIEGEL', 'tomkooij', 'testwoord', 'a', 'lettergreep'
        for woord in woorden:
            code = codeer(woord)
            print(code)
            woord2 = decodeer(code)
            print(woord2)
            assert(woord == woord2)
    else:
        woord = raw_input()
        io_print(decodeer(woord))
