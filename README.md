# PythonAlgorithmsForCodingTest
- 파이썬 알고리즘 코딩 테스트 대비 전략

## PART 2. 알고리즘 유형 분석

### Chapter 1. 자료구조 (코딩테스트에서 주로 사용되는 ...)
- data type
  - default
    - int, float, string
  - collection (STDL)
    - set, tuple, dictionary, list  
- mutable Vs. immutable
  - immutable : default, string, tuple
  - mutable : the others
- essential method
  - lambda expression (as a variable, parameter)
  - 조기반환 (early return for exception handling)
  - 보호구문 (if / return for parameter check)
  - 합성함수(using lambda expression)
#### 배열(Python: List)
- Size 변경 가능
- 정렬
  - .sort() method
    - list.sort(), list.sort(reverse=True)형태로 사용(default: ascending오름차순, reverse:False)
    - !주의! 위 메소드 사용 시 자기 자신 list 정렬이 되어 버림
  - sorted(arg) function
    - var = sorted(list), sorted(list, reverse=True)형태로 사용 (default: ascending오름차순, reverse:False)
    - !주의! 정렬된 결과 리스트가 저장될 변수를 선언해야 함
  - 간단한 오름/내림차순 정렬 시, 위 함수가 어떤 정렬알고리즘(e.g. 버블)들 보다 더 빠름

#### 벡터(Python: List)
- Size 변경 가능 == List로 통일
- 일반 값, 정수, 리스트, 튜플 온갖 것들을 넣을 수 있음

#### Linked List (Python: X)

#### stack (Python: List)
    s = []
    s.append('X')
    s.append('Z')
    while len(s) > 0:
        print(s[-1])
    s.pop(-1)

#### queue
    from collections import deque
    q = deque()
    q.append(1)
    q.append(2)
    
    print(q)
    
    while len(q) > 0:
        print(q.popleft())
    print(q)

#### priority queue (heap) - 우선순위 큐
- 17 <-- min_heap
- 13,    / 6
- 11, 19 / 3, 4
- 10, 4 / 2 ,5/ 1 / 0
- ...
- heappop을 하면, min_heap 부터 순서대로 빠져 나옴

##### mehod 1 : import heapq : fast, recommended
    import heapq // heapq 가 길면, 이렇게 "hq"로 선언 해도 됨 -> "import heapq as hq"
    
    pq = []
    heapq.heappush(pq, 123)
    heapq.heappush(pq, 456)
    heapq.heappush(pq, 789)
    heapq.heappush(pq, 88)
    heapq.heappush(pq, 66)
    
    print(pq)
    
    while len(pq) > 0:
        print(heapq.heappop(pq)) """ always pops min_heap queue value. """
        """ 66-88-123-456-789 """

##### mehod 2 : from queue import PriorityQueue : slow
    from queue import PriorityQueue
    
    pq = PriorityQueue()
    pq.put(100)
    pq.put(200)
    pq.put(30)
    print(pq)
    while not pq.empty()
        print(pq.get()) """ pop """
    print(pq)

#### MAP (Dictionary)
key, value // key는 중복 불가, value는 중복 가능

    #=================Ex.1
    m = {}
    m["KIM"] = 40
    m["LEE"] = 30
    m["PAK"] = 20
    print(m)
    
    for i in m:
        print(i, m[i])
    #=================Ex.2
    sample_dict = {'수학':80, '국어':90}
    
    ## 수학 성적을 95로 수정, 영어 성적 70점 추가
    sample_dict.update({'수학':95, '영어':70})
    print(sample_dict)


#### 집합(set)

원소의 중복 불가

    s = set()
    s.add(456)
    s.add(12)
    s.add(456)
    s.add(789)
    s.add(678)
    print(s)
    
    for i in s:
        print(i)
        
    """
    s.pop()   # random으로 아무 값이나 제거
    s.clear() # 모든 원소 값 제거
    s.remove(50) # 원소 50 제거
    """

### Chapter 2. 완전 탐색
- 장점: 확실히 답을 찾을 수 있으며, 전부 뒤졌지만 없으면, 이것은 진짜 답이 없다는 것 확인 한 셈(e.g. 중국집메뉴)
- 단점: 오래걸림, 리소스 많이 소요.
- 트레이드오프 관계: 리소스 와 시간. (커질 수록 작아질 수도, 작을수록 커질 수도)

#### Algorithm: 무차별 대입(Brute-Force)
- ex. 4자리 비번. 경우의 수는 10^4이므로, 10000가지를 전부 때려박아보면, 됨 (사람은 못하지만 컴퓨터는 가능)

#### Q: N개의 수를 입력 받아 2 개의 수를 뽑았을 때 합이 가장 큰 경우를 구하라
- If N == 8, 2개 조합 이므로 8C2(combination) = 8*7/2*1 = 28 가지 경우로 정의 가능
- If N == 10, 2개 조합 이므로 10C2(combination) = 10*9/2*1 = 45 가지 경우로 정의 가능
- ! Caution: 시간제한 1초, 2<= N <=1000000 조건 적용: NC2 -> 시간복잡도가 너무 커서 1초 이내 계산 어려움
- 정렬을 사용하여 적용 가능

  
##### mathod1: 순열 permutation 사용하면 해결 가능 (next_permutation)
    #Code
    from itertools import permutations
    
    v = [0,1,2,3] // already sorted
    for i in permutation(v, 2): #2: number of choices
        print(i)
##### mathod2: 조합 combinations 사용하면 해결 가능 (combinations)
    #Code
    from itertools import combinations
    
    v = [0,1,2,3] // already sorted
    for i in combinations(v, 2): #2: number of choices
        print(i)

#### Q
- boj.kr/2309, 2309. 일곱난쟁이
- algorithm: 조합, combinations

#### Summary
- 무식하게 모든 경우 수를 다 살펴봐도 시간 초과 나지 않을지 확인
- 될거 같음 완탐으로 문제를 풀고, 안될 거 같음 더 효율적인 알고리즘을 찾아보자 (그리디, DP, 이분법 등)


### Chapter 3. 탐욕법 Greedy Algorithm
- 매 순간마다 최선의 경우만 골라 감. 다른 경우는 고려X, 나중은 생각X
- 다 안까보니, 완탐 보다 빠름. 즉 어떤 경우가 최선인지 찾는게 포인트
- 최선을 알기 위해 패턴 규칙을 찾아야 할 수도 있음

#### 동전 거스름돈 문제
- 10, 50, 100, 500원 동전이 무제한 있음. 거스름돈 800원을 줄때 주는 동전을 최소로 하려면?
- 직관적으로 이건 큰단위 동전순서로 주는게 정답임을 알 수 있음 (500X1, 100X3 = 4)
- 그럼, 100, 400, 500원 동전이 무제한 있을때, 거스름돈 800원을 주는 최소 동전 갯수?
- 직관적으로 400원X2가 답임을 알 수 있음. 즉 동전 단위가 배수 관계가 깨지면, 기존 탐욕법(큰단위 순서)이 먹히질 않음
- 즉 이런 탐욕법 알고리즘의 가장 큰 문제는 문제 해결을 위해 탐욕법 적용 여부 판단이 어렵다는 것. (진짜 이게 탐욕법 문제인가?, 다른 방법은 없으까?)

#### Q
- boj.kr/11047, 11047. 동전0
- algorithm: greedy
- boj.kr/1449, 1449. 수리공 항승
- algorithm: greedy

### Chapter 4. DFS, BFS, 백트래킹
- 선행 습득 자료구조 : 그래프
- 자료들간의 개념을 나타내는 구조, 실생활 예: 지도, 내비, SNS, 메신저(관계도식), git(버전관리시스템)

- 구조 설명 (노드를 잇는 선을 Edge, E 라고 함)
  - 노드1.0(버텍스, 역)-- 노드1.1(버텍스, 역)-- 노드1.2(버텍스, 역)-- 노드1.3(버텍스, 역)-- ...
  - /
- 구조 종류
  - 1. 방향 그래프: 방향이 표시 (방향 없는 쪽은 이동 불가)
  - 2. 무(양)방향 그래프: 방향이 없음(어느쪽으로든 이동 가능
  - 3. 순환그래프: 사이클 엣지 라인이 존재
  - 4. 비순환 그래프: 사이클 엣지 라인이 없음

#### 방향성 비순환(DAG-Directed Acyclic Graph) 그래프 
- 위 1 + 4 개념 구조, git같은 버전관리시스템이 이 주요 예시
  - 현재에서 과거로 시간을 되돌리는 행위는 불가하기 때문 : 이는 과거 상태로 구조를 바꾼것 역시 현재 상태 기준에서의 변화이기 때문 임)
- 연결 요소: 그래프는 반드시 위 구조 처럼 노드와 엣지들이 모두 연결된 형태만 존재 하는 것이 아닐 수 있음.
  - 일부 노드 들만 엣지 라인으로 연결 된 N개의 구성 요소로 존재하여 하나의 그래프를 구성 할 수도 있음 (노드-노드,  노드-노드-노드 ...)
  - 이때 모두 연결된 형태로 존재하는 그래프는 연결 요소가 1개라고 정의 함

#### 트리(Tree, 무방향 비순환) 그래프 
- 특정하지 않는 한 어떤 노드든지 루트(Root)가 될 수 있음
- 가장 바깥 쪽(종점) 노드를 리프(Leaf, 나뭇잎) 노드라고 함
- 노드간 이동 경로는 반드시 존재하며 유일한 1개만 존재 함 (=싸이클 존재X)
- 노드 개수 = 간선(엣지라인)개수 + 1 이라는 특징이 존재 (이게 아니면, 트리가 맞는지 확인 필요)
- 이론적으로 트리는 무방향 비순환 이지만, 공학적인 자료구조 트리는 부모 자식 관계의 방향성(e.x. 위->아래, 왼->오)을 가진 그래프로 더 많이 통용 됨 == 루트를 1개로 특정 함

#### 코드로 그래프를 작성하는 법
- 1. 인접행렬 : 2차 행렬 매트릭스로 표시 
- 가로행은 시작 인덱스(0, 1, 2, 3) 세로열은 도착 인덱스(0, 1, 2, 3) 상에서, 방향과 연결을 1로 표시 하도록 함
  - 예1.1
    ```
    0111
    0010
    0000
    0010
    ```
  - 예를 들어 예1.1)의 경우, 0->1, 0->2, 0->3, 1->2, 3->2 의 노드와 엣지라인을 표시 할 수 있음
  - 대각선 인덱스를 대칭으로 표시된 1은 역방향을 의미하므로, 양방향을 표시 할 수 있음
  - 예1.2
    ```
    0111
    1010
    1101
    1010
    ```
  - 예를 들어 예1.2의 경우, 0<->1, 0<->2, 0<->3, 1<->2, 3<->2 의 노드와 엣지라인을 표시 할 수 있음

- 2. 인접리스트: 연결 리스트(또는 벡터*C++, 리스트*Python)로 표시
- 연결된 시작 인덱스(0, 1, 2, 3) 에 해당하는 도착 인덱스(0, 1, 2, 3)를 List 로 표시 하도록 함
  - 예2.1
    ```
    0->1->2->3
    1->2
    3->2
    ```
  - 예를 들어 예2.1의 경우, 예1.1 처럼 0->1, 0->2, 0->3, 1->2, 3->2 의 노드와 엣지라인을 표시 할 수 있음.
  - 이때 예1.1)은 미연결 상태는 0으로 표시가 남는 반면, 예2.1)은 미연결 상태가 아예 표시 되지 않음
  - 예2.2
    ```
    0->1->2->3
    1->0->2
    2->0->1->3
    3->0->2
    ```
    - 예를 들어 예2.2)의 경우, 예1.2) 처럼 0<->1, 0<->2, 0<->3, 1<->2, 3<->2 의 노드와 엣지라인을 표시 할 수 있음. 마찬가지로 예1.2)은 미연결 상태는 0으로 표시가 남는 반면, 예2.2)은 미연결 상태가 아예 표시 되지 않음

- 인접행렬 Vs. 인접리스트 비교
  - 인접행렬: 필연적으로 공간(메모리)을 많이 쓰지만, 구조(노드-엣지) 여부 확인이 빠름
    - 예: if g[0][2] == 1: then 0->2 구조 확인
    - edge가 많은 그래프일 떄 쓰는게 좋음. edge 탐색이 빠름
  - 인접리스트: 인접행렬대비 공간(메모리)을 적게 쓰지만, 구조(노드-엣지) 여부 확인이 느림
    - 예: 0->3 구조 확인 위해서 g[0] 에 3이 존재하는지 전부 검사 필요 (만약 999999 라면?? ㄷㄷ)
    - edge가 적은 그래프일 때 쓰는게 좋음. 메모리를 적게 사용
- 즉, 접점이 100개라고 하면, 인접행렬은 N^2(100*100) 개이지만, 인접리스트는 2N(2*100)개로 차이가 남

#### DFS
- Depth First Search: 깊이 우선 탐색, 탐색 알고리즘 중 하나이며, 완전 탐색에 속 함
- 스택 또는 재귀를 사용해서 구현
- 예시 트리 (하위로 방향 진행)
    - 0 (root)
      - 1
        - 2
          - 3
          - 4
        - 5
          - 6
      - 7
        - 8
        - 9
          - 10
          - 11
          - 12
- 즉 최대한 깊게 뒤져볼 수 있는데 까지 뒤지는 것
- 뒤지는 순서 : 0->1->2->3->2->4->2->1->5->6->5->1->0->... 이렇게 안뒤진데가 없을떄까지
- code lines using 재귀 방식
  ```
  adj = [[0]*13 for _ in range(13)]
  #input node connections using 인접행렬(Adjacency matrix) : [from][to]
  adj[0][1] = adj[0][7] = 1
  adj[1][2] = adj[1][5] = 1
  # ... ...
  for row in adj:
    print(row)
  def dfs(now):
    for nxt in range(13):
      if adj[now][nxt]:
        dfs(nxt)

  def(0) # call
  ``` 

#### BFS
- Breadth First Search: 넓이 우선 탐색, 탐색 알고리즘 중 하나이며, 완전 탐색에 속 함
- DFS 처럼 싹 뒤질거면, 무엇이 다른가?
  - 탐색순서가 다름. 얘는 큐를 사용해서 구현
- 예시 트리 (하위로 방향 진행)
  - 0 (root)
    - 1
      - 3
        - 7
        - 8
      - 4
        - 9
    - 2
      - 5
      - 6
        - 10
        - 11
        - 12
- 마찬가지로 전부 뒤져볼 수 있는데 까지 뒤지는데 계층순서로 뒤짐
- 뒤지는 순서 : 0->1->2 뒤지고 3->4->5->6 뒤지고 7->8->9>10->11->12 뒤지고 ...
  - 즉 다시 말해서 아래 순서로 푸쉬/팝 하면서 뒤
    - 큐에 0푸쉬, 0팝, 1, 2 푸쉬
    - 큐에 1팝, 3, 4 푸쉬, 2팝, 5, 6 푸쉬
    - 큐에 3팝, 7, 8 푸쉬, 4팝, 9 푸쉬, 5팝, 6팝, 10, 11, 12 푸쉬
    - 7, 8 팝, 9팝, 10, 11, 12 팝
    - ...
- code lines using 재귀 방식
  ```
  from collections import deque
  
  adj = [[0]*13 for _ in range(13)]
  #input node connections using 인접행렬(Adjacency matrix) : [from][to]
  adj[0][1] = adj[0][2] = 1
  adj[1][3] = adj[1][4] = 1; adj[2][5] = adj[2][6] = 1
  adj[3][7] = adj[3][8] = 1; adj[4][9] = 1; adj[6][10] = adj[6][11] = adj[6][12] = 1
  
  #for row in adj:
  #  print(row)
  
  def bfs():
    dq = deque()
    dq.append(0)
    while dq:
      now = dq.popleft()
      for nxt in range(13):
        if adj[now][nxt]:
          dq.append(nxt)


  bfs() # call
  ```
- /

#### DFS Vs. BFS
- 공통점
  - 완탐, 모든 경우를 뒤져 답을 반드시 찾음. 완탐의 특장점을 그래도 포함
- 차이점
  - 뒤지는 순서가 다름
  - 가령 최단거리를 묻는 경우, DFS는 모든 경우를 다 뒤진다음 무엇이 최단거리인지를 확인 해야
  - 하지만, BFS는 레이어 순서로 노드들을 뒤지기 때문에 최단 거리를 먼저 찾을 확률이 높음

#### 시간복잡도
- 인접 행렬 Vs. 인접 리스트 : 둘 중 어느것을 쓰는가에 의한 시간 복잡도 
  - 인접행렬O(V^2) : 2차원 배열 사용
  - 인접리스트O(V+E)
    - E는 Edge(간선) 갯수인데, 간선이 작을 수록 시간복잡도가 작은 이점이 있을 수 있음

#### 예제문제(1)
- 길찾기문제
  - 보통 Right, Down, Left, Up 4방향 간선 존재
  - 각 칸이 노드 의미 
  - 방향값을 미리 코드에 짜두고 For문으로 순회하는 기법을 익혀야 함
  - 방문체크 필요
  - 아래 예시 코드 처럼, dy, dx 배열(튜플)없이도 구현 가능하지만, 코드 길어지고, 실수 발생 가능
  ```
  dy = (0, 1, 0, -1)
  dx = (1, 0, -1, 0)
  chk = [[False] * 100 for _ in range(100)]
  N = int(input())

  def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N

  def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
      y, x = q.popleft()
      chk[y][x] = True
      for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and not chk chk[y][x]:
          q.append((ny, nx))
  ```
    
#### 백트래킹 (Back Tracking)
- 퇴각검색, 되추적이라고도 불림
- 삼국지처럼 전략시뮬레이션 게임처럼 상황/조건들을 선택하고 취소 할 떄마다 다른 결과들이 도출되는 것을 상상
- 기본적으로 모든 경우를 탐색 하는 점에서 DFS, BFS 와 유사
- 하지만 백트래킹은 "가지치기를 통해 탐색 경우의 수를 줄인다는 핵심 차이가 존재
  - 최악의 경우, 모든 경우를 다 살펴보게 될 수도 있지만 가급적 덜 보겠다는 전략
  - "가망이없는 곳은 포기" 전략

#### 예제문제(2)
- boj.kr/11724
- 11724. 연결 요소의 개수

#### 예제문제(3)

#### 정리
- DFS, BFS, 백트래킹 모두 완전탐색 알고리즘. 최악의 경우 모든 노드를 탐색하는 것은 동일
- 최단거리를 구할 때 : BFS
- DFS: 재귀(or Stack), BFS는 Queue로 구현
- 가지치기를 하면 백트랙킹
----------------
### Chapter 5. 이분(이진) 탐색 Binary Search
- 탐색 전에 반드시 정렬 되어있어야 함
  - 복잡도 계산: 정렬<O(NlogN)> + 이진 탐색<O(logN)> --> 결과적으로 O(NlogN)
  - 미리 정렬되어 있으면 이진탐색만 하면 되므로 O(logN)
- 살펴보는 범위를 절반 씩 줄여가면서 답을 찾음

#### 라이브러리
- 각 언어별로 이진 탐색 기반의 API 라이브러리들을 제공 함
- python : bisect_left/right
  - bisect_left : 찾는 요소가 처음 등장하는 idx를 반환
  - bisect_right: 찾는 요소가 마지막에 등장하는 idx의 다음 idx를 반환
  - 찾는 요소가 없는 경우 : 찾는 요소가 삽입 될 수 있는 idx를 반환
  ```
  EX.1
  list = [1,3,4,5,7,8,9,11,13]
  # 리스트에 있는 요소 탐색
  print(bisect.bisect_left(list, 11)) # 7
  print(bisect.bisect_right(list, 11)) # 8
  # 리스트에 없는 요소 탐색
  print(bisect.bisect_left(list, 2)) # 1
  print(bisect.bisect_right(list, 2)) # 1

  EX.2
  list = [1,3,4,5,7,8,9,12,12,12,12,12,13]
  # 리스트에 있는 요소 탐색
  print(bisect.bisect_left(list, 12)) # 7
  print(bisect.bisect_right(list, 12)) # 12
  # 두개의 차이 5 == 12의 갯수
  
  EX.3
  from bisect import bisect_left, bisect_right

  v = (0,1,3,3,6,6,6,7,8,8,9)
  three = bisect_right(v, 3) - bisect_left(v, 3)
  four = bisect_right(v, 4) - bisect_left(v, 4)
  six = bisect_right(v, 6) - bisect_left(v, 6)
  print(f"number of 3: {three}")  # 2
  print(f"number of 4: {four}")   # 0
  print(f"number of 6: {six}")    # 3
  ```
- /
#### 파라메트릭 서치(Parametric Search, 매개변수 탐색)
- 최적화 문제를 결정 문제로 바꾸어 이진 탐색으로 푸는 방법
  - 최적화 문제(Optimization Problem) : 문제 상황을 만족하는 변수의 최소값, 최대값을 구함
  - 결정 문제 (Decision Problem) : Yes/No를 구함
  - EX. 유데미 수강생들의 외모값과 커플/솔로 여부가 주어짐. 커플들은 솔로들보다 외모값이 높음. 외모값이 최소 얼마 이상일 때 부터 커플인가?
    - 입력정보
      - 회원  | a, b, c, d ... ...
      - 커플  | F, F, T, T ... ...
      - 외모값| 2, 3, 6, 8 ... ...
    - 풀이
      - 파라미터가 주어지면 True / False가 결정되어야 함 (파라미터서치 사용조건)
      - 가능한 해의 영역이 연속적(list)이어야 함 (파라미터서치 사용조건)
      - 범위를 반씩 줄여가면서 가운데 값이 True인지, False인지 구함
      - 이진탐색과 같은 원리

#### 예제문제(1)
- boj.kr/2512
- 2512. 예산
  - 입력
    - 첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다.
  - 출력
    - 첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다.
  - 예제 입력 1
    - 4
    - 120 110 140 150
    - 485
  - 예제 출력 1
    - 127
```
N = int(input())
req = list(map(int, input().split()))
M = int(input())
lo = 0; hi = max(req); mid = (lo + hi) / 2; ans = 0
def is_possible(mid):
  for r in req:
    return sum(min(r, mid) for r in req) < M
while(lo < hi):
  print(f"lo:{lo}, mid:{mid}, hi:{hi}, ans: {ans}")
  if is_possible(mid):
    lo = mid + 1
    ans =mid
  else:
    hi = mid - 1
  mid = (lo + hi) // 2
print(ans)
```
- /
#### 예제문제(2)
- boj.kr/10815
- 10815. 숫자카드
- 입력
  - N(1이상 50만이하): 상근이의 숫자카드 갯수
  - 숫자열(공백구분, -1000만이상, 1000만 이하, 중복없음): 상근이의 숫자카드들 N개
  - M(1이상 50만이하): 입력받을 숫자카드 갯수
  - 숫자열(공백구분, -1000만이상, 1000만 이하, 중복없음): 확인을할 숫자카드들 M개
- 출력
  - 확인을할 숫자카드들이 각각 상근이의 숫자카드들에 있으면 1, 아니면 0을 공백으로 구분 출력
- 예제1
  - 입력
    - 5
    - 6 3 2 10 -10
    - 8
    - 10 9 -5 2 3 4 5 -10
  - 출력
    - 1 0 0 1 1 0 0 1
```
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

#input
numN = int(input())
nListN = sorted(list(map(int, input().split())))
numM = int(input())
nListM = list(map(int, input().split()))
nListResult = []

#process
"""
for i in range(numM):
    if nListM[i] in nListN:
        nListResult.append(1)
    else:
        nListResult.append(0)
"""
for m in nListM:
    l = bisect_left(nListN, m)
    r = bisect_right(nListN, m)
    nListResult.append(1 if r - l else 0)

#output
#print(f"{nListResult}")
print(*nListResult)
```
- /
#### 이진탐색 정리
- 탐색 전에 반드시 입력 리스트가 정렬되어 있어야
- 살펴보는 범위를 절반씩 줄여가면서 답을 찾음
- 파이썬의 경우 bisect_left, bisect_right API를 반드시 사용할 줄 알아야 
----------------
### Chapter 6. 동적 계획법 Dynamic Programming (DP)
- 하나도 다이나믹하지 않음. 그냥 있어보이라고 붙인 이름 같음
- 문제를 쪼개서 작은 문제의 답을 구하고, 그걸로 더 큰 문제의 답을 구하는 걸 반복
- 분할 정복과 비슷한 느낌
- DP 구현 2가지
  - Top Down  --> 구현: 재귀   / 저장방식 : 메모이제이션 (Memoization)
    - Memoization ( !주의! 메모라이제이션 Memorization 아님)
      - 한번 구한 답들은 저장 해 둠
      - 부분 문제들의 답을 한 번 구했으면 또 구하지 않음 (중복 연산 방지). Cache에 저장 후 가져다 씀
      - 필요한 부분 문제들만 구함 (Lazy Evaluation), Top Dwon  방식에서 사용
      - 4살 아들한테 메모이제이션을 설명하기
        - 아빠 : (종이에 1+1+1+1+1+1+1+1 을 적고) 정답이 뭘까
        - 아들 : (세보고) 8이요
        - 아빠 : (왼쪽에 +1 을 또 적고) 정답이 뭘까
        - 아들 : (바로) 9요
        - 아빠 : 오, 어떻게 바로 알았냐
        - 아들 : 하나 더 했으니깐요
        - 아빠 : 앞에 답을 8로 기억했었으니까 처음부터 다시 셀필요가 없었네~
  - Bottom Up --> 구현: 반복문 / 저장방식 : 테이뷸레이션 (Tabulation)
    - Tabulation
      - 미리 다 구해두자
      - 부분 문제들의 답을 미리 다 구해두면 편함
      - 테이블을 채워나간다는 의미라서 테이뷸레이션
      - 필요 없는 부분 문제들까지 모두 구함 (Eager Evaluation), Bottom Up 방식에서 사용
  - 피보나치 수열 (Fibonacci)
    - 0 1 (0+1) 1+(0+1) (0+1)+1+(0+1) 1+(0+1)+(0+1)+1+(0+1) ...
      - Fn := 0 1 F(n-1)+F(n-2)
      - Example : 아래와 같은 형태의 피보나치 수열을 구해야 한다고 가정
      - F6
        - F5
          - F4
            - F3
              - F2
                - F1
                - +F0
              - +F1
            - +F2
              - F1
              - +F0
          - +F3
            - F2
              - F1
              - +F0
            - F1
        - +F4
          - F3
            - F2
              - F1
              - +F0
            - +F1
          - +F2
              - F1
              - +F0
    - 위에서 매번 구할 필요 없이 중복되는 연산은 하지 않고 저장해 두고 있다 불러 참조하면 단순화 가능
    - 저장하는 곳은 캐시(메모이제이션) 또는 테이블(테이블레이션)
    - 이 두개 방식은 직접적 연관은 없으나, DP를 구현하는데 사용된다는 공통점이 있음음

#### 예제문제(1)
- boj.kr/2748
- 2748. 피보나치 수 2
- 입력
  - 정수 N (N<=90)
- 출력
  - N번째 피보나치 수를 출력
- 예제1
  - 입력
    - 10
  - 출력
    - 55
```
import sys
input = sys.stdin.readline
#input
#process 
cache = [-1] * 91
cache[0] = 0
cache[1] = 1
cnt = 0

def f(n):
    global cnt
    cnt += 1
    # Top Down, using No cache[] : cnt goes much bigger
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)        # Issue : Time takes so long
    """
    # Top Down, using  cache[] : cnt goes much smaller
    """
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
        
    return cache[n]
    """
    # Bottom Up, using for loop
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
        
    return cache[n]
    
#output
print(f(int(input())))
print(cnt)
```
#### 예제문제(2)
- boj.kr/11051
- 11051. 이항 계수 2
- 입력
  - 첫째 줄에 정수 N과 K를 입력 (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)
- 출력
  - 이항계수binom{N}{K}를 10,007로 나눈 나머지를 출력
  - 이항계수 구하기 : NCK = C(N, K) = N! / K!(N-K)!
    - From 0 ~ 4, (!) 0! == 1
      - 0C0
      - 1C0 1C1
      - 2C0 2C1 2C2
      - 3C0 3C1 3C2 3C3
      - 4C0 4C1 4C2 4C3 4C4
      - ==
      - 1
      - 1 1
      - 1 2 1
      - 1 3 3 1
      - 1 4 6 3 1
- 예제1
  - 입력
    - 5 2
  - 출력
    - 10
    - 풀이
      - 5*4*3*2*1 / 2*1*(3*2*1) = 10, 10 % 10007 = 10
```
```
- (!)이항계수 이해 우선 필요(!)
  - https://youtu.be/lWlLeLT9GN0?si=n65d9FO9ml8FGbmN

#### DP구현2가지
- 구현
  - Top-Down : 재귀
  - Bottom Up : 반복문
- 저장방식
  - Top-Down : Memoization
  - Bottom Up : Tablation
- 장점
  - Top-Down : 직관적인 코드 가독성
  - Bottom Up : 시간과 메모리 절약
- 단점
  - Top-Down : 재귀 함수 호출로 인한 시간 소요
  - Bottom Up : DP 테이블을 채워 나가는 순서를 찾아야
 
#### 예제문제(4)
- boj.kr/11726
- 11726. 2xn 타일링
 
#### 예제문제(5)
- boj.kr/10844
- 10844. 쉬운 계단 수

#### DP(동적계획법) 정리
- 동적계획법은 문제를 쪼개서 작은 문제부터 구해가며 원래 문제의 답을 구하는 방식
- Memoization(메모이제이션) / Tablation (테이블레이션)을 사용
- 점화식을 찾고 테이블만 잘 정의하면 풀리는 문제들이 많음 (단, 문제는 그 점화식을 찾는게 쉽지 않음)

----------------
## PART 3. 알고리즘 핵심문제

#### 예제문제(1)
- boj.kr/1018
- 1018. 체스판 다시 칠하기

#### 예제문제(2)
- boj.kr/2841
- 2841. 외계인의 기타 연주

#### 예제문제(3)
- boj.kr/4796
- 4796. 캠핑

#### 예제문제(4)
- boj.kr/15686
- 15686. 치킨 배달

#### 예제문제(5)
- boj.kr/XXXXX
- XXXXX. 핵심 문제

#### 예제문제(6)
- boj.kr/XXXXX
- XXXXX. 핵심 문제

#### 예제문제(7)
- boj.kr/XXXXX
- XXXXX. 핵심 문제

#### 예제문제(8)
- boj.kr/XXXXX
- XXXXX. 핵심 문제


----------------
## PART 4. 삼성·카카오 기출 문제
