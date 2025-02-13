import sys
input = sys.stdin.readline

"""
"""
print("input any grade list")
nList = list(map(int, input().split()))
result = sorted(nList, reverse = True)

for i in range(len(result)):
    print(f"{i+1} grade is {result[i]}")
