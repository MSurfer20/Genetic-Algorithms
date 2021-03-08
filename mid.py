# from temp import *
# from temp1 import *
from naya import *
# from march_test1 import *
# from march_test2 import *
# from march_test3 import *
# from march_test4 import *
# from march_test5 import *
# from march_test6 import *
# from march_test7 import *
# from march_test8 import *
# from march_test9 import *
# from march_test10 import *

# for i in range(30):
#     print(fifth_gen[i][11], fifth_gen[i][12],'\t',sixth_gen[i][11], sixth_gen[i][12],'\t',seventh_gen[i][11], seventh_gen[i][12],'\t',fifth_gen[i][11]-seventh_gen[i][11], fifth_gen[i][12]-seventh_gen[i][12])

# arr = first_gen + second_gen + third_gen + fourth_gen + fifth_gen +sixth_gen +seventh_gen+eigth_gen+ninth_gen+tenth_gen
# arr = arr + a1+b1+c1+d1+e1+f1+g1
# arr = arr+ first_x1+second_x1+third_x1+fourth_x1+fifth_x1+sixth_x1+seventh_x1+eighth_x1+ninth_x1
# arr = arr + first_x2+second_x2+third_x2+fourth_x2+fifth_x2+sixth_x2+seventh_x2+eighth_x2+ninth_x2
# arr = arr + first_x3+second_x3+third_x3+fourth_x3+fifth_x3+sixth_x3+seventh_x3+eighth_x3
# arr = arr + first_x4+second_x4+third_x4+fourth_x4+fifth_x4+sixth_x4+seventh_x4+eighth_x4+ninth_x4+tenth_x4
# arr = arr + first_x5+second_x5+third_x5+fourth_x5+fifth_x5+sixth_x5+seventh_x5+eighth_x5+ninth_x5+tenth_x5
# arr = arr + first_x6+second_x6+third_x6+fourth_x6+fifth_x6+sixth_x6
# arr = arr + first_x7+second_x7+third_x7
# arr = arr + first_x8+second_x8+third_x8+fourth_x8+fifth_x8+sixth_x8+seventh_x8+eighth_x8+ninth_x8+tenth_x8
# arr = arr + first_x9+second_x9+third_x9+fourth_x9+fifth_x9
# arr = arr + first_x10+second_x10+third_x10+fourth_x10+fifth_x10+sixth_x10+seventh_x10+eighth_x10
# arr=first+second+third+fourth+fifth+sixth+seventh+eighth

arr = first1_gen+second1_gen+third1_gen#+[one,two,three,four,five]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][12] > arr[j][12] and i<j:
            xd = arr[i]
            arr[i] = arr[j]
            arr[j] = xd

cnt=0
for i in arr:
    if (i[11]<=i[12] and 2*i[11]>=i[12]) or (i[12]<=i[11] and 2*i[12]>=i[11]):
        print(i)
        print()
        cnt+=1
        if cnt>=10:
            break
print(cnt)

# for i in range(10,30):
#     print(arr[i])
#     print()
# print(arr[0:9])


################################################################

# cnt =0

# for i in arr:
#     if i[11]<=200000000000 and i[12]<=200000000000:
#         cnt=cnt+1
#         print(i)

# print(cnt)
# print(arr[:6])
# for i in range(6):
#     print(arr[i])
#     print()

################################################################

# cnt=0
# lol = []

# for i in range(len(arr)):
#     cnt=cnt+1
#     lol.append(arr[i])
#     if cnt==30:
#         break
# lol=[]
# for i in range(len(lol)):
#     for j in range(len(lol)):
#         if abs(lol[i][12]-lol[i][11]) > abs(lol[j][12]-lol[j][11]) and i<j:
#             xd = lol[i]
#             lol[i] = lol[j]
#             lol[j] = xd

# for i in range(6):
#     print(arr[i])
#     print()

# print(lol[7])

###############################################################

# cnt =0 

# for i in arr:
#     if i[11]<=i[12]:
#         cnt=cnt+1
#         if cnt == 2:
#             print(i)
#             exit()

