import sys

def InputData():
	readl = sys.stdin.readline
	B, S, D = readl().strip().split()
	return int(B), S, D

def c2i(s):
	if s<='9': return ord(s)-ord('0')
	else: return ord(s)-ord("A")+10

i2c = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 입력

# N : 테스트 케이스 수
# B : 진법
# S : 첫 번째 정수
# D : 두 번째 정수
N = int(input())
for _ in range(N):
	B, S, D = InputData()
	ans = -1
	# 코드를 작성 하세요
	if S=="0" or D=="0":
		print("0")
		continue
	flag = 1
	if S[0]=='-':
		S=S[1:]
		#flag = flag * -1
		flag *= -1
	if D[0]=='-':
		D=D[1:]
		flag = flag * -1
		#flag *= -1
	A = [0 for _ in range(len(S)+len(D))]
	for i, v1 in enumerate(S):
		for j, v2 in enumerate(D):
			A[i+j+1] = A[i+j+1] + c2i(v1) * c2i(v2)
			#A[i+j+1] += c2i(v1) * c2i(v2)
	A.reverse()
	for i in range(len(A)-1):
		q, r = divmod(A[i], B)
		A[i] = r
		A[i+1] = A[i+1] + q
		#A[i+1] += q
	A.reverse()
	if flag == -1:
		print("-", end="")
	if A[0] > 0:
		print(i2c[A[0]], end="")
	for i in range(1, len(A)):
		print(i2c[A[i]], end="")
	print()
	# 출력
	#print(ans)
