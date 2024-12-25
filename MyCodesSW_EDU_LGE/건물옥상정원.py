import sys

readl = sys.stdin.readline
def InputData():
	#readl = sys.stdin.readline
	N = int(readl())
	#H = [ int(readl()) for i in range(N) ]
	#return N, H
	return N



# 입력
# N: 건물 수
# H: 건물 높이
#N, H = InputData()
N = InputData()
A = []
#ans = -1
ans = 0

# 코드를 작성 하세요
for _ in range(N):
	x = int(readl())
	if not A:
		A.append(x)
	else:
		while A and A[-1]<=x:
			A.pop()
		ans += len(A)
		A.append(x)

# 출력
print(ans)
 
