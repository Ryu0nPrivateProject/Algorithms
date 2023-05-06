'''
https://www.acmicpc.net/problem/14500
'''
import copy

N, M = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]

ts = [
    [
        [1, 1, 1, 1]
    ],
    [
        [1, 1],
        [1, 1]
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1]
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1]
    ],
    [
        [1, 1, 1],
        [0, 1, 0]
    ]
]

def rotate(tetromino):
    r, c = len(tetromino), len(tetromino[0])
    rotated = []
    for j in range(c):
        row = [tetromino[i][j] for i in range(r-1, -1, -1)]
        rotated.append(row)
    return rotated

def symmetry(tetromino):
    return [list(reversed(row)) for row in tetromino]

def visit(tetromino, m):
    max_score = 0
    r, c = len(tetromino), len(tetromino[0])
    for r_v in range(len(m)-(r-1)):
        for c_v in range(len(m[0])-(c-1)):
            s = 0
            for r_t in range(r):
                for c_t in range(c):
                    if tetromino[r_t][c_t] == 1:
                        s += m[r_v+r_t][c_v+c_t]
            if max_score < s:
                max_score = s
    return max_score
                    

max_score = 0
for t in ts:
    t_list = list()
    t_list.append(t)
    t_list.append(symmetry(t))
    for _ in range(3):
        t = rotate(t)
        t_list.append(t)
        t_list.append(symmetry(t))
    for t in t_list:
        s = visit(t, m)
        if max_score < s:
            max_score = s
print(max_score)