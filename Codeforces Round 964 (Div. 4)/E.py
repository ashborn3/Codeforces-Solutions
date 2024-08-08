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
    l, r = invr()
    l1 = l
    l2 = l + 1
    turns = 0
    
    if l + 1 == r:
        while l != 0:
            turns = turns + 1
            l = l // 3
            r = r * 3
        while r != 0:
            r = r // 3
            turns += 1
        return turns
    
    while l1 != 0:
        l1 = l1 // 3
        l2 = l2 * 3
        turns = turns + 1
    l1 = l2
    l = l + 1
    while l < r:
        l1  = l1 // 3
        turns += 1
        if l1 == 0:
            l = l + 1
            l1 = l
    while r != 0:
        r = r // 3
        turns += 1
    return turns
    


t = inp()
for i in range(t):
    print(solve())