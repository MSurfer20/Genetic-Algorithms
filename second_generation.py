import random
from submit import *
from march_test12 import *

parent_generation = third_x12
next_generation = "fourth_x12"

SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'

def cross_over(parent1, parent2):
    
    child=[]
    cnt1=0
    cnt2=0

    for i in range(11):

        a=random.randint(0,1)

        if a and cnt1<5:
            child.append(parent1[i])
            cnt1=cnt1+1

        elif cnt2<5:
            child.append(parent2[i])
            cnt2=cnt2+1

        else:
            child.append(parent1[i])
            cnt1=cnt1+1

        chance=random.uniform(1,100)

        if chance<=20:
            ch = random.uniform(-0.01,0.01)
            child[i]=child[i]*(1+ch)
            if child[i]==0:
                child[i]=random.uniform(-1e-5,1e-5)

    return child
        
def get_score(vector):
    score=get_errors(SECRET_KEY, vector)
    vector.append(score[0])
    vector.append(score[1])
    return vector
    
def create_next_gen(population):
    return_population=[]
    for i in range(30):
        par1 = random.randint(0, 5)
        par2=random.randint(0,5)
        ch=cross_over(population[par1], population[par2])
        ch=get_score(ch)
        return_population.append(ch)
    #sort
    return return_population


for i in range(len(parent_generation)):
    for j in range(len(parent_generation)):
        if 0.7*parent_generation[i][11]+parent_generation[i][12] > 0.7*parent_generation[j][11]+parent_generation[j][12] and i<j:
            xd = parent_generation[i]
            parent_generation[i] = parent_generation[j]
            parent_generation[j] = xd

parent_for_breeding=[]
for i in (parent_generation):
    if (i[11]<=i[12] and 5*i[11]>=i[12]) or (i[12]<=i[11] and 5*i[12]>=i[11]):
        parent_for_breeding.append(i)

parent_generation=parent_for_breeding

child_generation=create_next_gen(parent_generation)

for i in range(len(child_generation)):
    for j in range(len(child_generation)):
        if 0.7*child_generation[i][12]+child_generation[i][11] > 0.7*child_generation[j][12]+child_generation[j][11] and i<j:
            xd = child_generation[i]
            child_generation[i] = child_generation[j]
            child_generation[j] = xd
            
print(next_generation,"=",child_generation)

