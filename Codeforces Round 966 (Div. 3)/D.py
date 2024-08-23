def has_consecutive_Rs(chars):
    for i in range(len(chars) - 1):
        if chars[i] == 'R' and chars[i + 1] == 'R':
            return True
    return False

def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    s = input().strip()
    
    total_sum = 0
    
    if not has_consecutive_Rs(s):
        # No consecutive 'R's
        first_l = -1
        last_r = -1
        for i in range(n):
            if s[i] == 'L' and first_l == -1:
                first_l = i
            if s[i] == 'R':
                last_r = i
        if first_l == -1 or last_r == -1 or first_l >= last_r:
            return 0
        return sum(a[first_l:last_r + 1])
    else:
        # There are consecutive 'R's
        first_l = -1
        last_r = -1
        for i in range(n):
            if s[i] == 'L' and first_l == -1:
                first_l = i
            if s[i] == 'R':
                last_r = i
        if first_l != -1 and last_r != -1 and first_l < last_r:
            total_sum += sum(a[first_l:last_r + 1])
        
        i = 0
        while i < n:
            if s[i] == 'R' and i + 1 < n and s[i + 1] == 'R':
                # Find the end of this sequence of consecutive 'R's
                j = i
                while j < n and s[j] == 'R':
                    j += 1
                # Find the first 'L' after the last 'R' of this sequence
                k = j
                while k < n and s[k] != 'L':
                    k += 1
                if k < n:
                    total_sum += sum(a[i:k + 1])
                i = k
            else:
                i += 1
        return total_sum

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    print(solve())