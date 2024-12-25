# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

base = [0,1,5,10,50,100,500,1000,3000,6000,12000]

def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	#cnt_box = list(map(int, readl().split()))
	num = [0] + list(map(int,readl().split()))
	psum = [0 for _ in range(11)]
	box = [0 for _ in range(11)]
	
	#return N, cnt_box
	return N, num, psum, box

sol = 0
sol_box_cnt = []

# 입력받는 부분
#N, cnt_box = input_data()
N, num, psum, box = input_data()

# 여기서부터 작성
for i in range(1,11):
	psum[i] = psum[i-1] + base[i]*num[i]

for i in range(10,0,-1):
	while N>psum[i-1] and num[i]>0:
		N -= base[i]
		num[i] -= 1
		box[i] += 1

# 출력하는 부분
#print(sol)
#print(*sol_box_cnt)
print(sum(box))
print(" ".join(map(str,box[1:])))
