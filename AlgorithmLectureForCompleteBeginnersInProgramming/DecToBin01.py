import sys

"""
"""

print("input any number to be binarized")
input = sys.stdin.readline

#1D list
#nList = list(map(int, input().split()))
num = int(input())
num_input = num
result = ''

while num >= 1 :
    left = num % 2
    num = num // 2
    result = result + str(left)

print(f"{num_input} of binary is {int(result)}")
