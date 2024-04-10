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
s = ""
n = 0
for _ in range(t):
    n = inp()
    s = insr()
    flag = False
    while True:
        flag = False
        for i in range(len(s) - 1):
            if s[i] == "(" and s[i + 1] == ")":
                s.pop(i)
                s.pop(i)
                flag = True
                break
        if (flag == True):
            continue
        break
    print(int(len(s)/2))
