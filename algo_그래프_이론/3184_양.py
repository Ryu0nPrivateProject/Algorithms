'''
https://www.acmicpc.net/problem/3184
'''
import sys
sys.setrecursionlimit(10**5)

R, C = map(int, input().split())
am = [input() for _ in range(R)]
visited = [[0]*C for _ in range(R)]
sheep, wolf = 0, 0

def visit(i:int, j:int, region:set):
    if visited[i][j] == 1:
        return region
    visited[i][j] = 1
    if am[i][j] == '#':
        return region
    
    region.add((i, j))
    
    if i > 0:
        region = visit(i-1, j, region)
    if j > 0:
        region = visit(i, j-1, region)
    if i < R-1:
        region = visit(i+1, j, region)
    if j < C-1:
        region = visit(i, j+1, region)
        
    return region

for i in range(R):
    for j in range(C):
        region = visit(i, j, set())
        if len(region) > 0:
            s, w = 0, 0
            for x, y in region:
                o = am[x][y]
                if o == 'v':
                    w += 1
                elif o == 'o':
                    s += 1
            if s > w:
                sheep += s
            else:
                wolf += w
print(sheep, wolf)
        