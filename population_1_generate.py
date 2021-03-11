from march_test18 import arr
from client import *
gen1=arr

SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'

for i in range(len(gen1)):
    score=get_errors(SECRET_KEY, gen1[i])
    gen1[i].append(score[0])
    gen1[i].append(score[1])

for i in range(len(gen1)):
    for j in range(len(gen1)):
        if gen1[i][11]+gen1[i][12] > gen1[j][11]+gen1[j][12] and i<j:
            xd = gen1[i]
            gen1[i] = gen1[j]
            gen1[j] = xd

print(gen1)
