# Informatica Olympiade 2014-15
# Opgave A2 Som kwadraten
#
# Schrijf een programma dat van standard input gehele niet-negatieve getallen inleest, tot er een 0
# wordt ingelezen. Het programma schrijft ��n regel uitvoer naar standard output; daarop staat de
# som van de kwadraten van de oneven getallen in de invoer.
# Voorbeeld
# Invoer: 12
# 9
# 6
# 3
# 0
# Uitvoer: 90

invoer = 999
som = 0

while invoer != 0:
    invoer = int(raw_input())
    if (invoer % 2) == 1:
        # oneven
        som += invoer**2
        #print "debug: deze is oneven, som is nu: ", som

print som
