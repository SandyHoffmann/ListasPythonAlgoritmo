pi = 3
for x in range(15):
    ultimotermo = 4+2*x
    print(ultimotermo)
    if x%2==0:
        pi+=(4/((ultimotermo-2)*(ultimotermo-1)*(ultimotermo)))
    else:
        pi-=(4/((ultimotermo-2)*(ultimotermo-1)*(ultimotermo)))

print(pi)