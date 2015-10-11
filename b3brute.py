#b3 brute force
# flauw maar effectief
"""
iteratie:  20
iteratie:  21
iteratie:  22
(2, 38, 47, 51, 64, 79, 82, 83)
22
"""

from itertools import combinations, izip

test = [17, 23, 5, 18, 20, 25, 21, 9, 15, 16]
test2 = [2, 38, 86, 8, 47, 66, 96, 85, 94, 51, 64, 79, 77, 59, 14, 73, 16]
opgave = [2, 38, 86, 8, 47, 66, 96, 85, 94, 51, 64, 79, 77, 59, 14, 73, 16, 9, 71, 98, 22, 97, 19, 82, 28, 4, 52, 83, 62, 42]

def brute_force(l):
    for DOORHALEN in range(20,30):
        print "iteratie: ", DOORHALEN
        for comb in combinations(l,len(l)-DOORHALEN):
            #print comb
            if all(eerste < tweede for eerste, tweede in izip(comb, comb[1:])):
                print comb
                print "antwoord: Aantal getallen doorstrepen: ", DOORHALEN
                assert(0)

if __name__ == '__main__':
    print opgave
    assert(len(opgave)==30)
    #brute_force()
