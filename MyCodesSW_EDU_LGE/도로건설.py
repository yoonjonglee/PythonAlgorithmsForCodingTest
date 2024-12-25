import sys
from collections import deque
from heapq import *

def input_data():
	INF = 987654321
	dir = [[0,1],[0,-1],[1,0],[-1,0]]
	readl = sys.stdin.readline
	N = int(readl())
	map_cost = []
	for _ in range(N):
		map_cost.append(list(map(int,list(readl().strip()))))
	dist = [[INF for _ in range(N)] for _ in range(N)]
	dist[0][0]=0
	Q = [[0,0,0]]
	"""
	map_cost = [
		[0] + list(map(int, readl()[:-1])) + [0] if 1 <= r <= N else [0] * (N + 2)
		for r in range(N + 2)
	]
	"""
	return dir, N, map_cost, dist, Q


sol = -2

# 입력받는 부분
dir, N, map_cost, dist, Q = input_data()

# 여기서부터 작성
while Q:
	w,y,x = heappop(Q)
	if y==N-1 and x==N-1:
		break
	if w>dist[y][x]:
		continue
	for dy,dx in dir:
		ny,nx = y+dy, x+dx
		if 0<=ny<N and 0<=nx<N and dist[ny][nx]>w+map_cost[ny][nx]:
			dist[ny][nx] = w+map_cost[ny][nx]
			Q.append([dist[ny][nx],ny,nx])

# 출력하는 부분
#print(sol)
print(dist[N-1][N-1])
