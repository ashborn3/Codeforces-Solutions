def max_spectacle(t, test_cases):
    results = []
    for case in test_cases:
        n, m, k = case['dimensions']
        w = case['w']
        heights = case['heights']
        
        # Sort the heights in descending order
        heights.sort(reverse=True)
        
        # Calculate the maximum spectacle
        max_spectacle = sum(heights[:k*k])
        
        # Store the result
        results.append(max_spectacle)
    
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
    m = int(data[index+1])
    k = int(data[index+2])
    w = int(data[index+3])
    heights = list(map(int, data[index+4:index+4+w]))
    test_cases.append({
        'dimensions': (n, m, k),
        'w': w,
        'heights': heights
    })
    index += 4 + w

# Get results
results = max_spectacle(t, test_cases)

# Print results
for result in results:
    print(result)