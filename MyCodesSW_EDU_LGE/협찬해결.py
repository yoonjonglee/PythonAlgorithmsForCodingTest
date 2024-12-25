import sys

def input_data() :
	readl = sys.stdin.readline
	N = int(readl())#협찬 물품의 수
	D = list(map(int, readl().split()))#선호도 
	return N, D

'''
def Solve():
	sol = -30001#첫번째 방법의 최대 선호도
	for i in range(0,N-2) :
		t = sum(D[i:i+3])
		if(t > sol) : sol = t
	return sol
'''

def Solve2():
	global sol,Sum
	Sum = 0
	sol = -10001
	
	for i in D:
		if(Sum > 0):
			Sum = Sum + i
		else:
			Sum = i
		if(sol < Sum):
			sol = Sum
	return sol

#입력받는 부분
N, D = input_data()
#sol = Solve()
sol = Solve2()
print(sol)#출력하는 부분
