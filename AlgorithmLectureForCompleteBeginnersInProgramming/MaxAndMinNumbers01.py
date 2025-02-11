import sys

"""
"""

print("input any numbers in serial")
input = sys.stdin.readline

#1D list
nList = list(map(int, input().split()))

print(f"max number is {max(nList)}")
print(f"min number is {min(nList)}")
print(f"min + max = {min(nList) + max(nList)}")
