# Informatica Olympiade 2014-15
# Opgave A1 Kerstboom
#
# Voorbeeld
# Invoer: 7
# Uitvoer:
# ------*------
# -----***-----
# ----*****----
# ---*******---
# --*********--
# -***********-
# *************
# ------*------

def kerstboom_rij(n, max):
    return (max-(n+1))*'_'+(2*n+1)*'*'+ (max-(n+1))*'_'

def kerstboom_steel(max):
    return (max-1)*'_'+'*'+ (max-1)*'_'

aantal = int(raw_input('hoeveel rijen?'))

for rij in range(aantal):
    print kerstboom_rij(rij,aantal)

print kerstboom_steel(aantal)
