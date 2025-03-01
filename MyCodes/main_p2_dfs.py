# Online Python - IDE, Editor, Compiler, Interpreter
import sys

#boj.kr/11724, 11724. 연결요소의 개수

#algorithm: DFS, BFS, back tracking

sys.setrecursionlimit(10 ** 6) #recursion 제한 증가
input = sys.stdin.readline      #입력시간 빠르게 하기 위함

#인접행렬만들기
N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: x - 1 , map(int, input().split()))
    adj[a][b] = adj[b][a] = 1

#인접행렬 확인 
#for row in adj:
#    print(row)

ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)
    
for i in range(N):
    if not chk[i]:
        ans = ans + 1
        chk[i] = True
        dfs(i)
        
print(ans)
