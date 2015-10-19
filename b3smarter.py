# b3
# Dit is een implementatie van het LIS (longest increasing subsequence) algoritme
#
# Dit is de O(n**2) versie die alle sub-LIS lijsten bepaald.
#  er is een snellere O(n*log(n)) versie, maar voor N=30 boeit dat niet
#
# algoritme:
# http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming
"""
Oplossing (brute force)
iteratie:  22
(2, 38, 47, 51, 64, 79, 82, 83)
22
"""

from itertools import combinations, izip

test = [4, 7, 5, 0, 3, 2, 6, 9, 1, 8]
test2 = [2, 38, 86, 8, 47, 66, 96, 85, 94, 51, 64, 79, 77, 59, 14, 73, 16]
opgave = [2, 38, 86, 8, 47, 66, 96, 85, 94, 51, 64, 79, 77, 59, 14, 73, 16, 9, 71, 98, 22, 97, 19, 82, 28, 4, 52, 83, 62, 42]

def find_all_lists(rij):
    """
    dynamic programming... vind alle langste rijen
    https://www.youtube.com/watch?v=4fQJGoeW5VE
    """

    langste_rij = [0]*len(rij)
    langste_rij[0] = 1

    for i in range(len(rij)):
        for j in range(i):
            #print "*******", i, rij[i], j, langste_rij[i]
            if ((rij[j] < rij[i]) and (langste_rij[i] < langste_rij[j]+1)):
                langste_rij[i] = langste_rij[j] + 1

    return langste_rij

if __name__ == '__main__':
    rij = opgave
    print rij
    max_lijst = find_all_lists(rij)
    print "m = ", max_lijst
    print "Langste oplopende rij = ", max(max_lijst)
