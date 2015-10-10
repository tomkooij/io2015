afstanden_lijst = [19, 41, 65, 28, 17]+ [22, 46, 33, 16] + [24, 55, 38] + [79, 62] + [17]


for i in range(9):
    for j in range(0, i):
        print(i,j)
        print("removing: ", afstanden_lijst[i]+afstanden_lijst[j])
        try:
            afstanden_lijst.remove(afstanden_lijst[i]+afstanden_lijst[j])
        except ValueError:
            pass

print afstanden_lijst
print "Oplossing: ", len(afstanden_lijst)
print "DIT IS NIET DE JUIST OPLOSSING! Opgave is veel makkelijker met een tekening... :("
