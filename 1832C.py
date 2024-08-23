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


def cont(a):
    con = 0
    for i in range(len(a) - 1):
        con += abs(a[i] - a[i + 1])
    return con

def solve(lna, a):
    con = cont(a)
    seta = parse(a)
    l = len(seta)
    if l == 1:
        return 1
    elif l == 2:
        return 2
    elif l == 3:
        if (seta[0] > seta[1] > seta[2]):
            return 2
        elif (seta[0] < seta[1] < seta[2]):
            return 2
    else:
        for i in range(1, len(seta) - 2):
            if (seta[i -1] > seta[i] > seta[i + 1]):
                l -= 1
            elif (seta[i -1] < seta[i] < seta[i + 1]):
                l -= 1
                
    return l

def parse(a):
    for i in range(len(a) - 1):
        if (a[i] == a[i + 1]):
            a[i] = -1
    aa = []
    for i in range(len(a)):
        if a[i] != -1:
            aa.append(a[i])
    return aa

# START
n = inp()

for i in range(n):
    lna = inp()
    a = inlt()
    print(solve(lna, a))
    

