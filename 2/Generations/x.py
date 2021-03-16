from generation_1 import *
import random
import sys

parent = pari+para
child = final2
param = 0.85
ans = []
cnt=0

# print(child[0])
# print()
# print(parent[0],"\n",parent[1],"\n",parent[2],"\n",parent[3],"\n",parent[4],"\n",parent[5])
# print()
# a=0
# b=0
# c=3
# print(child[a])
# print(parent[b])
# print(parent[c])
# print()
# for l in range(11):
# 	if (abs(child[a][l])>=(abs((1-param)*parent[b][l]))) and (abs(child[a][l])<=(abs((1+param)*parent[b][l]))):
# 		print("MATCH IN ARR1 FOR INDEX ",l)	
# 	elif (abs(child[a][l])>=(abs((1-param)*parent[c][l]))) and (abs(child[a][l])<=(abs((1+param)*parent[c][l]))):
# 		print("MATCH IN ARR1 FOR INDEX ",l)
# 	else:
# 		print("NO MATCH FOR INDEX ", l)
# sys.exit()

for i in range(len(child)):
	
	cand = []
	
	for j in range(6):
		for k in range(j,6):

			check=0
			arr = []
			
			for l in range(11):

				if (abs(child[i][l])>=(abs((1-param)*parent[j][l]))) and (abs(child[i][l])<=(abs((1+param)*parent[j][l]))):
					check+=1
					arr.append(parent[j][l])
					# print("MATCH FOUND IN ARR 1 for index",l)


				elif (abs(child[i][l])>=(abs((1-param)*parent[k][l]))) and (abs(child[i][l])<=(abs((1+param)*parent[k][l]))):
					check+=1
					arr.append(parent[k][l])
					# print("MATCH FOUND IN ARR 2 for index",l)
				
			if check == 11:
				cand.append([arr])

	# print(cand)

	if (len(cand)==0):
		print("CHANGE PARAMETER")
		sys.exit()
	ind = random.randint(0,len(cand)-1)
	ans.append(cand[ind][0])
	# print()

str="unmodulated_name"+"="
print(str,ans)
# print(ans)
# print(len(ans))