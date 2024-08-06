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
    n = inp()
    a = inlt()
    a.sort()
    i = 0
    even = 0
    odd = 0
    popped = False
    for num in a:
        if num % 2 == 0:
            even = even + 1
        elif num % 2 == 1:
            odd = odd + 1
    if (even % 2 == 0 and odd % 2 == 0):
        return "YES"
    else:
        while i < n - 1:
            if a[i + 1] - a[i] == 1:
                popped = True
                a.pop(i)
                a.pop(i)
                n = n - 2
                i = 0
            else:
                i = i + 1
        even = 0
        odd = 0
        for num in a:
            if num % 2 == 0:
                even = even + 1
            elif num % 2 == 1:
                odd = odd + 1
        if (even % 2 == 0 and odd % 2 == 0):
            return "YES"
        else:
            if (even % 2 == 1 and odd % 2 == 1) and popped == True:
                return "YES"
            else:
                return "NO"

t = inp()
for i in range(t):
    print(solve())
    


"""
44
75 26 45 72 81 47 29 97 2 75 25 82 84 17 56 32 2 28 37 57 39 18 11 79 6 40 68 68 16 40 63 93 49 91 10 55 68 31 80 57 18 34 28 76
"""