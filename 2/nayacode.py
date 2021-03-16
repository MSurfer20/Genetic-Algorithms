import numpy as np
from submit import *
import random
import time

parent_range=2
population_size=3
MAX_DEGREE=11
mutation_chance=20
training_weight=0.7
number_of_generations=4
initial_population_type=1
initial_mutation=0.3
mutation=0.1
zero_val_mutation=1e-5
parent_selection_type=1
SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'

def generate_initial_population (given_vector):
    
    return_population=np.zeros((population_size, MAX_DEGREE+2))

    for k in range(population_size):
        trial_arr=np.zeros(MAX_DEGREE+2)
        if initial_population_type:
            trial_arr=np.array([random.uniform(0,1)*1e-6, -random.uniform(0,1)*1e-12, -random.uniform(0,1)*1e-13, random.uniform(0,1)*1e-11, -random.uniform(0,1)*1e-10, -random.uniform(0,1)*1e-15, random.uniform(0,1)*1e-16,random.uniform(0,1)*1e-5, -random.uniform(0,1)*1e-6, -random.uniform(0,1)*1e-8, random.uniform(0,1)*1e-10, 0, 0])
        else:
            for i in range(len(given_vector)):
            
                ch = random.uniform(-initial_mutation,initial_mutation)
                
                if given_vector[i]!=0:
                    trial_arr[i]=given_vector[i]*(1+ch)
                
                else:
                    trial_arr[i]=(random.uniform(-zero_val_mutation, zero_val_mutation))

        return_population[k]=trial_arr
        
    return return_population


def cross_over(parent1, parent2):
    
    child=np.zeros(MAX_DEGREE+2)
    cnt1=0
    cnt2=0

    for i in range(11):
        a=random.randint(0,1)

        if a and cnt1<5:
            child[i]=(parent1[i])
            cnt1=cnt1+1

        elif cnt2<5:
            child[i]=(parent2[i])
            cnt2=cnt2+1

        else:
            child[i]=(parent1[i])
            cnt1=cnt1+1

        chance=random.uniform(1,100)

        if chance<=mutation_chance:
            ch = random.uniform(-mutation,mutation)
            child[i]=child[i]*(1+ch)
            if child[i]==0:
                child[i]=random.uniform(-zero_val_mutation,zero_val_mutation)
        

    return child
        
def get_score(vector):
    score=get_errors(SECRET_KEY, vector.tolist()[:11])
    vector[11]=(score[0])
    vector[12]=(score[1])
    return vector
    
def create_next_gen(population):
    return_population=np.zeros((population_size, MAX_DEGREE+2))
    for i in range(population_size):
        if parent_selection_type:
            par1 = random.randint(0, parent_range-1)
            par2=random.randint(0,parent_range-1)
        else:
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
            # boss+=1
            # if ch[11]<=650000000000 and ch[12]<=650000000000:
            #     return_population.append(ch)
            #     cnt+=1
            # if boss>=150:
            #     break
        ch=cross_over(population[par1], population[par2])
        ch=get_score(ch)
        return_population[i]=(ch)
    return return_population

def get_errors_and_sort(population):
    errors=np.zeros(population_size)
    for i in range(len(population)):
        errors_arr=get_errors(SECRET_KEY, population[i].tolist()[:11])
        population[i][11]=errors_arr[0]
        population[i][12]=errors_arr[1]
        errors[i]=training_weight*errors_arr[0]+errors_arr[1]
    geninds=np.copy(errors.argsort())
    population=np.copy(population[geninds[::1]])
    return population


og_arr=np.array([0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10])

random.seed(time.time())
starting_population=(generate_initial_population(og_arr))
starting_population=get_errors_and_sort(starting_population)
print("generation_1 = ",starting_population)
current_population=starting_population

for gen_number in range(number_of_generations-1):

    parent_for_breeding=[]
    for i in (current_population):
        if (i[11]<=i[12] and 5*i[11]>=i[12]) or (i[12]<=i[11] and 5*i[12]>=i[11]):
            parent_for_breeding.append(i)

    current_population=np.array(parent_for_breeding)

    child_generation=create_next_gen(current_population)

    child_generation=get_errors_and_sort(child_generation)

    print("genration_"+str(gen_number+2),"=",child_generation)
    current_generation=child_generation
