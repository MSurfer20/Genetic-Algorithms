import random
from client import *
from pprint import pprint
import time

def initial_population (given_vector):
    
    return_population=[]

    for k in range(30):
    
        prob = 90

        trial_arr = []

        for i in given_vector:
            
            random.uniform(1,100)

            chance = random.uniform(1,100)

            if chance <= prob:
                ch = random.uniform(-0.8,0.8)
                if i!=0:
                    trial_arr.append(i*(1+ch))
                else:
                    trial_arr.append(random.uniform(-1e-5, 1e-5))

            else:
                trial_arr.append(i)

        return_population.append(trial_arr)
        # print(trial_arr)
        
    return return_population

og_arr= [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
random.seed(time.time())
print(initial_population(og_arr))
