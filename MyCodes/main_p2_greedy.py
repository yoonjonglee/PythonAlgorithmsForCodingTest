# Online Python - IDE, Editor, Compiler, Interpreter
import sys

#boj.kr/1449, 1449. 수리공 항승
#algorithm: greedy
readl=sys.stdin.readline
N, L = map(int, readl().split())
coord = [False] * 1001 # 1000 sized list matrix
for i in map(int, readl().split()):
    coord[i ]= True

ans = 0
x = 0

while x < len(coord):
    if coord[x]:
        ans = ans + 1
        x = x + L
    else:
        x = x + 1

print(ans)

"""
#boj.kr/11047, 11047. 동전0
#algorithm: greedy

readl=sys.stdin.readline
N, K = map(int, readl().split())
coins = [int(readl()) for _ in range(N)]
coins.reverse()
ans = 0

for coin in coins:
    ans = ans + (K // coin)
    K = K % coin
    print(f"coin: {coin}, K: {K}, ans:{ans}")

#print(N, K)
#print(coins)
print(ans)
"""
