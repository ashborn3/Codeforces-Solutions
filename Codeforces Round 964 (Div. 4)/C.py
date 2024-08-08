import sys
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


def solve():
    n, s, m = invr()
    time = []
    for i in range(n):
        time.append(inlt())
    free = []
    l = 0
    for busy in time:
        free.append([l,busy[0]])
        l = busy[1]
    free.append([time[-1][1], m])
    for f in free:
        if f[1] - f[0] >= s:
            return "YES"
    return "NO"  
        
t = inp()
for i in range(t):
    print(solve())