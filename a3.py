# a3.py
import sys

TEST = 0

# Uit het voorschrift van de olympiade
def io_print(string):
    sys.stdout.write(str(string) + "\n")
    sys.stdout.flush()

def read_list():

    lijst = []

    while 1:
        getal = int(raw_input())
        if getal:
            lijst.append(getal)
        else:
            break
    return lijst

if __name__ == '__main__':

    if TEST:
        getallen = [12,14,77,17,7]
    else:
        getallen = read_list()

    counter = 0

    for getal in getallen:
        # tel de getallen dit deelbaar zijn door 7 of een 7 in het getal hebben
        if (getal % 7 == 0) or (str(getal).find('7') != -1):
            if TEST:
                print "DEBUG: gevonden:" , getal
            counter += 1

    io_print(counter)
