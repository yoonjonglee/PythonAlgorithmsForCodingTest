# Online Python - IDE, Editor, Compiler, Interpreter
import sys
from collections import deque
import heapq
from queue import PriorityQueue

#boj.kr/1302, 11286.베스트셀러
#algorithm: Map(dictionary)

d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] = d[book] + 1
    else:
        d[book] = 1
#print(d.keys())
#print(d.values())
#print(d.items())
m = max(d.values())
candidate = []
for key, val in d.items():
    if val == m:
        candidate.append(key)

print(sorted(candidate)[0]) # same as below
#candidate.sort(); print(candidate[0])


"""
#boj.kr/11286, 11286.절댓값 힙
#algorithm: heap(min_heap)
#lists = [3, 2, 6, 8, 9, 1, 7]; lists.sort()
#tuples = [(3, 2), (6, 8), (9, 1), (7, 4)]; tuples.sort()
#print(lists); print(tuples)
# sys.stdin.readline is faster than input()
input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(pq, (abs(x), x))
    else:
        print(heapq.heappop(pq)[1] if pq else 0) #same as below
        #if pq:
        #    print(heapq.heappop(pq))
        #else:
        #    print(0)

#boj.kr/2164, 2164.카드2
#algorithm: queue 
# caution!: If below is programmed with using List, it will take longer.
N = int(input())
dq = deque(range(1, N+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
    #print(dq)

print(dq[0])

#boj.kr/9012, 9012.괄호
#algorithm: stack
for _ in range(int(input())):
    isVPS = True
    stack = []
    for ch in input():
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                isVPS = False
                break
                
    if len(stack) > 0:
        isVPS = False
    else:
        isVPS = True
    print("YES" if isVPS else "NO")

# Set
s = set()
s.add(456)
s.add(12)
s.add(456)
s.add(789)
s.add(678)

print(s)

for i in s:
  print(i)

# MAP (Dictionary)
# key, value # key는 중복 불가, value는 중복 가능
m = {}
m["KIM"] = 40
m["LEE"] = 30
m["PAK"] = 20
print(m)
for i in m:
  print(i, m[i])

# mehod 2 : from queue import PriorityQueue
pq = PriorityQueue()
pq.put(100)
pq.put(200)
pq.put(30)
print(pq)
while not pq.empty():
  print(pq.get()) # pop
print(pq)


# mehod 1 : import heapq
# heapqueue: import heapq
pq = []
heapq.heappush(pq, 123)
heapq.heappush(pq, 456)
heapq.heappush(pq, 789)
heapq.heappush(pq, 77)
heapq.heappush(pq, 55)

print(pq)

while len(pq) > 0:
  print(heapq.heappop(pq)) # always pops min_heap queue value.

print(pq)

# queue: from collections import deque
q = deque()

q.append(1)
q.append(2)

print(q)

while len(q) > 0:
  print(q.popleft())

print(q)

# stack: make with list
s = []
s.append('X')
s.append('Z')
print(s)

while len(s) > 0:
  print(s[-1])
  s.pop(-1)

print(s)

# array & vector: make with list
v = []
#v.append((123, 456))
#v.append((789, 101112))
for i in range(10):
    v.append(i)

print(v)
print("size: ", len(v))
for i in v:
    print(i)

# reading input

read = sys.stdin.readline

N = int(read())
A = []
ans = 0
for _ in range(N):
    x = int(read())
    if not A:
        A.append(x)
print(x)
"""
"""
# reading 2 inputs and run summation
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
print(f'Sum of {a} and {b} is {sum(a, b)}')
"""
