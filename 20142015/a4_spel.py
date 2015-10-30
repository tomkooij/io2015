# Informatica Olympiade 2014-15
# Opgave A3. Je naam
# Schrijf een programma dat een naam inleest van standard input.
# Het programma schrijft vier regels uitvoer naar standard output.
# ? Op de eerste regel staat uit hoeveel tekens de invoer bestaat.
# ? Op de tweede regel staat hoeveel hoofdletters in de invoer voorkomen.
# ? Op de derde regel staat hoeveel verschillende tekens in de invoer voorkomen.
# ? Op de vierde regel staat de naam, maar dan achterstevoren weergegeven.
# Voorbeeld:
# Invoer: Anne van der Boom
# Uitvoer: 17
# 2
# 11
# mooB red nav ennA

naam = raw_input()
#naam = 'Anne van der Boom'

# 1 lengte:
print len(naam)
# 2 aantal hoofdletters:
print sum([c.isupper() for c in naam])
# 3 verschillende tekens:
print len(set(naam))
# 4 achterstevoren:
print naam[::-1]
