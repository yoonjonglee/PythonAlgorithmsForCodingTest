import sys
input = sys.stdin.readline

"""
input any integer numbers to be restricted in fibonacci list
34
 Fibonacci list is [1, 1, 2, 3, 5, 8, 13, 21, 34] and SUM is 88
"""
#input
#print("input any two of integer numbers")
#num1 = int(input())
#num2 = int(input())
print("input any integer numbers to be restricted in fibonacci list")
num = int(input())
#nListInput = list(map(int, input().split()))
#nList2Dout = [[0] * 5 for _  in range(5)]
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)

#process
nListout = [1, 1]
result_fibo = 0
while result_fibo < num:
    result_fibo = nListout[len(nListout)-2] + nListout[len(nListout)-1]
    nListout.append(result_fibo)

#output
print(f" Fibonacci list is {nListout} and SUM is {sum(nListout)}")
