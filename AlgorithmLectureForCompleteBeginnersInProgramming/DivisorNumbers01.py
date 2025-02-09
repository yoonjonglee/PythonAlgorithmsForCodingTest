import sys

print("input any number")
input = sys.stdin.readline
#num, dvs = input().split()
num = int(input())

dlists = []
        
for x in range(1, num+1):
    if num % x == 0:
        dlists.append(x)
        
print(dlists)
print(f"summation of the results is {sum(dlists)}")
print(f"numbers of the results is {len(dlists)}")
