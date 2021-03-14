import random
from client import *
# from gen1 import gen1
# from temp1 import *
from naya import *
from final import *


parent_generation = [para1,para2,pira3,pira4,pira2,pira1]
next_generation = "thirteenth_gen"

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

        if chance<=100:
            ch = random.uniform(-0.5,0.5)
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
    #TODO: SORT ON BASIS OF TRAINING
    cnt=0
    boss=0
    return_population=[]
    while cnt<=16:
        par1 = random.randint(1, 30)
        if par1<=5:
            par1=1
        elif par1<=10:
            par1=2
        elif par1<=15:
            par1=3
        elif par1<=20:
            par1=4
        elif par1<=25:
            par1=5
        else:
            par1=6
        par1-=1
        par2=random.randint(1,30)
        if par2<=5:
            par2=1
        elif par2<=10:
            par2=2
        elif par2<=15:
            par2=3
        elif par2<=20:
            par2=4
        elif par2<=25:
            par2=5
        else:
            par2=6
        par2-=1
        ch=cross_over(population[par1], population[par2])
        ch+=get_errors(SECRET_KEY, ch)
        boss+=1
        if ch[11]<=650000000000 and ch[12]<=650000000000:
            return_population.append(ch)
            cnt+=1
        if boss>=150:
            break
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