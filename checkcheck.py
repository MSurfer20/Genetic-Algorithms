import client
import submit
SECRET_KEY='H6geON26Ve5GxQDO1CDzkff4ZOn2kHEPV0DMMnfm6OEWfIBQ1I'
jai_mata_di = [3.603083193105678e-11, -1.3197261044307544e-12, -2.213785963757499e-13, 4.581086934703742e-11, -1.6681614728164575e-10, -1.803564324024427e-15, 8.4683341745183045e-16, 2.4065016435368993e-05, -2.0711260096490455e-06, -1.7031696163247858e-08, 1.0052651438176042e-09]
score = submit.submit(SECRET_KEY, jai_mata_di)
print(score)
