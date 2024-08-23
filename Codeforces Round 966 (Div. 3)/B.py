def check_boarding_rules(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        occupied = set()
        valid = True
        for i in range(n):
            seat = a[i]
            if i == 0:
                occupied.add(seat)
            else:
                if (seat - 1 not in occupied) and (seat + 1 not in occupied):
                    valid = False
                    break
                occupied.add(seat)
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index + 1: index + 1 + n]))
    test_cases.append((n, a))
    index += 1 + n

# Process and output results
results = check_boarding_rules(t, test_cases)
for result in results:
    print(result)