import numpy as np
matrix = []
input_str = input()
n , m = map(int, input_str.split())

for i in range(n):
    matrix.append([])
    matrix[i] = input().split()
a = int(input())
matrix = np.array(matrix)
rotated = np.rot90(matrix , k=-a)

for i in rotated:
    for j in i:
        print(j, end=" ")
    print("")


        