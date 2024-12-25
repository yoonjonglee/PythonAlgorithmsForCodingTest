import sys

def InputData():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	A = list(map(int, readl().split()))
	B = list(map(int, readl().split()))

	return N, M, A, B

first = 1
def Find(start) :
	global B, first
	
	if first == 1:
		first = 0
		B.sort()
		B = list(map(lambda x:x-B[0], B))
		
	P = A[start:start+M]
	P.sort()
	P = list(map(lambda x:x-P[0], P))
	
	#return B == P
	#print(f"value of B == P : {B == P}")
	
	if B == P:
		return 1
	else:
		return 0
'''
	for i in range(M) :
		if B[i] != A[start + i] : return 0
	return 1
'''

def Solve():
	sol = 0
	for i in range(N - M + 1) :
		sol += Find(i)
	return sol

sol = 0

# 입력
# N: 실행 코드의 데이터 개수
# M: 바이러스의 데이터 개수
# A: 실행 코드의 데이터
# B: 바이러스의 데이터
N, M, A, B = InputData()

# 코드를 작성하세요
sol = Solve()

# 출력
print(sol)
