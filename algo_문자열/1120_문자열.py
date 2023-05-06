'''
https://www.acmicpc.net/problem/1120
'''
A, B = input().split()

def search_character():
    for i in range(26):
        yield chr(97+i)

def check(s1, s2):
    acc = 0
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            acc += 1
    return acc

accs = []
mod = len(B) - len(A)
for num_prefix in range(mod+1):
    num_suffix = mod - num_prefix
    prefix, suffix = '', ''
    for p in range(num_prefix):
        for c in search_character():
            if c == B[p]:
                break
        prefix += c
    for s in range(len(B)-1, len(B)-1-num_suffix, -1):
        for c in search_character():
            if c == B[s]:
                break
        suffix = c + suffix
    concat = prefix + A + suffix
    acc = check(concat, B)
    accs.append(acc)
print(min(accs))
