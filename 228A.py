import sys
input = sys.stdin.readline

def invr():
    return(map(int,input().split()))


print(4 - len(set(invr())))