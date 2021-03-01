from temp import third_gen
from pprint import pprint
arr = third_gen

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][11] > arr[j][11] and i<j:
            xd = arr[i]
            arr[i] = arr[j]
            arr[j] = xd

print(arr)
