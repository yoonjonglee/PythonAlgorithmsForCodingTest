# Online Python - IDE, Editor, Compiler, Interpreter
import sys
from itertools import permutations
from itertools import combinations

#boj.kr/2309, 2309. 일곱난쟁이
#algorithm: 조합, combinations

h = [int(input()) for _ in range(9)]
for combi in combinations(h, 7):
    if sum(combi) == 100:
        for tall in sorted(combi):
            print(tall)
            
        break

"""
v = [0,1,2,3]  #already sorted

#for i in permutations(v, 2): #2: number of choices
for i in combinations(v, 2): #2: number of choices
    print(i)
"""
