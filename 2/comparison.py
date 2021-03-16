# from temp import *
# from temp1 import *
# from naya import *
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
# from march_test11 import *
from march_test14 import *
from march_test15 import *
from march_test16 import *
from march_test17 import *
from march_test18 import *
from march_test19 import *
from march_test20 import *
from march_test21 import *

# for i in range(30):
#     print(fifth_gen[i][11], fifth_gen[i][12],'\t',sixth_gen[i][11], sixth_gen[i][12],'\t',seventh_gen[i][11], seventh_gen[i][12],'\t',fifth_gen[i][11]-seventh_gen[i][11], fifth_gen[i][12]-seventh_gen[i][12])

# arr = first_gen + second_gen + third_gen + fourth_gen + fifth_gen +sixth_gen +seventh_gen+eigth_gen+ninth_gen+tenth_gen
# arr = arr + a1+b1+c1+d1+e1+f1+g1
# arr = first_x1+second_x1+third_x1+fourth_x1+fifth_x1+sixth_x1+seventh_x1+eighth_x1+ninth_x1
# arr = arr + first_x2+second_x2+third_x2+fourth_x2+fifth_x2+sixth_x2+seventh_x2+eighth_x2+ninth_x2
# arr = arr + first_x3+second_x3+third_x3+fourth_x3+fifth_x3+sixth_x3+seventh_x3+eighth_x3
# arr = arr + first_x4+second_x4+third_x4+fourth_x4+fifth_x4+sixth_x4+seventh_x4+eighth_x4+ninth_x4+tenth_x4
# arr = arr + first_x5+second_x5+third_x5+fourth_x5+fifth_x5+sixth_x5+seventh_x5+eighth_x5+ninth_x5+tenth_x5
# arr = arr + first_x6+second_x6+third_x6+fourth_x6+fifth_x6+sixth_x6
# arr = arr + first_x7+second_x7+third_x7
# arr = arr + first_x8+second_x8+third_x8+fourth_x8+fifth_x8+sixth_x8+seventh_x8+eighth_x8+ninth_x8+tenth_x8
# arr = arr + first_x9+second_x9+third_x9+fourth_x9+fifth_x9
# arr = arr + first_x10+second_x10+third_x10+fourth_x10+fifth_x10+sixth_x10+seventh_x10+eighth_x10

arr = []
# arr = arr+first_x11+second_x11+third_x11+fourth_x11+fifth_x11+sixth_x11+seventh_x11+eighth_x11+ninth_x11+tenth_x11
# arr = arr+first_x12+second_x12+third_x12+fourth_x12+fifth_x12+sixth_x12+seventh_x12+eighth_x12+ninth_x12+tenth_x12

arr = arr+first_x14+second_x14+third_x14+fourth_x14+fifth_x14#+sixth_x14+seventh_x14+eighth_x14+ninth_x14+tenth_x14
# arr = arr+first_x15+second_x15+third_x15+fourth_x15+fifth_x15+sixth_x15+seventh_x15+eighth_x15+ninth_x15+tenth_x15+eleventh_x15
# arr = arr+first_x16+second_x16+third_x16+fourth_x16+fifth_x16+sixth_x16+seventh_x16+eighth_x16+ninth_x16+tenth_x16
# arr = arr+first_x17+second_x17+third_x17+fourth_x17+fifth_x17+sixth_x17+seventh_x17+eighth_x17+ninth_x17+tenth_x17+eleventh_x17+twelfth_x17+thirteenth_x17
# arr = arr+first_x18+second_x18+third_x18+fourth_x18+fifth_x18
# arr = arr+first_x19+second_x19+third_x19+fourth_x19+fifth_x19+sixth_x19+seventh_x19+eighth_x19+ninth_x19+tenth_x19
# arr = arr+first_x20+second_x20+third_x20+fourth_x20+fifth_x20+sixth_x20+seventh_x20+eighth_x20+ninth_x20+tenth_x20+eleventh_x20
# arr = arr+first_x21+second_x21+third_x21+fourth_x21+fifth_x21+sixth_x21+seventh_x21+eighth_x21+ninth_x21+tenth_x21

# arr=first+second+third+fourth+fifth+sixth+seventh+eighth


for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][11]+arr[i][12] > arr[j][11]+arr[j][12] and i<j:
            xd = arr[i]
            arr[i] = arr[j]
            arr[j] = xd

# cnt=0
# for i in arr:
#     if (i[11]<=i[12] and 1.1*i[11]>=i[12]) or (i[12]<=i[11] and 1.1*i[12]>=i[11]):
#         if cnt >= 80:
#             print(i)
#             print()
#         cnt+=1
#         if cnt == 100:
#             break

# print(cnt)

# for i in range(10,30):
#     print(arr[i])
#     print()
# print(arr[0:9])


################################################################

cnt =0

for i in arr:
    if i[11]<=800000000000 and i[12]<=800000000000:# and i[11]<=10000000000000 and i[12]<=10000000000000:
        cnt=cnt+1
        print(i)
        print()

print(cnt)

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
