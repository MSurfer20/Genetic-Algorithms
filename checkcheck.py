import client
import submit
SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'
jai_mata_di = [5.591985036569838e-06, -1.582675728169255e-12, -1.7359285477580936e-13, 5.508993685740796e-11, -2.5320893657294154e-10, -2.1583737575101563e-15, 3.210132219509301e-16, 2.511654073479438e-05, -1.965555797894771e-06, -1.5140087108671845e-08, 9.214909160927855e-10]

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


score = submit.submit(SECRET_KEY, jai_mata_di)
score = submit.get_errors(SECRET_KEY, jai_mata_di)
print(score)


# 7967592426596.318 - [6.101651991514008e-06, -1.2764740103418866e-12, -1.9703439809858206e-13, 4.396430723625485e-11, -7.256876412950873e-11, -1.0739249647595844e-15, 3.658727722774004e-16, 2.9622074287767617e-05, -1.9615179204309246e-06, -1.518516920005905e-08, 8.601004856702239e-10, 194360719320.3122, 75684271432.82758]
# 16671845062396.34 - [7.3000149385339486e-06, -1.4649443926376347e-12, -1.740251215699652e-13, 5.5040821609381877e-11, -2.5448794058714256e-10, -1.1729621402736547e-15, 3.321162280251396e-16, 2.492985953688089e-05, -1.95260325957056e-06, -1.4879723555310096e-08, 8.886352647229086e-10, 118040637271.1665, 119637343045.177]
# 16641999233479.697 - [7.235432436183002e-06, -1.444519147741974e-12, -1.7273464723057338e-13, 5.517809418856912e-11, -2.5310572250093563e-10, -1.1658376910672744e-15, 3.3048095015500005e-16, 2.4812886502853343e-05, -1.964119169077712e-06, -1.4777953862585708e-08, 8.945619840357268e-10, 98015149423.40909, 125389712442.99564]
# 16050169990590.684 - [7.3000149385339486e-06, -1.4508582334938624e-12, -1.7446896418754742e-13, 5.109944355076077e-11, -2.5448794058714256e-10, -1.1658376910672744e-15, 3.1827015830354867e-16, 2.502027767038304e-05, -1.9664311146400523e-06, -1.4730561693079958e-08, 8.945619840357268e-10, 88113858040.47986, 127558862768.52084]
# 17017936670158.475 - [7.171513003462397e-06, -1.4334443716578728e-12, -1.749514610735409e-13, 5.509823004788858e-11, -2.5310572250093563e-10, -1.1729621402736547e-15, 3.321162280251396e-16, 2.4812886502853343e-05, -1.964119169077712e-06, -1.4799846596325615e-08, 8.965548334484032e-10, 85071583311.774, 128667385131.30013]
# 15598482203701.885 - [7.236287049225701e-06, -1.445911565527231e-12, -1.7498772740084537e-13, 5.109944355076077e-11, -2.5430545472048434e-10, -1.1709514644876058e-15, 3.210132219509301e-16, 2.502027767038304e-05, -1.975229899156637e-06, -1.4769695480936238e-08, 8.945619840357268e-10, 135323228000.64511, 130464457208.5385]





# 22553712588336.727 - [6.4442734160126695e-06, -1.2463732938819767e-12, -1.7912928652160854e-13, 3.990379556815055e-11, -7.256876412950873e-11, -1.128505986956859e-15, 3.855466000081844e-16, 2.7105518268805634e-05, -1.918022677712299e-06, -1.648586510957147e-08, 8.952907812465134e-10, 40874176708.45886, 129961018217.7445]
# 21737133950275.395 - [5.591985036569838e-06, -1.582675728169255e-12, -1.7359285477580936e-13, 5.508993685740796e-11, -2.5320893657294154e-10, -2.1583737575101563e-15, 3.210132219509301e-16, 2.511654073479438e-05, -1.965555797894771e-06, -1.5140087108671845e-08, 9.214909160927855e-10, 154168790181.56195, 151975095946.00134]

# No proof arrays
# Cheating - [0, -1.445911565527231e-12, -1.7498772740084537e-13, 5.109944355076077e-11, -2.5430545472048434e-10, -1.1709514644876058e-15, 3.210132219509301e-16, 3.902027767038304e-05, -1.975229899156637e-06, -1.4769695480936238e-08, 8.945619840357268e-10]
