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


n = inp()
x = 0
y = 0
z = 0

for i in range(n):
    f = inlt()
    x = x + f[0]
    y = y + f[1]
    z = z + f[2]

if (x == 0 and y == 0 and z == 0):
    print("YES")
else:
    print("NO")