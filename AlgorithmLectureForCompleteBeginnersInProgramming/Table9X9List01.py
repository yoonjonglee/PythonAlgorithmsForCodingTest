import sys
input = sys.stdin.readline

"""
"""
#input
print("input any integer numbers")
num = int(input())
#print("input any integer numbers")
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)

#process
#nList2dOut = [[0]*num_col for _ in range(num_row)]
nListOut = []

if num != 0:
    for i in range(1, 10):
        print(f"{num}X{i}={num*i}")
        nListOut.append(num*i)
else:
     for i in range(2, 10):
         for j in range(1, 10):
             print(f"{i}X{j}={i*j}")
             nListOut.append(i*j)

#output
print(nListOut)
