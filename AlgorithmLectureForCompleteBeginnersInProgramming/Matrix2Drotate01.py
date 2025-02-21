import sys
input = sys.stdin.readline

"""
Rotate 90 degrees to the right

1, 2, 3, 4
    2, 3, 4
        3, 4
            4
->
            1
        2, 2
    3, 3, 3
4, 4, 4, 4

0,0 -> 0,3
0,1->1,3
0,2->2,3
0,3->3,3

1,0->0,2
1,1->1,2
1,2->2,2
1,3->3,2

2,0->0,1
2,1->1,1
2,2->2,1
2,3->3,1

3,0->0,0
3,1->1,0
3,2->2,0
3,3->3,0
"""
#input
print("input any integer numbers")
num = int(input())
print("input any integer numbers")
nList2Din = [list(map(int, input().split())) for _ in range(num)]
#result = sorted(nList, reverse = True)

#process
num_row = len(nList2Din)
num_col = len(nList2Din[0])
nList2dOut = [[0]*num_col for _ in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        nList2dOut[j][num_row-1-i] = nList2Din[i][j]

#output
print(nList2dOut)
