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

t = inp()
n = 0
s = 0
for _i in range(t):
    n = inp()
    n = int(n/2)
    print(int(((n*(n+1)*(2*n + 1))/6)*8))