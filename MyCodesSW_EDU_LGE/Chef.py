import sys

def Input_Data():
	maxt = 0
	readl = sys.stdin.readline
	N = int(readl())
	#PT = [list(map(int,readl().split())) for _ in range(N)]
	#P = [x[0] for x in PT]
	#T = [x[1] for x in PT]
	PT = list()
	for _ in range(N):
		P, T = map(int,input().split())
		maxt = max(maxt, T)
		PT.append([T, P])
	
	#return N, P, T
	return N, P, T, PT, maxt

#ans = -1
ans = 0

# 입력
# N : 손님 수
# P : 음식 값
# T : 예약 희망 시간
#N, P, T = Input_Data()
N, P, T, PT, maxt = Input_Data()

# 코드를 작성하세요
PT.sort()
S = list()
for T in reversed(range(1,maxt+1)):
	while PT and PT[-1][0]>=T:
		S.append(PT.pop()[1])
	if S: 
		m = max(S)
		ans += m
		S.remove(m)

# 출력
print(ans)
