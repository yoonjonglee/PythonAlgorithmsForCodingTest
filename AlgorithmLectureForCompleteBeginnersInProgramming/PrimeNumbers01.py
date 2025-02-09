import sys

input = sys.stdin.readline
num = int(input())

plists = []
        
for x in range(num+1):
    if x < 4:
        plists.append(x)
    if x >= 4:
        for i in range(2, x+1):
            a = x % i
            if a == 0 and i == x :
                print(f"{x} is a p-num, devisor is {i}")
                plists.append(x)
            if a == 0 and i != x:
                print(f"{x} is not a p-num, devisor is {i}")
                break
                
print(plists)

print(f"the summation of p-numbers is {sum(plists)}")
print(f"the numebrs of p-numbers is {len(plists) - 1}")
