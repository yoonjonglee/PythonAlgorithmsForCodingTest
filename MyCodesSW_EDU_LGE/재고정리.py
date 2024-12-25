# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from itertools import permutations

def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	#prod = [0] + list(map(int, readl().split()))
	prod = list(map(int, readl().split()))
	return N, M, prod


sol = -1
# 입력받는 부분
N, M, prod = input_data()

# 여기서부터 작성
num = [0]*10
psum = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i, a in enumerate(prod):
	num[a] += 1
	for b in range(1,M+1):
		psum[b][i+1] = psum[b][i]
		if a==b:
			psum[b][i+1] += 1

total = 0
for P in permutations(range(1,M+1)):
	idx = 0
	cnt = 0
	for p in P:
		s,e = idx, idx+num[p]
		cnt += psum[p][e]-psum[p][s]
		idx = e
	total = max(total,cnt)

# 출력하는 부분
#print(sol)
print(N-total)
