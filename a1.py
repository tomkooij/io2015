# Opgave A1
from __future__ import division

import sys

TEST = False

DASH = '-'
STAR = '*'


# Uit het voorschrift van de olympiade
def io_print(string):
    sys.stdout.write(str(string) + "\n")
    sys.stdout.flush()


def print_halter(N):

    number_of_lines = 2 * N - 1
    halter = []

    # generate and print the top part of the "halter"
    for linenumber in range(int(number_of_lines / 2) + 1):
        number_of_stars = int(number_of_lines - 2 * linenumber)
        line = linenumber * DASH + number_of_stars * STAR + linenumber * DASH
        io_print(line)
        if number_of_stars > 1:
            halter.append(line)

    # pop the lines in reverse order to print the bottom part "halter"
    for _ in range(len(halter)):
        io_print(halter.pop())

if __name__ == '__main__':
    if TEST:
        for N in range(1, 42):
            print("N = ", N)
            print_halter(N)
    else:
        N = int(raw_input(""))
        print_halter(N)
