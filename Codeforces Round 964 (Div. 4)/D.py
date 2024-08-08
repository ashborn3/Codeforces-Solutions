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
    s = insr()
    t = insr()
    ls = 0
    lt = 0
    while ls < len(s) and lt < len(t):
        if s[ls] == t[lt]:
            ls = ls + 1
            lt = lt + 1
        elif s[ls] == "?":
            s[ls] = t[lt]
            ls = ls + 1
            lt = lt + 1
        else:
            return "NO"
    for i in range(ls, len(s)):
        if s[i] == "?":
            s[i] = "a"
    string = "".join(s)
    return "YES\n" + string
    


t = inp()
for i in range(t):
    print(solve())