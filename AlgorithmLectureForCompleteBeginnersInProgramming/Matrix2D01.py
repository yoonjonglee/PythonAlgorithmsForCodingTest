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
        nList.append(j+i*num)
    nList2D[i] = nList
    nList = []

print(nList2D)
