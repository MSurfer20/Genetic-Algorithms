import random
from client import *
# from gen1 import gen1
# from temp1 import *
from naya import *



parent_generation = [one,two,three,four,five]
next_generation = "first_gen"

# SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'

def cross_over(parent1, parent2):
    
    child=[]

    for i in range(11):
        a=random.randint(0,1)
        if a:
            child.append(parent1[i])
        else:
            child.append(parent2[i])

        chance=random.uniform(1,100)

        if chance<=40:
            ch = random.uniform(-0.01,0.01)
            child[i]=child[i]*(1+ch)

    return child
        
def get_score(vector):
    score=get_errors(SECRET_KEY, vector)
    vector.append(score[0])
    vector.append(score[1])
    return vector
    
def create_next_gen(population):
    #TODO: SORT ON BASIS OF TRAINING
    return_population=[]
    for i in range(16):
        par1 = random.randint(1, 23)
        if par1<=5:
            par1=1
        elif par1<=10:
            par1=2
        elif par1<=15:
            par1=3
        elif par1<=19:
            par1=4
        elif par1<=23:
            par1=5
        par1-=1
        par2=random.randint(1,23)
        if par2<=5:
            par2=1
        elif par2<=10:
            par2=2
        elif par2<=15:
            par2=3
        elif par2<=19:
            par2=4
        elif par2<=23:
            par2=5
        par2-=1
        ch=cross_over(population[par1], population[par2])
        ch+=get_errors(SECRET_KEY, ch)
        return_population.append(ch)
    #sort
    return return_population


for i in range(len(parent_generation)):
    for j in range(len(parent_generation)):
        if parent_generation[i][11] > parent_generation[j][11] and i<j:
            xd = parent_generation[i]
            parent_generation[i] = parent_generation[j]
            parent_generation[j] = xd

            
child_generation=create_next_gen(parent_generation)

for i in range(len(child_generation)):
    for j in range(len(child_generation)):
        if child_generation[i][11] > child_generation[j][11] and i<j:
            xd = child_generation[i]
            child_generation[i] = child_generation[j]
            child_generation[j] = xd
            
print(next_generation,"=",child_generation)