import sys
from collections import deque

sys.setrecursionlimit(10**4)
INF = 987654321
dir = [[0,1], [0,-1],[1,0],[-1,0]]

def input_data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_line = []
	for _ in range(R):
		map_line.append(list(map(int,readl().split())))
	
	"""
	map_line = [
		[0] + list(map(int, readl().split())) + [0] if 1 <= r <= R else [0] * (C + 2)
		for r in range(R + 2)
	]
	"""
	return R, C, map_line


sol = -1
# 입력받는 부분
R, C, map_line = input_data()

# 여기서부터 작성
def dfs(y,x):
	map_line[y][x] = 2
	for dy,dx in dir:
		ny,nx = y+dy, x+dx
		if 0<=ny<R and 0<=nx<C and map_line[ny][nx]==1:
			dfs(ny,nx)

def bfs(sy,sx):
	dist = [[INF for _ in range(C)] for _ in range(R)]
	dist[sy][sx]=0
	Q = deque()
	Q.append([sy,sx])
	while Q:
		y,x = Q.popleft()
		if map_line[y][x]==1:
			return dist[y][x]-1
		for dy,dx in dir:
			ny,nx = y+dy, x+dx
			if 0<=ny<R and 0<=nx<C and map_line[ny][nx]!=2 and dist[ny][nx]>dist[y][x]+1:
				dist[ny][nx]=dist[y][x]+1
				Q.append([ny,nx])
	return INF

flag = False
for i in range(R):
	for j in range(C):
		if map_line[i][j]==1:
			dfs(i,j)
			flag = True
			break
	if flag:break

ans = INF
for i in range(R):
	for j in range(C):
		if map_line[i][j]==2:
			ans = min(ans, bfs(i,j))
			
# 출력하는 부분
#print(sol)
print(ans)
