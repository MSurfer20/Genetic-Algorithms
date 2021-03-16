import client
import submit
# from march_test22 import *

# print(len(twelfth_gen))

SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'
jai_mata_di = [3.556696343267478e-07, -3.529062546606351e-13, -5.451401585449298e-14, 6.8459409900641435e-12, -1.982128358625292e-11, -4.2310106815257504e-16, 2.0432185799129026e-18, 4.107275855871576e-06, -4.404992791173524e-07, -2.3980513913450297e-10, 1.1075227979499961e-10, 477414168225.589, 452363926969.6763]

jai_mata_di=jai_mata_di[:11]

# for arr in twelfth_gen:
#     jai_mata_di = arr
#     # jai_mata_di=jai_mata_di[:11]
#     submit.submit(SECRET_KEY, jai_mata_di[:11])
#     print(jai_mata_di)
#     input()

# score = submit.get_errors(SECRET_KEY, jai_mata_di)
# print(score)
# print()

# for i in range(11):

#     lol = jai_mata_di
#     print("At index",i,"x1.03")
#     lol[i]=lol[i]*1.03
#     score = submit.get_errors(SECRET_KEY, jai_mata_di)
#     print(score)
#     print()
    
#     lol = jai_mata_di
#     print("At index",i,"/1.03")
#     lol[i]=lol[i]/1.03
#     score = submit.get_errors(SECRET_KEY, jai_mata_di)
#     print(score)
#     print()

submit.submit(SECRET_KEY, jai_mata_di)
score = submit.get_errors(SECRET_KEY, jai_mata_di)
print(score)