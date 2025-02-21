import sys
input = sys.stdin.readline

"""
input any integer numbers
2 4 6 8 10
SUM of the [2, 4, 6, 8, 10] is 30
MAX of the [2, 4, 6, 8, 10] is 10
MIN of the [2, 4, 6, 8, 10] is 2
AVG of the [2, 4, 6, 8, 10] is 6.0
"""
#input
#print("input any two of integer numbers")
#num2 = int(input())
print("input any integer numbers")
nListInput = list(map(int, input().split()))
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)

#process

#output
print(f"SUM of the {nListInput} is {sum(nListInput)}")
print(f"MAX of the {nListInput} is {max(nListInput)}")
print(f"MIN of the {nListInput} is {min(nListInput)}")
print(f"AVG of the {nListInput} is {sum(nListInput) / len(nListInput)}")
