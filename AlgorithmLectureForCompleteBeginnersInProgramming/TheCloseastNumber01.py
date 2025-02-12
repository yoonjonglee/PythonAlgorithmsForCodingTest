import sys
input = sys.stdin.readline
"""
"""
print("input any numbers")
nList = list(map(int, input().split()))
print("input the number to be closed")
num = int(input())

gapList = []

for i in range(len(nList)):
     gapList.append(abs(nList[i] - num))

print(f"the closeast number with {num} is {nList[gapList.index(min(gapList))]}")
