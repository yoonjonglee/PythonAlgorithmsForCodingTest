import sys

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	A = [int(x) for x in readl().split()]

	return N, A

# 입력
# N: 후보자 수
# A: 기질 값
N, A = InputData()

# 코드를 작성하세요
l,r = 0,N-1
ans = 2000000000
p1,p2 = -1,-1

while l<r and ans>0:
	val = A[l]+A[r]
	if abs(val)<ans:
		ans = abs(val)
		p1=l
		p2=r
	if val<0:
		l+=1
	else: 
		r-=1

# output	
print(p1,p2)
