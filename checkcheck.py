import client
import submit
from march_test22 import *

print(len(twelfth_gen))

SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'
jai_mata_di = [6.101651991514008e-06, -1.2764740103418866e-12, -1.9703439809858206e-13, 4.396430723625485e-11, -7.256876412950873e-11, -1.0739249647595844e-15, 3.658727722774004e-16, 2.9622074287767617e-05, -1.9615179204309246e-06, -1.518516920005905e-08, 8.601004856702239e-10]

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
# score = submit.get_errors(SECRET_KEY, jai_mata_di)
# print(score)

#********** 59 - 7967592426596.318 - [6.101651991514008e-06, -1.2764740103418866e-12, -1.9703439809858206e-13, 4.396430723625485e-11, -7.256876412950873e-11, -1.0739249647595844e-15, 3.658727722774004e-16, 2.9622074287767617e-05, -1.9615179204309246e-06, -1.518516920005905e-08, 8.601004856702239e-10, 194360719320.3122, 75684271432.82758]
#********** 61 - ?????????? 16050169990590.684 - [7.3000149385339486e-06, -1.4508582334938624e-12, -1.7446896418754742e-13, 5.109944355076077e-11, -2.5448794058714256e-10, -1.1658376910672744e-15, 3.1827015830354867e-16, 2.502027767038304e-05, -1.9664311146400523e-06, -1.4730561693079958e-08, 8.945619840357268e-10, 88113858040.47986, 127558862768.52084]
#********** 62 - 15598482203701.885 - [7.236287049225701e-06, -1.445911565527231e-12, -1.7498772740084537e-13, 5.109944355076077e-11, -2.5430545472048434e-10, -1.1709514644876058e-15, 3.210132219509301e-16, 2.502027767038304e-05, -1.975229899156637e-06, -1.4769695480936238e-08, 8.945619840357268e-10, 135323228000.64511, 130464457208.5385]

# Big error arrays
#?????????? 46 - 6099687402990.945 - [-6.343240178512456e-06, -2.5692378099176043e-12, -2.672944146830604e-13, 7.408804733142116e-11, -2.700989039764157e-10, -1.81908085976778e-15, 1.0399915397184073e-15, 2.4351418265881644e-05, -2.3350714908429875e-06, -1.321712429352243e-08, 9.942363065575206e-10, 1724039813384.2522, 1930285565731.3062]
#********** 46 - 6008097001454.215 - [-6.262654719739863e-06, -2.5724228747664743e-12, -1.383517203908993e-13, 6.793446936872744e-11, -2.700989039764157e-10, -9.135874787154603e-16, 1.279142274595691e-15, 2.418590618371933e-05, -2.3535081066451473e-06, -1.3279865562160824e-08, 9.98214034e-10, 1105873936351.0945, 1444544751168.535]
# 44 -  MUTAT 4778408037737.365  - [-1.3117582113612693e-06, -2.5724228747664743e-12, -1.383517203908993e-13, 6.793446936872744e-11, -1.724429917251298e-10, -9.181290594676944e-16, 1.279142274595691e-15, 2.4214954007825292e-05, -2.3535081066451473e-06, -1.2489939325062837e-08, 9.98214034e-10, 687874426406.4147, 713248175540.8792]

# 72 - 22553712588336.727 - [6.4442734160126695e-06, -1.2463732938819767e-12, -1.7912928652160854e-13, 3.990379556815055e-11, -7.256876412950873e-11, -1.128505986956859e-15, 3.855466000081844e-16, 2.7105518268805634e-05, -1.918022677712299e-06, -1.648586510957147e-08, 8.952907812465134e-10, 40874176708.45886, 129961018217.7445]
# 71 - 21737133950275.395 - [5.591985036569838e-06, -1.582675728169255e-12, -1.7359285477580936e-13, 5.508993685740796e-11, -2.5320893657294154e-10, -2.1583737575101563e-15, 3.210132219509301e-16, 2.511654073479438e-05, -1.965555797894771e-06, -1.5140087108671845e-08, 9.214909160927855e-10, 154168790181.56195, 151975095946.00134]

# No proof arrays
# Cheating - [0, -1.445911565527231e-12, -1.7498772740084537e-13, 5.109944355076077e-11, -2.5430545472048434e-10, -1.1709514644876058e-15, 3.210132219509301e-16, 3.902027767038304e-05, -1.975229899156637e-06, -1.4769695480936238e-08, 8.945619840357268e-10]
# CHUMTIYA -errors [99871865434.22476, 123933224114.80229]  15104431334584.479 - [6.525636151737385e-10, -1.5516831882387681e-12, -1.7065883936338436e-13, 4.6265959327559024e-11, -2.669670220497726e-10, -1.0739249647595844e-15, 9.085513864943156e-16, 2.5963751617497686e-05, -1.9757021060346726e-06, -1.5031696163247858e-08, 8.945619840357268e-10]
#********** RANK 29 BESHT HAI - VERY NICE 3005858292076.3022 [664104919915.0051, 640897827580.1987] [-1.3117582113612693e-06, -2.5724228747664743e-12, -1.383517203908993e-13, 6.793446936872744e-11, -1.724429917251298e-10, -9.181290594676944e-16, 1.279142274595691e-15, 2.8214954007825292e-05, -2.3535081066451473e-06, -1.2489939325062837e-08, 9.98214034e-10]
#********** 3957180759857.25 - all errors are equalist - [-7.518617150813274e-10, -1.3367571219929618e-12, -2.500979117749022e-13, 4.433999719625366e-11, -1.877519819191411e-10, -4.083574991568985e-15, 7.467092268737589e-16, 4.2152693452009957e-05, -2.3059598804836114e-06, -1.3162301564494056e-08, 9.90074739616953e-10]


#********** RANK 38 CLOSE ERRORS - [2015318183614.3386, 2349389445115.3633] 5953455246313.916 [2.1175328577299415e-10, -1.6907719215642795e-12, -2.7352272011324796e-13, 5.0661196238540214e-11, -2.0780774158604122e-10, -1.781138167003089e-15, 8.836470142939426e-16, 2.4862401368953688e-05, -2.3073029287752947e-06, -1.3548657768450628e-08, 9.78214034e-10]
#********** RANK 35 - [2634464631713.647, 3276198210982.946] 5184022312492.341 [2.1175328577299415e-10, -1.6907719215642795e-12, -2.7352272011324796e-13, 5.0661196238540214e-11, -2.0780774158604122e-10, -1.781138167003089e-15, 8.836470142939426e-16, 2.4862401368953688e-05, -2.3073029287752947e-06, -1.3548657768450628e-08, 9.68214034e-10]
#********** RANK 33 - [2141767587556.8645, 2410514338241.423] 4585913600003.684 [2.1175328577299415e-10, -1.6907719215642795e-12, -2.7352272011324796e-13, 5.0661196238540214e-11, -2.0780774158604122e-10, -1.781138167003089e-15, 8.836470142939426e-16, 2.5862401368953688e-05, -2.3073029287752947e-06, -1.3548657768450628e-08, 9.68214034e-10]
#********** RANK 36 - [3447050048208.796, 4578024420490.268] 6112120251531.787  [2.1175328577299415e-10, -1.6907719215642795e-12, -2.7352272011324796e-13, 5.0661196238540214e-11, -2.0780774158604122e-10, -1.781138167003089e-15, 3.236470142939426e-16, 2.5862401368953688e-05, -2.3073029287752947e-06, -1.4548657768450628e-08, 9.68214034e-10]

#********** RANK 44 - [1033474822589.9867, 1525732864221.8857] 7832808102482.3955 [2.817755644784455e-06, -1.0119742550997892e-12, -2.844979480163992e-13, 4.126650026509282e-11, -1.2662668861856032e-10, -2.8974126006394015e-15, 9.42939053120434e-16, 2.496438570638627e-05, -1.711417815905163e-06, -4.974633322260416e-09, 6.465953256202544e-10]
#********** RANK 37 - [1285378967855.8164, 3033072312909.3604] 5952109577079.635  [2.817755644784455e-06, -1.0119742550997892e-12, -2.844979480163992e-13, 4.126650026509282e-11, -1.2662668861856032e-10, -2.8974126006394015e-15, 9.42939053120434e-16, 2.496438570638627e-05, -1.711417815905163e-06, -4.974633322260416e-09, 6.665953256202544e-10]
#********** RANK 31 - [1900354940144.3481, 5227298407555.233] 4366991498050.04   [2.817755644784455e-06, -1.0119742550997892e-12, -2.844979480163992e-13, 4.126650026509282e-11, -1.2662668861856032e-10, -2.8974126006394015e-15, 9.42939053120434e-16, 2.496438570638627e-05, -1.711417815905163e-06, -4.974633322260416e-09, 6.865953256202544e-10]
#DECENT
# [2.817755644784455e-06, -1.0119742550997892e-12, -2.844979480163992e-13, 4.126650026509282e-11, -1.2662668861856032e-10, -2.8974126006394015e-15, 9.42939053120434e-16, 2.496438570638627e-05, -1.711417815905163e-06, -4.974633322260416e-09, 5.465953256202544e-10]



#********** 7714006448736.948 - [2.1175328577299415e-10, -1.6907719215642795e-12, -2.7352272011324796e-13, 5.0661196238540214e-11, -2.0780774158604122e-10, -1.781138167003089e-15, 8.836470142939426e-16, 2.4862401368953688e-05, -2.3073029287752947e-06, -1.3548657768450628e-08, 9.98214034e-10, 1049329157682.7354, 1010936897849.0107]






# THIRD BATCH
# RANK 49 - 18165836782803.96[-7.450161173321208e-10, -1.3367571219929618e-12, -2.500979117749022e-13, 4.433999719625366e-11, -1.877519819191411e-10, -2.0968757702013353e-15, 7.467092268737589e-16, 2.1019467074962244e-05, -2.1661404016251173e-06, -1.3062301564494056e-08, 9.942128049660624e-10, 201960558984.41663, 263902255707.94092]


#********** Rank 49 - [-7.518617150813274e-10, -1.3367571219929618e-12, -2.500979117749022e-13, 4.433999719625366e-11, -1.877519819191411e-10, -2.083574991568985e-15, 7.467092268737589e-16, 2.2152693452009957e-05, -2.1859598804836114e-06, -1.3062301564494056e-08, 9.90074739616953e-10, 276746294786.2581, 264874462268.0191]