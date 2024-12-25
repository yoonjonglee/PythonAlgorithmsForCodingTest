# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N, L, M = map(int, readl().split())
	#list_pos = [tuple(map(int, readl().split())) for _ in range(M)]
	list_pos = [list(map(int, readl().split())) for _ in range(M)]
	return N, L, M, list_pos


#sol = -1
sol = 0
# 입력받는 부분
N, L, M, list_pos = input_data()

# 여기서부터 작성
def calc(y1,x1,y2,x2):
	ret = 0
	for y,x in list_pos:
		if y1<=y<=y2 and x1<=x<=x2:
			ret += 1
	return ret



for y,x in list_pos:
	for h in range(1,L//2):
		w = L//2-h
		for i in range(w+1):
			sol = max(sol, calc(y,x-i,y+h,x+w-i))

# 출력하는 부분
print(sol)
