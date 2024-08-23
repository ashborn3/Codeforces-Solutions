import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
# Take int input
def inp():
    return int(input().strip())

# Take list input
def inlt():
    return list(map(int, input().strip().split()))

# For taking space separated integer variable inputs.
def invr():
    return map(int, input().strip().split())

def solve():
    na = inp()
    a = inlt()
    m = inp()
    mstr = [input().strip() for _ in range(m)]
    answer = []

    for string in mstr:
        if len(string) != na:
            answer.append("NO")
            continue
        
        a_to_s = {}
        s_to_a = {}
        valid = True
        
        for i in range(na):
            ai = a[i]
            si = string[i]
            
            if ai in a_to_s and a_to_s[ai] != si:
                valid = False
                break
            if si in s_to_a and s_to_a[si] != ai:
                valid = False
                break
            
            a_to_s[ai] = si
            s_to_a[si] = ai
        
        if valid:
            answer.append("YES")
        else:
            answer.append("NO")
    
    return answer

t = inp()

for _ in range(t):
    ans = solve()
    for a in ans:
        print(a)