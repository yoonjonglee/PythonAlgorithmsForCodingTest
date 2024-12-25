# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	led = readl().split()
	led2 = []
	pre = led[0]
	cnt = 1
	for i in range(1,len(led)):
		if pre!=led[i]:
			cnt+=1
		else:
			led2.append(cnt)
			cnt=1
		pre = led[i]
		
	led2.append(cnt)
	
	#return N, led
	return N, led2

sol = 0

# 입력받는 부분
#N, led = input_data()
N, led2 = input_data()

# 여기서부터 작성

if len(led2) < 3:
	print(N)
	
else:
	for i in range(2,len(led2)):
		sol = max(sol, led2[i-2] + led2[i-1] + led2[i])
		
	print(sol)

# 출력하는 부분
#print(sol)
