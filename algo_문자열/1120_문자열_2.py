'''
https://www.acmicpc.net/problem/1120
'''
A, B = input().split()

diffs = []
for offset in range(len(B)-len(A)+1):
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i+offset]:
            diff += 1
    diffs.append(diff)
print(min(diffs))