'''
https://www.acmicpc.net/problem/2559
'''

N, K = map(int, input().split(' '))
ts = list(map(int, input().split(' ')))
s = [0] * (len(ts)+1)
m = -100*100000
for i in range(N):
    s[i+1] = s[i] + ts[i]
for i in range(K, len(s)):
    t = s[i]-s[i-K]
    if t > m:
        m = t
print(m)