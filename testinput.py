# controleer of er geen runtimeerror optreed bij inlezen..
from random import randint
N = int(raw_input())
rij = [int(x) for x in str(raw_input()).split(' ')]
print N
for i in range(N):
    print randint(0,10), randint(0,10)
