import sys

input = sys.stdin.readline

print("input any number of the number of row and colomn")
num = int(input())

#nList =  list(map(int, input().split()))
#nLIst1D = [ i for i in range(num) ]
nList2D = []

for i in range(1, num+1):
    for j in range(1, num+1):
       list(nList2D.append(j*i))

print(nList2D)
