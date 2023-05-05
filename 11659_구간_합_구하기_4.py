'''
https://www.acmicpc.net/problem/11659
'''

N, M = list(map(int, input().split(' ')))
values = list(map(int, input().split(' ')))
ijs = [list(map(int, input().split(' '))) for _ in range(M)]
acc = [0] * (len(values)+1)
for i in range(N):
    acc[i+1] = acc[i] + values[i]
for i, j in ijs:
    print(acc[j]-acc[i-1])