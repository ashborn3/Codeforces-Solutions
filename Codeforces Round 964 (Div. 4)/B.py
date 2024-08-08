import sys
input = sys.stdin.readline

def inp():
    return int(input())

def invr():
    return map(int, input().split())

def count_suneet_wins(a1, a2, b1, b2):
    suneet_wins = 0
    combinations = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]
    
    for (s1, sl1, s2, sl2) in combinations:
        suneet_rounds = 0
        slavic_rounds = 0
        
        if s1 > sl1:
            suneet_rounds += 1
        elif s1 < sl1:
            slavic_rounds += 1
        
        if s2 > sl2:
            suneet_rounds += 1
        elif s2 < sl2:
            slavic_rounds += 1
        
        if suneet_rounds > slavic_rounds:
            suneet_wins += 1
    
    return suneet_wins

t = inp()
results = []

for _ in range(t):
    a1, a2, b1, b2 = invr()
    results.append(count_suneet_wins(a1, a2, b1, b2))

for result in results:
    print(result)