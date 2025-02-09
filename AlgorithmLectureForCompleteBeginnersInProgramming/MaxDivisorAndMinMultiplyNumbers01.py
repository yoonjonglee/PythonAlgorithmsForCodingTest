import sys

"""
10 4

1 2 5
1 2 4

"""

print("input any number")
input = sys.stdin.readline
num1, num2 = input().split()
#num = int(input())

if num1 >= num2:
    numBig = int(num1)
    numSmall = int(num2)
else:
    numBig = int(num2)
    numSmall = int(num1)
    

    
    
dlists = []
        
for x in range(1, num+1):
    if num % x == 0:
        dlists.append(x)
        
print(dlists)
print(f"summation of the results is {sum(dlists)}")
print(f"numbers of the results is {len(dlists)}")
