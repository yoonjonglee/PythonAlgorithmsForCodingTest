# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_pic = []
	color = set()
	#map_pic = [list(map(int, readl().strip())) for _ in range(N)]
	for _ in range(N):
		temp = readl().strip()
		for c in temp:
			if c !="0":
				color.add(c)
		map_pic.append(temp)
	
	return N, map_pic, color


sol = -1
# 입력받는 부분
N, map_pic, color = input_data()
#print("map_pic",map_pic)
#print("color",color)

# 여기서부터 작성
pos = dict()
for c in color:
    y1,x1,y2,x2 = 11,11,-1,-1
    for i in range(N):
        for j in range(N):
            if map_pic[i][j]==c:
                y1,x1,y2,x2 = min(y1,i), min(x1,j), max(y2,i), max(x2,j)
    pos[c] = [y1,x1,y2,x2]

check = [0 for _ in range(10)]
for i in color:
    check[int(i)] = 1
for k,v in pos.items():
    for i in range(v[0], v[2]+1):
        for j in range(v[1],v[3]+1):
            if map_pic[i][j]!=0 and map_pic[i][j]!=k:
                check[int(map_pic[i][j])] = 0

# 출력하는 부분
#print(sol)
print(sum(check))