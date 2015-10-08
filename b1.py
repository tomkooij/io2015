# opgave B1
import math

lijst_van_bewoners = [(11,54),
            (12,59),
            (12,58),
            (12,55),
            (13,55),
            (13,52),
            (14,50),
            (23,50),
            (24,59),
            (25,52),
            (25,54),
            (25,55),
            (26,53)]


def afstand(x,y,bx,by):
    return math.sqrt((x-bx)**2 + (y-by)**2)

def maak_plaatje(bewoners):
    for y in range(59,49,-1):
        row = str(y)+""
        for x in range(11,27):
            if (x,y) in bewoners:
                row += " X "
            else:
                row += " . "
        print row

if __name__ == '__main__':
    maak_plaatje(lijst_van_bewoners)
    maxlijst = []
    maxl2 = []
    for y in range(59,49,-1):
        for x in range(11,27):
            lijst = []
            for (bx,by) in lijst_van_bewoners:
                lijst.append(afstand(x,y,bx,by))
            maxlijst.append([x,y,max(lijst)])
            maxl2.append(max(lijst))
    print("Oplossing:")
    # Vind MEERDERE MAXIMA!
    my_list = maxl2
    # http://stackoverflow.com/questions/21861730/how-to-find-the-max-numbers-in-a-list-with-tied-numbers
    min_value = min(my_list)
    indices = [i for i in range(len(my_list)) if my_list[i] == min_value]
    for idx in indices:
        print(maxlijst[idx])
