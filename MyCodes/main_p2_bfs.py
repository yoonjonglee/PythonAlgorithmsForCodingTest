# Online Python - IDE, Editor, Compiler, Interpreter
import sys
from collections import deque

#boj.kr/2178, 2178. 미로탐색

#algorithm: DFS, BFS, back tracking

input = sys.stdin.readline      #입력시간 빠르게 하기 위함

#미로탐색 (최단거리찾기)

#인접행렬만들기
N, M = map(int, input().split())
board = [input() for _ in range(N)]

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0, 0))
    while dq:
        y, x = dq.popleft()
        for k in range(4):

bfs()

#인접행렬 확인 
#for row in adj:
#    print(row)

