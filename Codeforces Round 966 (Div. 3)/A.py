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
    num = str(inp())
    
    if int(num) < 100:
        return ("NO")
    
    ten = num[0:2]
    rest = num[2:]
    
    if ten == "10" and int(rest) >= 2 and int(rest[0]) != 0:
        return ("YES")
    else:
        return ("NO")

t = inp()

for i in range(t):
    print(solve())
    