import numpy as np
from submit import *
import random
import time

parent_range=2
population_size=3
MAX_DEGREE=11
mutation_chance=90
training_weight=0.7
number_of_generations=4
initial_population_type=1
initial_mutation=0.3
mutation=0.1
zero_val_mutation=1e-5
parent_selection_type=1
overfit_factor=5
mutation_chance_decrease=20
SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'

# This function is used to generate the first generation of a branch, for which further generations are generated using
# a different function. We have tried two approaches to create the first generatiion, both have been briefly explained below -
# 1) This approach generates the first generation by assigning a random number to each
# index which is of the same order as the the index has in the overfit vector given to us.
# 2) This approach generates the inital population by multiplying each index in the given 
# overfit vector by a random number between (1-parameneter) to (1+parameter). We tested with
# a wide range of parameters ranging from 0.7 to 0.01.
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


# This is the cross-over function which is used to generate a child vector for two given parent 
# vectors which are passed to the function as parameters. The child array is calculated by taking
# atleast 5 indices from each of the arrays and then returns both, the non-mutated and mutated array child.
def cross_over(parent1, parent2):
    
    child=np.zeros(MAX_DEGREE+2)
    unmodulated_child=np.zeros(MAX_DEGREE+2)
    cnt1=0
    cnt2=0

    for i in range(MAX_DEGREE):
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
        unmodulated_child[i]=child[i]

        chance=random.uniform(1,100)

        if chance<=mutation_chance:
            ch = random.uniform(-mutation,mutation)
            child[i]=child[i]*(1+ch)
            if child[i]==0:
                child[i]=random.uniform(-zero_val_mutation,zero_val_mutation)

    return (child, unmodulated_child)

# Used to fetch the training and validation/testing error for the vector passed as the parameter.
def get_score(vector):
    score=get_errors(SECRET_KEY, vector.tolist()[:11])
    vector[11]=(score[0])
    vector[12]=(score[1])
    return vector
    
# This function generates a i+1th generation on passing the ith generation as the parameter. We have sorted the 
# arrays on basis seighted sum of training and validation error and taken the top six vectors of the ith generation
# as the parents for the next generations. Two appraches have been followed to generate the next generation.
# 1) This approach assigned weighted probablity to the parents for being selected
# 2) This apprach gives equal probablity to each of the parents for being selected. 
def create_next_gen(population):
    return_population=np.zeros((population_size, MAX_DEGREE+2))
    unmodulated_population=np.zeros((population_size, MAX_DEGREE+2))
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
            # if ch[11]<=650000000000 and ch[12]<=650000000000: # To make sure we only store the good arrays (used for case of high modulation)
            #     return_population.append(ch)
            #     cnt+=1
            # if boss>=150:
            #     break
        ch=cross_over(population[par1], population[par2])
        unmodulated_population[i]=ch[1]
        ch=ch[0]
        ch=get_score(ch)
        return_population[i]=(ch)
    return (return_population, unmodulated_population)

# This function fetches the errors for the first generation formed using generate_inital_population, pushes the 
# errors into the vectors and then sorts the vectors on basis of weighted sum of training and testing errors.
def get_errors_and_sort_initial(population):
    errors=np.zeros(population_size)
    for i in range(len(population)):
        errors_arr=get_errors(SECRET_KEY, population[i].tolist()[:11])
        population[i][11]=errors_arr[0]
        population[i][12]=errors_arr[1]
        errors[i]=training_weight*errors_arr[0]+errors_arr[1]
    geninds=np.copy(errors.argsort())
    population=np.copy(population[geninds[::1]])
    return population

# This function fetches the errors for the later generation formed using create_next_gen, pushes the 
# errors into the vectors and then sorts the vectors on basis of weighted sum of training and testing errors.
def get_errors_and_sort(population, unmodulated_population):
    errors=np.zeros(population_size)
    for i in range(len(population)):
        errors_arr=get_errors(SECRET_KEY, population[i].tolist()[:11])
        population[i][11]=errors_arr[0]
        population[i][12]=errors_arr[1]
        errors[i]=training_weight*errors_arr[0]+errors_arr[1]
    geninds=np.copy(errors.argsort())
    population=np.copy(population[geninds[::1]])
    unmodulated_population=np.copy(unmodulated_population[geninds[::1]])
    return (population, unmodulated_population)


# The original over-fitted vector provided to us. 
og_arr=np.array([0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10])

random.seed(time.time()) # To assure the randomness
starting_population=(generate_initial_population(og_arr)) # Creates the first_generation
starting_population=get_errors_and_sort_initial(starting_population) # Fetches errors for inital population and sort them
print("generation_1 = ",starting_population.tolist()) # Prints the first generation
current_population=starting_population # Setting the ith generation as the first generation

for gen_number in range(number_of_generations-1): # Iterate through each of the generations

    parent_for_breeding=[] # Will store the parents for creating the next generation
    for i in (current_population):
    # Used to make sure any training/testing overfit vector isn't selected as parent
        if (i[11]<=i[12] and overfit_factor*i[11]>=i[12]) or (i[12]<=i[11] and overfit_factor*i[12]>=i[11]):
            parent_for_breeding.append(i)

    current_population=np.array(parent_for_breeding) # Stores the parents of i+th generation

    next_gen_tuple=create_next_gen(current_population) # Gets the ith generation in the form of a tuple whith modulated and unndulated generations

    child_generation=next_gen_tuple[0] # Stores the child generation
    unmodulated_child_generation=next_gen_tuple[1] #Stores the child generation before modulation

    next_gen_tuple=get_errors_and_sort(child_generation, unmodulated_child_generation)
    child_generation=next_gen_tuple[1] # Store sorted child generation(based on the fitness function)
    unmodulated_child_generation=next_gen_tuple[0] # Store sorted unmodulated child generation(based on the fitness function)

    if((gen_number+1)%3==0):
        mutation_chance=max(20, mutation_chance-mutation_chance_decrease) # Reduces the mutation chance with each increasing iteration

    print("unmodulated_genration_"+str(gen_number+2),"=",child_generation.tolist())
    print("genration_"+str(gen_number+2),"=",unmodulated_child_generation.tolist())
    current_population=child_generation
