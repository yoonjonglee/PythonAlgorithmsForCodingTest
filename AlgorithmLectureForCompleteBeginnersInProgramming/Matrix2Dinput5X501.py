import sys
input = sys.stdin.readline

"""
# if val == 1
 [[1, 0, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 3, 0, 0], [1, 2, 3, 4, 0], [1, 2, 3, 4, 5]]
 ->
 [[1, 0, 0, 0, 0],
  [1, 2, 0, 0, 0],
  [1, 2, 3, 0, 0],
  [1, 2, 3, 4, 0],
  [1, 2, 3, 4, 5]]
# if val == 2
[[2, 0, 0, 0, 0], [2, 3, 0, 0, 0], [2, 3, 4, 0, 0], [2, 3, 4, 5, 0], [2, 3, 4, 5, 6]]
->
[[2, 0, 0, 0, 0],
 [2, 3, 0, 0, 0],
 [2, 3, 4, 0, 0],
 [2, 3, 4, 5, 0],
 [2, 3, 4, 5, 6]]
"""
#input
#print("input any two of integer numbers")
#num1 = int(input())
#num2 = int(input())
#print("input any integer numbers")
#nListInput = list(map(int, input().split()))
#nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)
val = 1
#val = 2
nList2Dout = [[0] * 5 for _  in range(5)]
#process
for i in range(5):
    for j in range(i+1):
        nList2Dout[i][j] = val+j
        #print(val+j)

#output
print(f"{nList2Dout}")
