import random
from client import *
from pprint import pprint
import time

def initial_population (given_vector):
    
    return_population=[]

    for k in range(1):
    
        trial_arr = []

        for i in given_vector:
        
            ch = random.uniform(-0.1,0.1)
            
            if i!=0:
                trial_arr.append(i*(1+ch))
            
            else:
                trial_arr.append(random.uniform(-1e-5, 1e-5))

        return_population.append(trial_arr)
        
    return return_population

og_arr=[0]*11 
random.seed(time.time())
print(initial_population(og_arr))
