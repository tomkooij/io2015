import itertools

rij = [17, 23, 1, 27, 29, 2, 15] #, 21, 9, 15, 16]

def list_is_ascending(l):
    # adapted from:
    # http://stackoverflow.com/questions/12734178/determine-if-a-list-is-in-descending-order/12734223#12734223
    # Fastest implementation, requires itertools
    return all(earlier >= later for earlier, later in itertools.izip(l, l[1:]))


def streep_weg(lijst, index):

    originele_lijst = list(lijst) # maak kopie

    klaar = False
    vorige = lijst[index]
    print "enter: index, vorige, lijst = ", index, vorige, lijst
    assert(vorige != 'X')
    lijst[index] = 'X'
    index += 1
    while (lijst[index] > vorige):
        vorige = lijst[index]
        lijst[index] = 'X'
        print index, lijst
        index += 1
        if index > len(lijst) - 1:
            print "einde lijst!"
            klaar = True
            break

    print "Decision time @ ", index, lijst

    # als we meer hebben weggestreept dan de lijst toeneemt := break
    if klaar or index > len(lijst)-1:
        # returns het aantal weggestreepte getallen X
        print "klaar:", lijst
        return len([x for x in lijst if x == 'X'])

    print "wegstreep branch", lijst, vorige
    len1 = streep_weg(lijst, index+1)
    index -= 1
    l2 = originele_lijst
    print "returning from wegstreep. index1, index2", index, l2
    # heeft het zin om te branchen?
    if l2[index-1] > l2[index]:
        print "skip branch"
        if index < len(l2)-3:
            len2 = streep_weg(l2, index+2)
            print len2
        else:
            print "einde lijst!"


    print len1

print rij

origineel = list(rij)
streep_weg(origineel, 1)
