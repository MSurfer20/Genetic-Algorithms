from temp import *
from temp1 import *

# for i in range(30):
#     print(fifth_gen[i][11], fifth_gen[i][12],'\t',sixth_gen[i][11], sixth_gen[i][12],'\t',seventh_gen[i][11], seventh_gen[i][12],'\t',fifth_gen[i][11]-seventh_gen[i][11], fifth_gen[i][12]-seventh_gen[i][12])

arr = first_gen + second_gen + third_gen + fourth_gen + fifth_gen +sixth_gen +seventh_gen+eigth_gen+ninth_gen+tenth_gen+a1+b1+c1+d1+e1+f1+g1

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][12]+arr[i][11] > arr[j][12]+arr[j][11] and i<j:
            xd = arr[i]
            arr[i] = arr[j]
            arr[j] = xd

cnt=0
for i in arr:
    if (i[11]<=i[12] and 3.5*i[11]>=i[12]) or (i[12]<=i[11] and 3.5*i[12]>=i[11]):
        print(i)
        cnt+=1
        if cnt>=10:
            break
print(cnt)


################################################################

# cnt =0

# for i in arr:
#     if i[11]<=150000000000 and i[12]<=190000000000:
#         cnt=cnt+1
#         print(i)

# print(cnt)


################################################################

# cnt=0
# lol = []

# for i in range(len(arr)):
#     cnt=cnt+1
#     lol.append(arr[i])
#     if cnt==30:
#         break

# for i in range(len(lol)):
#     for j in range(len(lol)):
#         if abs(lol[i][12]-lol[i][11]) > abs(lol[j][12]-lol[j][11]) and i<j:
#             xd = lol[i]
#             lol[i] = lol[j]
#             lol[j] = xd

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