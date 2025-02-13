import sys
inputs = sys.stdin.readline

"""
4231
42(01)->2431
43(12)->2341
41(23)->2314
23(01)->2314
31(12)->2134
21(01)->1234
"""
        
# 2025.02.13
# Bubble Sort

# input
print("input any integer numbers to be bubble sorted")
nList = list(map(int, inputs().split()))

# process
for i in range(1, len(nList)):
    for j in range(len(nList)-i):
        #print(f"{j}, {j+1}")
        if nList[j] > nList[j+1]:
            temp = nList[j+1]
            nList[j+1] = nList[j]
            nList[j] = temp

# output
print(nList)