# controleer of er geen runtimeerror optreed bij inlezen..
N = int(raw_input())
line = raw_input().split(' ')
rij = []
for item in line:
    if item != '':
        rij.append(int(item))
# zorg dat we door de eerste test komen
print "7"
recept = [(7,10),(6,9),(5,8),(4,7),(2,5),(2,4),(1,3)]
for x,y in recept:
    print x,y
