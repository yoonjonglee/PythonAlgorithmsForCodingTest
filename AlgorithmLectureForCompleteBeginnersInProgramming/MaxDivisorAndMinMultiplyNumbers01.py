import sys

"""
"""

print("input any number")
input = sys.stdin.readline
num1, num2 = input().split()
#num = int(input())
num1 = int(num1)
num2 = int(num2)

if num1 >= num2:
    numBig = num1
    numSmall = num2
else:
    numBig = num2
    numSmall = num1
    
dlists = []
        
for i in range (1, numSmall+1):
    if numBig % i == 0 and numSmall % i == 0:
        print(f"{i} is a devisor")
        dlists.append(i)
        
print(dlists)
GCD = max(dlists)
SCM = max(dlists) * numBig/max(dlists) * numSmall/max(dlists)
print(f"greatest common devisor is {GCD}")
print(f"smalleast common multipy is {SCM}")
