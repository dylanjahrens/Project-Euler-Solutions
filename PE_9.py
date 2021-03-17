# a > b > c
# a**2 + b**2 = c**2
# a + b + c = 1000

import math
a=3
b=4
c=5
asquared = []
bsquared = []
csquared = []

for c in range(5,1000):
    csquared.append(c**2)

for a in range(5,1000):
    asquared.append(a**2)

for b in range(5,1000):
    bsquared.append(b**2)

for x in asquared:
    for y in bsquared:
        z=x+y
        if z in csquared and math.sqrt(x) + math.sqrt(y) + math.sqrt(z) == 1000 and x<y<z:
            print(math.sqrt(x), math.sqrt(y), math.sqrt(z))
            print("Total product: ", (math.sqrt(x) * math.sqrt(y) * math.sqrt(z)))
        
            break
        