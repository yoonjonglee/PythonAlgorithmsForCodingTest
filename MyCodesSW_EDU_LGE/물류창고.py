# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

INF = 987654321

def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	#infos = [list(map(int, readl().split())) for _ in range(M)]
	infos = [[INF for _ in range(N+1)] for _ in range(N+1)]
	for _ in range(M):
		u,v,c = map(int, readl().split())
		infos[u][v] = c
		infos[v][u] = c
	
	return N, M, infos

sol = -1

# 입력받는 부분
N, M, infos = input_data()

# 여기서부터 작성
for k in range(1,N+1):
	for i in range(1,N+1):
		for j in range(1,N+1):
			if i==j:continue
			infos[i][j] = min( infos[i][j], infos[i][k] + infos[k][j])

			ans = []
for i in range(1,N+1):
	m = 0
	for j in range(1,N+1):
		if infos[i][j] != INF:
			m = max(m, infos[i][j])
	ans.append(m)
	
# 출력하는 부분
#print(sol)
print(min(ans))
