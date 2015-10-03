# a2.py
import sys

TEST = False

# Uit het voorschrift van de olympiade
def io_print(string):
    sys.stdout.write(str(string) + "\n")
    sys.stdout.flush()

if __name__ == '__main__':

    if TEST:
        naam = 'Anne Louise van der Boom'
    else:
        naam = raw_input()

    delen = naam.upper().split(' ')

    print delen[-1][0]+delen[-1][-1]+delen[0][0]
