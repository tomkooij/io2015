# test Bord class form board.py

from board import *
from random import randint

def test_schuiven():
    b = Bord([[1,-1,0,0],[1,0,0,-1],[-1,1,1,0],[-1,0,0,0]])
    b.show()
    print "R:"
    b.move(RIGHT)
    b.show()
    print b._free_squares()
    print "L:"
    b.move(LEFT)
    b.show()
    print "Up:"
    b.move(UP)
    b.show()
    print "Down:"
    b.move(DOWN)
    b.show()
    print "Left"
    b.move(LEFT)
    b.show()

def test_random_moves():
    b = Bord([[1,-1,0,0],[1,0,0,-1],[-1,1,1,0],[-1,0,0,0]])
    for _ in range(2):
        print "random RED: ",
        print b.place_random_tile(RED)
        b.show()
        print "random BLUE: ",
        print b.place_random_tile(BLUE)
        b.show()
        direction = randint(1,4)
        print "random shift: ", direction
        b.move(direction)
        b.show()

def test_game():
    """
    testgame from caia
    """

    MOVES=['12', '33', '22', '11', 'R', 'L', '22', '41', '42', '12', 'U', 'R', '31', '33', '11', '41', 'R', 'D', '13', '21', '41', '32', 'U', 'D', '21', '23', '13', '22', 'U', 'D', '12', '23', '13', '22', 'R', 'U', '11', '44', '33', '43', 'D', 'R', '12', '41', '32', '13', 'R', 'L', '24', '34', '14', '23', 'R', 'U', '44', '32', '41', '33', 'U', 'D', '14', '31', '33', '13', 'R', 'U', '41', '23', '44', '31', 'U', 'R', '43', '32', '23', '41', 'R', 'L', '24', '33', '43', '42', 'U', 'L', '34', '43', '24', '32', 'R', 'R', '41', '43', '32', '31', 'D', 'U', '21', '34', '41', '31', 'R', 'L', '34', '42', '33', '32', 'U', 'R', '42', '31', '11', '21', 'D', 'U', '31', '44', '21', '41', 'U', 'L', '33', '42', '34', '23', 'L', 'R', '42', '43', '21', '32', 'L', 'R', '43', '41', '31', '42', 'U', 'D', '12', '14', '21', '22', 'L', 'U', '14', '43', '34', '24', 'L', 'D', '24', '11', '13', '34', 'R', 'L', '13', '14', '24', '34', 'D', 'U', '42', '34', '44', '33', 'R', 'U', '43', '21', '41', '44', 'R', 'L', '23', '33', '44', '13', 'D', 'U', '33', '24', '34', '43', 'L', 'R', '12', '21', '11', '32', 'U', 'D', '11', '42', '32', '13', 'U', 'L', '33', '24', '34', '44', 'R', 'L', '33', '42', '34', '43', 'U', 'R', '31', '43', '42', '41', 'R', 'U', '42', '41'];

    U = UP
    D = DOWN
    R = RIGHT
    L = LEFT

    b = Bord()
    b.show()
    print "Start!"
    color = 1   # rood eerst
    for move in MOVES:
        print "Move : ", move
        if move in ['U', 'D', 'R', 'L']:
            b.move(move)
        else:
            b.place(move[0], move[1], color)
            color = -color  # de ander is nu aan zet
        b.show
        raw_input()



if __name__ == '__main__':
    test_random_moves()
