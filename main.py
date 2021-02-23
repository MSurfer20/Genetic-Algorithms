from client import *
from csv import writer 
og_arr= [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'
ans=get_errors(SECRET_KEY, og_arr)
with open('tested_vals.csv', 'a') as f_object: 
    writer_object = writer(f_object) 
    writer_object.writerow([og_arr, ans]) 
    f_object.close() 
print([og_arr, ans])
