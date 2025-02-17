import sys

input = sys.stdin.readline

#input
#nList =  list(map(int, input().split()))
#nLIst1D = [ i for i in range(num) ]
#nList = []
#nList2D = [[] for _ in range(num)]
print("input any number of the row of the 2d matrix input ")
num = int(input())
print("input any listed numbers of the 2d matrix input ")
nList2dInput =  [list(map(int , input().split())) for _ in range(num)]
print(f"input matrix : {nList2dInput}")

# process
num_row = len(nList2dInput)
num_col  = len(nList2dInput[0])
num2_col = num_row
num2_row = num_col
nList2dOut = [[0]*num2_col for _ in range(num2_row)]
nList2dTemp = []

for i in range(num_row):
    for j in range(num_col):
        nList2dTemp.append(nList2dInput[i][j])

print(f"tempList: {nList2dTemp}")

for a  in range(num2_row):
    for b in range(num2_col):
           nList2dOut[a][b] = nList2dTemp[a*num2_col+b]

print(f"Output matrix : {nList2dOut}")

"""
ex.
input : 4
matrix : [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
output : [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
"""
