import sys

print("input any number and multipy default number")
input = sys.stdin.readline
num, mux = input().split()

mlists = []
        
for x in range(1, int(num)+1):
    if x % int(mux) == 0:
        mlists.append(x)
        
print(mlists)
print(f"summation of the results is {sum(mlists)}")
print(f"numbers of the results is {len(mlists)}")
