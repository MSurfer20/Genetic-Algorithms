from gen1 import gen1
from client import *

SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'

for i in range(len(gen1)):
    score=get_errors(SECRET_KEY, gen1[i])
    gen1[i].append(score[0])
    gen1[i].append(score[1])

print(gen1)
