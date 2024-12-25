# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
	readl = sys.stdin.readline
	N, S, M = map(int, readl().split())
	
	A = list(range(1,N+1))
	#return N, S, M
	return N, S, M, A


sol_list = []

# 입력받는 부분
N, S, M, A = input_data()

# 여기서부터 작성
idx = (S-1)%N
while A:
	idx = (idx - 1 + M)%len(A)
	sol_list.append(str(A.pop(idx)))

# 출력하는 부분
#print(*sol_list)
print(" ".join(sol_list))
