import sys
input = sys.stdin.readline

"""
input any two of integer numbers
3
7

SUM from 3 to 7 is 25
"""
#input
print("input any two of integer numbers")
num1 = int(input())
num2 = int(input())
if num1 >= num2:
    numBig = num1
    numSml = num2
else:
    numBig = num2
    numSml = num1
    
#print("input any integer numbers")
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)

#process
#nList2dOut = [[0]*num_col for _ in range(num_row)]
result = 0
for i in range(numSml, numBig+1):
    result = result + i

#output
print(f"SUM from {numSml} to {numBig} is {result}")
