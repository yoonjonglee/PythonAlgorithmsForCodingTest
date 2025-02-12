import sys
#input = sys.stdin.readline

"""
"""
print("input any binary numbers")
#nList = list(map(int, input().split()))
numStr = input()

gryList = []
gryList.append(numStr[0])

for i in range(len(numStr)-1):
    temp = int(numStr[i])^int(numStr[i+1])
    gryList.append(str(temp))

print(gryList)
