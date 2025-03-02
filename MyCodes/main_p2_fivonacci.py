import sys

input = sys.stdin.readline
"""

"""
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
