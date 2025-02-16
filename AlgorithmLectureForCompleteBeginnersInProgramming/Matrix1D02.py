import sys

input = sys.stdin.readline

print("input any number of the number of row and colomn")
num = int(input())

#nList =  list(map(int, input().split()))
#nLIst1D = [ i for i in range(num) ]
nList = []
nList2D = [[] for _ in range(num)]
              
for i in range(num):
    for j in range(1, num+1):
        nList.append(i+j*num-(num-1))
    nList2D[i] = nList
    nList = []

print(nList2D)

"""
ex.
input : 5
output : [[1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25]]
"""
