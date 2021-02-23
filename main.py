import random
from client import *
from csv import writer
import csv
from super50 import arr

og_arr= [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
# SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'
curr_population=[]
with open('tested_vals.csv', newline='') as csvfile:
    curr_population+=list(csv.reader(csvfile))
# print(curr_population)
curr_population=arr
print(arr)
##########################################################################################################################################


def initial_population (given_vector):
    
    return_population=[]

    for k in range(20):
    
        prob = 75

        trial_arr = []

        for i in given_vector:

            chance = random.randint(1,100)

            if chance < prob:
                trial_arr.append(random.uniform(-10,10))

            else:
                trial_arr.append(i)

        return_population.append(trial_arr)
    return return_population

def get_total_error(error_arr):
    return error_arr[0]

def cross_over(parent1, parent2):
    child=[]
    print(parent1)
    for i in range(len(parent1)):
        a=random.randint(0,1)
        if a:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
        

def get_score(population):
    return_arr=[]
    for each_arr in population:
        score=get_errors(SECRET_KEY, each_arr)
        return_arr.append([each_arr, score])
        insert_csv(each_arr, score)
        print(each_arr, score)
    return return_arr
        

def insert_csv(current_arr, score):
    with open('tested_vals.csv', 'a') as f_object: 
        writer_object = writer(f_object) 
        writer_object.writerow([current_arr, score]) 
        f_object.close()

def create_next_gen(population):
    training_dict={}
    testing_dict={}
    for i in population:
        # print(i[2])
        training_dict[i[0]]=i[1]
        training_dict[i[0]]=i[2]
    sorted_d={k: v for k, v in sorted(training_dict.items(), key=lambda item: item[1])}
    for i in range(50):
        par1 = random.randint(0, 9)
        par2=random.randint(0,9)
        ch=cross_over(list(sorted_d.keys())[par1], list(sorted_d.keys())[par2])
        get_score(ch)

##########################################################################################################################################


# curr_population=initial_population(og_arr)
# print(curr_population)
# create_next_gen(curr_population)