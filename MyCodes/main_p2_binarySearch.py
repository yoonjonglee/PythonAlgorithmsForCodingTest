import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
"""

"""
#input
#print("input any two of integer numbers")
numN = int(input())
nListN = sorted(list(map(int, input().split())))
numM = int(input())
nListM = list(map(int, input().split()))
#print("input any integer numbers")
#nListInput = list(map(int, input().split()))
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)
nListResult = []

#process
"""
for i in range(numM):
    if nListM[i] in nListN:
        nListResult.append(1)
    else:
        nListResult.append(0)
"""
for m in nListM:
    l = bisect_left(nListN, m)
    r = bisect_right(nListN, m)
    nListResult.append(1 if r - l else 0)

#output
#print(f"{nListResult}")
print(*nListResult)
