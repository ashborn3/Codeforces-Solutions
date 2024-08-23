import sys
from collections import defaultdict
input = sys.stdin.readline

############ ---- Input Functions ---- ############
# Take int input
def inp():
    return(int(input()))
# Take list input
def inlt():
    return(list(map(int,input().split())))
# Take string input as a array of chars
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
# For taking space seperated integer variable inputs.
def invr():
    return(map(int,input().split()))

n, m = invr()

colordict = defaultdict(lambda: [])

sum = 0

for i in range(n):
    l = inlt()
    for j in range(len(l)):
        colordict[l[j]].append((i, j))
for i, v in colordict.items():
    print(v)
    for i in range(len(v)):
        for j in range(i, len(v)):
            sum += abs(v[i][0] - v[j][0]) + abs(v[i][1] - v[j][1])

print(sum)