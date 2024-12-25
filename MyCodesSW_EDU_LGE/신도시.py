# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#from collections import deque

dir = [[-1,0],[1,0],[0,-1],[0,1]]
con = [1,0,3,2]
adj = {	"1":[2,3], "2":[0,1], "3":[1,3],
"4":[1,2], "5":[0,2], "6":[0,3], "7":[0,1,3],
"8":[1,2,3], "9":[0,1,2], "A":[0,2,3], "B":[0,1,2,3] }

def input_data():
	N = int(input())
	sr, sc = map(int, input().split())
	"""
	sc += 1
	sr += 1
	map_city = [
		[0] + list(map(int, input(), [16] * (N))) + [0]
		if 1 <= r <= N
		else [0] * (N + 2)
		for r in range(N + 2)
	]
	"""
	map_city = []
	total = N*N
	for _ in range(N):
		line = input()
		total -= line.count("0")
		map_city.append(line)
		
	vis = [[0 for _ in range(N)] for _ in range(N)]
	vcnt = 0
	return N, sc, sr, map_city, total, vis, vcnt


sol = -1
# 입력받는 부분
N, sc, sr, map_city, total, vis, vcnt = input_data()

# 여기서부터 작성
def dfs(y,x):
	global vcnt,N
	vis[y][x]=1
	vcnt += 1
	for d, di in enumerate(dir):
		if d not in adj[map_city[y][x]]: continue
		ny,nx = y+di[0], x+di[1]
		if 0<=ny<N and 0<=nx<N and vis[ny][nx]==0 and map_city[ny][nx]!="0":
			if con[d] in adj[map_city[ny][nx]]:
				dfs(ny,nx)

dfs(sc,sr)

# 출력하는 부분
#print(sol)
print(total-vcnt)
