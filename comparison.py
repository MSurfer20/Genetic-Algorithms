from temp1 import *

# for i in range(30):
#     print(fifth_gen[i][11], fifth_gen[i][12],'\t',sixth_gen[i][11], sixth_gen[i][12],'\t',seventh_gen[i][11], seventh_gen[i][12],'\t',fifth_gen[i][11]-seventh_gen[i][11], fifth_gen[i][12]-seventh_gen[i][12])

# mx = 100000000000000000000

arr = first_gen + second_gen + third_gen + fourth_gen + fifth_gen +sixth_gen +seventh_gen #+eigth_gen +ninth_gen +tenth_gen

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][11] > arr[j][11] and i<j:
            xd = arr[i]
            arr[i] = arr[j]
            arr[j] = xd

for i in range(len(arr)):
    if arr[i][12] < arr[i][11]*8:
        print(arr[i][11], arr[i][12])