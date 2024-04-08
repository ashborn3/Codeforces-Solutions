import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def invr():
    return(map(int,input().split()))


n = inp()
c = 0
for i in range(n):
    if sum(invr()) > 1:
        c = c + 1
print(c)