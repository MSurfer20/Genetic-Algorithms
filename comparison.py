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


# Sorted on training, kept parameter = 5 - rank 20 for 10th parent
# Sorted on training, kept parameter = 5 - rank 37 for 5th parent
# Sorted on training, kept parameter = 5 - rank 25 for 1st parent

# Sorted on testing, kept parameter = 5 - rank 15 for 1st parent
# Sorted on testing, kept parameter = 5 - rank 37 for 5th parent
# Sorted on testing, kept parameter = 5 - rank 37 for 10th parent

# Sorted on testing, kept parameter = 3 - rank 77 for 10th parent
# Sorted on testing, kept parameter = 5 - rank 15 for 1st parent

# Sorted on testing, took top 30, sorted on diff of testing and training - rank 15 on 10th parent
# Sorted on testing, took top 30, sorted on diff of testing and training - rank 20 on 1st parent
# Sorted on testing, took top 30, sorted on diff of testing and training - rank 37 on 5th parent



# print(arr[0])

# For temp and temp1
################### 12 - Weird with min testing - [6.101651991514008e-06, -1.2764740103418866e-12, -1.9703439809858206e-13, 4.396430723625485e-11, -7.256876412950873e-11, -1.0739249647595844e-15, 3.658727722774004e-16, 2.9622074287767617e-05, -1.9615179204309246e-06, -1.518516920005905e-08, 8.601004856702239e-10, 194360719320.3122, 75684271432.82758]

# For temp1
################### 65 - Least training - [-5.628275668550069e-06, -3.649639038459907e-13, -2.284393135476573e-13, 1.6289007857915527e-11, -4.717046916285488e-11, -1.8567423416427873e-15, 1.1719879191942962e-15, 1.3152348475013418e-05, -2.04721003e-06, -1.2540395681920438e-08, 1.008303025700666e-09, 80029280323.19698, 450140800022.3739]
################### 7 - Least testing - [-5.741849879962975e-06, -1.89060363589249e-12, -2.309083534343819e-13, 5.1518206432165725e-11, -2.0135985000566238e-10, -2.39775089373808e-15, 3.2404697853493794e-16, 2.842564838110933e-05, -2.169181039257015e-06, -1.3532597385608181e-08, 9.38517230643662e-10, 699701529719.1001, 228405941874.74063]
################### 65 - Least sum - [-5.617409345196591e-06, -3.627089133295798e-13, -1.5366182281525714e-13, 1.616876200286938e-11, -1.7269053205713778e-10, -1.845999084018376e-15, 1.4178096344499785e-15, 1.3233616391550314e-05, -2.031753695181468e-06, -1.2638051723292012e-08, 1.0013250468883223e-09, 89123504082.8116, 418280894404.96155]
################### 63 - Weird with plus - [-5.617409345196591e-06, -3.627089133295798e-13, -1.5366182281525714e-13, 1.616876200286938e-11, -1.7269053205713778e-10, -1.845999084018376e-15, 1.4178096344499785e-15, 1.3233616391550314e-05, -2.031753695181468e-06, -1.2638051723292012e-08, 1.0013250468883223e-09, 89123504082.8116, 418280894404.96155] #

# For temp + message
################### 56 - Least training - [6.696359519152039e-06, -1.6806672425262612e-12, -1.7283379604645672e-13, 4.8440227405759515e-11, -6.777132904317334e-11, -2.246907962703412e-15, 3.2098900729221586e-16, 2.1637286721594793e-05, -1.9908174803216078e-06, -1.519685072881031e-08, 9.787440669746039e-10, 31779421191.48164, 405591026192.2128]
################### 66 - Least testing - [-1.4760294017774943e-05, -1.3954173924818427e-12, -6.446720548201191e-13, 1.8154773387725886e-11, -2.1188553746619404e-10, -1.0675304203627318e-15, 4.0166772590305315e-16, 1.2174935551324621e-05, -8.38603769998493e-07, -3.5190485961969665e-08, 9.411631568970105e-10, 7359117248475.697, 54972882359.971]
################### 16 - Least sum - [6.4442734160126695e-06, -1.2463732938819767e-12, -1.7912928652160854e-13, 3.990379556815055e-11, -7.256876412950873e-11, -1.128505986956859e-15, 3.855466000081844e-16, 2.7105518268805634e-05, -1.918022677712299e-06, -1.648586510957147e-08, 8.952907812465134e-10, 40874176708.45886, 129961018217.7445]
# 62 - Weird with plus - [-5.628275668550069e-06, -3.6586181845792205e-13, -2.284393135476573e-13, 1.6305197645226203e-11, -4.717046916285488e-11, -1.845999084018376e-15, 1.1719879191942962e-15, 1.3338329849650813e-05, -2.0407630665519822e-06, -1.2558584383340146e-08, 1.0001000862567501e-09, 98333613512.30313, 399791308751.3226]
# 65 - Weird - least testing - [-5.571006895572071e-06, -2.01163513551145e-12, -2.282651327247416e-13, 5.159129119294625e-11, -2.0135985000566238e-10, -2.4033228594059976e-15, 1.1815786971896956e-15, 1.2988100497056408e-05, -1.790948368491602e-06, -1.3532597385608181e-08, 9.276134081521192e-10, 296555923317.9643, 247394689786.71967]

# For temp
# 56 - Least training - [6.696359519152039e-06, -1.6806672425262612e-12, -1.7283379604645672e-13, 4.8440227405759515e-11, -6.777132904317334e-11, -2.246907962703412e-15, 3.2098900729221586e-16, 2.1637286721594793e-05, -1.9908174803216078e-06, -1.519685072881031e-08, 9.787440669746039e-10, 31779421191.48164, 405591026192.2128] #
# 10 - Least testing - [6.101651991514008e-06, -1.2764740103418866e-12, -1.9703439809858206e-13, 4.396430723625485e-11, -7.256876412950873e-11, -1.0739249647595844e-15, 3.658727722774004e-16, 2.9622074287767617e-05, -1.9615179204309246e-06, -1.518516920005905e-08, 8.601004856702239e-10, 194360719320.3122, 75684271432.82758] #
################### 16 - Least sum - [6.4442734160126695e-06, -1.2463732938819767e-12, -1.7912928652160854e-13, 3.990379556815055e-11, -7.256876412950873e-11, -1.128505986956859e-15, 3.855466000081844e-16, 2.7105518268805634e-05, -1.918022677712299e-06, -1.648586510957147e-08, 8.952907812465134e-10, 40874176708.45886, 129961018217.7445] #
################### 17 - Weird with plus - [6.4442734160126695e-06, -1.2463732938819767e-12, -1.7912928652160854e-13, 3.990379556815055e-11, -7.256876412950873e-11, -1.128505986956859e-15, 3.855466000081844e-16, 2.7105518268805634e-05, -1.918022677712299e-06, -1.648586510957147e-08, 8.952907812465134e-10, 40874176708.45886, 129961018217.7445] #

# [-9.21638336795256e-06, -1.7687988520056947e-12, -2.204935625994249e-13, 4.3793116957138087e-11, -7.836900651814418e-11, -1.1144395812629652e-15, 3.9450769168451223e-16, 2.7032020511938422e-05, -1.94370446213427e-06, -1.6378170180037386e-08, 9.087764392773309e-10, 39000226076.410065, 208587592039.54865]
# [5.591985036569838e-06, -1.5732644861037622e-12, -1.2586540738798186e-13, 5.508993685740796e-11, -2.345347836605763e-10, -2.1583737575101563e-15, 3.315525502908504e-16, 2.240369111953624e-05, -1.8808495402864136e-06, -1.5154818034574072e-08, 9.134128217572173e-10, 95538034865.65512, 192689393537.75766]