import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
# Take int input
def inp():
    return(int(input()))
def invr():
    return(map(int,input().split()))

def find_biggest_power(a, l):
    max_power = 0
    while l % a == 0:
        l //= a
        max_power += 1
    return max_power


t = inp()
for i in range(t):
    a, b, l = invr()
    dup = []
    ans = 0
    m = 0
    pa = find_biggest_power(a, l) + 1
    pb = find_biggest_power(b, l) + 1
    for j in range(pa):
        for k in range(pb):
            m = (a**j)*(b**k)
            if (l%m == 0) and (m <= l) and (m not in dup):
                ans = ans + 1
                dup.append(m)
    print(ans)
