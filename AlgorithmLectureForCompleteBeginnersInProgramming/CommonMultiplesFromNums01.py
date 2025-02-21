import sys
input = sys.stdin.readline

"""
input any two of integer numbers
7
9
common multipe number of 7, 9 between 1~500 is 63
common multipe number of 7, 9 between 1~500 is 126
common multipe number of 7, 9 between 1~500 is 189
common multipe number of 7, 9 between 1~500 is 252
common multipe number of 7, 9 between 1~500 is 315
common multipe number of 7, 9 between 1~500 is 378
common multipe number of 7, 9 between 1~500 is 441
"""
#input
print("input any two of integer numbers")
num1 = int(input())
num2 = int(input())
#print("input any integer numbers")
#nListInput = list(map(int, input().split()))
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)

#process
for i in range(1, 500+1):
    if (i%num1 == 0) and (i%num2 == 0):
        print(f"common multipe number of {num1}, {num2} between 1~500 is {i}")

#output
#print(f"SUM of the {nListInput} is {sum(nListInput)}")
